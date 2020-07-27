#! /usr/bin/env python3

import rospy
import std_msgs as ms

########################################

topic = "mqttout"
messagetype = ms.String
mq = 10
gateway_name = "mqttOUT"

########################################


def roscallback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def listener():  # this is the main loop
    # here we must connect to mqtt
    rospy.init_node(gateway_name, anonymous=True)
    rospy.Subscriber(topic, messagetype, roscallback)
    rospy.loginfo("ros_to_mqtt gateway sucessfully started !!")
    rospy.spin()   # while true:


if __name__ == '__main__':
    listener()
