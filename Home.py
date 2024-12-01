import streamlit as st
from demo_page import main
col1 = st.columns(1)[0]  # Access the first column

# Background image styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpapercave.com/wp/wp10299390.jpg");
    background-size: cover;
    background-attachment: fixed; /* Ensure background stays fixed when scrolling */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# Subtitle styling for centering the subtitle below the title
subtitle_style = """
<style>
p#subtitle {
    position: fixed;
    top: 50%; /* Adjust this value to move the subtitle vertically */
    left: 74%;
    transform: translateX(-50%); /* Center the subtitle horizontally */
    color: white;
    font-family: 'Verdana', sans-serif;
    font-size: 2.5em; /* Adjust font size as needed */
    margin: 0;
    z-index: 1000; /* Ensure it stays above other elements */
}
</style>
"""
st.markdown(subtitle_style, unsafe_allow_html=True)

# Button styling for centering the demo button below the subtitle
demo_button_style = """
<style>
div.stButton > button {
    position: fixed;
    top: 80%; /* Adjust this value to move the button vertically */
    left: 80%;
    transform: translateX(-50%); /* Center the button horizontally */
    z-index: 1000;  /* Ensure the button stays above other elements */
}
</style>
"""
st.markdown(demo_button_style, unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'show_chatbot' not in st.session_state:
    st.session_state.show_chatbot = False
if 'download_content' not in st.session_state:
    st.session_state.download_content = False  # Set to the appropriate default value

# Display the home page content if show_chatbot is False
if st.session_state.show_chatbot:
    main()
if not st.session_state.show_chatbot:
    with col1:
        st.markdown(
            """
            <h1 style="
                position: fixed;
                text-align: left; 
                color: white; 
                font-family: 'Verdana', sans-serif; 
                font-size: 3em;">
                Welcome to Smart DocBotX !!
            </h1>
            """,
            unsafe_allow_html=True
        )
    demo_button_style = """
    <style>
    div.stButton > button {
        position: fixed;
        top: 68%; /* Adjust this value to move the button vertically */
        left: 74%;
        transform: translateX(-50%); /* Center the button horizontally */
        z-index: 1000;  /* Ensure the button stays above other elements */
    }
    </style>
    """
    st.markdown('<p id="subtitle">Faster insights, smarter answers <br/>— powered by RAG</p>', unsafe_allow_html=True)
    if st.button("Ask DocBotX", key="demo_button"):
        st.session_state.show_chatbot= True