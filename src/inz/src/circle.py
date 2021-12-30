#! /usr/bin/python
import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from gazebo_msgs.srv import GetModelState, GetModelStateRequest
from std_msgs.msg import Int32
from math import pow, atan2, sqrt, sin, cos
import sys

global set_x_position 
global set_y_position
global set_z_position
global act_x_position 
global act_y_position 
global act_z_position 

def callback_position(wiad): 
	global set_x_position 
	global set_y_position
	global set_z_position
	global act_x_position 
	global act_y_position 
	global act_z_position 
	set_x_position = wiad.position.x
	set_y_position = wiad.position.y
	set_z_position = wiad.position.z
	
def callback_actual_position(pos):
	global set_x_position 
	global set_y_position
	global set_z_position
	global act_x_position 
	global act_y_position 
	global act_z_position 
	act_x_position = pos.pose.pose.position.x
	act_y_position = pos.pose.pose.position.y
	act_z_position = pos.pose.pose.position.z
	
def main():
	global set_x_position 
	global set_y_position
	global set_z_position
	global act_x_position 
	global act_y_position 
	global act_z_position  
	 
	set_x_position = 0  
	set_y_position = 0 
	set_z_position = 1  
	act_x_position = 0  
	act_y_position = 0  
	act_z_position = 0  
	
	t = 0;
	
	rospy.init_node('manual_publisher')	
	
	sub_set_position = rospy.Subscriber('position_ardrone_1_set', Pose, callback_position)
	sub_actual_position = rospy.Subscriber('position_ardrone_1', Odometry, callback_actual_position)
	
	pub = rospy.Publisher('/ardrone_1/cmd_vel', Twist, queue_size=10)
	pub_dif = rospy.Publisher('position_ardrone_1_diff', Pose, queue_size=10) #todo make topic name position/ardrone_1/diff
	
	#rospy.spin()
	r = rospy.Rate(100)
	
	while not rospy.is_shutdown():
		sub_set_position = rospy.Subscriber('set_position_ardrone_1', Twist, callback_position)
		sub_actual_position = rospy.Subscriber('position_ardrone_1', Odometry, callback_actual_position)
		
		# Tworzenie waidomosci Twist
		msg_twist_cmd_vel = Twist()
		msg_twist_cmd_vel.linear.x = 0
		msg_twist_cmd_vel.linear.y = 0
		msg_twist_cmd_vel.linear.z = 0
		msg_twist_cmd_vel.angular.x = 0
		msg_twist_cmd_vel.angular.y = 0
		msg_twist_cmd_vel.angular.z = 0
		
		z_distance_diff = (set_z_position-act_z_position)

		
		msg_twist_cmd_vel.linear.x = 2 * sin(2 * 3.1415 * 1 * t)
		msg_twist_cmd_vel.linear.y = 2 * cos(2 * 3.1415 * 1 * t)
		
		#Regulator yaw		
		if z_distance_diff > 0.2:
			msg_twist_cmd_vel.linear.z = z_distance_diff * 0.5
		if z_distance_diff < -0.2:
			msg_twist_cmd_vel.linear.z = z_distance_diff * 0.5
		
		
		pub.publish(msg_twist_cmd_vel) # Wyslanie danych na topic
	
		x_act = "aktualna x: %s"%act_x_position
		x_zad = "zadana x: %s"%set_x_position
		x_cmd_vel = "sterowanie x: %s"%msg_twist_cmd_vel.linear.x
		print("-------------------------")
		print("     ")
		rospy.loginfo(x_act)
		rospy.loginfo(x_zad)
		rospy.loginfo(x_cmd_vel)
		
		t = t + 0.001
		
		r.sleep()
		
		
		
    
if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
