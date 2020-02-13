from clock import Clock
import unittest

class MyUnitTestClass(unittest.TestCase):

    def test_1(self):
        c1 = Clock(4, 7, 3)
        self.assertEqual(str(c1), "04: 07: 03")
        #Starting the initial clock string above
        self.assertEqual(c1.hr, 4)
        self.assertEqual(c1.min, 7)
        self.assertEqual(c1.sec, 3)
        c1.tick( )
        #Calling the tick function that adds a second onto time.
        self.assertEqual(str(c1), "04: 07: 04")

    def test_2(self):
        c2 = Clock(4, 7, 59)
        self.assertEqual(str(c2), "04: 07: 59")
        c2.tick( )
        self.assertEqual(str(c2), "04: 08: 00")

    def test_3(self):
        c3 = Clock(4, 59, 59)
        self.assertEqual(str(c3), "04: 59: 59")
        c3.tick( )
        self.assertEqual(str(c3), "05: 00: 00")

    def test_4(self):
        c4 = Clock(23, 59, 59)
        self.assertEqual(str(c4), "23: 59: 59")
        c4.tick( )
        self.assertEqual(str(c4), "24: 00: 00")

if __name__ == '__main__':
    unittest.main( )
