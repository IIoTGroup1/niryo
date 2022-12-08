"""
...
"""
from pyniryo import *



class Robot:
  @staticmethod
  def init(ip_address: str):
    """
    Initializes the robot with the given IP address.
    """
    return NiryoRobot(ip_address)
