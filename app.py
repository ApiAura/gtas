import streamlit as st 
from gtts import gTTS
def text_to_speech(text, language='en'):
    tts =  gTTS (text=text, lang=language, slow=False)
    tts.save("output.mp3")
    st.audio("output.mp3")
# tampilan ui  
st.title("Delivere")
text = st.text_input("mau makan apa?")
language =st.selectbox("pls select your language",("en","id","fr","zh-CN","es"))
if st.button("play"):
    text_to_speech(text, language)
