import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
from unittest.mock import patch
import robot

class TestRobot(unittest.TestCase):
    def test_get_robot_name(self):
        """Test robot name input"""

        with captured_io(StringIO("Raees")):
            self.assertEqual("Raees", robot.get_robot_name())

    def test_get_command(self):
        """Test command input"""

        with captured_io(StringIO("he\nhelp\nforward 20\nback 20\nreplay\nreplay silent\nreplay reversed silent\nreplay reversed")):
            self.assertEqual(robot.get_command("Raees"), "help")
            self.assertEqual(robot.get_command("Raees"), "forward 20")
            self.assertEqual(robot.get_command("Raees"), "back 20")
            self.assertEqual(robot.get_command("Raees"), "replay")
            self.assertEqual(robot.get_command("Raees"), "replay silent")
            self.assertEqual(robot.get_command("Raees"), "replay reversed silent")

    def test_split_command_input(self):
        """Test split command input"""

        self.assertEqual(robot.split_command_input("forward 20"), ("forward", "20"))
        self.assertEqual(robot.split_command_input("back 20"), ("back", "20"))
        self.assertEqual(robot.split_command_input("sprint 5"), ("sprint", "5"))
        self.assertEqual(robot.split_command_input("help"), ("help", ""))
        self.assertEqual(robot.split_command_input("off"), ("off", "")) 
        self.assertEqual(robot.split_command_input("right"), ("right", ""))
        self.assertEqual(robot.split_command_input("replay"), ("replay", ""))
        self.assertEqual(robot.split_command_input("replay reversed silent"), ("replay", "reversed silent")) 

    def test_int_value(self):
        """Test if its and integer"""

        self.assertEqual(robot.is_int("13"), True)
        self.assertEqual(robot.is_int("1"), True)
        self.assertEqual(robot.is_int("a"), False)
        self.assertEqual(robot.is_int("aa"), False)

    def test_valid_command(self):
        """Test if input is valid"""

        self.assertEqual(robot.valid_command("forward 5"), True)
        self.assertEqual(robot.valid_command("back 5"), True)
        self.assertEqual(robot.valid_command("sprint 5"), True)
        self.assertEqual(robot.valid_command("help"), True)
        self.assertEqual(robot.valid_command("off"), True)
        self.assertEqual(robot.valid_command("replay"), True)
        self.assertEqual(robot.valid_command("replay silent"), True)
        self.assertEqual(robot.valid_command("replay reversed"), True)
        self.assertEqual(robot.valid_command("replay reversed silent"), True)
        self.assertEqual(robot.valid_command("go"), False)
        self.assertEqual(robot.valid_command("now"), False)
        self.assertEqual(robot.valid_command("hello"), False)


    def test_handle_command(self):
        
        with captured_io(StringIO("")):
            self.assertTrue(robot.handle_command("Raees", "forward 10"))
            self.assertTrue(robot.handle_command('Raees', "back 30"))
            self.assertFalse(robot.handle_command( 'Raees', "off"))


    def test_sprint(self):
        sys.stdout = StringIO()
        
        robot.do_sprint("hal", 10)
        self.assertEqual(sys.stdout.getvalue(), """ > hal moved forward by 10 steps.
 > hal moved forward by 9 steps.
 > hal moved forward by 8 steps.
 > hal moved forward by 7 steps.
 > hal moved forward by 6 steps.
 > hal moved forward by 5 steps.
 > hal moved forward by 4 steps.
 > hal moved forward by 3 steps.
 > hal moved forward by 2 steps.
""")


    def test_do_forward(self):
        robot_name = "Raees"
        steps = 5
        with captured_io(StringIO("")):
            self.assertEqual(robot.do_forward(robot_name, steps), (True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'))


    def test_do_back(self):
        robot_name = "Raees"
        steps = 5
        with captured_io(StringIO("")):
            self.assertEqual(robot.do_back(robot_name, steps), (True, ' > '+robot_name+' moved back by '+str(steps)+' steps.')) 


    def test_do_right_turn(self):
        robot_name = "Raees"
        self.assertEqual(robot.do_right_turn(robot_name), (True, ' > '+robot_name+' turned right.'))

    
    def test_do_left_turn(self):
        robot_name = "Raees"
        self.assertEqual(robot.do_left_turn(robot_name), (True, ' > '+robot_name+' turned left.'))

    
    def test_call_command(self):

        self.assertEqual(robot.call_command("forward", "15", "Raees"), (True, ' > '+'Raees '+ 'moved forward by '+str(15)+' steps.'))