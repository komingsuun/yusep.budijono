from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Yusep Budijono"
PAGE_ICON = ":wave:"
NAME = "Yusep Budijono"
DESCRIPTION = """
Quality Assurance Engineer
"""
EMAIL = "sepdijono@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/yusep-budijono-504688215/",
    "GitHub": "https://github.com/sepdijono",
}

PROJECTS = {
    "🏆 BCA Young Comunity": "Social Media for BCA Solitaire & BCA Prioritas (Webadmin, Android, iOS)",
    "🏆 MCM BudMon": "Budget Monitoring for PT Merah Cipta Media (Webadmin)",
    "🏆 BCA MC2": "Internal Social Media PT BCA Tbk (Web, Android, Desktop App)",
    "🏆 EurekaEveryDay": "Internal Social Media PT Bukit Muria Jaya (Web, Android)",
    "🏆 DisiniSharing": "Internal Social Media PT Djarum (Web)",
    "🏆 MindTalk": "Indonesia Social Media Pioneer (Web, Android)",
}

GIT_HUBS = {
    "🏆 Robot Framework Connect & Simple Automation Test using Appium": "https://github.com/sepdijono/appium",
    "🏆 TerminalX (pyside2-termx) using Python PySide2": "https://github.com/sepdijono/pyside2-termx",
    "🏆 ANPR Another Realtime Plate Recognition Application": "https://github.com/sepdijono/another-realtime-anpr",
    "🏆 ANPR Another Realtime Plate Recognition (OCR API Server using easyocr & fastapi)": "https://github.com/sepdijono/another-realtime-anpr-ocr",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
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
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 7 Years expereince work in development environment using JiRa, Git
- ✔️ Able to develop test methods for debugging processes, both during product development and when performing maintenance. 
- ✔️ Good understanding of automation principles and their respective applications such as : Appium, Selenium, Cypress
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Qt, PySine2, Flask, openCV, parmiko), SQL
- 📊 PostgreSQL: console
- 📚 Computer Literacy: PC Troubleshooting, data recovery, linux, windows, 
- 🗄️ Project & source Management: JiRa, Git
- 🌐 Android Studio: build simple app
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Software Quality Assurance | PT Ansvia**")
st.write("02/2015 - Present")
st.write(
    """
- ► Using all possibilities frontend and backend end to end test the project 
- ► Provide automated dummy data generation to the project especially for new project that come with no data
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Gereja Santo Yusuf - Cemani Surakarta**")
st.write("2020 - 2021 6 Months")
st.write(
    """
- ► Built: Flask API Server & Android Client "Presensi QR Code Kehadiran Umat untuk Mitigasi Covid19"
- ► PostgreSQL & OpenCV
- ► Social working
"""
)


# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f" {project} {link}")

# --- Github Projects ---
st.write('\n')
st.subheader("Github Projects")
st.write("---")
for gitprj, link in GIT_HUBS.items():
    st.markdown(f" [{gitprj}]({link})")
st.markdown('[Back to Top](#section-1)')
# txt = """
# <script>window.parent.document.querySelector('section.main').scrollTo(0, 0);</script>
# """
# st.markdown(txt, unsafe_allow_html=True)

# st.markdown(''' <a target="_self" href="#section-1">
#                     <button>
#                         Back to Top
#                     </button>
#                 </a>''', unsafe_allow_html=True)

# from pathlib import Path
#
# import streamlit as st
# from PIL import Image
#
# # ------------ PATH SETTINGS  ---------------
# current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# print(current_dir)
# css_file = current_dir / "styles" / "main.css"
# resume_file = current_dir / "assets" "cv.pdf"
# profile_file = current_dir / "assets" "profile-pic.png"
#
# # ------------ GENERAL SETTINGS  ---------------
# PAGE_TITLE = "Digital "
#
#
