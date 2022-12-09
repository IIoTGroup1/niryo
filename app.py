"""
...
"""
import asyncio
import streamlit as st
from robot import Robot
from numpy import radians as rad
from util import valid_ip, get_datetime


st.set_page_config(
    page_title="Niryo",
    layout="centered",
    page_icon=":computer:"
)


if 'robot' not in st.session_state:
    st.session_state.robot = None

if 'count' not in st.session_state:
    st.session_state.count = 0

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'ip_address' not in st.session_state:
    st.session_state.ip_address = None
    
if 'max_arm_velocity' not in st.session_state:
    st.session_state.max_arm_velocity = 10

if 'saved_pose_dict' not in st.session_state:
    st.session_state.saved_pose_dict = {}


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
        try: st.session_state.count += 1
        except: st.session_state.count = 1
        try: st.session_state.counter += 1
        except: st.session_state.counter = 1
        current_datetime = get_datetime()
        st_empty.markdown(f"<h3 style='position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; color: #fafafa;'>{current_datetime}</h3>", unsafe_allow_html=True)
        if st.session_state.robot and st.session_state.count%5 == 0:
            joints = st.session_state.robot.get_joints()
            st_empty2.write(str(joints))
            pose = st.session_state.robot.get_pose().to_list()
            st_empty3.write(str(pose))
        await asyncio.sleep(1)


# ----------------------------------------------


st.markdown("# Dashboard")
st.markdown("---")
st.markdown("##")


with st.form(key='ip_input'):
    ip_address = st.text_input("IP Address")
    submit_button = st.form_submit_button("Connect")
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




st.markdown("## Parameters")
st.markdown("---")
# Max arm velocity control slider
max_arm_velocity = st.slider("Max Arm Velocity",min_value=1,max_value=100,value=st.session_state.max_arm_velocity,step=1)



st.markdown("##")
st.markdown("##")




st.markdown("## Commands")
st.markdown("---")
homeButton = st.button("Go To Home Position", key=None, help=None, on_click=go_home)

st.markdown("##")

with st.form(key='joint_pos_input'):
    st.markdown("### Set joint angles (degrees)")
    col1,col2 = st.columns(2)
    with col1:
        joint1 = st.number_input("Joint 1", min_value=0, max_value=360, step=1)
        joint2 = st.number_input("Joint 2", min_value=0, max_value=360, step=1)
        joint3 = st.number_input("Joint 3", min_value=0, max_value=360, step=1)
    with col2:
        joint4 = st.number_input("Joint 4", min_value=0, max_value=360, step=1)
        joint5 = st.number_input("Joint 5", min_value=0, max_value=360, step=1)
        joint6 = st.number_input("Joint 6", min_value=0, max_value=360, step=1)
    submit_joint_pos_button = st.form_submit_button("Send Joint Angles")
    if submit_joint_pos_button:
        try:
            joint_positions = [rad(joint1),rad(joint2),rad(joint3),rad(joint4),rad(joint5),rad(joint6)]
            st.session_state.robot.move_joints(joint_positions)
            st.success(f"Successfully sent joint angles  {str(joint_positions)}.")
        except Exception as e:
            st.error(f"{e}")

st.markdown("##")

with st.form(key='end_effector_pos'):
    st.markdown("### Set pose (meters, degrees)")
    location,angles = st.columns(2)
    with location:
        x = st.number_input("x")
        y = st.number_input("y")
        z = st.number_input("z")
    with angles:
        roll = st.number_input("Roll", min_value=0, max_value=360, step=1)
        pitch = st.number_input("Pitch", min_value=0, max_value=360, step=1)
        yaw = st.number_input("Yaw", min_value=0, max_value=360, step=1)
    linear = st.checkbox("Linear", value=True, help="Move to specified pose with a linear trajectory.")
    submit_pose_button = st.form_submit_button("Send Pose")
    if submit_pose_button:
        try:
            pose = [x,y,z,rad(roll),rad(pitch),rad(yaw)]
            if linear:
                st.session_state.robot.move_linear_pose(pose)
            else: st.session_state.robot.move_pose(pose)
            st.success(f"Successfully sent pose  {str(joint_positions)}.")
        except Exception as e:
            st.error(f"{e}")

st.markdown("##")

with st.form(key='save_pose'):
    st.markdown("### Save Current Pose")
    pose_name = st.text_input("Name of pose")
    save_button = st.form_submit_button("Save")
    if save_button:
        try:
            st.session_state.robot.save_pose(pose_name, st.session_state.robot.get_pose().to_list())
#             st.session_state.saved_pose_dict[pose_name] = st.session_state.robot.get_pose().to_list()
            st.success("Successfully saved pose.")
        except:
            st.error("Failed to save pose.")
    
st.markdown("##")

with st.form(key='pick_from_pose'):
    st.markdown("### Pick Object")
    pose_name = st.text_input("Object's Pose Name")
    execute_button = st.form_submit_button("Execute")
    if execute_button:
        try:
            st.session_state.robot.pick_from_pose(st.session_state.robot.get_pose_saved(pose_name))
            st.success("Successfully saved pose.")
        except:
            st.error("Failed to save pose.")
        
            

st.markdown("##")
st.markdown("##")
st.markdown("##")
st.markdown("##")


st.markdown("## Position Info")
st.markdown("---")
st.markdown("##")
# joint_pos = st.empty()
st.markdown("### Current pose:")
st.markdown("### Joint positions:")
st.markdown("##")


# st.markdown("##")
# st.markdown("##")
# st.markdown("##")


# st.markdown("### Current Pose")
st.markdown("---")
st.markdown("##")
current_pose = st.empty()



# ----------------------------------------------    FOOTER


st.markdown("##")
st.markdown("##")
footer = st.empty()

#asyncio.run(update(footer, joint_pos, current_pose))
