#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud2
import tf2_ros
from tf2_sensor_msgs.tf2_sensor_msgs import do_transform_cloud

def callback_function(message):
    global link_1_pointcloud

    transform_buffer = tf2_ros.Buffer()
    transform_listener = tf2_ros.TransformListener(transform_buffer)
    
    current_transformation = transform_buffer.lookup_transform("laser", "link1", rospy.Time(0,0), rospy.Duration(1.0))

    link_1_pointcloud = do_transform_cloud(message, current_transformation)

    pointcloud2_publisher.publish(link_1_pointcloud)

if __name__ == "__main__":
    rospy.init_node("pointcloud_transform_listener_tf2")

    link_1_pointcloud = PointCloud2()
            
    pointcloud2_fixed_subscriber = rospy.Subscriber("/my_pointclouds2_fixed", PointCloud2, callback_function)

    pointcloud2_publisher = rospy.Publisher("/my_pointclouds2", PointCloud2, queue_size= 10)

    rospy.spin()