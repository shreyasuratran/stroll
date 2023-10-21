import streamlit as st

def home_page():
    st.title("Welcome to Stroll")

    st.write("Step into Savings: Find Coupons Near You")

    placeholder_image = st.empty()

    user_location = st.text_input("Enter your ZIP code or click 'Find Current Location' to get your coordinates:")
    find_location_button = st.button("Find Current Location")

    search_button = st.button("Search")

    nearby_places = [
        {"name": "Restaurant A", "description": "A nice restaurant", "link": "https://restaurantA.com"},
        {"name": "Store B", "description": "A local store", "link": "https://storeB.com"},
        {"name": "Shop C", "description": "A good shop", "link": "https://shopC.com"},
    ]

    for place in nearby_places:
        st.subheader(place["name"])
        st.write(place["description"])
        
        button_text = f"Learn More about {place['name']}"
        show_popup = st.button(button_text)

        if show_popup:
            # Display the pop-up with additional information
            with st.expander(f"{place['name']} Details"):
                st.write(f"**{place['name']}**")
                st.write(f"*{place['description']}*")
                st.write(f"Link: [{place['name']}]({place['link']}")
                st.write("Coupon Code: ABC123")
                st.write("Coupon Details: 10% off your order")
                st.write("Distance: 1.5 miles")  # Replace with actual distance
                if st.button("Start Your Stroll"):
                    st.write("Redirecting to Stroll Page...")  
                    st.session_state.selected_page = "Stroll" 

            button_text = f"Close Window"
            st.button(button_text)

def stroll_page():
    st.title("Begin our stroll")
    st.write("Let's begin our stroll")

# Initialize the selected page outside of functions
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

st.sidebar.header("Navigate to a Page")
page = st.sidebar.selectbox("Select a page", ["Home", "Stroll"])

# Mapping of pages to their corresponding functions
page_dict = {"Home": home_page, "Stroll": stroll_page}

# Display the selected page
if page in page_dict:
    page_dict[page]()
