import streamlit as st
# Set the page title and add a heading
st.set_page_config(page_title="Stroll")
st.title("Welcome to Stroll")


# Provide a brief description
st.write("Step into Savings: Find Coupons Near You")

# Create input elements for user interaction
user_location = st.text_input("Enter your location:")
search_button = st.button("Search")