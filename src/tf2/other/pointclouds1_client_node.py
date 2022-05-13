#!/usr/bin/env python3
import roslib
roslib.load_manifest('laser_assembler')
import rospy
from laser_assembler.srv import AssembleScans
from sensor_msgs.msg import PointCloud

if __name__ == "__main__":
    #Inicializar el nodo.
    rospy.init_node("pointclouds1_assembler_client")

    #Espera a que el service "assemble_scans" se encuentre activado.
    rospy.wait_for_service("/assemble_scans")

    #Se crea el ROS Client Node.
    assemble_scans = rospy.ServiceProxy('/assemble_scans', AssembleScans)

    #Se crea el ROS Publisher Node.
    rviz_publisher = rospy.Publisher("/pointclouds1_assembled", PointCloud, queue_size=10)

    #Se asigna la frecuencia para enviar mensajes.
    frequency_object = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            #Se asume la respuesta de la solicitud del ROS Client.
            response_object = assemble_scans(rospy.Time(0,0), rospy.get_rostime())

            print(f"Got cloud with {len(response_object.cloud.points)} points")

            rviz_publisher.publish(response_object.cloud)
            
            frequency_object.sleep()
            
        except rospy.ServiceException as e:
            print(f"Service call failed: {e}")