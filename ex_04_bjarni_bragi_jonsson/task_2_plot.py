import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from myforest import *



def get_avg_shortest_and_avg_percol(number_of_forests, p, N):
    percol_total = 0
    shortest_path_list = []
    for i in range(number_of_forests):
        my_forest = Forest(p, N)
        my_forest.burn_forest()
        my_grid = my_forest.forest_grid
        shortest_path = my_forest.get_number_of_steps_in_shortest_path()
        if shortest_path != "no percolation":
            shortest_path_list.append(shortest_path)
            percol_total = percol_total+1
    percol_avg = float(percol_total)/float(number_of_forests)

    try:
        avg_shortest_path = sum(shortest_path_list)/len(shortest_path_list)
    except ZeroDivisionError:
        avg_shortest_path = 0
    return percol_avg, avg_shortest_path

##########Task 2 - fixed N -fixed p##############
#percol_avg, avg_shortest_path = get_avg_shortest_and_avg_percol(1000, 0.6, 30)
#print percol_avg, avg_shortest_path

#####Task 2 -varying N and p#########
N_list = [30, 50, 70, 200]
for N in N_list:
    print N
    prob_list=[]
    percol_avg_list = []
    for p in range(1,99, 5):
        print p
        prob = float(p)/float(100)
        percol_avg, avg_shortest_path = get_avg_shortest_and_avg_percol(100, prob, N)
        prob_list.append(prob)
        percol_avg_list.append(percol_avg)
    print prob_list
    print percol_avg_list
    plt.plot(prob_list, percol_avg_list)
plt.legend(['N = 30', 'N = 50', "N = 70", 'N = 200'], loc='upper left')
plt.xlabel("p")
plt.ylabel("wrapping probability")

plt.savefig("percol.png")

plt.show()
