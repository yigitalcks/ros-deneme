#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class turtle():
    x0 = 5.44
    y0 = 5.44
    theta = 0

    def __init__(self, speed, distance, is_forward):

        rospy.init_node("turtlesim_motion_pose", anonymous=True)
        velocity_message = Twist()

        self.x = turtle.x0
        self.y = turtle.y0

        if is_forward:
            velocity_message.linear.x = abs(speed)
        else:
            velocity_message.linear.x = -abs(speed)

        distance_moved = 0.0
        loop_rate = rospy.Rate(10)

        cmd_vel_topic = "/turtle1/cmd_vel"
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        pose_topic = "/turtle1/pose"
        rospy.Subscriber(pose_topic, Pose, self.poseCallback)

        velocity_publisher.publish(velocity_message)

        while True:
            loop_rate.sleep()
            velocity_publisher.publish(velocity_message)
            distance_moved = abs(math.sqrt((self.x - turtle.x0)*2 - (self.y - turtle.y0)*2))
            rospy.loginfo("Distance moved: " + str(distance_moved))
            rospy.loginfo("x = {}, y = {}" .format(self.x, self.y))
            if distance_moved >= distance:
                rospy.loginfo("reached")
                break
    
    def poseCallback(self, pose_message):

        self.x = pose_message.x
        self.y = pose_message.y
        self.yaw = pose_message.theta            
        rospy.loginfo("{} {} {}" .format(self.x, self.y, self.yaw))

    


if __name__ == "__main__":
    turtle(0.5, 15, True)
    
    

    


    