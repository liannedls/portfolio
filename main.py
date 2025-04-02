import streamlit as st

# Set the page config
st.set_page_config(page_title="Researcher Landing Page", layout="wide")

# Set the custom CSS for earthy color palette
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f0f5f1;  # Light earthy background
        }
        .title {
            color: #4b3c31;  # Dark brown title text
        }
        .header {
            color: #5a4e39;  # Medium brown
        }
        .subheader {
            color: #6d7b4d;  # Olive green subheader text
        }
        .section {
            background-color: #e4e9e2;  # Light greenish beige for sections
            padding: 20px;
            border-radius: 10px;
        }
        .button {
            background-color: #7b6d4e;  # Earthy brown button
            color: white;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True
)

# Title and introductory section
st.markdown('<h1 class="title">Dr. Sara de la Salle - Researcher</h1>', unsafe_allow_html=True)
st.markdown('<p class="header">Welcome to the landing page of Dr. Sara de la Salle, a passionate scientist focused on environmental sustainability and climate change.</p>', unsafe_allow_html=True)

# Research Interests Section
st.markdown('<h2 class="subheader">Research Interests</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <ul>
        <li>Climate Change Impact on Biodiversity</li>
        <li>Sustainable Agricultural Practices</li>
        <li>Environmental Policy and Global Climate Initiatives</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Publications Section
st.markdown('<h2 class="subheader">Key Publications</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <ul>
        <li><a href="https://example.com/publication1" target="_blank">"The Role of Forests in Carbon Sequestration"</a></li>
        <li><a href="https://example.com/publication2" target="_blank">"Sustainable Water Management Practices in Agriculture"</a></li>
        <li><a href="https://example.com/publication3" target="_blank">"Innovations in Green Technology for the 21st Century"</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown('<h2 class="subheader">Contact</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <p>Interested in collaborating or learning more about my research? Feel free to reach out:</p>
    <a href="mailto:sara.delasalle@example.com" class="button">Email Dr. Sara de la Salle</a>
</div>
""", unsafe_allow_html=True)

# Footer with social links
st.markdown('<h3 class="subheader">Follow Me</h3>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <a href="https://twitter.com/saradelasalle" target="_blank">Twitter</a> | 
    <a href="https://github.com/saradelasalle" target="_blank">GitHub</a> | 
    <a href="https://www.linkedin.com/in/saradelasalle" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
