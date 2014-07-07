import unittest
import math

def circle (radius) :
	
	try :
		trans = float (radius)

		if trans >= 0 :
			result = trans * trans * math.pi
			return int(result)
		else :
			return -1

	except ValueError :
		return 0