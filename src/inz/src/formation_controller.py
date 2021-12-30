#! /usr/bin/python
import rospy
from mgr.msg import Formation
import sys


def get_formation_type():
	formation_type = 0
	if rospy.has_param('formation_type'):
		formation_type = rospy.get_param('formation_type')
	else:
		rospy.set_param('formation_type', formation_type)
	return formation_type	

def set_manual_formation_parameter():
	follower_1_Lx = 1
	if rospy.has_param('follower_1_Lx'):
		follower_1_Lx = rospy.get_param('follower_1_Lx')
	else:
		rospy.set_param('follower_1_Lx', follower_1_Lx)
	
	follower_1_Ly = 0
	if rospy.has_param('follower_1_Ly'):
		follower_1_Ly = rospy.get_param('follower_1_Ly')
	else:
		rospy.set_param('follower_1_Ly', follower_1_Ly)

	follower_2_Lx = -1
	if rospy.has_param('follower_2_Lx'):
		follower_2_Lx = rospy.get_param('follower_2_Lx')
	else:
		rospy.set_param('follower_2_Lx', follower_2_Lx)
	
	follower_2_Ly = 0
	if rospy.has_param('follower_2_Ly'):
		follower_1_Ly = rospy.get_param('follower_2_Ly')
	else:
		rospy.set_param('follower_2_Ly', follower_2_Ly)

def get_manual_parameter(follower_nr):
	
	formation_parameter = Formation()
	
	if follower_nr == 1:
		formation_parameter.Lx = rospy.get_param('follower_1_Lx')
		formation_parameter.Ly = rospy.get_param('follower_1_Ly')
	
	if follower_nr == 2:
		formation_parameter.Lx = rospy.get_param('follower_2_Lx')
		formation_parameter.Ly = rospy.get_param('follower_2_Ly')
	
	return formation_parameter


def simple_formation(follower_nr, formation_publisher):
	
	formation_parameter = Formation()

	if follower_nr == 1:
		formation_parameter.Lx = 1
		formation_parameter.Ly = 0
	elif follower_nr == 2:
		formation_parameter.Lx = -1
		formation_parameter.Ly = 0

	formation_publisher.publish(formation_parameter)


def v_formation(follower_nr, formation_publisher):
	
	formation_parameter = Formation()
	
	if follower_nr == 1:
		formation_parameter.Lx = 1
		formation_parameter.Ly = 1
	elif follower_nr == 2:
		formation_parameter.Lx = -1
		formation_parameter.Ly = 1

	formation_publisher.publish(formation_parameter)


def v2_formation(follower_nr, formation_publisher):
	
	formation_parameter = Formation()
	
	if follower_nr == 1:
		formation_parameter.Lx = 1
		formation_parameter.Ly = -1
	elif follower_nr == 2:
		formation_parameter.Lx = -1
		formation_parameter.Ly = -1
		
	formation_publisher.publish(formation_parameter)

def line_formation(follower_nr, formation_publisher):
	
	formation_parameter = Formation()
	
	if follower_nr == 1:
		formation_parameter.Lx = 0
		formation_parameter.Ly = 1
	elif follower_nr == 2:
		formation_parameter.Lx = 0
		formation_parameter.Ly = 4
		
	formation_publisher.publish(formation_parameter)
	
def line_formation_v2(follower_nr, formation_publisher):
	
	formation_parameter = Formation()
	
	if follower_nr == 1:
		formation_parameter.Lx = 0
		formation_parameter.Ly = -4
	elif follower_nr == 2:
		formation_parameter.Lx = 0
		formation_parameter.Ly = -1
		
	formation_publisher.publish(formation_parameter)
	
def line_above(follower_nr, formation_publisher):
	
	formation_parameter = Formation()
	
	if follower_nr == 1:
		formation_parameter.Lx = 0
		formation_parameter.Ly = -1
	elif follower_nr == 2:
		formation_parameter.Lx = 0
		formation_parameter.Ly = -4
		
	formation_publisher.publish(formation_parameter)
	
def manual(follower_nr, formation_publisher):
	
	manual_parameter  = get_manual_parameter(follower_nr)
	
	formation_parameter = Formation()
	
	if follower_nr == 1:
		formation_parameter.Lx = manual_parameter.Lx
		formation_parameter.Ly = manual_parameter.Ly
	elif follower_nr == 2:
		formation_parameter.Lx = manual_parameter.Lx
		formation_parameter.Ly = manual_parameter.Ly
	
	
	print ('Formation parameter '), formation_parameter
	formation_publisher.publish(formation_parameter)

	
def set_formation_parameter(follower_nr, formation_publisher):
		
		formation_nr = get_formation_type()
		
		if formation_nr == 0:
			simple_formation(follower_nr, formation_publisher)
		elif formation_nr == 1:
			v_formation(follower_nr, formation_publisher)
		elif formation_nr == 2:
			v2_formation(follower_nr, formation_publisher)
		elif formation_nr == 3:
			line_formation(follower_nr, formation_publisher)
		elif formation_nr == 4:
			line_formation_v2(follower_nr, formation_publisher)
		elif formation_nr == 5:
			line_above(follower_nr, formation_publisher)
		elif formation_nr == 6:
			manual(follower_nr, formation_publisher)
		else:
			simple_formation(follower_nr, formation_publisher)

	
def main(follower_1_name, follower_2_name):
	
	
	rospy.init_node('formation_controller')	
		
	formation_follower_1 = rospy.Publisher('formation_control_' + follower_1_name, Formation, queue_size=10)
	formation_follower_2 = rospy.Publisher('formation_control_' + follower_2_name, Formation, queue_size=10) 
	
	rate = rospy.Rate(10)
	
	set_manual_formation_parameter()
	
	while not rospy.is_shutdown():
		
		
		set_formation_parameter(1, formation_follower_1)
		set_formation_parameter(2, formation_follower_2)
		
		rate.sleep()
		
		
		
    
if __name__ == '__main__':
	try:
		main(sys.argv[1], sys.argv[2])
	except rospy.ROSInterruptException:
		pass
