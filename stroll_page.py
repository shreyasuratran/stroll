import streamlit as st

def stroll_page():
    st.title("Begin our stroll")
    st.write("Let's begin our stroll")

# Initialize the selected page outside of functions
if "selected_page" not in st.session_state:
    st.session_state.start_stroll = True

st.sidebar.header("Navigate to a Page")
page = st.sidebar.selectbox("Select a page", ["Home", "Stroll"])

# Mapping of pages to their corresponding functions
page_dict = {"Home": home_page, "Stroll": stroll_page}

# Display the selected page
if page in page_dict:
    page_dict[page]()