#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):

	if msg.data == "ping":
		rospy.loginfo('"Pong"')
	else:
		rospy.loginfo('"Failed!"')
	
rospy.init_node('pong_node', anonymous=True)
pub = rospy.Publisher("/pong", String, queue_size=10)
sub = rospy.Subscriber("/ping", String, callback)
rospy.spin()
