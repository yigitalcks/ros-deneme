#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Rotate():
    def __init__(self, clokweise, angular_speed_degree, relative_angle_degree):
        rospy.init_node("rotate", anonymous = True)

        angular_speed = math.radians(abs(angular_speed_degree))


        velocity_message = Twist()
        pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 10)
        sub = rospy.Subscriber("/turtle1/pose", Pose, self.posecallBack)

        if clokweise:
            velocity_message.angular.z = -abs(angular_speed)
        else:
            velocity_message.angular.z = abs(angular_speed)

        loop_rate = rospy.Rate(10)
        t0 = rospy.Time.now().to_sec()

        while True:
            
            rospy.loginfo("Rotates")
            pub.publish(velocity_message)

            t1 = rospy.Time.now().to_sec()
            current_angle_degree = (t1 - t0) * angular_speed_degree

            if current_angle_degree >= relative_angle_degree or rospy.is_shutdown():
                rospy.loginfo("reached")
                break
        
            loop_rate.sleep()
        velocity_message.angular.z = 0.0
        pub.publish(velocity_message)

    def posecallBack(self, pos):
        rospy.loginfo(pos.theta)
        

Rotate(1, 5, 180)

            
