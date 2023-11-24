import streamlit as st 
from sendmail import send_mail
st.header("CONTACT ME")
with st.form(key="Contct"):
    email = st.text_input("Enter your email...")
    messege = st.text_area('Enter your messege....')
    button1 = st.form_submit_button()
# Social media links
st.markdown(
    """
    <style>
    .social-media {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 80px;
    }
    .social-media a {
        margin: 0 50px;
        text-decoration: none;
        color: #4a4a4a;
    }
    </style>
    """
    , unsafe_allow_html=True)
st.markdown(
    """
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    </head>
    """
    , unsafe_allow_html=True)

st.markdown(
    """
    <div class="social-media">
        <a href="https://www.twitter.com/krshxcx"><i class="fab fa-twitter"></i></a>
        <a href="https://github.com/krshxcx"><i class="fab fa-github"></i></a>
        <a href="https://www.instagram.com/krshxcx"><i class="fab fa-instagram"></i></a>
        <a href="https://www.linkedin.com/in/saikrishna-durgam/"><i class="fab fa-linkedin"></i></a>
    </div>
    """
    , unsafe_allow_html=True)


