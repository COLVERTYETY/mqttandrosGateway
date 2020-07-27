#! /usr/bin/env python3

import rospy
import std_msgs.msg as ms

########################################

topic = "mqttin"
messagetype = ms.String
mq = 10
gateway_name = "mqttIN"

########################################


def talker():  # setup the pub and launch to main loop
    pub = rospy.Publisher(topic, messagetype, queue_size=mq)
    rospy.init_node(gateway_name, anonymous=True)
    rospy.loginfo("mqtt_to_ros gateway started succesfully !!")
    while not rospy.is_shutdown():  # ################## this is main loop
        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        # pub.publish(hello_str)
        pass


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
