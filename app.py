import streamlit as st
import requests

# OpenRouter setup
MODEL = "deepseek/deepseek-r1-0528:free"
API_key = "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"

# Function to generate grammar lesson
def generate_response(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"
    messages = [
        {
            "role": "system",
            "content": """
You are an expert English teacher. Your job is to teach grammar in a **very simple and friendly way**...

📚 Always follow this structured format using Markdown:
# 📘 Topic Title
## 🔹 1. Simple Explanation
### 🔹 2. Example Sentences
### 🔹 3. Quick Q&A Practice
### 🔹 4. MCQ for Practice
### 🔹 5. Fun Tip or Reminder
Use emojis, spacing, and bold text to keep it friendly and clear.
"""
        },
        {
            "role": "user",
            "content": f"Teach this topic: {user_input}"
        }
    ]
    
    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {API_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/your-username/your-repo",  # Replace with your actual repo
            "X-Title": "English Grammar Chatbot"
        },
        json={
            "model": MODEL,
            "messages": messages,
            "temperature": 0.7,
            "stream": False
        }
    )
    
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Streamlit App
st.set_page_config(page_title="Grammar Bot", layout="centered")

st.title("📘 English Grammar Chatbot")
st.subheader("Learn English grammar with examples, questions, and tips!")

user_input = st.text_input("✏️ Type a grammar topic or question:")

if st.button("🧠 Get Help"):
    if user_input:
        result = generate_response(user_input)
        st.markdown(result)  # Enables bold text, emojis, and markdown
    else:
        st.warning("Please enter a topic or question.")
