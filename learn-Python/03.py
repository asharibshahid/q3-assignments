import streamlit as st
import re

# Set page configuration
st.set_page_config(
    page_title="Password Security Checker",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        color: #4F8BF9;
        background-color: #F0F2F6;
    }
    .stButton>button {
        background-color: #4F8BF9;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background-color: #6fa8dc;
    }
    .stMarkdown {
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Description
st.title("🔒 Password Security Checker")
st.markdown("""
    Welcome to the **Password Security Checker**! 
    This tool helps you evaluate the strength of your password based on its length, complexity, and common patterns.
    """)

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        strength += 1
        feedback.append("✅ Password length is good (12+ characters).")
    else:
        feedback.append("❌ Password should be at least 12 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
        feedback.append("✅ Contains uppercase letters.")
    else:
        feedback.append("❌ Should contain at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
        feedback.append("✅ Contains lowercase letters.")
    else:
        feedback.append("❌ Should contain at least one lowercase letter.")

    # Digit check
    if re.search(r'[0-9]', password):
        strength += 1
        feedback.append("✅ Contains numbers.")
    else:
        feedback.append("❌ Should contain at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
        feedback.append("✅ Contains special characters.")
    else:
        feedback.append("❌ Should contain at least one special character.")

    # Common patterns check
    common_patterns = ['123', 'password', 'qwerty', 'admin']
    if not any(pattern in password.lower() for pattern in common_patterns):
        strength += 1
        feedback.append("✅ No common patterns detected.")
    else:
        feedback.append("❌ Avoid common patterns like '123', 'password', etc.")

    # Strength rating
    if strength == 5:
        return "💪 Excellent! Your password is very strong.", feedback
    elif strength >= 3:
        return "👍 Good! Your password is moderately strong.", feedback
    else:
        return "⚠️ Weak! Your password needs improvement.", feedback

# Streamlit UI
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password Strength"):
    if password:
        result, feedback = check_password_strength(password)
        st.subheader(result)
        for item in feedback:
            st.markdown(item)
    else:
        st.error("Please enter a password to check.")

# Footer
st.markdown("---")
st.markdown("""
    **Tips for a strong password:**
    - Use at least 12 characters.
    - Mix uppercase and lowercase letters.
    - Include numbers and special characters.
    - Avoid common words and patterns.
    """)