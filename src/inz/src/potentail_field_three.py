#! /usr/bin/python
import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from gazebo_msgs.srv import GetModelState, GetModelStateRequest
from std_msgs.msg import Int32
from mgr.msg import Formation
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

def callback_actual_position_follower_1(pos):
	global act_follower_1_x_position 
	global act_follower_1_y_position 
	global act_follower_1_z_position 
	global act_follower_1_x_velocity
	global act_follower_1_y_velocity 
	global act_follower_1_z_velocity 
	
	act_follower_1_x_position = pos.pose.pose.position.x
	act_follower_1_y_position = pos.pose.pose.position.y
	act_follower_1_z_position = pos.pose.pose.position.z
	
	act_follower_1_x_velocity = pos.twist.twist.linear.x
	act_follower_1_y_velocity = pos.twist.twist.linear.y
	act_follower_1_z_velocity = pos.twist.twist.linear.z

def callback_actual_position_follower_2(pos):
	global act_follower_2_x_position 
	global act_follower_2_y_position 
	global act_follower_2_z_position 
	global act_follower_2_x_velocity
	global act_follower_2_y_velocity 
	global act_follower_2_z_velocity 
	
	act_follower_2_x_position = pos.pose.pose.position.x
	act_follower_2_y_position = pos.pose.pose.position.y
	act_follower_2_z_position = pos.pose.pose.position.z
	
	act_follower_2_x_velocity = pos.twist.twist.linear.x
	act_follower_2_y_velocity = pos.twist.twist.linear.y
	act_follower_2_z_velocity = pos.twist.twist.linear.z

def callback_formation_control_follower_1(formation):
	global follower_1_formation_lx 
	global follower_1_formation_ly  
	
	follower_1_formation_lx = formation.Lx
	follower_1_formation_ly = formation.Ly
	
def callback_formation_control_follower_2(formation):
	global follower_2_formation_lx 
	global follower_2_formation_ly  
	
	follower_2_formation_lx = formation.Lx
	follower_2_formation_ly = formation.Ly
	

	
def generate_potential_field(xf, yf, zf, x_other_f, y_other_f, publisher, follower_nr):
		global xl
		global yl
		global zl
		global follower_1_formation_lx 
		global follower_1_formation_ly  
		global follower_2_formation_lx 
		global follower_2_formation_ly 
		
		field_L = rospy.get_param('field_L')
		field_r = rospy.get_param('field_r')
		field_Kd = rospy.get_param('field_Kd')
		field_Kc = rospy.get_param('field_Kc')
		field_Da = rospy.get_param('field_Da')
		field_Lx = rospy.get_param('field_Lx')
		field_Ly = rospy.get_param('field_Ly')
		field_Lfx = rospy.get_param('field_Lfx')
		field_Lfy = rospy.get_param('field_Lfy')
		
		if follower_nr == 1:
			Kc = field_Kc
			Kd = field_Kd
			r = field_r
			L = field_L
			Lx = follower_1_formation_lx
			Ly = follower_1_formation_ly
			Da = field_Da
			Ka = 2
		
		if follower_nr == 2:
			Kc = field_Kc
			Kd = field_Kd
			r = field_r
			L = field_L
			Lx = follower_2_formation_lx
			Ly = follower_2_formation_ly
			Da = field_Da
			Ka = 10
		
		Lfx = field_Lfx
		Lfy = field_Lfy
		
		dci = sqrt(pow(yf -yl, 2) + pow(xf-xl,2))
		dcix = (xl - xf)
		dciy = (yl - yf)
		
		dij = sqrt(pow(yf-y_other_f,2) + pow(xf-x_other_f,2))
		
		
		if dcix == 0:
			dcix = 0.000001
			
		if dciy == 0:
			dciy = 0.000001
			
		if dci == 0:
			dci = 0.000001
			
		if dij == 0:
			dij = 0.000001
		
		z = zl - zf
		
		# Rownowaga gdy:
		
		#Lx = 1
		# Ptt_x -->  (-20 / 3) * (3 - 1)  * (3) = -40
		# Prep_x --> (10 / -3) * (-3 - 1) * (3) = 40
		#
		#Lx = 2
		# Ptt_x -->  (-20 / 4) * (4 - 1)  * (3) = -60
		# Prep_x --> (10 / -4) * (-4 - 2) * (4) = 60
		#
		
		
		Ptt_x = (-Kc / dci ) * (dci - r) * (xf - xl) # przyciagajaca do leadera Kc 20
		Ptt_y = (-Kc / dci ) * (dci - r) * (yf - yl)

		Prep_x = (Kd / dcix) * (dcix - Lx) * (xf - xl)	# odpychajaca od leadera Kd 10
		Prep_y = (Kd / dciy) * (dciy - Ly) * (yf - yl) 
		
		
		if (abs(xf - x_other_f) < 1 and abs(yf - y_other_f) < 1 ):  	# sily miedzy followerami
			Pff_x = (Ka/dij)*(dij - Lfx)*(xf - x_other_f)
			Pff_y = (Ka/dij)*(dij - Lfy)*(yf - y_other_f)
		else:
			Pff_x = 0
			Pff_y = 0
		
		
		Px = Ptt_x + Da + Prep_x + Pff_x
		Py = Ptt_y + Da + Prep_y + Pff_y
		
		
		msg_twist_cmd_vel = Twist()
		msg_twist_cmd_vel.linear.x = Px
		msg_twist_cmd_vel.linear.y = Py
		msg_twist_cmd_vel.linear.z = z
		msg_twist_cmd_vel.angular.x = 0
		msg_twist_cmd_vel.angular.y = 0
		msg_twist_cmd_vel.angular.z = 0
		
		if follower_nr == 1 :
			pttx = "Przy x: %s"%Ptt_x
			ptty = "Przy y: %s"%Ptt_y
			prepx = "Odpy x: %s"%Prep_x
			prepy = "Odpy y: %s"%Prep_y
			pffx = "Odp fol2 x: %s"%Pff_x
			pffy = "Odp fol2 y: %s"%Pff_y
			p2x = "Suma x: %s"%Px
			p2y = "Suma y: %s"%Py
			dcis = "Dci: %s"%dci
			dcixs = "Dcx: %s"%dcix
			dciys = "Dcy: %s"%dciy
			print("-------------------------")
			print("     ")
			rospy.loginfo(pttx)
			rospy.loginfo(ptty)
			rospy.loginfo(prepx)
			rospy.loginfo(prepy)
			rospy.loginfo(pffx)
			rospy.loginfo(pffy)
			rospy.loginfo(p2x)
			rospy.loginfo(p2y)
			rospy.loginfo(dcis)
			rospy.loginfo(dcixs)
			rospy.loginfo(dciys)
		
		publisher.publish(msg_twist_cmd_vel)

	
def main(leader_name, follower_1_name, follower_2_name):
	
	global act_follower_1_x_position 
	global act_follower_1_y_position 
	global act_follower_1_z_position
	global act_follower_1_x_velocity
	global act_follower_1_y_velocity 
	global act_follower_1_z_velocity 
	global act_follower_2_x_position 
	global act_follower_2_y_position 
	global act_follower_2_z_position
	global act_follower_2_x_velocity
	global act_follower_2_y_velocity 
	global act_follower_2_z_velocity 
	global act_leader_x_position 
	global act_leader_y_position 
	global act_leader_z_position
	global act_leader_x_velocity
	global act_leader_y_velocity 
	global act_leader_z_velocity  
	global follower_1_formation_lx 
	global follower_1_formation_ly  
	global follower_2_formation_lx 
	global follower_2_formation_ly  
	global xl
	global yl
	global zl
	 
	act_leader_x_position = 0  
	act_leader_y_position = 0  
	act_leader_z_position = 0
	act_leader_x_velocity = 0
	act_leader_y_velocity = 0
	act_leader_z_velocity = 0
	act_follower_1_x_position = 0
	act_follower_1_y_position = 0
	act_follower_1_z_position = 0
	act_follower_1_x_velocity = 0 
	act_follower_1_y_velocity = 0
	act_follower_1_z_velocity = 0
	act_follower_2_x_position = 0
	act_follower_2_y_position = 0
	act_follower_2_z_position = 0
	act_follower_2_x_velocity = 0 
	act_follower_2_y_velocity = 0
	act_follower_2_z_velocity = 0
	follower_1_formation_lx = 1
	follower_1_formation_ly = 0 
	follower_2_formation_lx = -1
	follower_2_formation_ly = 0 
	
	
	xl = 0
	yl = 0
	zl = 0
	
	rospy.init_node('potential_field_generation')	
	
	sub_actual_position_leader = rospy.Subscriber('position_' + leader_name, Odometry, callback_actual_position_leader)
	sub_actual_position_follower_1 = rospy.Subscriber('position_' + follower_1_name, Odometry, callback_actual_position_follower_1)
	sub_actual_position_follower_2 = rospy.Subscriber('position_' + follower_2_name, Odometry, callback_actual_position_follower_2)
	sub_formation_control_follower_1 = rospy.Subscriber('formation_control_' + follower_1_name, Formation, callback_formation_control_follower_1)
	sub_formation_control_follower_2 = rospy.Subscriber('formation_control_' + follower_2_name, Formation, callback_formation_control_follower_2)
	
	#pub = rospy.Publisher('/ardrone_1/cmd_vel', Twist, queue_size=10)
	pub_field_follower_1 = rospy.Publisher('potentail_field_' + follower_1_name, Twist, queue_size=10) #todo make topic name position/ardrone_1/diff
	pub_field_follower_2 = rospy.Publisher('potentail_field_' + follower_2_name, Twist, queue_size=10) #todo make topic name position/ardrone_1/diff

	field_on = 0
	if rospy.has_param('FIELD_ON'):
		field_on = rospy.get_param('FIELD_ON')
	else:
		rospy.set_param('FIELD_ON', field_on)
	
	field_L = 1
	if rospy.has_param('field_L'):
		field_L = rospy.get_param('field_L')
	else:
		rospy.set_param('field_L', field_L)
	
	field_r = 1
	if rospy.has_param('field_r'):
		field_r = rospy.get_param('field_r')
	else:
		rospy.set_param('field_r', field_r)
		
	field_Kc = 20
	if rospy.has_param('field_Kc'):
		field_Kc = rospy.get_param('field_Kc')
	else:
		rospy.set_param('field_Kc', field_Kc)
	
	field_Kd = 10
	if rospy.has_param('field_Kd'):
		field_Kd = rospy.get_param('field_Kd')
	else:
		rospy.set_param('field_Kd', field_Kd)
	
	field_Da = 0
	if rospy.has_param('field_Da'):
		field_Da = rospy.get_param('field_Da')
	else:
		rospy.set_param('field_Da', field_Da)
		
	field_Lx = 0
	if rospy.has_param('field_Lx'):
		field_Lx = rospy.get_param('field_Lx')
	else:
		rospy.set_param('field_Lx', field_Lx)
	
	field_Ly = 0
	if rospy.has_param('field_Ly'):
		field_Da = rospy.get_param('field_Ly')
	else:
		rospy.set_param('field_Ly', field_Ly)
	
	field_Lfx = 0
	if rospy.has_param('field_Lfx'):
		field_Lfx = rospy.get_param('field_Lfx')
	else:
		rospy.set_param('field_Lfx', field_Lfx)
	
	field_Lfy = 0
	if rospy.has_param('field_Lfy'):
		field_Lfy = rospy.get_param('field_Lfy')
	else:
		rospy.set_param('field_Lfy', field_Lfy)
	
	
	
	#rospy.spin()
	rate = rospy.Rate(50)
	
	while not rospy.is_shutdown():
		sub_actual_position_leader = rospy.Subscriber('position_' + leader_name, Odometry, callback_actual_position_leader)
		sub_actual_position_follower_1 = rospy.Subscriber('position_' + follower_1_name, Odometry, callback_actual_position_follower_1)
		sub_actual_position_follower_2 = rospy.Subscriber('position_' + follower_2_name, Odometry, callback_actual_position_follower_2)
		field_on = rospy.get_param('FIELD_ON')
		field_L = rospy.get_param('field_L')
		field_r = rospy.get_param('field_r')
		field_Kd = rospy.get_param('field_Kd')
		field_Kc = rospy.get_param('field_Kc')
		field_Da = rospy.get_param('field_Da')
		field_Lx = rospy.get_param('field_Lx')
		field_Ly = rospy.get_param('field_Ly')
		
		xl = act_leader_x_position
		xf_1 = act_follower_1_x_position
		xf_2 = act_follower_2_x_position
		
		yl = act_leader_y_position
		yf_1 = act_follower_1_y_position
		yf_2 = act_follower_2_y_position
		
		zl = act_leader_z_position
		zf_1 = act_follower_1_z_position
		zf_2 = act_follower_2_z_position
		
		
		#rx = "aktualna x: %s"%Rxo
		#ry = "zadana x: %s"%Ryo
		#rz = "sterowanie x: %s"%Rzo
		#print("-------------------------")
		#print("     ")
		#rospy.loginfo(rx)
		#rospy.loginfo(ry)
		#rospy.loginfo(rz)
		
		generate_potential_field(xf_1, yf_1, zf_1, xf_2, yf_2, pub_field_follower_1, 1)	
		generate_potential_field(xf_2, yf_2, zf_2, xf_1, yf_1, pub_field_follower_2, 2)	
		
		rate.sleep()
		
		
		
    
if __name__ == '__main__':
	try:
		main(sys.argv[1], sys.argv[2], sys.argv[3])
	except rospy.ROSInterruptException:
		pass
