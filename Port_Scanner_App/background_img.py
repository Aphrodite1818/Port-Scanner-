import streamlit as st






def set_bg_url(url):
    css = f"""
    <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
        }}
        .result-box {{
            background: rgba(0,0,0,0.6);
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 8px;
            color: white;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)