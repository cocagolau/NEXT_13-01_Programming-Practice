def error_split (error, msg):

	msg_cause_position = msg.find('] [')+3
	cause_text = msg[msg_cause_position:msg_cause_position+5]
	#print error_text
	error.append (cause_text)

	date = msg[1:msg_cause_position-3]
	#print date
	error.append (date)

	after_error_text = msg[msg_cause_position+7:]
	#print after_error_text

	client_position = after_error_text.find('] ')
	client_text = after_error_text[1:client_position]
	#print client_text
	error.append (client_text)


	after_client_text = after_error_text[client_position+2:]
	#print after_client_text

	cause_position = after_client_text.find (': ')
	cause = after_client_text[:cause_position]
	#print cause
	error.append (cause)

	error_dir = after_client_text[cause_position+3:]
	#print error_dir
	error.append (error_dir)

	return error




error = []
error_msg1 = "[Fri Oct 05 08:38:21 2012] [error] [client ::1] File does not exist: /Library/WebServer/Documents/favicon.ico"
error_msg = "[Mon Oct 08 09:25:40 2012] [error] [client 127.0.0.1] File does not exist: /Library/WebServer/Documents/favicon.ico"
result = error_split (error, error_msg)
print result

