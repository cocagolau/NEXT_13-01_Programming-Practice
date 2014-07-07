def data_filter(dict, data_fil):
	for key in dict:
		age = key/10
		ages = age*10
		ages_val = "%ds" %(ages)
		data_fil[ages_val].append(key)


data = {'minsu':43, 'jisu':33, 'john':21, 'david':33, 'hary':36,'messi':33,'ronaldo':27}
data_fil={}

a=list()
a.append('a')
print a

#data_filter(data, data_fil)
print data_fil