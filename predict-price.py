def estimatePrice(mileage):
	return (a * mileage + b)

def getVar():
	f = open("var.csv", "r")
	lines = f.readlines()
	f.close()
	tmp = lines[1].strip().split(",")
	return (float(tmp[0]), float(tmp[1]))

var = getVar()
a = var[0]
b = var[1]

print("a:", a)
print("b:", b)

mileage = int(input("Mileage: "))
print("Estimated price:", estimatePrice(mileage))