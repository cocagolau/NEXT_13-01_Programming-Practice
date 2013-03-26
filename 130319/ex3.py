def num_ZtoT(num):
	if (num>0 and num<10):
		return num+10
	elif(num>=10 and num<=100):
		return num*0.1
	else:
		return 0

num = input("input : ")
result = num_ZtoT(num)

print("output : %.1f \n" %result)