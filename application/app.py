import streamlit as st

from PIL import Image
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces
from streamlit_extras.switch_page_button import switch_page
from streamlit.components.v1 import html

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()




import base64

gif_fp = "C:/Users/mvams/OneDrive/Documents/VeriSure/application/assets/VerifyLabPro.gif"

try:
    with open(gif_fp, "rb") as gif_file:
        gif_data = gif_file.read()

    
    gif_base64 = base64.b64encode(gif_data).decode("utf-8")

    
    html_code = f"""
    <div style="display: flex; justify-content: center; align-items: center; height: auto; margin-top:-130px;">
        <img src="data:image/gif;base64,{gif_base64}" alt="Our Logo" style="width: 600px;">
    </div>
    """

    
    st.markdown(html_code, unsafe_allow_html=True)
except FileNotFoundError:
    st.error(f"File not found: {gif_fp}")







st.title("VeriFyIt")
st.write("")
st.subheader("Select Your Role")

col1, col2 = st.columns(2)
institite_logo = Image.open("../assets/MyIns.png")
with col1:
    st.image(institite_logo, output_format="png", width=230)
    clicked_institute = st.button("Institute")

company_logo = Image.open("../assets/VerifiersLog.jpg")
with col2:
    st.image(company_logo, output_format="jpg", width=230)
    clicked_verifier = st.button("Verifier")

if clicked_institute:
    st.session_state.profile = "Institute"
    switch_page('login')
elif clicked_verifier:
    st.session_state.profile = "Verifier"
    switch_page('login')
    
    
js_code = """
<script>
    async function connectMetaMask() {
        if (typeof window.ethereum !== 'undefined') {
            console.log('MetaMask is installed!');
            try {
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                const account = window.ethereum.selectedAddress;
                document.getElementById('wallet').textContent = "Connected: " + account;
            } catch (error) {
                console.error("Error connecting to MetaMask:", error);
                alert('Connection failed.');
            }
        } else {
            alert('MetaMask not installed!');
            document.getElementById('wallet').textContent = "MetaMask not installed";
        }
    }
</script>
<p id="wallet">Not connected</p>
<button onclick="connectMetaMask()">Connect MetaMask</button>
"""    
