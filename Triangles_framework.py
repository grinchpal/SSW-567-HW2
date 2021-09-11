# -*- coding: utf-8 -*-

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    
    if a == 0 or b == 0 or c == 0 or a+b < c or a+c < b or b+c < a:
        return "NotATriangle"
    elif a == b and b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isoceles"
    elif a+b == c**2 or a+c == b**2 or b+c == a**2:
        return "Right"
    else:
        return "Scalene"
    
    # Note: This code is completely bogus but demonstrates a few features of python
##    if a == 3 and b == 4 and c == 5:
##        return 'Right'
##    elif a == 3 and b == c:
##        return 'Scalene'
##    else:
##        return 'NotATriangle'
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle','Should be NotATriangle')
        self.assertEqual(classifyTriangle(0,15,30),'NotATriangle','Should be NotATriangle')
        self.assertEqual(classifyTriangle(10,0,30),'NotATriangle','Should be NotATriangle')
        self.assertEqual(classifyTriangle(10,15,0),'NotATriangle','Should be NotATriangle')
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(3,3,5),'Isoceles','3,3,5 is a Isoceles triangle')
        self.assertEqual(classifyTriangle(3,6,5),'Scalene','3,6,5 is a Scalene triangle')

if __name__ == '__main__':
    # examples of running the code
    classifyTriangle(1,2,3)
    classifyTriangle(1,1,1)
    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       
