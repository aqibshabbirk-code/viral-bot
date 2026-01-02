import streamlit as st
import time
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Viral Post Generator", page_icon="🚀", layout="centered")

# --- STYLE AND HEADERS ---
st.title("🚀 Viral Post Generator Ultimate")
st.write("The only content tool you need. Generate market-proven hooks instantly.")
st.markdown("---")

# --- INPUT SECTION ---
topic = st.text_input("Enter your topic (e.g. Copywriting, Python, Remote Work):")

# Expanded Market Categories
category = st.selectbox(
    "Select Content Style:", 
    [
        "🔥 Contrarian (Go Viral)", 
        "📚 Educational (Value Lists)", 
        "📖 Storytelling (Personal)", 
        "💰 Social Proof (Results)", 
        "🤝 Engagement (Ask Questions)", 
        "📢 Sales (Direct Offer)", 
        "🧠 Motivation (Mindset)"
    ]
)

# --- THE TEMPLATE VAULT ---

# 1. CONTRARIAN (Polarizing / High Viral Potential)
templates_contrarian = [
    "Stop doing {topic} the hard way. It is killing your progress.",
    "Unpopular Opinion: Most advice about {topic} is completely wrong.",
    "Why 99% of people fail at {topic} (and how to be the 1%).",
    "You don't need more resources for {topic}. You need more focus.",
    "The biggest lie you've been told about {topic} is...",
    "If you aren't using automation for {topic}, you are already behind.",
    "Stop listening to 'gurus' about {topic}. Watch what they DO, not what they SAY."
]

# 2. EDUCATIONAL (How-To / Listicles / Value)
templates_educational = [
    "How to master {topic} in 30 days (Step-by-Step Guide).",
    "7 Tools to 10x your {topic} workflow.",
    "The Ultimate Cheat Sheet for {topic} (Bookmark this).",
    "I spent 100 hours learning {topic}. Here is what I learned so you don't have to.",
    "10 mistakes to avoid when starting with {topic}.",
    "The simple framework I use to crush {topic} every single day.",
    "If you want to learn {topic}, read this thread."
]

# 3. STORYTELLING (Vulnerability / Journey)
templates_story = [
    "I used to hate {topic}. Now it makes me $5k/month.",
    "3 years ago, I quit my job to focus on {topic}. Here is what happened.",
    "The biggest mistake I made when I started learning {topic}.",
    "I almost gave up on {topic} in 2022. Here is why I didn't.",
    "How I went from zero to hero in {topic} (The honest truth).",
    "My journey with {topic} hasn't been easy. Here are the scars."
]

# 4. SOCIAL PROOF (Results / Case Studies)
templates_social_proof = [
    "How I helped a client generate $10k using {topic}.",
    "We just crossed a major milestone in {topic}. Here is the breakdown.",
    "The exact strategy that got me 10,000 followers in the {topic} niche.",
    "I just saved 20 hours a week using this {topic} hack.",
    "Numbers don't lie: {topic} is the fastest way to grow right now."
]

# 5. ENGAGEMENT (Questions / Community)
templates_engagement = [
    "What is your biggest struggle with {topic} right now?",
    "If you could only use one tool for {topic}, what would it be?",
    "Agree or Disagree: {topic} is the future of our industry.",
    "What is the best piece of advice you've ever received about {topic}?",
    "Drop your favorite resource for {topic} in the comments! 👇"
]

# 6. SALES (Direct Offers / Promo)
templates_sales = [
    "I have 3 spots left for my {topic} coaching program. DM me 'READY' to join.",
    "Stop wasting time on {topic}. Let me handle it for you.",
    "We are launching a new {topic} course next week. Join the waitlist.",
    "The ROI of {topic} is undeniable. Are you ready to invest in yourself?",
    "Want to fix your {topic} problems forever? Click the link in my bio."
]

# 7. MOTIVATION (Mindset / Inspiration)
templates_motivation = [
    "{topic} is not about talent. It is about consistency.",
    "Don't let the fear of {topic} stop you from starting today.",
    "Your future self will thank you for mastering {topic}.",
    "The only bad workout is the one that didn't happen. Same goes for {topic}.",
    "Success in {topic} is boring. It's doing the same thing every day for years."
]

# --- GENERATION LOGIC ---
if st.button("Generate Content 🚀"):
    if not topic:
        st.error("Please enter a topic first!")
    else:
        with st.spinner('Accessing the viral database...'):
            time.sleep(0.8) 
        
        st.success("Analysis Complete. Here are your hooks:")
        st.markdown("### 📝 Copy & Paste These Hooks:")
        
        # Mapping Logic
        if "Contrarian" in category:
            selected_templates = templates_contrarian
        elif "Educational" in category:
            selected_templates = templates_educational
        elif "Storytelling" in category:
            selected_templates = templates_story
        elif "Social Proof" in category:
            selected_templates = templates_social_proof
        elif "Engagement" in category:
            selected_templates = templates_engagement
        elif "Sales" in category:
            selected_templates = templates_sales
        else:
            selected_templates = templates_motivation
            
        # Display Results
        for temp in selected_templates:
            final_text = temp.format(topic=topic)
            st.code(final_text, language="text")
            
        st.info("💡 Pro Tip: Mix and match these styles to keep your audience engaged.")

# --- FOOTER ---
st.markdown("---")
st.caption("Built by Aqib | v2.0 Ultimate Edition")
