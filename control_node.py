#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
 

nodeName = 'messagePublisher' 
topicName = 'information'

rospy.init_node(nodeName, anonymous=True)

publisher1=rospy.Publisher(topicName,Int32, queue_size=5)

ratePublisher = rospy.Rate(1)
intMessage = 0

while not rospy.is_shutdown():

    rospy.loginfo(intMessage)
    publisher1.publish(intMessage)
    intMessage = intMessage+1
    ratePublisher.sleep()
