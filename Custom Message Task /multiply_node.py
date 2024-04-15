import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class CustomPublisher(Node):
    def __init__(self):
        super().__init__('custom_publisher')
        self.num1 = 0
        self.num2 = 0
        self.num1 = int(input("Enter initial value for num1: "))
        self.num2 = int(input("Enter initial value for num2: "))
        self.publisher_twos = self.create_publisher(Int64, '/data_twos', 10)
        self.publisher_fives = self.create_publisher(Int64, '/data_fives', 10)
        self.timer = self.create_timer(1, self.publish_numbers)

    def publish_numbers(self):
        self.num1 *= 2
        self.num2 *= 5
        msg1 = Int64()
        msg2 = Int64()
        msg1.data = self.num1
        msg2.data = self.num2
        self.publisher_twos.publish(msg1)
        self.publisher_fives.publish(msg2)
        self.get_logger().info(f"num1= {msg1.data}, num2= {msg2.data}")

    '''def timer_callback(self):
        #creating message
        msg = String()
        msg.data = f"Hello {self.count}"
        self.publisher_.publish(msg)
        self.count += 1
        self.get_logger().info(f"{msg.data}")'''

        

def main(args=None):
    rclpy.init(args=args)
    custom_publisher = CustomPublisher()
    rclpy.spin(custom_publisher)
    custom_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
