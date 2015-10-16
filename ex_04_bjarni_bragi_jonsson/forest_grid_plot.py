import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from myforest import Forest

p = 0.615
N = 100
my_forest = Forest(p, N)
my_forest.burn_forest()
my_grid = my_forest.forest_grid
N = my_forest.forest_size
print my_grid

steps = my_forest.get_number_of_steps_in_shortest_path()
lifetime = my_forest.lifetime_of_fire

for line in range(N):
    for col in range(N):
        if my_grid[line][col] == "empty":
            my_grid[line][col] = -100
        if my_grid[line][col] == "tree":
            my_grid[line][col] = -50


# make a color map of fixed colors
cmap = colors.ListedColormap(["white", "green", "red"])
bounds=[-90,-70,0,1000]
norm = colors.BoundaryNorm(bounds, cmap.N)

# tell imshow about color map so that only set colors are used
fig = plt.figure()
plt.title("p: " + str(p) + "   N: " + str(N) + "  lifetime:" + str(lifetime) + "   Shortest path: " + str(steps) )

img = plt.imshow(my_grid, interpolation='nearest', origin='lower',
                    cmap=cmap, norm=norm)

title = "p_" + str(p) + "_N_" + str(N) + "_lifetime_" + str(lifetime) + "_Shortest path_" + str(steps)
plt.savefig(title+".png")
plt.show()
