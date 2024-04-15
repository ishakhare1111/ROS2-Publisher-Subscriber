import rclpy
from rclpy.node import Node

from  std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):   # constructor
        super().__init__("talker_node")   # initialise base class
        self.publisher_= self.create_publisher(String, 'node1', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        #creating message
        msg = String()
        msg.data = f"Hello {self.count}"
        self.publisher_.publish(msg)
        self.count += 1
        self.get_logger().info(f"{msg.data}")


def main(args=None):
    rclpy.init(args=args)  

    #create instance of the node
    talkerNode = TalkerNode()

    #use node
    rclpy.spin(talkerNode) #spins until we kill the node

    #destroy node 
    talkerNode.destroy_node()


    rclpy.shutdown()

if __name__== "__main__":
    main()
