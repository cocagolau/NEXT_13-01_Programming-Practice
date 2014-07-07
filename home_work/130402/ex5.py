a = []

for value in range(7):
   if value % 2 == 0:
      a.append(value)


for value in range(4) :
   print("%d th value of list 'a' is %s " % (value,a[value]))