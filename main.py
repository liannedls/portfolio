import streamlit as st

# Sidebar for researcher navigation and info
with st.sidebar:
    #st.image("sara_de_la_salle.jpg", width=200)  # Replace with Sara's image
    st.title("Researcher Profile")
    st.markdown("Welcome to my professional profile. Explore my research, publications, and ongoing projects.")
    st.markdown("### Contact Information")
    st.markdown("📧 sara@example.com")  # Replace with actual email if needed
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/sara-de-la-salle-19b8a250/)")
    st.markdown("[Google Scholar](https://scholar.google.com/citations?user=yourID)")  # Replace with actual Google Scholar link if available

# Main title
st.title("Dr. Sara de la Salle - Postdoctoral Fellow")
st.caption("Exploring altered states of consciousness and advancing mental health treatments.")

# Introduction Section
st.header("About Me")
st.markdown("""
I am a Postdoctoral Fellow in the Department of Psychiatry at McGill University, where I work with Drs. Kyle Greenway, Soham Rej, Alex Lehmann, and Michael Lifshitz. 
I completed my Ph.D. in Experimental Psychology at the University of Ottawa, where I examined clinical and electrophysiological correlates of the antidepressant treatment response to ketamine infusions in treatment-resistant depression.
My current research focuses on altered states of consciousness, psilocybin-assisted psychotherapy, the experiential factors of ‘set’ (mindset) and ‘setting’ (physical and social environments), and the importance of culture and individually-tailoring mental health treatments.
Currently, I am supported by a Canadian Institutes of Health Research (CIHR) Postdoctoral Fellowship award.
""")

# Research Interests
st.header("Research Interests")
st.markdown("""
- **Altered States of Consciousness**: Investigating how altered states, including those induced by psychedelics, affect mental health.
- **Psilocybin-Assisted Psychotherapy**: Exploring the use of psilocybin in therapeutic settings for mental health disorders.
- **Mindset and Environment**: Studying the importance of 'set' (mindset) and 'setting' (physical/social environment) in mental health treatments.
- **Cultural Tailoring of Mental Health Treatments**: Focusing on the integration of cultural considerations in personalizing mental health care.
""")

# Publications Section
st.header("Publications")
st.markdown("""
Here are some of my most recent publications:

1. **Acute subanesthetic ketamine-induced effects on the mismatch negativity and their relationship to early and sustained treatment response in major depressive disorder**  
   *Sara de la Salle, Jennifer L Phillips, Pierre Blier, Verner Knott*  
   _Published: February 2025_  
   A study exploring how ketamine's antidepressant effects correlate with neural markers in major depressive disorder.  
   [Read more](#)

2. **Ontario healthcare workers who sought treatment for their mental health during the first five waves of the COVID-19 pandemic: a snapshot of self-referrals across the province**  
   *Judith M Laposa, Duncan Cameron, Kim Corace, Randi E McCabe, Sara de la Salle*  
   _Published: February 2025_  
   Examines mental health referrals by healthcare workers in Ontario during the pandemic.  
   [Read more](#)

3. **The ketamine chameleon: history, pharmacology, and the contested value of experience**  
   *Danny Diep, Sara de la Salle, Julien Thibault Lévesque, Kyle Greenway*  
   _Published: January 2025_  
   A review of ketamine's diverse applications and subjective effects in clinical practice.  
   [Read more](#)

4. **Electrocortical Profiles in Relation to Childhood Adversity and Depression Severity: A Preliminary Report**  
   *Natalia Jaworska, Sara de la Salle, Bronwen Schryver, Verner Knott*  
   _Published: November 2024_  
   Investigates the relationship between childhood adversity and depression severity through electroencephalographic measures.  
   [Read more](#)

5. **Longitudinal experiences of Canadians receiving compassionate access to psilocybin-assisted psychotherapy**  
   *Sara de la Salle, Hannes Kettner, Julien Thibault Lévesque, Kyle Greenway*  
   _Published: July 2024_  
   A longitudinal study on the effectiveness of psilocybin-assisted psychotherapy in Canadian patients with life-threatening illnesses.  
   [Read more](#)

6. **Influence of GABAA and GABAB receptor activation on auditory sensory gating and its association with anxiety in healthy volunteers**  
   *Sara de la Salle, Justin Piche, Brittany Duncan, Verner Knott*  
   _Published: April 2024_  
   This research investigates how GABA receptor activation influences sensory processing and its link to anxiety.  
   [Read more](#)

7. **Auditory P50 Sensory Gating Alterations in Major Depressive Disorder and their Relationship to Clinical Symptoms**  
   *Sara de la Salle, Hayley Bowers, Meagan Birmingham, Verner Knott*  
   _Published: April 2024_  
   Explores how sensory gating dysfunction is a feature of depression and its impact on clinical symptoms.  
   [Read more](#)

(And more…)
""")

# Ongoing Projects Section
st.header("Ongoing Projects")
st.markdown("""
- **Project 1**: Investigating the effects of psilocybin-assisted psychotherapy on treatment-resistant depression.
- **Project 2**: Exploring the role of mindset and environment in the success of psychedelic-assisted therapies.
- **Project 3**: Analyzing the cultural factors in mental health treatment, focusing on individual needs and cultural relevance.
""")

# Optional: Add a Contact Form or Feedback Section
st.header("Contact Me")
st.markdown("""
Feel free to reach out to me for collaboration, inquiries, or feedback.
""")
contact_form = st.form(key='contact_form')
name = contact_form.text_input("Your Name")
email = contact_form.text_input("Your Email")
message = contact_form.text_area("Your Message")

if contact_form.form_submit_button("Send Message"):
    st.success("Thank you for reaching out! I'll get back to you soon.")
    # Here you could add functionality to send the message to an email or database if necessary

# Add a footer with additional links
st.markdown("---")
st.markdown("""
Created with ❤️ by Dr. Sara de la Salle
- [Research Lab Website](https://lab-website.com)
- [GitHub](https://github.com/username)
""")
