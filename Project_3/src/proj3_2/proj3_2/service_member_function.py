from tutorial_interfaces.srv import ThirdService
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64MultiArray


import rclpy
from rclpy.node import Node
import numpy as np


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')


        self.v1_reference=0.0
        self.v2_reference=0.0
        self.v3_reference=0.0

        self.srv = self.create_service(ThirdService, 'velo_serv', self.service_callback)
        #self.i=0

        self.effort_v1=0.0
        self.effort_v2=0.0
        self.effort_v3=0.0

        self.v1_prev=0.0
        self.v2_prev=0.0
        self.v3_prev=0.0

        
        self.subscription_1 = self.create_subscription(
            JointState,
            '/joint_states',
            self.listener_callback,
            10)
        self.subscription_1



        

        self.publisher_1= self.create_publisher(Float64MultiArray, '/forward_effort_controller/commands', 10)
        msg=Float64MultiArray()
        msg.data=[0.0,0.0,0.0]
        self.publisher_1.publish(msg)
        # timer_period = 0.1  # seconds
        # self.timer = self.create_timer(timer_period, self.publisher_callback)


    def service_callback(self, request, response):
        #response.sum = request.a + request.b
        
        v1=request.x
        v2=request.y
        v3=request.z
        
        response.v1=v1
        response.v2=v2
        response.v3=v3

        self.v1_reference=v1
        self.v2_reference=v2
        self.v3_reference=v3

        return response

    def listener_callback(self,msg):

        # print(msg)

        # q1=msg.position[0]
        # q2=msg.position[1]
        # q3=msg.position[2]

        v1=msg.velocity[0]
        v2=msg.velocity[1]
        v3=msg.velocity[2]

        

        K_p_v1=4.2
        K_d_v1=0.4

        K_p_v2=4
        K_d_v2=0.5

        K_p_v3=10
        K_d_v3=1

        diff_e1=v1-self.v1_prev
        diff_e2=v2-self.v2_prev
        diff_e3=v3-self.v3_prev



        # e2=(v2-self.v2_reference)-(v1-self.v1_reference)
        # e3=(v3-self.v3_reference)-(v2-self.v2_reference)

        self.effort_v1= K_p_v1*(v1-self.v1_reference)+K_d_v1*(diff_e1)
        self.effort_v2=K_p_v2*(v2-self.v2_reference)+K_d_v2*diff_e2
        self.effort_v3=K_p_v3*(v3-self.v3_reference)+K_d_v3*diff_e3

        msg=Float64MultiArray()
        msg.data=[float(self.effort_v1),float(self.effort_v2),float(self.effort_v3)]

        self.publisher_1.publish(msg)

        self.v1_prev=v1
        self.v2_prev=v2
        self.v2_prev=v3

        
        # if self.i<1000:

        #     # print(self.i)

        #     f=open('q1_1.txt','a')
        #     f.write(str(q1))
        #     f.write('\n')
        #     f.close()

        #     f=open('q2_1.txt','a')
        #     f.write(str(q2))
        #     f.write('\n')
        #     f.close()

        #     f=open('q3_1.txt','a')
        #     f.write(str(q3))
        #     f.write('\n')
        #     f.close()
        
        # self.i+=1


    # def publisher_callback(self):

    #     msg=Float64MultiArray()
    #     msg.data=[float(self.effort_q1),float(self.effort_q2),float(self.effort_q3)]

    #     ##Publish

    #     self.publisher_1.publish(msg)




def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
