import rclpy
from rclpy.node import Node   #we inherit from Node

from  std_msgs.msg import String    #as message type is string 

#for creating node we need a class that inherits from Node
class ListenerNode(Node):
    def __init__(self): #constructor
        super().__init__("talker_node")
        self.subscription = self.create_subscription(String, 'node1', self.listener_callback, 10)  #10 is the queue size

    def listener_callback(self,msg):
        #printing message
        self.get_logger().info(f"Received {msg.data}")



def main(args=None):
    rclpy.init(args=args)

    #create node 
    listenerNode = ListenerNode()

    #use node 
    rclpy.spin(listenerNode) #spin makes sure that node is alive 

    #destroy node 
    listenerNode.destroy_node()
    rclpy.shutdown() #shutdown the context

if __name__== "__main__":
    main()
