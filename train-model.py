import matplotlib.pyplot as plt
import numpy as np

def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    x_lim = axes.get_xlim()
    y_lim = axes.get_ylim()
    plt.plot(x_vals, y_vals, '--')
    axes.set_xlim(x_lim)
    axes.set_ylim(y_lim)

def parse_file(filename):
	data = list()
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	for line in lines[1:]:
		tmp = line.strip().split(",")
		data.append((int(tmp[0]), int(tmp[1])))
	return data

def save_results(a, b):
	f = open("var.csv", "w")
	f.write("a,b\n")
	f.write(str(a) + "," + str(b) + "\n")
	f.close()

# def mean_squared_error(y_true, y_predicted):
# 	cost = sum((y_predicted - y_true) ** 2) / len(y_true)
# 	return cost

def normalization(x):
	min_x = min(x)
	max_x = max(x)
	return (x - min_x) / (max_x - min_x)

# def standardization(x):
# 	return (x - x.mean()) / x.std()

def gradient_descent(x, y, iterations = 10000, learning_rate = 0.01, stopping_threshold = 1e-4):
	xn = normalization(x)
	yn = normalization(y)
	an = 0
	bn = 0
	a = 0
	b = 0
	n = len(x)

	plt.ion()

	for i in range(iterations):
		yn_predicted = an * xn + bn

		an_derivative = 1 / n * sum(xn * (yn_predicted - yn))
		bn_derivative = 1 / n  * sum(yn_predicted - yn)

		# stop condition
		# if (abs(an_derivative) < stopping_threshold and abs(bn_derivative) < stopping_threshold):
		# 	break

		an = an - (learning_rate * an_derivative)
		bn = bn - (learning_rate * bn_derivative)

		# denormalize
		a = an * (max(y) - min(y)) / (max(x) - min(x))
		b = bn * (max(y) - min(y)) + min(y) - a * min(x)

		# show graph
		plt.clf()
		plt.scatter(x, y)
		abline(a, b)
		plt.show()
		plt.pause(0.001)

		# print(f"iteration: {i} | a={a} | b={b}")

	plt.ioff()
	plt.show(block=True)

	return [a, b]

# parse dataset
data = parse_file("data.csv")
mileages = list()
prices = list()
for el in data:
	mileages.append(el[0])
	prices.append(el[1])
mileages = np.array(mileages)
prices = np.array(prices)

# gradient descent ; set iterations to 10000 to get more accurate results
model = gradient_descent(mileages, prices, 1000, 0.1)
print("results:", model)

save_results(model[0], model[1])

# solution from numpy library
# model = np.polyfit(mileages, prices, 1)
# print("solution:", model)
