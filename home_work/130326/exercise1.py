def data_filter(dict, data_fil):
	for key in dict:
		if (dict[key] >= 20) and (dict[key] < 30):
			data_fil['20s'].append(key)
		elif (dict[key] >= 30) and (dict[key] < 40):
			data_fil['30s'].append(key)

data = {'minsu':43, 'jisu':33, 'john':21, 'david':33, 'hary':36,'messi':33,'ronaldo':27}
data_fil={'20s':[],'30s':[]}

data_filter(data, data_fil)
print data_fil