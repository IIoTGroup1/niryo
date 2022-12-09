"""
...
"""

import os
import sys
import socket
import streamlit as st
from functions import valid_ip


st.set_page_config(
    page_title="Niryo",
    layout="centered",
    page_icon=":computer:"
)


class Client:
    def __init__(self,serverIP,serverPort):
        self.serverIP = serverIP
        self.serverPort = serverPort
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def connect_to_server(self) -> None:
        self.socket.connect((self.serverIP,self.serverPort))
        print(f"\n\n>> Connected to {self.serverIP}:{self.serverPort}.\n\n")
    
    def send(self,message) -> None:
        self.socket.send(str.encode(message))
        print(f"\n      >>     Sent: \"{message}\"")
    
    def receive(self,bufferSize) -> None:
        message = self.socket.recv(bufferSize)
        if message:
            print(f"      >> Received: \"{message.decode('utf-8')}\"\n\n")
            return message

    def close_connection(self) -> None:
        self.socket.close()
        print(">> Connection closed.\n\n\n")


        
        
        
if 'client' not in st.session_state:
    st.session_state.client = None

if 'ip_address' not in st.session_state:
    st.session_state.ip_address = None
        
        
        
        
        
# -----------


st.markdown("# Robot Stuff")
st.markdown("---")
st.markdown("##")



with st.form(key='ip_input'):
    ip_address = st.text_input("IP Address")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        if valid_ip(ip_address):
            st.session_state.ip_address = ip_address
            client = Client(ip_address,40001)
            #st.session_state.client = client
            client.connect_to_server()
            client.send("{'param_list': ['AUTO'], 'command': 'CALIBRATE'}")
            msg = client.receive(1024)
            st.success(f"Received {msg}.")
            #st.success(f"Successfully connected to robot with IP {ip_address}.")
            #try:
                #st.session_state.robot = Robot.init(ip_address)
                #st.success(f"Successfully connected to robot with IP {ip_address}.")
            #except Exception as e:
                #st.error(f"{e}")
        else:
            st.error(f"The IP address {ip_address} is not valid.")
        









# from robot import *
# import streamlit as st
# from functions import *



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
