import streamlit as st

# Add custom CSS for psychedelic theme
st.markdown("""
    <style>
        body {
            background: radial-gradient(circle, rgba(255, 105, 180, 0.7), rgba(0, 255, 255, 0.7));
            font-family: 'Courier New', Courier, monospace;
            color: #fff;
        }
        
        h1, h2, h3 {
            font-family: 'Arial', sans-serif;
            color: #ff1493;
            text-align: center;
        }
        
        h1 {
            font-size: 3.5rem;
            color: #00ffff;
            text-shadow: 2px 2px 8px rgba(0, 255, 255, 0.7);
        }

        h2, h3 {
            font-size: 2.5rem;
            text-shadow: 2px 2px 5px rgba(255, 105, 180, 0.8);
        }

        p, li {
            font-size: 1.2rem;
            line-height: 1.8;
        }

        .stButton button {
            background-color: #ff1493;
            color: #fff;
            font-size: 1.5rem;
            border-radius: 10px;
            border: none;
            padding: 10px 20px;
            transition: background-color 0.3s ease;
        }

        .stButton button:hover {
            background-color: #00ffff;
        }

        .section-title {
            color: #ff6347;
            text-shadow: 2px 2px 6px rgba(255, 69, 0, 0.9);
            font-size: 2.5rem;
            text-align: center;
        }

        .section-content {
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 12px rgba(255, 105, 180, 0.7);
        }

        .contact-form input, .contact-form textarea {
            background-color: rgba(255, 255, 255, 0.1);
            color: #fff;
            border: 1px solid #ff6347;
            padding: 10px;
            border-radius: 10px;
            width: 100%;
            margin-bottom: 10px;
        }

        .contact-form button {
            background-color: #00ffff;
            color: #fff;
            border: none;
            border-radius: 10px;
            padding: 12px 20px;
            font-size: 1.5rem;
            cursor: pointer;
        }

        .contact-form button:hover {
            background-color: #ff1493;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the webpage
st.title("Sara de la Salle - Researcher Portfolio")

# Home Section
st.header("Welcome to My Research Portfolio!")
st.write("""
    Hello, I am Sara de la Salle, a researcher specializing in neuropsychology and psychiatry. 
    My work focuses on the neural mechanisms of psychiatric disorders, with a particular interest in sensory processing, depression, and the effects of psychedelics.
    Feel free to browse through my work, publications, and get in touch if you'd like to collaborate.
""")

# About Me Section
st.header("About Me")
st.write("""
    I am currently a researcher at [Institution or University Name], specializing in the neural basis of psychiatric disorders. 
    My research interests include [Research Focus 1], [Research Focus 2], and the effects of various pharmacological interventions on mental health.
    I am deeply involved in clinical studies and research exploring treatments for mood disorders, including depression and anxiety.
""")

# Research Section
st.header("Research")
st.write("""
    Here are some of my recent projects and publications:
""")

# Example Research/Publication 1
st.subheader("Acute subanesthetic ketamine-induced effects on the mismatch negativity and their relationship to early and sustained treatment response in major depressive disorder")
st.write("""
    **Published**: Feb 2025  
    **Co-authors**: Jennifer L Phillips, Pierre Blier, Verner Knott  
    This study examines the effects of sub-anesthetic doses of ketamine on mismatch negativity (MMN), a neural marker, in patients with major depressive disorder.
    [View Article](#)
""")

# Contact Section
st.header("Contact Me")
st.write("""
    You can reach me at:
    - Email: [email@example.com]
    - LinkedIn: [LinkedIn Profile Link]
    - ResearchGate: [ResearchGate Profile Link]
""")

# Contact Form
st.header("Contact Form")
contact_form = """
<div class="contact-form">
    <form action="https://formsubmit.co/your-email@example.com" method="POST">
      <input type="text" name="name" placeholder="Your Name" required>
      <input type="email" name="email" placeholder="Your Email" required>
      <textarea name="message" placeholder="Your Message" required></textarea>
      <button type="submit">Send Message</button>
    </form>
</div>
"""
st.markdown(contact_form, unsafe_allow_html=True)
