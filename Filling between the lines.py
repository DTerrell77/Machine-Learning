# CSC-356 ML
# Dylan Terrell 
# Jan 21, 2021

# Multi-line comment is ctrl+ '+' +'/'

# Example 1 
# Fill in Area Between Two Horizontal Lines
# import matplotlib.pyplot as plt
# import numpy as np

# #define x and y values 
# #np.arrange(start, stop, step)
# x = np.arange(0, 10, 0.1)
# y = np.arange(10, 20, 0.1)

# #create plot of values
# plt.plot(x, y, linewidth = 5.0, color = 'dodgerblue')

# #fill in area between the two lines
# plt.fill_between(x, y, color = 'red', alpha = 0.5)

# #add gridlines
# plt.grid(color='lightgrey', linewidth=0.5)

# #create a title for the graph
# plt.title("Figure_1")

# #display graph
# plt.show()

# #save graph
# plt.savefig("my plot.png")

# end of Fill in Area Between Two Horizontal Lines


# Example 2
# Fill in area under a curve
# import matplotlib.pyplot as plt
# import numpy as np

# #define x and y values
# x = np.arange(0, 10, 0.1)
# y = x**2

# #create plot of values
# plt.plot(x,y)

# #fill in area between the two lines
# plt.fill_between(x, y, color='red', alpha=0.5)

# #create a title for the graph
# plt.title("Figure_2")

# plt.show()
# end of Example 2 


# Example 3
#Fill in area above a curve
# import matplotlib.pyplot as plt
# import numpy as np

# #define x and y values
# x = np.arange(0,10,0.1)
# y = x**2

# #create plot of values
# plt.plot(x,y)

# #fill in area between the two lines
# # max() returns the largest input values
# plt.fill_between(x, y, np.max(y), color='red', alpha=0.5)

# #create a title for the graph
# plt.title("Figure_3")

# plt.show()
# end of Example 3 


# Example 4 
# Fill in area between 2 vertical lines
import matplotlib.pyplot as plt
import numpy as np

#define x and y values
x = np.arange(0,10,0.1)
y = np.arange(10,20,0.1)

#create plot of values
plt.plot(x,y)

#fill in area between the two lines
#fills between 2 x-values
plt.fill_betweenx(y, 2, 4, color='red', alpha=.5)

# create a title for the graph
plt.title("Figure_4")

plt.show()
# end of Example 4