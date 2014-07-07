def check_samestr(str):
	slen = len(str)	
	count = 0
	while(int(slen/2)>count):
		if(str[slen-count-1]!=str[count]):
			return 0
		count = count + 1
	return 1

char=raw_input("input : ")
result = check_samestr(char)

if(result == 1):
	print ("same")
else:
	print("different")