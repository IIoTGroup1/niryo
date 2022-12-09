"""
...
"""
from pyniryo import api



class Robot:
    @staticmethod
    def init(ip_address: str):
        """
        Initializes the robot with the given IP address.
        """
        robot = api.tcp_client.NiryoRobot(ip_address)
        robot.calibrate_auto()
        return robot
