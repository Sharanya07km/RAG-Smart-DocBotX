import streamlit as st
st.set_page_config(page_title="Smart DocBotX", page_icon="🤖", layout="wide")
from demo_page import main
# Initialize session state variables if not already present
if "conversation" not in st.session_state:
    st.session_state.conversation = []


# Set page configuration here (if not already set in landing_page.py)
home_page = st.Page(
    page="views/Home.py",
    title="Home",
    icon="🏠",
    default=True,
)
about_page = st.Page(
    page="views/About.py",
    title="About",
    icon="🧑‍💻",

)
contact_page = st.Page(
    page="views/Contact Us.py",
    title="Team",
    icon="☎",
)
feedback_page = st.Page(
    page="views/Feedback.py",
    title="Feedback",
    icon="📩",
)

pg = st.navigation(pages=[home_page, about_page, contact_page, feedback_page])
pg.run()