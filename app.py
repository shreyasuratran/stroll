import streamlit as st
from home_page import home_page
from stroll_page import stroll_page
st.set_page_config(page_title="Stroll App")

# Initialize the session state variable
if "start_stroll" not in st.session_state:
    st.session_state.start_stroll = False

# Create the sidebar navigation
st.sidebar.header("Navigate to a Page")
page = st.sidebar.selectbox("Select a page", ["Home", "Stroll"])

# Display the selected page
if page == "Home":
    home_page()
elif page == "Stroll" and st.session_state.start_stroll:
    stroll_page()