import streamlit as st 
import pandas

st.set_page_config(layout='wide')

col1 ,col2 = st.columns(2)

with col1:
    st.image("photo.jpg")
    
with col2:
    st.title('Sai Krishna Durgam')
    content = """Hey, This is Sai Krishna Durgam, I'm presently pursuing my Bachelors in Ai&Ml.
I'm a passionate python Programmer.I have worked for small scale and medium firms and businesses in
our locality as a freelancer.
"""

    st.info(content)
st.subheader("Some of the apps that I made are:")

col3,empty_col,col4 = st.columns([1.5 , 1.0 , 1.5])
df = pandas.read_csv('data.csv',sep=';')
with col3:
    for index, items in df[:10].iterrows():
        st.header(items['title'])
        st.write(items['description'])
        st.image(items['image'])
        st.write(f"[Source code]({items['url']})")
    
with col4:
    for index, items in df[10:].iterrows():
        st.header(items['title'])
        st.write(items['description'])
        st.image(items['image'])
        st.write(f"[Source code]({items['url']})")
        
# Social media links
st.markdown(
    """
    <style>
    .social-media {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 50px;
    }
    .social-media a {
        margin: 0 30px;
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
                
