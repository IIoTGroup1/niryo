"""
...
"""
import asyncio
import streamlit as st
from robot import Robot
from util import valid_ip, footer, update_footer


st.set_page_config(
    page_title="Niryo",
    layout="centered",
    page_icon=":computer:"
)
st.markdown(footer,unsafe_allow_html=True)

if 'robot' not in st.session_state:
    st.session_state.robot = None

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if 'ip_address' not in st.session_state:
    st.session_state.ip_address = None


async def update():
    while True:
        st.session_state.counter += 1
        # do stuff
        st.markdown(update_footer(str(st.session_state.counter)), unsafe_allow_html=True)
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
st.markdown("---")
st.markdown("##")


asyncio.run(update())
