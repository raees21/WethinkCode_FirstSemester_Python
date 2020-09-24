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

    def test_get_user_help(self):
        
        with captured_io(StringIO("")):
            self.assertEqual(robot.do_help(), (True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays commands previously done
REPLAY SILENT - replays commands done silently
REPLAY REVERSED - replays commands in reverse order
REPLAY REVERSED SILENT - replays commands in reverse order silently
"""))

    def test_handle_command(self):
        
        with captured_io(StringIO("")):
            self.assertTrue(robot.handle_command("Raees", "forward 10", ["forward 20"], True))
            self.assertTrue(robot.handle_command('Raees', "back 30", ["forward 20"], True))
            self.assertFalse(robot.handle_command( 'Raees', "off", ["forward 20"], True))

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

    @patch("sys.stdin", StringIO("hal\nforward 50\nback 40\nreplay\noff\n"))
    def test_replay(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 50 steps.
 > hal now at position (0,50).
hal: What must I do next?  > hal moved back by 40 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved forward by 50 steps.
 > hal now at position (0,60).
 > hal moved back by 40 steps.
 > hal now at position (0,20).
 > hal replayed 2 commands.
 > hal now at position (0,20).
hal: What must I do next? hal: Shutting down..
""")

    @patch("sys.stdin", StringIO("hal\nforward 50\nback 40\nreplay silent\noff\n"))
    def test_replay_silent(self):
        sys.stdout = StringIO()

        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 50 steps.
 > hal now at position (0,50).
hal: What must I do next?  > hal moved back by 40 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal replayed 2 commands silently.
 > hal now at position (0,20).
hal: What must I do next? hal: Shutting down..
""")


    @patch("sys.stdin", StringIO("hal\nforward 50\nback 40\nreplay reversed\noff\n"))
    def test_replay_reversed(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 50 steps.
 > hal now at position (0,50).
hal: What must I do next?  > hal moved back by 40 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal moved back by 40 steps.
 > hal now at position (0,-30).
 > hal moved forward by 50 steps.
 > hal now at position (0,20).
 > hal replayed 2 commands in reverse.
 > hal now at position (0,20).
hal: What must I do next? hal: Shutting down..
""")


    @patch("sys.stdin", StringIO("hal\nforward 50\nback 40\nreplay reversed silent\noff\n"))
    def test_replay_reversed_silent(self):
        sys.stdout = StringIO()

        robot.robot_start()

        self.assertEqual(sys.stdout.getvalue(), """What do you want to name your robot? hal: Hello kiddo!
hal: What must I do next?  > hal moved forward by 50 steps.
 > hal now at position (0,50).
hal: What must I do next?  > hal moved back by 40 steps.
 > hal now at position (0,10).
hal: What must I do next?  > hal replayed 2 commands in reverse silently.
 > hal now at position (0,20).
hal: What must I do next? hal: Shutting down..
""")


def test_posiition_allowed(self):

    self.assertEqual(robot.is_position_allowed(200, 400), (0, 0))