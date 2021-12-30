#! /usr/bin/python
import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from gazebo_msgs.srv import GetModelState, GetModelStateRequest
from std_msgs.msg import Int32
from math import pow, atan2, sqrt
import numpy
import sys


def callback_actual_position_leader(pos):
	global act_leader_x_position 
	global act_leader_y_position 
	global act_leader_z_position
	global act_leader_x_velocity
	global act_leader_y_velocity 
	global act_leader_z_velocity 
	 
	act_leader_x_position = pos.pose.pose.position.x
	act_leader_y_position = pos.pose.pose.position.y
	act_leader_z_position = pos.pose.pose.position.z
	act_leader_x_velocity = pos.twist.twist.linear.x
	act_leader_y_velocity = pos.twist.twist.linear.y
	act_leader_z_velocity = pos.twist.twist.linear.z

def callback_actual_position_follower(pos):
	global act_follower_x_position 
	global act_follower_y_position 
	global act_follower_z_position 
	global act_follower_x_velocity
	global act_follower_y_velocity 
	global act_follower_z_velocity 
	
	act_follower_x_position = pos.pose.pose.position.x
	act_follower_y_position = pos.pose.pose.position.y
	act_follower_z_position = pos.pose.pose.position.z
	
	act_follower_x_velocity = pos.twist.twist.linear.x
	act_follower_y_velocity = pos.twist.twist.linear.y
	act_follower_z_velocity = pos.twist.twist.linear.z

	
	
def main():
	
	global act_follower_x_position 
	global act_follower_y_position 
	global act_follower_z_position
	global act_follower_x_velocity
	global act_follower_y_velocity 
	global act_follower_z_velocity 
	global act_leader_x_position 
	global act_leader_y_position 
	global act_leader_z_position
	global act_leader_x_velocity
	global act_leader_y_velocity 
	global act_leader_z_velocity   
	 
	act_leader_x_position = 0  
	act_leader_y_position = 0  
	act_leader_z_position = 0  
	act_leader_x_velocity = 0
	act_leader_y_velocity = 0
	act_leader_z_velocity = 0
	act_follower_x_position = 0
	act_follower_y_position = 0
	act_follower_z_position = 0
	act_follower_x_velocity = 0 
	act_follower_y_velocity = 0
	act_follower_z_velocity = 0
	
	rospy.init_node('potential_publisher')	
	
	sub_actual_position_leader = rospy.Subscriber('position_ardrone_1', Odometry, callback_actual_position_leader)
	sub_actual_position_follower = rospy.Subscriber('position_ardrone_2', Odometry, callback_actual_position_follower)
	
	pub = rospy.Publisher('/ardrone_1/cmd_vel', Twist, queue_size=10)
	pub_dif = rospy.Publisher('position_ardrone_1_field', Twist, queue_size=10) #todo make topic name position/ardrone_1/diff
	
	field_on = 0
	
	if rospy.has_param('FIELD_ON'):
		field_on = rospy.get_param('FIELD_ON')
	else:
		rospy.set_param('FIELD_ON', field_on)
	
	#rospy.spin()
	r = rospy.Rate(2)
	
	while not rospy.is_shutdown():
		sub_actual_position_leader = rospy.Subscriber('position_ardrone_1', Odometry, callback_actual_position_leader)
		sub_actual_position_follower = rospy.Subscriber('position_ardrone_2', Odometry, callback_actual_position_follower)
		field_on = rospy.get_param('FIELD_ON')
		
		x_leader = act_leader_x_position - act_follower_x_position - 0.7
		y_leader = act_leader_y_position - act_follower_y_position - 0.7
		z_leader = act_leader_z_position - act_follower_z_position
		
		
		dx = x_leader
		dy = y_leader
		dz = z_leader
		ddx = act_leader_x_velocity
		ddy = act_leader_y_velocity
		ddz = act_leader_z_velocity
		cx = 0
		cy = 0
		cz = 0
		
		Vc = act_leader_x_velocity
		
		msg_twist_cmd_vel = Twist()
		msg_twist_cmd_vel.linear.x = 0
		msg_twist_cmd_vel.linear.y = 0
		msg_twist_cmd_vel.linear.z = 0
		msg_twist_cmd_vel.angular.x = 0
		msg_twist_cmd_vel.angular.y = 0
		msg_twist_cmd_vel.angular.z = 0
		
		Rx = 0.0000001
		Ry = 0.0000001
		Rz = 0.0000001
		
		if dx>=0:
			Rx = Vc/(1+10000*pow(dx,2.0)+1000*ddx*pow(dx,2.0))  
			Ry = -(10000)*numpy.sign(dy)*pow(dy,2.0) 
			Rz = -(10000)*numpy.sign(dz)*pow(dz,2.0)

			if cx>=0:
				Rx = Vc/(1+10000*pow(dx,2.0)+10000*abs(cx)*pow(dx,2.0)+10000*ddx*pow(dx,2.0))  
				Ry = -(10000)*numpy.sign(dy)*pow(dy,2)  
				Rz = -(10000)*numpy.sign(dz)*pow(dz,2)

			if (((cy>=0) and (dy>=0)) or  ((cy<0) and (dy<0))):
				Rx = Rx + 0 
				Ry = Ry + -10000*abs(cy)*numpy.sign(dy)*pow(dy,2.0)-10000*ddy*pow(dy,2.0) 
				Rz = Rz + 0
			else:
				Rx = Rx + 0 
				Ry = Ry + -10000*ddy*pow(dy,2.0) 
				Rz = Rz + 0

			if (((cz>=0) and (dz>=0)) or  ((cz<0) and (dz<0))):
				Rx = Rx + 0 
				Ry = Ry + 0 
				Rz = Rz -10000*abs(cz)*numpy.sign(dz)*pow(dz,2.0)-10000*ddz*pow(dz,2.0)
			else:
				Rx = Rx + 0 
				Ry = Ry + 0 
				Rz = Rz -10000*ddz*pow(dz,2.0)
		else:
			Rx = Vc-10000*numpy.sign(dx)*pow(dx,2.0)-10000*ddx*pow(dx,2.0) 
			Ry = -(10000.0)*numpy.sign(dy)*pow(dy,2.0)
			Rz = -(10000)*numpy.sign(dz)*pow(dz,2.0)

			if cx<=0:
				Rx = Vc-10000*numpy.sign(dx)*pow(dx,2.0)-10000*abs(cx)*numpy.sign(dx)*pow(dx,2.0)-10000*ddx*pow(dx,2.0)  
				Ry = -(10000)*numpy.sign(dy)*pow(dy,2.0) 
				Rz = -(10000)*numpy.sign(dz)*pow(dz,2.0) 

			if (((cy>=0) and (dy>=0)) or  ((cy<0) and (dy<0))):
				Rx = Rx + 0 
				Ry = Ry -10000*abs(cy)*numpy.sign(dy)*pow(dy,2.0)-10000*ddy*pow(dy,2.0) 
				Rz = Rz + 0
			else:
				Rx = Rx + 0 
				Ry = Ry -10000*ddy*pow(dy,2.0) 
				Rz = Rz + 0

			if (((cz>=0) and (dz>=0)) or  ((cz<0) and (dz<0))):
				Rx = Rx + 0 
				Ry = Ry + 0 
				Rz = Rz -10000*abs(cz)*numpy.sign(dz)*pow(dz,2.0)-10000*ddz*pow(dz,2.0)
			else:
				Rx = Rx + 0 
				Ry = Ry + 0 
				Rz = Rz -10000*ddz*pow(dz,2.0)	
				
				
		Vr=sqrt(pow(Rx,2.0)+pow(Ry,2.0)+pow(Rz,2.0));
	
		Rxo = Rx * 0
		Ryo = Ry * 0
		Rzo = Rz * 0.4
		if Vr != 0:
			Rxo = Rx / Vr
			Ryo = Ry / Vr
			Rzo = Rz / Vr
		
		
		msg_twist_cmd_vel.linear.x = 0
		msg_twist_cmd_vel.linear.y = 0
		msg_twist_cmd_vel.linear.z = Rzo
		
		if field_on == 1:
			pub.publish(msg_twist_cmd_vel)
		
		
		pub_dif.publish(msg_twist_cmd_vel)
		
		#rx = "aktualna x: %s"%Rxo
		#ry = "zadana x: %s"%Ryo
		#rz = "sterowanie x: %s"%Rzo
		#print("-------------------------")
		#print("     ")
		#rospy.loginfo(rx)
		#rospy.loginfo(ry)
		#rospy.loginfo(rz)
		
		
		a2x = "x: %s"%x_leader
		a2y = "y: %s"%y_leader
		a2z = "z: %s"%z_leader
		print("-------------------------")
		print("     ")
		rospy.loginfo(a2x)
		rospy.loginfo(a2y)
		rospy.loginfo(a2z)
		
		
		r.sleep()
		
		
		
    
if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
