import numpy as np 
import matplotlib.pyplot as plt

#1000 dogs
greyhounds = 500
labs = 500

# adding variation in height by random number
grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.rand(labs)

#histogram
plt.hist([grey_height, lab_height], stacked=True, color=['r','b'])
plt.show()


