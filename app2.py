"""
...
"""
import os
import sys
import socket
import streamlit as st
from pyniryo import api
from functions import valid_ip



class Robot:
  @staticmethod
  def init(ip_address: str):
    """
    Initializes the robot with the given IP address.
    """
    return api.tcp_client.NiryoRobot(ip_address)





# st.set_page_config(
#     page_title="Niryo",
#     layout="centered",
#     page_icon=":computer:"
# )


# if 'robot' not in st.session_state:
#     st.session_state.robot = None

# if 'ip_address' not in st.session_state:
#     st.session_state.ip_address = None

    
    
# # -----------


# st.markdown("# Robot Stuff")
# st.markdown("---")
# st.markdown("##")




# with st.form(key='ip_input'):
#     ip_address = st.text_input("IP Address")
#     submit_button = st.form_submit_button("Submit")
#     if submit_button:
#         if valid_ip(ip_address):
#             st.session_state.ip_address = ip_address
#             st.session_state.robot = Robot.init(ip_address)
#             st.success(f"Successfully connected to robot with IP {ip_address}.")
#             try:
#                 st.session_state.robot = Robot.init(ip_address)
#                 st.success(f"Successfully connected to robot with IP {ip_address}.")
#             except Exception as e:
#                 st.error(f"{e}")
#         else:
#             st.error(f"The IP address {ip_address} is not valid.")
