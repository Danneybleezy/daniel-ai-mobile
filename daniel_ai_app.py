import streamlit as st
from utils.chat import chat_tab
from utils.image_editor import image_editor_tab
from utils.image_gen import image_gen_tab
from utils.video import video_tab
from utils.voice import voice_tab
from utils.pdf import pdf_tab
from utils.music import music_tab
from utils.avatar import avatar_tab
from utils.search import search_tab
from utils.code_assistant import code_tab
from utils.settings import settings_tab

st.set_page_config(page_title="Daniel😎 AI", page_icon="🤖")

tabs = st.sidebar.radio("📚 Select a Feature", [
    "🧠 Chat",
    "🖼️ Enhance Image",
    "🎨 Generate Image",
    "🎬 Create Video",
    "🎤 Voice Assistant",
    "📄 PDF Summarizer",
    "🎵 Music Generator",
    "🧑‍🎨 Create Avatar",
    "🌐 Web Search",
    "💻 Code Assistant",
    "⚙️ Settings"
])

if tabs == "🧠 Chat":
    chat_tab()
elif tabs == "🖼️ Enhance Image":
    image_editor_tab()
elif tabs == "🎨 Generate Image":
    image_gen_tab()
elif tabs == "🎬 Create Video":
    video_tab()
elif tabs == "🎤 Voice Assistant":
    voice_tab()
elif tabs == "📄 PDF Summarizer":
    pdf_tab()
elif tabs == "🎵 Music Generator":
    music_tab()
elif tabs == "🧑‍🎨 Create Avatar":
    avatar_tab()
elif tabs == "🌐 Web Search":
    search_tab()
elif tabs == "💻 Code Assistant":
    code_tab()
elif tabs == "⚙️ Settings":
    settings_tab()
