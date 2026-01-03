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

# --- SIDEBAR (Branding & Info) ---
with st.sidebar:
    # Adding a Logo (using a free icon URL)
    st.image("https://cdn-icons-png.flaticon.com/512/2620/2620987.png", width=80)
    st.title("ViralBot Pro")
    st.caption("v3.1 - Ultimate Edition")
    st.markdown("---")
    https://gumroad.com/l/yourproduct
    # 👇 NEW BUY BUTTON ADDED HERE 👇
    st.link_button(
        label="⚡ Get Source Code ($9)", 
        url="[YOUR_GUMROAD_LINK_HERE]"  # <--- PASTE YOUR LINK HERE
    )
    st.caption("Launch your own SaaS in minutes.")
    st.markdown("---")
    # 👆 END OF NEW CODE 👆
    
    # "How to Use" Guide inside an Expander
    with st.expander("ℹ️ How to use this tool"):
        st.write("""
        1. **Enter Topic:** What are you writing about?
        2. **Select Style:** Choose a tone (e.g., Contrarian).
        3. **Generate:** Click the button.
        4. **Download:** Save your hooks instantly.
        """)
    
    st.info("💡 Tip: Try the 'Contrarian' style for max engagement.")

# --- MAIN APP HEADER ---
st.title("🚀 Viral Post Generator")
st.subheader("Generate market-proven hooks in seconds.")
st.markdown("---")

# --- INPUT SECTION (Using Columns for better layout) ---
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("Enter your topic (e.g. Copywriting, Python, Remote Work):")

with col2:
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
templates_contrarian = [
    "Stop doing {topic} the hard way. It is killing your progress.",
    "Unpopular Opinion: Most advice about {topic} is completely wrong.",
    "Why 99% of people fail at {topic} (and how to be the 1%).",
    "You don't need more resources for {topic}. You need more focus.",
    "The biggest lie you've been told about {topic} is...",
    "If you aren't using automation for {topic}, you are already behind."
]

templates_educational = [
    "How to master {topic} in 30 days (Step-by-Step Guide).",
    "7 Tools to 10x your {topic} workflow.",
    "The Ultimate Cheat Sheet for {topic} (Bookmark this).",
    "I spent 100 hours learning {topic}. Here is what I learned so you don't have to.",
    "10 mistakes to avoid when starting with {topic}.",
    "The simple framework I use to crush {topic} every single day."
]

templates_story = [
    "I used to hate {topic}. Now it makes me $5k/month.",
    "3 years ago, I quit my job to focus on {topic}. Here is what happened.",
    "The biggest mistake I made when I started learning {topic}.",
    "I almost gave up on {topic} in 2022. Here is why I didn't.",
    "How I went from zero to hero in {topic} (The honest truth)."
]

templates_social_proof = [
    "How I helped a client generate $10k using {topic}.",
    "We just crossed a major milestone in {topic}. Here is the breakdown.",
    "The exact strategy that got me 10,000 followers in the {topic} niche.",
    "I just saved 20 hours a week using this {topic} hack."
]

templates_engagement = [
    "What is your biggest struggle with {topic} right now?",
    "If you could only use one tool for {topic}, what would it be?",
    "Agree or Disagree: {topic} is the future of our industry.",
    "Drop your favorite resource for {topic} in the comments! 👇"
]

templates_sales = [
    "I have 3 spots left for my {topic} coaching program. DM me 'READY' to join.",
    "Stop wasting time on {topic}. Let me handle it for you.",
    "We are launching a new {topic} course next week. Join the waitlist.",
    "The ROI of {topic} is undeniable. Are you ready to invest in yourself?"
]

templates_motivation = [
    "{topic} is not about talent. It is about consistency.",
    "Don't let the fear of {topic} stop you from starting today.",
    "Your future self will thank you for mastering {topic}.",
    "The only bad workout is the one that didn't happen. Same goes for {topic}."
]

# --- GENERATION LOGIC ---
if st.button("Generate Content 🚀", type="primary"):
    if not topic:
        st.error("Please enter a topic first!")
    else:
        with st.spinner('Accessing the viral database...'):
            time.sleep(0.5)
        
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
            
        # 1. Create a list to hold the results text
        results_text = ""
        
        st.success("Analysis Complete. Here are your hooks:")
        st.markdown("---")
        
        # 2. Display Results Loop
        for temp in selected_templates:
            final_text = temp.format(topic=topic)
            st.code(final_text, language="text")
            # Add to our text list for downloading later
            results_text += final_text + "\n\n"
            
        # 3. THE DOWNLOAD BUTTON
        st.download_button(
            label="📥 Download Hooks as .txt",
            data=results_text,
            file_name=f"{topic}_hooks.txt",
            mime="text/plain"
        )

# --- FOOTER ---
st.markdown("---")
st.caption("Built by Aqib | v3.1 Pro")
