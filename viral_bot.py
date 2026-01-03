import streamlit as st
import time
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Viral Post Generator", page_icon="🚀", layout="wide")

# --- HIDE STREAMLIT BRANDING ---
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stAppDeployButton {display: none;}
[data-testid="stToolbar"] {display: none !important;}
.viewerBadge_container__1QSob {display: none !important;}
div[class^='viewerBadge'] {display: none !important;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("Settings")
st.sidebar.info("The buy link is now on the main screen.")

# --- MAIN APP HEADER ---
# 👇 I CHANGED THE TITLE. IF THIS DOES NOT SHOW "V2", YOUR APP IS STUCK.
st.title("🚀 ViralBot V2 (Update Check)") 

# 👇 THIS LINK IS NOW IN THE CENTER OF THE PAGE
st.markdown("### 👉 [CLICK HERE TO DOWNLOAD SOURCE CODE ($9)](https://maqib395.gumroad.com/l/viralpostbot)")
st.info("👆 If you can see this blue box, the link is working.")

st.markdown("---")

# --- INPUT SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("Enter your topic (e.g. Copywriting, Python):")

with col2:
    category = st.selectbox(
        "Select Content Style:", 
        [
            "🔥 Contrarian", 
            "📚 Educational", 
            "📖 Storytelling", 
            "📢 Sales"
        ]
    )

# --- TEMPLATES ---
templates_contrarian = [
    "Stop doing {topic} the hard way.",
    "Unpopular Opinion: Most advice about {topic} is wrong.",
    "Why 99% of people fail at {topic}."
]

templates_educational = [
    "How to master {topic} in 30 days.",
    "7 Tools to 10x your {topic} workflow.",
    "The Ultimate Cheat Sheet for {topic}."
]

templates_story = [
    "I used to hate {topic}. Now it makes me $5k/month.",
    "3 years ago, I quit my job to focus on {topic}."
]

templates_sales = [
    "I have 3 spots left for my {topic} coaching program.",
    "Stop wasting time on {topic}. Let me handle it for you."
]

# --- GENERATION LOGIC ---
if st.button("Generate Content 🚀", type="primary"):
    if not topic:
        st.error("Please enter a topic first!")
    else:
        with st.spinner('Thinking...'):
            time.sleep(0.5)
        
        if "Contrarian" in category:
            selected = templates_contrarian
        elif "Educational" in category:
            selected = templates_educational
        elif "Storytelling" in category:
            selected = templates_story
        else:
            selected = templates_sales
            
        results_text = ""
        st.success("Here are your hooks:")
        
        for temp in selected:
            final_text = temp.format(topic=topic)
            st.code(final_text, language="text")
            results_text += final_text + "\n\n"
            
        st.download_button("📥 Download .txt", results_text, f"{topic}.txt")
