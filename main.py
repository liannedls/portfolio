import streamlit as st

# Setting up the page config
st.set_page_config(page_title="Researcher Portfolio", page_icon="📚", layout="wide")

# Define custom styles
st.markdown("""
    <style>
        body {
            background-color: #f4f1e1;  /* Soft earthy background */
            font-family: "Arial", sans-serif;
        }
        .header {
            color: #3d4c43;  /* Deep earthy green */
            font-size: 2.5em;
            font-weight: bold;
        }
        .subheader {
            color: #5a7462;  /* Lighter earthy green */
            font-size: 1.5em;
            margin-top: 20px;
        }
        .content {
            color: #3d4c43;  /* Deep earthy green */
            line-height: 1.8;
        }
        .footer {
            color: #8e9a7d;  /* Light earthy green */
            font-size: 1em;
            text-align: center;
            padding-top: 50px;
        }
        .card {
            background-color: #e7f1e7; /* Light green card background */
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
        }
        .card-title {
            font-weight: bold;
            font-size: 1.2em;
            color: #3d4c43;
        }
        .card-description {
            color: #5a7462;
        }
    </style>
""", unsafe_allow_html=True)

# Main content

# Header section
st.markdown('<p class="header">Welcome to My Research Portfolio</p>', unsafe_allow_html=True)
st.write("Hello, I'm [Your Name], a passionate researcher in [Your Field of Research]. Explore my work and learn more about my ongoing projects and publications.")

# About me section
st.markdown('<p class="subheader">About Me</p>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <p>I am a researcher focused on [Your Research Focus]. With years of experience in [mention expertise areas],
        I work on [briefly describe your research contributions, methodologies, or goals].</p>
    </div>
""", unsafe_allow_html=True)

# Research Projects section
st.markdown('<p class="subheader">Research Projects</p>', unsafe_allow_html=True)
# Example research project 1
with st.expander("Project 1: Title of Your Research Project"):
    st.markdown("""
        <div class="card">
            <p class="card-title">Project Title</p>
            <p class="card-description">Brief description of your research project. This can include methodology, findings, and outcomes. You can also link to your papers or project pages here.</p>
        </div>
    """, unsafe_allow_html=True)
    
# Example research project 2
with st.expander("Project 2: Another Research Project"):
    st.markdown("""
        <div class="card">
            <p class="card-title">Project Title</p>
            <p class="card-description">Brief description of another research project. Include any important results or applications. You can also provide links or visuals for the project here.</p>
        </div>
    """, unsafe_allow_html=True)

# Contact section
st.markdown('<p class="subheader">Contact</p>', unsafe_allow_html=True)
st.markdown("""
    <div class="content">
        <p>Feel free to reach out to me via email at: <a href="mailto:your.email@example.com">your.email@example.com</a></p>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">Made with ❤️ using Streamlit</p>', unsafe_allow_html=True)

