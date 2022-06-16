import matplotlib.pyplot as plt

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

#       Function to calculate the slope-intercept form
def get_y(m, b, x):
    y = m * x + b
    return y

#       Function to calculate the error from a known datapoint
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y = m * x_point + b
    error = abs(y - y_point)
    return error

#       Function to calculate the error from the whole list of datapoints
def calculate_all_error(m, b, datapoints):
    total_error = 0
    for point in datapoints:
        all_errors = calculate_error(m, b, point)
        total_error+= all_errors
    return total_error


#       List Comprehension that starts at -10 and ends at 10 in increments of .1
#       This will be our slope
possible_ms = [m * .1 for m in range(-100, 101)]

#       List Comprehension that starts at -20 and ends at 20 in increments of .1
#       This will be our y-intercept
possible_bs = [b * .1 for b in range(-200, 201)]


#       Finds the slope and y-intercept with the smallest error compared to a list of datapoints
smallest_error = float("inf")
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints) 
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error
            
#       The results will give us our slope-intercept form to perform our linear regression model         
print(best_m, best_b, smallest_error)

#       List Comprehension that creates x values from 0 to 25 in increments of .5
possible_x = [x * .5 for x in range(0, 51)]

x_value = []
y_value = []

#       Plugs the x values list comprehension into our slope-intercept form
#       and prints the x and y values separately
for x in possible_x:
    y_answer = best_m * x + best_b
    x_value.append(round(x, 2))
    y_value.append(round(y_answer, 2))
print(x_value)
print(y_value)

#       Plots the x and y values using MatPlotLib to create visual of linear regression model       
plt.plot(x_value, y_value)
plt.show()


#       Separates y values from the list called datapoints to start process to calculate R squared       
yvalues = []
for points in datapoints:
    yvalues.append(points[1])

ysquared = []
for y in yvalues:
    squarednumber = round(round((y - average(yvalues)), 2) ** 2, 2)
    ysquared.append(squarednumber)
# print("Squared: ", ysquared)
sumy = sum(ysquared)
print("Sum of y: ", sumy)

#       Iterates through the list of y values and calculates the estimated y value 
t = 0
estimated_yvalues = []
while t < len(yvalues):
    for y in yvalues:
        estimate_y = .3 * y + 1.7
        estimate_yvalues.append((round(estimate_y, 2)))
        t+=1

estimate_ysquared = []
for y in estimate_yvalues:
    squarednumber = round(round((y - average(estimate_yvalues)), 2) ** 2, 2)
    estimate_ysquared.append(squarednumber)
# print("Squared: ", fakeysquared)
estimate_ysum = sum(estimate_ysquared)
print("Sum of fake y: ", estimate_ysum)
rsquared = round(estimate_ysum/sumy * 100, 2)
print(f"R squared: {rsquared}%")    


