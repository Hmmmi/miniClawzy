"""
detecting.detecting.sub_cam 的 Docstring

@Author:        Hmmmi
@Description:   Subscribe the camera img of miniClawzy
                , and maybe detecting based on YOLO 
@Created Date:  2025-12-11
"""

import rclpy
import cv2

from rclpy.node         import Node
from sensor_msgs.msg    import Image
from cv_bridge          import CvBridge

class CameraImgSubscriber(Node):

    def __init__(self, name):
        super().__init__(name)

        # (msg_type, topic_name, listener, qsprofile)
        self.sub = self.create_subscription(
            Image, 'image_raw', self.listener_callback, 10)
        self.cv_bridge = CvBridge()

    def listener_callback(self, data):
        frame = self.cv_bridge.imgmsg_to_cv2(data, 'bgr8')
        self.get_logger().info('Got img msg!')
        print(f'frame size: {len(frame)}')
        cv2.imshow("Ras-Cam", frame)
        cv2.waitKey(10)


def main(args=None):
    rclpy.init(args=args)
    node = CameraImgSubscriber("topic_sub_cam")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()