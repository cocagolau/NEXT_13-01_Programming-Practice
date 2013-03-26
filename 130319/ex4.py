import math

def num_between(x1,x2,y1,y2):
	dx = x2-x1
	dy = y2-y1
	result = math.sqrt(dx**2 + dy**2)

	return result

result = num_between(1,5,5,8)
print("output : %.2f" %result)