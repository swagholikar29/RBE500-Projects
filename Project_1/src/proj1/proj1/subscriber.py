import rclpy
from rclpy.node import Node

from sensor_msgs.msg import JointState
from geometry_msgs.msg import Pose

import math
import numpy as np


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.listener_callback,
            1)

        self.subscription = self.create_subscription(
            Pose,
            'hw4_topic',
            self.listener_callback_inverse,
            1)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        
        q1=msg.position[0]
        q2=msg.position[1]
        q3=msg.position[2]
        
        l1=2.0 
        l2=1.0
        l3=1.0
        
        A1 = np.array([[math.cos(q1),-math.sin(q1),0,l2*math.cos(q1)],[math.sin(q1),math.cos(q1),0,l2*math.sin(q1)],[0,0,1,l1],[0,0,0,1]])
        A2 = np.array([[math.cos(q2),(-math.sin(q2)),0,(l3*math.cos(q2))],[math.sin(q2),math.cos(q2),0,(l3*math.sin(q2))],[0,0,1,0],[0,0,0,1]])
        A3 = np.array([[1,0,0,0],[0,-1,0,0],[0,0,-1,-q3],[0,0,0,1]])
        
        h_temp=np.matmul(A1,A2)
        H=np.matmul(h_temp,A3)

        
        
        self.get_logger().info('The matrix is : \n')

        print(H)

    def listener_callback_inverse(self, msg):
        
        xc = msg.position.x
        yc = msg.position.y
        zc = msg.position.z


        l1 = 2.0	#l1 link length is 2.0 units
        l2 = 2.0	# l2 link length is 2.0 units
        l3 = 2.0	# l3 link length is 2.0 units
        

        ### The following inverse kinematics calculations are done by trignometry and the cosine rule.
        Q1 = np.arctan2([yc],[xc]) -np.arctan2([l2+l3*math.cos(q2)],[l3*math.sin(q2)])
        Q2 = np.arctan2([math.cos(q2)],[np.sqrt(1-1)])
        Q3=l1-zc


        self.get_logger().info("The Q1, Q2 and Q3 are (%f,%f,%f)"%(Q1,Q2,Q3))
        



def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
