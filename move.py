#!/usr/bin/env python3

import time
import rospy 
from geometry_msgs.msg import Twist


class Movement():

	def __init__(self):
		rospy.init_node("My_node",anonymous=False)
		rospy.on_shutdown(self.shutdown)
		self.cmd_vel=rospy.Publisher('pioneer/cmd_vel', Twist, queue_size=1)
		
		t_0 = rospy.get_time()
		move_cmd = Twist()
		r=rospy.Rate(100)
		
		while(rospy.get_time() == 0.00000):
			print("wait..")
			
#--------------------1h kinisi----------------
		t_b= 0.39
		t_f=3	
		acceleration = 0.453
		u_coast = acceleration * t_b
		
		while((rospy.get_time() - t_0) <= t_b):
			move_cmd.angular.z = acceleration * (rospy.get_time() - t_0 ) 
			print(move_cmd.angular.z)
			
			self.cmd_vel.publish(move_cmd)
			#r.sleep()
	
		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		#rospy.sleep(1)

		while((rospy.get_time() - t_0) <= (t_f -t_b)):
			move_cmd.angular.z =  u_coast
			print(move_cmd.angular.z)

			self.cmd_vel.publish(move_cmd)
			#r.sleep()
			

		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		
		t_f_minus_t_b = rospy.get_time() - 0.00001
		while((rospy.get_time() - t_0) <= t_f):

			move_cmd.angular.z = u_coast - ( 0.453 * (rospy.get_time() - t_f_minus_t_b ) )
			print(move_cmd.angular.z)
			self.cmd_vel.publish(move_cmd)
			#r.sleep()

		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		#rospy.sleep(1)
		
#---------------telos 1hs kinisis	----------------
		
		
#---------2h kinisi------------------------------
		t_0=rospy.get_time()
		t_f=150 
		t_b=1.51
		d=22.36
		acceleration = 0.1
		while((rospy.get_time() - t_0) <=  t_b ):
			move_cmd.linear.x =  acceleration * (rospy.get_time() - t_0) 
			self.cmd_vel.publish(move_cmd)
		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		u_coast = t_b * acceleration
		while((rospy.get_time() - t_0) <=  t_f - (t_b ) ):
			move_cmd.linear.x = u_coast
			self.cmd_vel.publish(move_cmd)
			print(move_cmd.linear.x,"vel")
		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		
		t_f_minus_t_b = rospy.get_time() - 0.00001
		while((rospy.get_time() - t_0) <=  (t_f ) ):
			move_cmd.linear.x =  u_coast - acceleration * (rospy.get_time() - t_f_minus_t_b ) 
			print(move_cmd.linear.x,"vel")
			self.cmd_vel.publish(move_cmd)
			

		
		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)

#---------telos 2hs kinisi----------------------		
		
		
#---------3h kinisi------------------------------
		u_0 = 0.46 
		t_0=rospy.get_time()
		t_f=10
		u_f=4.71
		t_b=1.42
		acceleration = 0.35
		u_coast = t_b * acceleration
		
		while((rospy.get_time() - t_0) <= t_b):
			move_cmd.angular.z = acceleration * (rospy.get_time() - t_0 ) 
			print(move_cmd.angular.z)
			self.cmd_vel.publish(move_cmd)
			#r.sleep()
	
		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		#rospy.sleep(1)

		while((rospy.get_time() - t_0) <= (t_f - t_b)):
			move_cmd.angular.z =  u_coast
			print(move_cmd.angular.z)

			self.cmd_vel.publish(move_cmd)
			#r.sleep()
			

		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		
		t_f_minus_t_b = rospy.get_time() - 0.00001
		while((rospy.get_time() - t_0) <= t_f):

			move_cmd.angular.z = u_coast - ( 0.35 * (rospy.get_time() - t_f_minus_t_b ) )
			print(move_cmd.angular.z)
			self.cmd_vel.publish(move_cmd)
			#r.sleep()

		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		#rospy.sleep(1)
		
		
		
#---------telos 3hs kinisi----------------------				


#---------4h kinisi------------------------------
		t_0=rospy.get_time()
		t_f=150
		t_b=1.34
		acceleration = 0.1
		u_coast = t_b * acceleration #0.134
				
		while((rospy.get_time() - t_0) <=  t_b ):
			move_cmd.linear.x =  acceleration * (rospy.get_time() - t_0) 
			self.cmd_vel.publish(move_cmd)
		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)

		while((rospy.get_time() - t_0) <=  t_f - (t_b ) ):
			move_cmd.linear.x = u_coast
			self.cmd_vel.publish(move_cmd)
			print(move_cmd.linear.x,"vel")
		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		
		t_f_minus_t_b = rospy.get_time() - 0.00001
		while((rospy.get_time() - t_0) <=  (t_f ) ):
			move_cmd.linear.x =  u_coast - acceleration * (rospy.get_time() - t_f_minus_t_b ) 
			print(move_cmd.linear.x,"vel")
			self.cmd_vel.publish(move_cmd)
			

		
		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)

#---------telos 4hs kinisi----------------------		

#---------5h kinisi------------------------------
		u_0 = 0.46 
		t_0=rospy.get_time()
		t_f=7
		u_f=2.05
		t_b=1.35
		acceleration = -0.34
		u_coast = t_b * acceleration
		
		while((rospy.get_time() - t_0) <= t_b):
			move_cmd.angular.z = acceleration * (rospy.get_time() - t_0 ) 
			print(move_cmd.angular.z)
			self.cmd_vel.publish(move_cmd)
			#r.sleep()
	
		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		#rospy.sleep(1)

		while((rospy.get_time() - t_0) <= (t_f - t_b)):
			move_cmd.angular.z =  u_coast
			print(move_cmd.angular.z)

			self.cmd_vel.publish(move_cmd)
			#r.sleep()
			

		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		
		t_f_minus_t_b = rospy.get_time() - 0.00001
		while((rospy.get_time() - t_0) <= t_f):

			move_cmd.angular.z = u_coast - ( acceleration * (rospy.get_time() - t_f_minus_t_b ) )
			print(move_cmd.angular.z)
			self.cmd_vel.publish(move_cmd)
			#r.sleep()

		move_cmd=Twist()
		self.cmd_vel.publish(move_cmd)
		#rospy.sleep(1)
		
		
		
#---------telos 5hs kinisi----------------------
		
	def shutdown(self):
		rospy.loginfo("Stop the robot")
		self.cmd_vel.publish(Twist())
		rospy.sleep(1)
			
if __name__ == '__main__':
	try:
		Movement()
	except:
		rospy.loginfo("skata")
