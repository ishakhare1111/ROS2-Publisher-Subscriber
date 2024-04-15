# ROS2-Publisher-Subscriber
This ROS2 project consists of two nodes: a publisher node and a subscriber node. The publisher node sends the message "hello" on the topic '/node1', while the subscriber node listens to the same topic and prints the incoming data to the terminal. This simple demonstration showcases the basic communication between nodes in a ROS2 environment.


## Setup

Before running the ROS 2 nodes, necessary dependencies must be installed and configured.

### Dependencies
Added the following dependencies to package.xml file:

<pre>
<exec_depend>rclpy</exec_depend>
<exec_depend>std_msgs</exec_depend>
</pre>

### Setup Configuration

Modified setup.py file to include the ROS 2 nodes as console scripts:

<pre>
entry_points={
        'console_scripts': [
            'talkerNode = talker_listener.talker_node:main',
            'listenerNode = talker_listener.listener_node:main'
        ],
    },
</pre>
This configuration helps in running the talkerNode and listenerNode directly from the command line.
