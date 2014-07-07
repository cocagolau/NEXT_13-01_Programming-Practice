import unittest
from test import circle

class TestUm (unittest.TestCase) :
	def test1_number_1st (self) :
		self.assertEqual (circle(0),0)
	def test2_number_1st (self) :
		self.assertEqual (circle(1),3)
	def test3_number_1st (self) :
		self.assertEqual (circle(-1),-1)
	def test4_number_1st (self) :
		self.assertEqual (circle(" "),0)
	def test5_number_1st (self) :
		self.assertEqual (circle("2"),12)

if __name__ == '__main__' :
	unittest.main()