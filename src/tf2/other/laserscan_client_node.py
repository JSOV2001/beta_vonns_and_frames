#!/usr/bin/env python3
import roslib
roslib.load_manifest('laser_assembler')
import rospy
from laser_assembler.srv import AssembleScans2
from sensor_msgs.msg import PointCloud2

#Inicializar el nodo.
rospy.init_node("laser_assembler_client_tf2")

#Espera a que el service "assemble_scans" se encuentre activado.
rospy.wait_for_service("/assemble_scans2")

#Se crea el ROS Client Node.
assemble_scans = rospy.ServiceProxy('/assemble_scans2', AssembleScans2)

#Se crea el ROS Publisher Node.
pointclouds2_publisher = rospy.Publisher("/my_pointclouds2_fixed", PointCloud2, queue_size=10)

#Se asigna la frecuencia para enviar mensajes.
frequency_object = rospy.Rate(1)

while not rospy.is_shutdown():
    try:
        #Se asume la respuesta de la solicitud del ROS Client.
        response_object = assemble_scans(rospy.Time(0,0), rospy.get_rostime())

        pointclouds2_publisher.publish(response_object.cloud)

        frequency_object.sleep()
        
    except rospy.ServiceException as e:
        print(f"Service call failed: {e}")
    