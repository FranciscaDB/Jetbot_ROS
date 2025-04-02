#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import numpy as np

class FilteredLidar(Node):
    def __init__(self):
        super().__init__('filtered_lidar_node')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            100)
        self.publisher = self.create_publisher(
            LaserScan,
            '/filtered_scan',
            100)

        self.declare_parameter('min_angle', -1.5)  # Rango de -30° a 30° (en radianes)
        self.declare_parameter('max_angle', 1.5)
        self.declare_parameter('min_distance', 0.05)  # Min 5cm
        self.declare_parameter('max_distance', 1.0)  # Max 1m
    

    def scan_callback(self, msg):
        min_angle = self.get_parameter('min_angle').get_parameter_value().double_value
        max_angle = self.get_parameter('max_angle').get_parameter_value().double_value
        min_distance = self.get_parameter('min_distance').get_parameter_value().double_value
        max_distance = self.get_parameter('max_distance').get_parameter_value().double_value

        # Crear una copia del mensaje original para modificarlo
        filtered_msg = LaserScan()
        filtered_msg.header = msg.header
        filtered_msg.header.frame_id = 'laser'
        filtered_msg.header.stamp = self.get_clock().now().to_msg()
        filtered_msg.angle_min = msg.angle_min
        filtered_msg.angle_max = msg.angle_max
        filtered_msg.angle_increment = msg.angle_increment
        filtered_msg.time_increment = msg.time_increment
        filtered_msg.scan_time = msg.scan_time
        filtered_msg.range_min = min_distance
        filtered_msg.range_max = max_distance

        # Convertir índices a ángulos
        num_readings = len(msg.ranges)
        angles = np.linspace(msg.angle_min, msg.angle_max, num_readings)

        # Filtrar datos
        filtered_ranges = []
        for i in range(num_readings):
            if min_angle <= angles[i] <= max_angle and min_distance <= msg.ranges[i] <= max_distance:
                filtered_ranges.append(msg.ranges[i])
            else:
                filtered_ranges.append(float('inf'))  # Se descartan valores fuera del rango

        filtered_msg.ranges = filtered_ranges
        filtered_msg.intensities = msg.intensities

        self.publisher.publish(filtered_msg)
        self.get_logger().info('Publicando datos filtrados del LiDAR')

def main(args=None):
    rclpy.init(args=args)
    node = FilteredLidar()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
