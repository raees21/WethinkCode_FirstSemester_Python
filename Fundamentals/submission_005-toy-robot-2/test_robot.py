import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot

class TestRobot(unittest.TestCase):
    def test_user_name(self):
        """Test robot name input"""

        with captured_io(StringIO("Raees")):
            self.assertEqual("Raees", robot.user_input_name())

    
    def test_greet_user(self):
        """Test robot greeting"""

        with captured_io(StringIO("")):
            self.assertEqual(robot.greet_user("Raees"), print("Raees: Hello kiddo!") )


    def test_user_command(self):
        """Test command input"""

        with captured_io(StringIO("he\nyou\n")):
            self.assertEqual(robot.user_input_command("Raees"), "he")
            self.assertEqual(robot.user_input_command("Raees"), "you")


    def test_command_list(self):
        """Test command list function"""

        with captured_io(StringIO("forward 20\nback 20\nsprint 5\ngo\nforward 20\nback 20\nsprint 5\ngo\nforward 20\nback 20\nsprint 5\ngo\nforward 20\nback 20\nsprint 5\ngo\n")):
            robot_name = "Raees"
            """Test Coordinate 0"""
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 0), [0, 20])
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 0), [0, -20]) 
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 0), [0, 15]) 
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 0), [0, 0]) 
            """Test Coordinate 1"""           
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 1), [20, 0])
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 1), [-20, 0])
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 1), [15, 0]) 
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 1), [0, 0]) 
            """Test Coordinate 2"""
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 2), [0, -20])
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 2), [0, 20])
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 2), [0, -15]) 
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 2), [0, 0]) 
            """Test Coordinate 3"""
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 3), [-20, 0])
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 3), [20, 0])
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 3), [-15, 0]) 
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 3), [0, 0]) 
        

    def test_command_list_upper_lower(self):
        """Test Command List with uppercase"""

        with captured_io(StringIO("FoRward 20\nBaCK 20\nSpRiNt 5")):
            robot_name = "Raees"
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 0), [0, 20])
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 0), [0, -20]) 
            input = robot.user_input_command(robot_name)
            self.assertEqual(robot.commands_list(input, robot_name, [0, 0], 0), [0, 15]) 
    

    def test_robot_off(self):
        """Test robot off command"""
    
        with captured_io(StringIO("")):
            robot_name = "Raees"
            """Test Off"""
            self.assertEqual(robot.turn_robot_off("off" , robot_name), True)
            """Test any other command"""
            self.assertEqual(robot.turn_robot_off("go", robot_name), False)

    
    def test_move_forward(self):
        """Test Move forward command"""

        with captured_io(StringIO("")):
            robot_name = "Raees"
            self.assertEqual(robot.move_forward(["forward", "20"], robot_name, [0, 0], 0), [0, 20])
            self.assertEqual(robot.move_forward(["forward", "20"], robot_name, [0, 20], 0), [0, 40])
            self.assertEqual(robot.move_forward(["forward", "50"], robot_name, [0, 0], 1), [50, 0])
            self.assertEqual(robot.move_forward(["FORWARD", "50"], robot_name, [0, 0], 1), [50, 0])

    
    def test_move_back(self):
        """Test Move back command"""

        with captured_io(StringIO("")):
            robot_name = "Raees"
            self.assertEqual(robot.move_back(["back", "20"], robot_name, [0, 0], 0), [0, -20])
            self.assertEqual(robot.move_back(["back", "20"], robot_name, [0, 20], 0), [0, 0])
            self.assertEqual(robot.move_back(["back", "50"], robot_name, [0, 0], 1), [-50, 0])
            self.assertEqual(robot.move_back(["BACK", "20"], robot_name, [0, 20], 0), [0, 0])   


    def test_robot_coordinate(self):
        """Test correct coordinates:
                0
                |
                |
          3-----|-----1
                |
                |
                2   """

        with captured_io(StringIO("")):
            robot_name = "Raees"
            """Test Right with different coordinates"""
            self.assertEqual(robot.robot_coordinate("right", robot_name, 0), 1)
            self.assertEqual(robot.robot_coordinate("right", robot_name, 1), 2)
            self.assertEqual(robot.robot_coordinate("right", robot_name, 2), 3)
            self.assertEqual(robot.robot_coordinate("right", robot_name, 3), 0)
            """Test Right Uppercase with coordinates"""
            self.assertEqual(robot.robot_coordinate("Right", robot_name, 0), 1)
            self.assertEqual(robot.robot_coordinate("rIght", robot_name, 1), 2)
            self.assertEqual(robot.robot_coordinate("riGht", robot_name, 2), 3)
            self.assertEqual(robot.robot_coordinate("rigHt", robot_name, 3), 0)
            """Test Left with different coordinates"""
            self.assertEqual(robot.robot_coordinate("left", robot_name, 0), 3)
            self.assertEqual(robot.robot_coordinate("left", robot_name, 1), 0)
            self.assertEqual(robot.robot_coordinate("left", robot_name, 2), 1)
            self.assertEqual(robot.robot_coordinate("left", robot_name, 3), 2)
            """Test Left uppercase with coordinates"""
            self.assertEqual(robot.robot_coordinate("Left", robot_name, 0), 3)
            self.assertEqual(robot.robot_coordinate("lEft", robot_name, 1), 0)
            self.assertEqual(robot.robot_coordinate("leFt", robot_name, 2), 1)
            self.assertEqual(robot.robot_coordinate("lefT", robot_name, 3), 2)

    def test_robot_position(self):
        """Test robot position returned """
        
        with captured_io(StringIO("")):
            robot_name = "Raees"
            """Test Lowercase with different coordinates"""
            self.assertEqual(robot.robot_position(["forward", "20"], robot_name, [0, 0], 0), [0, 20])
            self.assertEqual(robot.robot_position(["back", "20"], robot_name, [0, 0], 0), [0, -20])
            self.assertEqual(robot.robot_position(["forward", "20"], robot_name, [0, 0], 1), [20, 0])
            self.assertEqual(robot.robot_position(["back", "20"], robot_name, [0, 0], 1), [-20, 0])
            self.assertEqual(robot.robot_position(["forward", "20"], robot_name, [0, 0], 2), [0, -20])
            self.assertEqual(robot.robot_position(["back", "20"], robot_name, [0, 0], 2), [0, 20])
            self.assertEqual(robot.robot_position(["forward", "20"], robot_name, [0, 0], 3), [-20, 0])
            self.assertEqual(robot.robot_position(["back", "20"], robot_name, [0, 0], 3), [20, 0])
            self.assertEqual(robot.robot_position(["go", "20"], robot_name, [0, 0], 0), [0, 0])
            """Test Uppercase with different coordinates"""
            self.assertEqual(robot.robot_position(["FOrward", "20"], robot_name, [0, 0], 0), [0, 20])
            self.assertEqual(robot.robot_position(["BAck", "20"], robot_name, [0, 0], 0), [0, -20])
            self.assertEqual(robot.robot_position(["FOrward", "20"], robot_name, [0, 0], 1), [20, 0])
            self.assertEqual(robot.robot_position(["BAck", "20"], robot_name, [0, 0], 1), [-20, 0])
            self.assertEqual(robot.robot_position(["FOrward", "20"], robot_name, [0, 0], 2), [0, -20])
            self.assertEqual(robot.robot_position(["BAck", "20"], robot_name, [0, 0], 2), [0, 20])
            self.assertEqual(robot.robot_position(["FOrward", "20"], robot_name, [0, 0], 3), [-20, 0])
            self.assertEqual(robot.robot_position(["BAck", "20"], robot_name, [0, 0], 3), [20, 0])


    def test_sprint_range_check(self):
        """Test if sprint is in range of the area"""

        with captured_io(StringIO("")):
            robot_name = "Raees"
            self.assertEqual(robot.sprint_range_check("sprint", 5, robot_name, [0, 0], 0), [0, 15])
            self.assertEqual(robot.sprint_range_check("sprint", 10, robot_name, [0, 5], 0), [0, 60])
            self.assertEqual(robot.sprint_range_check("sprint", 20, robot_name, [0, 0], 0), [0, 0])
            self.assertEqual(robot.sprint_range_check("SPrint", 5, robot_name, [0, 0], 0), [0, 15])

    
    def test_sprint_forward(self):
        """Test Sprint Forward"""

        with captured_io(StringIO("")):
            robot_name = "Raees"
            self.assertEqual(robot.sprint_forward("sprint", 5, robot_name, [0, 0], 0), [0, 15])
            self.assertEqual(robot.sprint_forward("sprint", 10, robot_name, [0, 5], 0), [0, 60])
            self.assertEqual(robot.sprint_forward("sprint", 20, robot_name, [0, 0], 0), [0, 209])
            self.assertEqual(robot.sprint_forward("SPrint", 5, robot_name, [0, 0], 0), [0, 15])