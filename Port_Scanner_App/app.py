import streamlit as st
from utils import scan  # port scanner function
from utils import set_bg_url  # to set the background image

st.set_page_config(
    page_title="Port Scanner",
    page_icon=":computer:",
    menu_items={
        "Get help": None,
        "Report a Bug": None,
        "About": None
    },
)

# Hide menu, footer, header
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Set URL background
set_bg_url("https://th.bing.com/th/id/R.5814d61be498a0eff3997214d11bb081?rik=4wuM50bSvOD4jw&pid=ImgRaw&r=0")

st.title("Port Scanner")

targets = st.text_input("Enter target IP(s), separated with commas")

ports = st.number_input(
    "How many ports do you want to scan?",
    min_value=1,
    max_value=65535,
    value=100,
    step=1
)

if st.button("Start Scan"):
    st.write("Scanning...")
    results = scan(targets, ports)

    for line in results:
        st.markdown(f'<div class="result-box">{line}</div>', unsafe_allow_html=True)

    st.title("Scan completed")
