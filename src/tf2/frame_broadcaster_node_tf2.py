#!/usr/bin/env python3
import rospy
import tf2_ros
from tf_conversions import transformations 
from geometry_msgs.msg import TransformStamped
import time
import math

rospy.init_node("transform_broadcaster_tf2")
transform_broadcaster = tf2_ros.TransformBroadcaster()

while not rospy.is_shutdown():
    angle = 0
    while angle < 45:
        if(angle == 44):
            angle = 0
        
        transform_broadcaster = tf2_ros.TransformBroadcaster()
        transformation_data = TransformStamped()

        #Se define los frames en cuestion
        transformation_data.header.frame_id = "laser"
        transformation_data.child_frame_id = "link1"
        #Se define cuando se toma la ultima transformacion del frame
        transformation_data.header.stamp = rospy.Time.now()
        #Se definen los datos de la traslacion
        transformation_data.transform.translation.x = 0.0
        transformation_data.transform.translation.y = 0.0
        transformation_data.transform.translation.z = 0.0
        #Se definen los datos de la rotacion
        quaternions = transformations.quaternion_from_euler(0.0, math.radians(angle), 0.0)
        transformation_data.transform.rotation.x = quaternions[0]
        transformation_data.transform.rotation.y = quaternions[1]
        transformation_data.transform.rotation.z = quaternions[2]
        transformation_data.transform.rotation.w = quaternions[3]

        transform_broadcaster.sendTransform(transformation_data)

        angle = angle + 1 

        time.sleep(1)