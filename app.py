"""
...
"""

#import pyniryo
from pyniryo import *
import streamlit as st



st.set_page_config(
    page_title="Niryo",
    layout="centered",
    page_icon=":computer:"
)


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
        st.success("Successfully stored IP.")
        st.session_state.ip_address = ip_address
