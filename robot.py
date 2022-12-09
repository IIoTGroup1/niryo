"""
...
"""
from pyniryo import api



class Controller:
    def __init__(self, robot, ip_address):
        """
        Constructs the robot controller.
        """
        self.robot = robot
        self.ip_address = ip_address
        


class Robot:
    @staticmethod
    def init(ip_address: str):
        """
        Initializes the robot with the given IP address.
        """
        robot = api.tcp_client.NiryoRobot(ip_address)
#         robot.calibrate_auto()
        return robot

    
