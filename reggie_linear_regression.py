import matplotlib.pyplot as plt

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

def get_y(m, b, x):
    y = m * x + b
    return y

def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y = m * x_point + b
    error = abs(y - y_point)
    return error

def calculate_all_error(m, b, datapoints):
    total_error = 0
    for point in datapoints:
        all_errors = calculate_error(m, b, point)
        total_error+= all_errors
    return total_error



possible_ms = [m * .1 for m in range(-100, 101)]

possible_bs = [b * .1 for b in range(-200, 201)]


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
print(best_m, best_b, smallest_error)


possible_x = [x * .5 for x in range(0, 51)]

x_value = []
y_value = []

for x in possible_x:
    y_answer = best_m * x + best_b
    x_value.append(round(x, 2))
    y_value.append(round(y_answer, 2))
print(x_value)
print(y_value)

plt.plot(x_value, y_value)
plt.show()

    


