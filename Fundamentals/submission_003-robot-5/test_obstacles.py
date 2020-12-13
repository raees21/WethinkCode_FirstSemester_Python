import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
from unittest.mock import patch
import maze.obstacles as obstacles
import robot

class TestRobot(unittest.TestCase):

    def test_is_position_blocked(self):
            obstacles.random.randint = lambda a, b: 50
            obstacles.get_obstacles()

            self.assertEqual(obstacles.is_position_blocked(50,50), True)
            self.assertEqual(obstacles.is_position_blocked(49,49), False)

    def test_is_position_blocked_range(self):
            obstacles.random.randint = lambda a, b: 50
            obstacles.get_obstacles()

            self.assertEqual(obstacles.is_position_blocked(53,53), True)  
            self.assertEqual(obstacles.is_position_blocked(51,53), True)   
            self.assertEqual(obstacles.is_position_blocked(60,60), False)  
            self.assertEqual(obstacles.is_position_blocked(55,55), False)       

    def test_is_path_blocked(self):
            obstacles.random.randint = lambda a, b: 50
            obstacles.get_obstacles()

            self.assertEqual(obstacles.is_path_blocked(50,20,50,70), True)

    
