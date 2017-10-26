import unittest

class GraderTestCase(unittest.TestCase):
    '''
    A Python unit test for grading and printing out points.
    For one grading all tests must be in a one test case.
    Individual tests should use available_points(points) before
    test to record the maximum and self.grant_points(points)
    to grant points.

    '''

    @classmethod
    def setUpClass(cls):
        '''
        Sets up the point counters for the test case.

        '''
        cls.points = 0
        cls.max_points = 0


    @classmethod
    def tearDownClass(cls):
        '''
        Prints the points to the system out at the end of the test case.

        '''
        print("TotalPoints: %d" % (cls.points))
        print("MaxPoints: %d" % (cls.max_points))


    def available_points(self, max_points):
        '''
        Records max points for a single test.

        '''
        self.__class__.max_points += max_points


    def grant_points(self, points):
        '''
        Grants points for a single test.

        '''
        self.__class__.points += points
