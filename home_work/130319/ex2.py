def num_abs(num):
	if num >= 0:
		return num
	else:
		return -num

num = input("input : ")
result = num_abs(num)

print("output : %d \n" %result)