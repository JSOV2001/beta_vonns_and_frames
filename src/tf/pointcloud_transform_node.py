#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud
import tf

def callback_function(message):
    global laser_pointcloud
    global link_1_pointcloud
    transform_listener = tf.TransformListener()

    laser_pointcloud.header = message.header
    laser_pointcloud.points = message.points
    laser_pointcloud.channels = message.channels

    transform_listener.waitForTransform("link_1", "laser", rospy.Time.now(), rospy.Duration(4.0))
    new_pointcloud = transform_listener.transformPointCloud("link_1", laser_pointcloud)

    link_1_pointcloud.header = new_pointcloud.header
    link_1_pointcloud.points = new_pointcloud.points
    link_1_pointcloud.channels = new_pointcloud.channels
    print(f"\nGot cloud with {len(link_1_pointcloud.points)} points")
    rviz_publisher = rospy.Publisher("/laser_pointcloud", PointCloud, queue_size= 10)
    rviz_publisher.publish(link_1_pointcloud)

if __name__ == "__main__":
    rospy.init_node("pointcloud_transform")
    
    laser_pointcloud = PointCloud()
    link_1_pointcloud = PointCloud()
            
    pointcloud_subscriber = rospy.Subscriber("/my_points", PointCloud, callback_function)

    rospy.spin()