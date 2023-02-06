from tutorial_interfaces.srv import FirstService

import rclpy
from rclpy.node import Node

import numpy as np


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(FirstService, 'inverse', self.service_callback)

    def service_callback(self, request, response):
        #response.sum = request.a + request.b
        
        x=request.x
        y=request.y
        z= request.z
        
        
        l1=2.0
        l2=1.0
        l3=1.0
        
        Q3=l1-z
        
        n=(x**2+y**2-l2**2-l3**2)
        d=2*l2*l3
        
        Q2=np.arccos(n/d)
        
        
        n_1=(l2+l3*np.cos(Q2))*x +(l3*np.sin(Q2)*y)
        d_1=(l2+l3*np.cos(Q2))**2+(l3*np.sin(Q2))**2
        
        Q1=np.arccos(n_1/d_1)
        
        self.get_logger().info('The Joint values are Q1: %f Q2: %f and Q3:%f' % (Q1,Q2,Q3))
        
        response.q1=Q1
        response.q2=Q2
        response.q3=Q3

        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
