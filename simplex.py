# -*- coding: utf-8 -*-
# @Date    : 2016/11/17
# @Author  : hrwhisper

import numpy as np

class Simplex(object):
    def __init__(self, obj, max_mode=False):
        self.max_mode = max_mode  # default is solve min LP, if want to solve max lp,should * -1
        self.mat = np.array([[0] + obj]) * (-1 if max_mode else 1)

    def add_constraint(self, a, b):
        self.mat = np.vstack([self.mat, [b] + a])

    def solve(self):
        m, n = self.mat.shape  # m - 1 is the number slack variables we should add
        temp, B = np.vstack([np.zeros((1, m - 1)), np.eye(m - 1)]), list(range(n - 1, n + m - 1))  # add diagonal array
        mat = self.mat = np.hstack([self.mat, temp])  # combine them!
        while mat[0, 1:].min() < 0:
            col = np.where(mat[0, 1:] < 0)[0][0] + 1  # use Bland's method to avoid degeneracy. use mat[0].argmin() ok?
            row = np.array([mat[i][0] / mat[i][col] if mat[i][col] > 0 else 0x7fffffff for i in
                            range(1, mat.shape[0])]).argmin() + 1  # find the theta index
            if mat[row][col] <= 0: return None  # the theta is ∞, the problem is unbounded
            mat[row] /= mat[row][col]
            ids = np.arange(mat.shape[0]) != row
            mat[ids] -= mat[row] * mat[ids, col:col + 1]  # for each i!= row do: mat[i]= mat[i] - mat[row] * mat[i][col]
            B[row] = col
        return mat[0][0] * (1 if self.max_mode else -1), {B[i]: mat[i, 0] for i in range(1, m) if B[i] < n}


# """
#        minimize -x1 - 14x2 - 6x3
#        st
#         x1 + x2 + x3 <=4
#         x1 <= 2
#         x3 <= 3
#         3x2 + x3 <= 6
#         x1 ,x2 ,x3 >= 0
#        answer :-32
#     """
# t = Simplex([-1, -14, -6])
# t.add_constraint([1, 1, 1], 4)
# t.add_constraint([1, 0, 0], 2)
# t.add_constraint([0, 0, 1], 3)
# t.add_constraint([0, 3, 1], 6)
# print(t.solve())
# print(t.mat)
#
#
#
# """
#        minimize 50x1 + 20x2 + 30x3 + 80x4
#        st
#         -400x1 - 200x2 -150x3 -500x4 <=-500
#         -3x1 -2x2 <= -6
#         -2x1 - 2x2 - 4x3 - 4x4 <= -10
#         -2x1 - 4x2 - 1x3 - 5x4 <= -8
#         x1 ,x2 ,x3 ,x4>= 0
#        answer :
#     """
# t = Simplex([50, 20, 30, 80])
# t.add_constraint([3, 2, 0, 0], 6)
# t.add_constraint([2, 2, 4, 4], 10)
# t.add_constraint([400, 200, 150, 500], 500)
# t.add_constraint([2, 4, 1, 5], 8)
# print(t.solve())
# print(t.mat)



"""
       minimize -60x1 - 30x2 - 20x3
       st
        8x1 + 6x2 +x3 <=48
        4x1 + 2x2 + 1.5x3 <= 20
        2x1 + 1.5x2 + 0.5x3<= 8
        x2 <= 5
        x1 ,x2 ,x3 >= 0
       answer :
    """
t = Simplex([-60, -30, -20])
t.add_constraint([8, 6, 3], 48)
t.add_constraint([4, 2, 1.5], 20)
t.add_constraint([0, 1, 0], 5)
t.add_constraint([2, 1.5, 0.5], 8)
print(t.solve())
print(t.mat)