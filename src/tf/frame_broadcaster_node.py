#!/usr/bin/env python3
import rospy
import tf
import tf.transformations as conversion_of_transformations
import time

rospy.init_node("frame_broadcaster", anonymous= True)
transform_broadcaster = tf.TransformBroadcaster()

i = 0
while not rospy.is_shutdown():
    if (i > 45):
        i = 0

    rotation_quaternion = conversion_of_transformations.quaternion_from_euler(0.0, i, 0.0)
    traslation_vector = (0.0, 0.0, 0.0)
    
    transform_broadcaster.sendTransform(traslation_vector, rotation_quaternion, rospy.Time.now(), "link_1", "laser")
    print(f"Pitch in angle: {i}\n")

    i = i + 1

rospy.spin()