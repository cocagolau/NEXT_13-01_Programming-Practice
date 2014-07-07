#-*- coding: utf-8 -*-
def split_error (msg):
	
	msg_cause_position = msg.find ('] [')+3
	cause_text = msg [msg_cause_position : msg_cause_position+5]

	if (cause_text != 'error'):
		return 0

	date = msg [1 : msg_cause_position-3]
	after_error_text = msg [msg_cause_position+7 : ]
	client_position = after_error_text.find ('] ')
	client_text = after_error_text [1 : client_position]
	after_client_text = after_error_text [client_position+2 : ]
	cause_position = after_client_text.find (': ')
	cause = after_client_text [ : cause_position]
	error_dir = after_client_text [cause_position+2 : len (after_client_text)-1]

	error=[]
	error.append (cause)
	error.append (error_dir)

	return error


def print_summary (error_count):
	for key in error_count:
		print "\"%s\" : %d개" %(key, error_count[key])


def print_detail (error_dic):
	i=0;
	for error_cause in error_dic:
		i = i+1
		print "--------------------------------------------"
		print "%d. %s" %(i, error_cause)
		for error_line in error_dic[error_cause]:
			print error_line


def insert_error_key (error_dic, result):
	tempList = []
	tempList.append (result[1])
	error_dic[result[0]] = tempList
	return error_dic


def insert_error_value (error_dic, result):
	tempList = error_dic[result[0]]
	#해당 key값에 value가 있다면 return
	if (result[1] in tempList):
		return error_dic

	tempList.append (result[1])
	error_dic[result[0]] = tempList
	return error_dic


# Main
error_dic = {}
error_count = {}

try :
	errorFile = open ('../error_log')

	for line in errorFile:
		result = split_error (line)

		#File에서 error인 경우만 실행
		if (result != 0):

			#key값이 있는 경우
			if (error_dic.has_key (result[0])):
				error_count[result[0]] += 1
				error_dic = insert_error_value (error_dic, result)

			#key값이 없는 경우
			else:
				error_count[result[0]] = 1
				error_dic = insert_error_key (error_dic, result)
				
			#임시 저장배열 초기화	
			error = []


	# 갯수 출력
	print "[SUMMARY REPORT]"
	print_summary (error_count)
	print "\n"


	# 세부 오류내역 출력	
	print "[Detail REPORT]"
	print_detail (error_dic)


# error발생시
except IOError:
	print ("What the hell am i doing")

except :
	print ("Why!!!!")