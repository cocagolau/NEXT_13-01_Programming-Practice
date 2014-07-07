#-*- coding: utf-8 -*-
class ErrorLog:
	
	def __init__ (self, file_name) :
		self.error_dic = {}
		self.error_count = {}
		self.file_format = ['jpg', 'gif', 'png', 'ico','icod']

		errorFile = open ('../'+file_name)

		for self.line in errorFile:
			self.result = self.split_error()

			#File에서 error인 경우만 실행
			if (self.result != 0):

				#key값이 있는 경우
				if (self.error_dic.has_key (self.result[0])):
					self.error_count[self.result[0]] += 1
					self.insert_error_value ()

				#key값이 없는 경우
				else:
					self.error_count[self.result[0]] = 1
					self.insert_error_key ()
					

	def split_error (self):
		line_cause_position = self.line.find ('] [')+3
		cause_text = self.line [line_cause_position : line_cause_position+5]

		# error가 아닐경우 종료
		if (cause_text != 'error'):
			return 0

		date = self.line [1 : line_cause_position-3]
		after_error_text = self.line [line_cause_position+7 : ]
		client_position = after_error_text.find ('] ')
		client_text = after_error_text [1 : client_position]
		after_client_text = after_error_text [client_position+2 : ]
		cause_position = after_client_text.find (': ')
		cause = after_client_text [ : cause_position]
		error_dir = after_client_text [cause_position+2 : len (after_client_text)-1]
		error_format_position = error_dir.find('.')
		error_format = error_dir[error_format_position+1:error_format_position+4]

		# format이 file_format에 포함될 경우 종료
		for format in self.file_format :
			if (error_format == format) :
				return 0

		error=[]
		error.append (cause)
		error.append (error_dir)

		return error


	def insert_error_key (self):
		tempList = []
		tempList.append (self.result[1])
		self.error_dic[self.result[0]] = tempList


	def insert_error_value (self):
		tempList = self.error_dic[self.result[0]]
		#해당 key값에 value가 있다면 return
		if not(self.result[1] in tempList):
			tempList.append (self.result[1])
			self.error_dic[self.result[0]] = tempList


	def print_summary (self):
			for key in self.error_count:
				print "\"%s\" : %d개" %(key, self.error_count[key])


	def print_detail (self):
		i=0;
		for error_cause in self.error_dic:
			i = i+1
			print "--------------------------------------------"
			print "%d. %s" %(i, error_cause)
			for error_line in self.error_dic[error_cause]:
				print error_line

# Main
try :
	file_name = 'error_log'
	obj = ErrorLog (file_name)
	
	# 갯수 출력
	print "[SUMMARY REPORT]"
	obj.print_summary ()
	print "\n"

	# 세부 오류내역 출력	
	print "[Detail REPORT]"
	obj.print_detail ()


# error발생시
except IOError:
	print ("What the hell am i doing")

except :
	print ("Why!!!!")
