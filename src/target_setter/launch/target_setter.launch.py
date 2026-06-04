from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'communication',
            namespace = 'listener',
            executable = 'udp_listener_node',
            name = 'udp_listener_node'
        ),
        Node(
            package = 'communication',
            namespace = 'sender',
            executable = 'udp_sender_node',
            name = 'udp_sender_node'
        ),
        Node(
            package = 'hardware_interface',
            namespace = 'can_driver',
            executable = 'can_driver_node',
            name = 'can_driver_node'
        ),
        Node(
            package = 'hardware_interface',
            namespace = 'hfi_a9',
            executable = 'hfi_a9_node',
            name = 'hfi_a9_node'
        ),
        Node(
            package = 'hardware_interface',
            namespace = 'inverse_kinematic',
            executable = 'inverse_kinematic_node',
            name = 'inverse_kinematic_node'
        ),
        Node(
            package = 'hardware_interface',
            namespace = 'odometry',
            executable = 'odometry_node',
            name = 'odometry_node'
        ),
        Node(
            package = 'manipulation',
            namespace = 'gripper_control',
            executable = 'gripper_control_node',
            name = 'gripper_control_node'
        ),
        Node(
            package = 'navigation',
            namespace = 'mission_planner',
            executable = 'mission_planner_node',
            name = 'mission_planner_node'
        ),
        Node(
            package = 'perception',
            namespace = 'distance_estimation',
            executable = 'distance_estimation_node',
            name = 'distance_estimation_node'
        ),
        Node(
            package = 'perception',
            namespace = 'object_detection',
            executable = 'object_detection_node',
            name = 'object_detection_node'
        ),
        Node(
            package = 'control',
            namespace = 'robot_control',
            executable = 'robot_control_node',
            name = 'robot_control_node'
        )
    ])