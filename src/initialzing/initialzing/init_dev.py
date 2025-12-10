"""
@Author:        Hmmmi
@Description:   initialzing devices of miniClawzy
@Created Date:  2025-12-09
"""

import rclpy
from rclpy.node import Node
import time

from .ros_control.ros_robot_controller_sdk import Board

# pwm舵机初始位置
pwm_start_positions = [
    [1, 1500],
    [3, 900],
    [4, 2400],
    [5, 1000],
    [6, 1500]
]

"""
初始化机械臂舵机位置
"""
def init_pwm_positions():
    board = Board()
    for position in reversed(pwm_start_positions):
        board.pwm_servo_set_position(2, [position])
        print(f'init pwm {position}')
        time.sleep(2)

def main(args=None):                                    # ROS2节点主入口 main函数
    rclpy.init(args=args)                               # ROS2 Python接口初始化
    node = Node("init_dev")                             # 创建Node对象并进行初始化
    
    if rclpy.ok():
        init_pwm_positions()
        node.get_logger().info('Initializing Over!!')

    # rclpy.spin_once(node)
    # rclpy.spin(node)                                    # 循环等待ROS2退出
    node.destroy_node()                                 # 销毁Node对象
    rclpy.shutdown()                                    # 关闭ROS2 Python接口