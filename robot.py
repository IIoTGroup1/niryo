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
        return api.tcp_client.NiryoRobot(ip_address)
