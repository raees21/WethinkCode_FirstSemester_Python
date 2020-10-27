import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
from unittest.mock import patch
import world.text.world as world

class TestRobot(unittest.TestCase):

    def test_posiition_allowed_false(self):
        self.assertEqual(world.is_position_allowed(200, 400), False)

    
    def test_position_allowed_true(self):
        self.assertEqual(world.is_position_allowed(100, 100), True)


    def test_update_position(self):
        self.assertEqual(world.update_position(5), True)


    def test_update_position_out(self):
        self.assertEqual(world.update_position(201), False)


