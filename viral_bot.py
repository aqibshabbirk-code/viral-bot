import streamlit as st
import time
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Viral Post Generator", page_icon="⚡")

# --- STYLE AND HEADERS ---
st.title("⚡ Viral Post Generator")
st.write("Generate high-converting LinkedIn & Twitter posts in seconds.")
st.markdown("---")

# --- INPUT SECTION ---
topic = st.text_input("Enter your topic (e.g., Python, Marketing, Gym):")
niche = st.selectbox("Select Tone:", ["Aggressive", "Educational", "Storytelling"])

# --- VIRAL TEMPLATES (The "Engine") ---
templates_aggressive = [
    "Stop doing {topic} the hard way. It is killing your progress.",
    "Why 99% of people fail at {topic} (and how to be the 1%).",
    "Unpopular Opinion: Most advice about {topic} is completely wrong.",
    "If you aren't using automation for {topic}, you are already behind."
]

templates_educational = [
    "How to master {topic} in 30 days (Step-by-Step Guide).",
    "7 Tools to 10x your {topic} workflow.",
    "The Ultimate Cheat Sheet for {topic}.",
    "I spent 100 hours learning {topic}. Here is what I learned so you don't have to."
]

templates_story = [
    "I used to hate {topic}. Now it makes me $5k/month.",
    "How I went from zero to hero in {topic}.",
    "The biggest mistake I made when I started learning {topic}.",
    "3 years ago, I quit my job to focus on {topic}. Here is what happened."
]

# --- GENERATION LOGIC ---
if st.button("Generate Content 🚀"):
    if not topic:
        st.error("Please enter a topic first!")
    else:
        with st.spinner('Analyzing viral trends...'):
            time.sleep(1.5) # Fake loading to make it feel premium
        
        st.success("Analysis Complete. Here are your hooks:")
        st.markdown("### 📝 Copy & Paste These Hooks:")
        
        # Select templates based on Niche
        if niche == "Aggressive":
            selected_templates = templates_aggressive
        elif niche == "Educational":
            selected_templates = templates_educational
        else:
            selected_templates = templates_story
            
        # Display Results
        for temp in selected_templates:
            # We use .format to replace {topic} with the user's word
            final_text = temp.format(topic=topic)
            st.code(final_text, language="text")
            
        st.info("💡 Pro Tip: Use these as the first line of your post.")

# --- FOOTER ---
st.markdown("---")
st.caption("Built by Aqib | v1.0")