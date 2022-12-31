from pathlib import Path

import streamlit as st
from PIL import Image


# st.set_page_config(
#     page_title="HomePage",
#     page_icon=":house:",
# )



#Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "Profile.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Tyler Chinn"
PAGE_ICON = ":wave:"
NAME = "Tyler Chinn"
DESCRIPTION = """
Data Analyst Masters Student | Materials Science and Engineering Reliability Testing
"""
EMAIL = "tyler.chinn@csuglobal.edu"
SOCIAL_MEDIA = {
    #"YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    #"Twitter": "https://twitter.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.sidebar.success("Select a page from the sidebar")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)