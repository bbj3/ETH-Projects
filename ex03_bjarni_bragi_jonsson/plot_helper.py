import matplotlib.pyplot as plt
import numpy as np

# Some dummy data
def best_line(x,y):
    # Find the slope and intercept of the best fit line
    slope,intercept=np.polyfit(x,y,1)

    # Create a list of values in the best fit line
    ablineValues = []
    for i in x:
        ablineValues.append(slope*i+intercept)

    # Plot the best fit line over the actual values
    plt.plot(x,y,'o')
    plt.plot(x, ablineValues, 'b')
    plt.title("slope: " + str(slope))
    plt.ylabel(r'$ log( \langle R^{2} \rangle )$')
    plt.xlabel('log(N)')
    plt.savefig("random_walk.png")

    plt.show()
