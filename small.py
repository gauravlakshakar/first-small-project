import streamlit as st

# 1. Displaying Text
st.write("Welcome to My First Streamlit App")

# 2. Adding a Header
st.header("This is a Header")

# 3. Using a Button
if st.button("Click Me"):
    st.write("Button Clicked")

# 4. Displaying a Simple List
favorite_fruits = ["Apple", "Banana", "Cherry"]
st.write("My favorite fruits:")
st.write(favorite_fruits)

# 5. Adding an Image
image_url = "https://images.pexels.com/photos/14918477/pexels-photo-14918477.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"  
st.image(image_url, caption="Sample Image", use_column_width=True)
