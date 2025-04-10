import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    planner_arg = DeclareLaunchArgument(
        'arm_planner',
        default_value='PRM',
        description='ID планировщика для MoveIt'
    )
    arm_planner = LaunchConfiguration('arm_planner')

    moveit_node = Node(
        package='youbot_moveit',
        executable='script',  
        name='script',
        output='screen',
        parameters=[{'arm_planner': arm_planner}],
    )
    
    return LaunchDescription([
        planner_arg,
        moveit_node
    ])
