from pathlib import Path

import streamlit as st
from PIL import Image


#Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Tyler Chinn"
PAGE_ICON = ":home:"
NAME = "Tyler Chinn"
DESCRIPTION = """
Data Analyst Masters Student | Materials Engineering Reliability Testing
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

# --- Personal SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Introduction")
st.write(
    """
Hello! This is my personal page. I am a data analyst student looking for collaborative opportunities on data analytics/data science projects. I will do my best to keep it updated with current projects.
Linked are some of my projects and my resume. Feel free to reach out to me if you have any questions or would like to collaborate.
"""
)

st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/04bb78e7667a17e908b57c4f98b60c9d" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: PowerBi, Tableau MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🎮", "**Reliability Engineering Technician | Microsoft (Contact Through Cascade Engineering Services**")
st.write("10/2019 - 10/2020")
st.write(
    """
- ► Led the qualification of suppliers for the Xbox Series X and Xbox Series S based on product lifecycle criteria.
- ► Carried out accelerated environmental and mechanical stress testing to ascertain the product's lifespan.
- ► Created executive dashboards for project progress and performance metrics, saving 10 hours per week.
- ► Streamlined report generation for management and reliability engineers, including predicted field life and inventory for several hundred high-impact prototypes.
"""
)

# --- JOB 2
st.write('\n')
st.write("🧃", "**Quality Assurance | Talking Rain**")
st.write("05/2019 - 09/2019")
st.write(
    """
- ► Managed quality control paperwork and reported inspection test data to ensure regulatory compliance.
- ► Monitored crucial control points and verified procedures using electronic inspection equipment.
- ► Took corrective steps to address the production issue, saving one day's worth of production at the factory.
- ► Used statistical process control software to analyze data and recommend changes to the manufacturing process.
"""
)

# --- JOB 3
st.write('\n')
st.write("🔬", "**Undergraduate Researcher | University of Washington GEMSEC Research Group**")
st.write("06/2017 - 06/2018")
st.write(
    """
- ► Carried out peptide assembly control research with an emphasis on creating medical device products.
- ► generated reports and conducted data analysis for the interdisciplinary lab group. 
- ► Regularly updated standard operating procedures for ongoing lab experiments.
- ► Designed an assembly diagram for the formation of material on a graphite surface.
- ► Collected atomic force microscopy data from samples and processed surface data for categorization.
"""
)

# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")