"""
@Author:        Hmmmi
@Description:   Publishing the camera img of miniClawzy
@Created Date:  2025-12-10
"""

import rclpy
import cv2

from rclpy.node import Node
from sensor_msgs.msg import Image   # 图像消息类型
from cv_bridge import CvBridge      # ROS与OpenCV图像转换类

class CameraImgPubliser(Node):

    def __init__(self, name):
        super().__init__(name)
        
        # msg_type(any), topic_name(str), qsprofile(int)
        self.publisher = self.create_publisher(Image, "image_raw", 10)
        # 定时器，周期执行回调函数(any)
        # 即周期发布图像
        self.timer = self.create_timer(0.15, self.timer_callback)
        
        self.cap = cv2.VideoCapture(0)
        self.cv_bridge = CvBridge()

    def timer_callback(self):
        success, frame = self.cap.read()

        if success:
            msg = self.cv_bridge.cv2_to_imgmsg(frame, 'bgr8')
            self.publisher.publish(msg)
        
        self.get_logger().info('Publishing camera frame')

def main(args=None):
    rclpy.init(args=args)
    node = CameraImgPubliser("topic_pub_cam")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()