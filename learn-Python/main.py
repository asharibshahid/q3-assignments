# Growth Mindset Challege By Giaic 


import streamlit as st  

# Page Title  
st.title("🌱 Growth Mindset Challenge")  
st.subheader("Believe in Learning, Effort, and Persistence")  

# User Input
name = st.text_input("Enter your name:")

# Display Personalized Message
if name:
    st.success(f"Welcome, {name}! Start your growth journey today 🚀")

# Growth Mindset Tips  
st.markdown("""
### 🔥 Why Adopt a Growth Mindset?
✅ **Embrace Challenges** Learn from obstacles  
✅ **Learn from Mistakes** Failure is a step towards success  
✅ **Persist Through Difficulties** Keep going, even when it's hard  
✅ **Celebrate Effort** Focus on learning, not just results  
✅ **Stay Positive** Growth comes from continuous effort  
""")

# Feedback Section
st.text_area("Share your thoughts on growth mindset:")

# Submit Button
if st.button("Submit"):
    st.success("Thanks for sharing! Keep growing! 🌟")
