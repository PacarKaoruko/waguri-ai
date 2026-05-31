import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

from engine import WaguriBrain
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="Waguri AI", page_icon="🌸", layout="centered")

st.title("🌸 Waguri AI Assistant")
st.caption("Asisten Portofolio Interaktif oleh Haitamim Jahran Mahendra")
st.divider()

# Inisialisasi Engine
if "waguri_engine" not in st.session_state:
    st.session_state.waguri_engine = WaguriBrain(file_portofolio="portofolio.txt")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Saya Waguri. Ada yang ingin Anda ketahui tentang portofolio atau keahlian teknis Haitamim?"}
    ]

# Tampilkan history chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input Chat
if prompt := st.chat_input("Ketikkan pertanyaanmu di sini..."):
    
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Waguri sedang berpikir..."):
            # 1. Dapatkan jawaban teks utama
            jawaban = st.session_state.waguri_engine.jawab_pertanyaan(prompt)
            st.markdown(jawaban)
            
            # 2. Menu Tambahan (Copy & Suara) disembunyikan dalam menu lipat
            with st.expander("🛠️ Opsi: Salin Teks & Dengarkan Suara"):
                
                # Fitur Copy
                st.caption("📝 Salin Jawaban:")
                st.code(jawaban, language="markdown")
                
                # Fitur Suara (TIDAK AUTOPLAY)
                st.caption("🔊 Dengarkan Jawaban:")
                try:
                    tts = gTTS(text=jawaban, lang='id')
                    audio_bytes = BytesIO()
                    tts.write_to_fp(audio_bytes)
                    st.audio(audio_bytes, format='audio/mp3', autoplay=False)
                except Exception as e:
                    st.warning("Pita suara Waguri sedang gangguan.")

    st.session_state.messages.append({"role": "assistant", "content": jawaban})