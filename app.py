"""
...
"""
import asyncio
import streamlit as st
from robot import Robot
from util import valid_ip, get_datetime


st.set_page_config(
    page_title="Niryo",
    layout="centered",
    page_icon=":computer:"
)


if 'robot' not in st.session_state:
    st.session_state.robot = None

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'ip_address' not in st.session_state:
    st.session_state.ip_address = None


def go_home():
    """
    Returns the robot to home position.
    """
    if st.session_state.robot:
        try:
            st.session_state.robot.move_to_home_pose()
            st.success("Home position command sent successfully.")
        except:
            st.error("Failed to send home position command.")
        


async def update(st_empty, st_empty2, st_empty3):
    while True:
        st.session_state.counter += 1
        current_datetime = get_datetime()
        st_empty.markdown(f"<h3 style='position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; color: #fafafa;'>{current_datetime}</h3>", unsafe_allow_html=True)
        if st.session_state.robot and st.session_state.counter%5 == 0:
            joints = st.session_state.robot.get_joints()
            st_empty2.write(str(joints))
            pose = st.session_state.robot.get_pose().to_list()
            st_empty3.write(str(pose))
        await asyncio.sleep(1)


# ----------------------------------------------


st.markdown("# Robot Stuff")
st.markdown("---")
st.markdown("##")


with st.form(key='ip_input'):
    ip_address = st.text_input("IP Address")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        if valid_ip(ip_address):
            st.session_state.ip_address = ip_address
            try:
                robot = Robot.init(ip_address)
                st.success(f"Successfully connected to robot with IP {ip_address}.")
                st.session_state.robot = robot
            except Exception as e:
                st.error(f"{e}")
        else:
            st.error(f"The IP address {ip_address} is not valid.")


st.markdown("##")
st.markdown("##")
st.markdown("##")

homeButton = st.button("Home Position", key=None, help=None, on_click=go_home)

st.markdown("##")
st.markdown("##")
st.markdown("##")


st.markdown("# Joint position")
st.markdown("---")
st.markdown("##")
joint_pos = st.empty()


st.markdown("##")
st.markdown("##")
st.markdown("##")


st.markdown("# Current Pose")
st.markdown("---")
st.markdown("##")
current_pose = st.empty()



# ----------------------------------------------    FOOTER


st.markdown("##")
st.markdown("##")
footer = st.empty()

asyncio.run(update(footer, joint_pos, current_pose))
