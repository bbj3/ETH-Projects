import math
import random
from plot_helper import best_line
import numpy as np


class RandomChain(object):

    def __init__(self, x_pos, y_pos, z_pos):
        self.x_pos_list = []
        self.y_pos_list = []
        self.z_pos_list = []
        self.x_pos_list.append(x_pos)
        self.y_pos_list.append(y_pos)
        self.z_pos_list.append(z_pos)

    def is_there_a_overlapping_sphere(self, new_x, new_y, new_z):
        number_of_spheres = len(x_pos_list)
        for i in range(0,number_of_spheres):
            old_x = self.x_pos_list[i]
            old_y = self.y_pos_list[i]
            old_z = self.z_pos_list[i]
        dis = sqrt((old_x-new_x)**2+(old_x-new_x)**2+(old_x-new_x)**2)
        if dis<1:
            return True
        else:
            return False


    def add_one_sphere(self):
        last_z = self.z_pos_list[-1]
        last_x = self.x_pos_list[-1]
        last_y = self.y_pos_list[-1]
        overlap = True
        while overlap:
            new_x, new_y, new_z = get_random_unit_vector(last_x, last_y, last_z)
            overlap = self.is_there_a_overlapping_sphere(new_x, new_y, new_z)
        self.x_pos_list.append(new_x)
        self.y_pos_list.append(new_y)
        self.z_pos_list.append(new_z)

    def add_X_spheres(self, X):
        for i in range(0,X):
            self.add_one_sphere()
        return self.x_pos_list[-1], self.y_pos_list[-1], self.z_pos_list[-1]



    def is_there_a_overlapping_sphere(self, new_x, new_y, new_z):
        number_of_spheres = len(self.x_pos_list)
        overlap = False
        for i in range(0,number_of_spheres):
            old_x = self.x_pos_list[i]
            old_y = self.y_pos_list[i]
            old_z = self.z_pos_list[i]
            dis = math.sqrt((old_x-new_x)**2+(old_x-new_x)**2+(old_x-new_x)**2)
            if dis<1:
               overlap = True
               break
        return overlap


def get_random_theta():
    rnd = random.random()
    rnd_theta = rnd*math.pi
    return rnd_theta


def get_random_phi():
    rnd = random.random()
    rnd_phi = rnd*2.0*math.pi
    return rnd_phi

def get_random_unit_vector(last_x, last_y, last_z):
    rnd_phi = get_random_phi()
    rnd_theta = get_random_theta()
    x = math.sin(rnd_theta)*math.cos(rnd_phi)+last_x
    y = math.sin(rnd_theta)*math.sin(rnd_phi)+last_y
    z = math.cos(rnd_theta)+last_z
    return x,y,z



def main():
    distance_list=[]
    expected_of_R_2_sum_list=[]
    expected_of_R_4_sum_list=[]
    steps_list=[]
    M=350000
    for steps in range(10,35,5):
        distance_list = []
        for walker_number in range (0,M):
            a= RandomChain(0,0,0)
            x,y,z = a.add_X_spheres(steps)
            distance_squared = math.sqrt(x**2+y**2+z**2)
            distance_list.append(distance_squared)

        expected_of_R_2_sum = 0
        expected_of_R_4_sum = 0
        for distance_square in distance_list:
            expected_of_R_2_sum = expected_of_R_2_sum + distance_square
            expected_of_R_4_sum = expected_of_R_4_sum + distance_square**2
        expected_of_R_2_sum = expected_of_R_2_sum/M
        expected_of_R_4_sum = expected_of_R_4_sum/M
        expected_of_R_2_sum_list.append(expected_of_R_2_sum)
        expected_of_R_4_sum_list.append(expected_of_R_4_sum)
        steps_list.append(steps)
        delta = math.sqrt((expected_of_R_4_sum-expected_of_R_2_sum)/M)
        print "expected_of_R_2_sum: " + str(expected_of_R_2_sum)
        print "expected_of_R_4_sum: " + str(expected_of_R_4_sum)
        print "delta: " + str(delta)
    best_line(np.log(steps_list), np.log(expected_of_R_2_sum_list))


if __name__ == "__main__":
    main()
