from tutorial_interfaces.srv import FirstService
from tutorial_interfaces.srv import SecondService
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray


import rclpy
from rclpy.node import Node
import numpy as np
import math

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')

        self.srv1 = self.create_service(FirstService, 'joint_to_endeffector', self.service_callback_1)
        self.srv2 = self.create_service(SecondService, 'endeffector_to_joint', self.service_callback_2)

        # self.j1=0
        # self.j2=0
        # self.j3=0
        
        self.J=np.zeros((6,3))

        # self.e1=0
        # self.e2=0
        # self.e3=0

        #create subscription
        self.subscription_1 = self.create_subscription(
            JointState,
            '/joint_states',
            self.listener_callback,
            10)
        self.subscription_1


    def service_callback_1(self, request, response):
        #response.sum = request.a + request.b

        #response.endeffector = J*request.joint
        
        jv1=request.x
        jv2=request.y
        jv3=request.z

        JV=np.array([[jv1],[jv2],[jv3]])
        
        EV=np.matmul(self.J,JV)


                
        response.ex=float(EV[0])
        response.ey=float(EV[1])
        response.ez=float(EV[2])
        response.ewx=float(EV[3])
        response.ewy=float(EV[4])
        response.ewz=float(EV[5])


        
        #self.q1_reference=q1
        #self.q2_reference=q2
        #self.q3_reference=q3

        return response

    def service_callback_2(self, request, response):
        #response.sum = request.a + request.b

        #response.endeffector = J*request.joint
        
        e1=request.v_x
        e2=request.v_y
        e3=request.v_z
        e4=request.w_x
        e5=request.w_y
        e6=request.w_z

        J_inverse=np.linalg.pinv(self.J)

        EV=np.array([[e1],[e2],[e3],[e4],[e5],[e6]])

        Q_array=np.matmul(J_inverse,EV)


        response.q1=float(Q_array[0])
        response.q2=float(Q_array[1])
        response.q3=float(Q_array[2])
        

        #self.q1_reference=q1
        #self.q2_reference=q2
        #self.q3_reference=q3

        return response

    def listener_callback(self,msg):

        # print(msg)

        q1=msg.position[0]
        q2=msg.position[1]
        q3=msg.position[2]

        l1=2.0 
        l2=1.0
        l3=1.0

        s1=math.sin(q1)
        s12=math.sin(q1+q2)
        c1=math.cos(q1)
        c12=math.cos(q1+q2)
        
        self.J = np.array([[-l2*s1-l3*s12,-l3*s12,0],[l2*c1+l3*c12,l3*c12,0],[0,0,-1],[0,0,0],[0,0,0],[1,1,0]])


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()
