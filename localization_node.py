#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

nodeName = 'messagesubscriber'
topicName = 'information'

def callbackFunction(message):
    print("we received %d"%message.data)

rospy.init_node(nodeName)
rospy.Subscriber(topicName, Int32, callbackFunction)

rospy.spin()
