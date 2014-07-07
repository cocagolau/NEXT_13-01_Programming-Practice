#-*- coding: utf-8 -*-
import re

def split_error (line):

	# 정규표현식에 맞지 않는 경우 종료
	correct_line = re.search (r'^\[...\s...\s..\s........\s....\]\s\[(error)]\s\[', line)
	
	if not correct_line :
		return 0

	# error 다음의 조건일 경우 종료
	img_format = re.search (r'\w+.(jpg|gif|png|ico|icod)', line)
	if img_format :
		return 0
	
	# 정규 표현식을 통해 '] '로 분리 후 4번째 부분만 추출
	split_text = re.split (r'\]\s', line)[3]
	split_text = split_text[:len(split_text)-1]

	# 식에 ': /'이 들어가 있는지 검색 
	can_split = re.search (r':\s', split_text)
	if can_split :
		error = re.split (r':\s', split_text)
	else :
		error = list ()
		error.append (split_text)

	return error


errorFile = open ('../error_log')
for line in errorFile:
	result = split_error(line)
	
	#File에서 error인 경우만 실행
	if (result != 0):
		print result