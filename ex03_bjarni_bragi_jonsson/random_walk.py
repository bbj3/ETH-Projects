import random
import math
from plot_helper import best_line

class Randomwalker(object):

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def take_one_step_randomly(self):
        rnd_x, rnd_y = get_random_unit_vector()
        self.x_pos = self.x_pos+rnd_x
        self.y_pos = self.y_pos+rnd_y
        return self.x_pos, self.y_pos

    def walk_X_steps(self, x):
        for i in range(0,x):
            self.take_one_step_randomly()
        return self.x_pos, self.y_pos


def get_random_angle():
    rnd = random.random()
    rnd_angle = rnd*2.0*math.pi
    return rnd_angle

def get_random_unit_vector():
    rnd_angle = get_random_angle()
    y = math.sin(rnd_angle)
    x = math.cos(rnd_angle)
    return x,y



def main():
    distance_list=[]
    expected_of_R_2_sum_list=[]
    expected_of_R_4_sum_list=[]
    steps_list=[]
    M=350000
    for steps in range(10,40,5):
        distance_list = []
        for walker_number in range (0,M):
            walker = Randomwalker(0,0)
            x,y = walker.walk_X_steps(steps)
            distance_squared = math.sqrt(x**2+y**2)
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
    best_line(steps_list, expected_of_R_2_sum_list)


if __name__ == "__main__":
    main()
