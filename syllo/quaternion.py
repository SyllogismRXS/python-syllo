import numpy as np
from math import pow, cos, sin, pi

class Quaternion(object):
    def __init__(self):

        angle = pi / 4.0
        axis = np.array([0, 1, 0])
        
        self.q0 = cos(angle / 2.0)
        self.q1 = axis[0] * sin(angle / 2.0)
        self.q2 = axis[1] * sin(angle / 2.0)
        self.q3 = axis[2] * sin(angle / 2.0)        
        
        # D = pi/4.0
        # A = pi/2.0  # X-axis
        # B = 0  # Y-axis
        # C = pi/2.0  # Z-axis        
        # self.q0 = cos(D / 2.0)
        # self.q1 = cos(A) * sin(D / 2.0)
        # self.q2 = cos(B) * sin(D / 2.0)
        # self.q3 = cos(C) * sin(D / 2.0)        
    
    def to_rotation_matrix(self):
        q0 = self.q0
        q1 = self.q1
        q2 = self.q2
        q3 = self.q3
        
        R_00 = pow(q0,2) + pow(q1,2) - pow(q2,2) - pow(q3,2)
        R_01 = 2*(q1*q2 - q0*q3)
        R_02 = 2*(q0*q2 + q1*q3)
        
        R_10 = 2*(q1*q2 + q0*q3)
        R_11 = pow(q0,2) - pow(q1,2) + pow(q2,2) - pow(q3,2)
        R_12 = 2*(q2*q3 - q0*q1)

        R_20 = 2*(q1*q3 - q0*q2)
        R_21 = 2*(q2*q3 + q0*q1)
        R_22 = pow(q0,2) - pow(q1,2) - pow(q2,2) + pow(q3,2)

        R = np.array([[R_00, R_01, R_02],
                      [R_10, R_11, R_12],
                      [R_20, R_21, R_22]])
        return R
