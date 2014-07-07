#-*- coding: utf-8 -*-
import re

class ErrorLog:
	
	def __init__ (self, file_name) :
		self.error_dic = {}
		self.error_count = {}
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
		
		# 정규표현식에 맞지 않는 경우 종료
		correct_line = re.search (r'^\[...\s...\s..\s........\s....\]\s\[(error)]\s\[', self.line)
		if not correct_line :
			return 0

		# error 다음의 조건일 경우 종료
		img_format = re.search (r'\w+.(jpg|gif|png|ico|icod)', self.line)
		if img_format :
			return 0
		
		# 정규 표현식을 통해 '] '로 분리 후 4번째 부분만 추출
		split_text = re.split (r'\]\s', self.line)[3]
		# 개행문자 제거
		split_text = split_text[:len(split_text)-1]

		# 식에 ': /'이 들어가 있는지 검색 
		can_split = re.search (r':\s', split_text)
		if can_split :
			error = re.split (r':\s', split_text)
		else :
			error = list ()
			error.append (split_text)
			error.append ('')

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
