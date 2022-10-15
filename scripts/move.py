#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import S
import sys
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Turtel():
    pose_topic = "/turtle1/pose"
    speed_topic = "/turtle1/cmd_vel"

    c_angular = 4

    def __init__(self):
        rospy.Subscriber(Turtel.pose_topic, Pose, self.poseCallback)
        self.pub = rospy.Publisher(Turtel.speed_topic, Twist, queue_size=10)
        self.velocity_message = Twist()

    def toGoal(self, x_goal, y_goal):
        rospy.init_node("toGoal", anonymous = True)

        loop = rospy.Rate(10)

        c_linear = 0.5
         
        while True:
            
            distance = abs(math.sqrt((x_goal - self.x) ** 2) - ((y_goal - self.y) ** 2))
            linear_speed = distance * c_linear
            self.rotate(x_goal, y_goal)

            self.velocity_message.linear.x = linear_speed

            if distance < 0.2 or rospy.is_shutdown():
                rospy.loginfo("reached")
                break

            self.pub.publish(self.velocity_message)
            loop.sleep()

        self.velocity_message.linear.x = 0.0
        self.pub.publish(self.velocity_message)

    def rotate(self, x_goal, y_goal):
        angle_goal = math.atan2(y_goal - self.y, x_goal - self.x)
        angular_speed = (angle_goal - self.yaw) * Turtel.c_angular

        self.velocity_message.angular.z = angular_speed    
        

    def poseCallback(self, location):
        self.x = location.x
        self.y = location.y
        self.yaw = location.theta
        rospy.loginfo("x: {} y: {}" .format(self.x, self.y))

if __name__ == "__main__" :
    a = Turtel()
    a.toGoal(1.0, 0.5)    


