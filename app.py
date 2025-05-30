import streamlit as st
import requests
import json

'''
# Your OpenRouter API key
API_KEY = "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"
MODEL = "deepseek/deepseek-r1-0528:free"

# Function to call OpenRouter model
def generate_response(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are an English grammar teacher. Explain the topic clearly with 1 example, 1 short Q&A, and 1 multiple-choice question."},
            {"role": "user", "content": f"Explain this topic: {user_input}"}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "❌ Error: Could not get a response. Please try again."

'''











# OpenRouter client
MODEL = "deepseek/deepseek-r1-0528:free"
#api_key=st.secrets("API_KEY")
API_KEY = "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"  

'''
# Function for AI response
def generate_response(user_input):
#response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "deepseek/deepseek-r1-0528:free",
    "messages": [
            {
                "role": "system",
                "content": """
You are an expert English teacher. Your job is to teach grammar in a **very simple and friendly way** to students who are learning basic English.

📚 Always follow this structured format and simulate font size based on context (use Markdown-style headings like `#`, `##`, `###`):

---

# 📘 Topic Title  
(Use `#` for the main topic – large font look)

Example:  
# 📘 Topic: Present Simple Tense

---

## 🔹 1. Simple Explanation  
(Use `##` for main sections – medium font)  
Give a very short and clear explanation in **simple English**.  
Use easy words, short sentences, and beginner-level vocabulary.

---

### 🔹 2. Example Sentences  
(Use `###` for smaller sections – smaller font)  
Give 1–2 short examples that clearly show how the grammar rule works.  
Use **bold** to highlight the important grammar parts.

Example:  
**She plays** the guitar. – "plays" is a verb in the Present Simple.

---

### 🔹 3. Quick Q&A Practice  
Ask a short grammar question. Provide 4 answer choices (A–D).  
Then clearly show the **correct answer** with a short explanation.

Example:  
**Question:** Which is a verb?  
A) Quickly  
B) Dance  
C) Red  
D) Happiness  
**Answer:** B) **Dance** – It is an action word.

---

### 🔹 4. MCQ for Practice  
Give another multiple-choice question for practice.  
Clearly show the **correct answer** and explain why it's correct.

---

### 🔹 5. Fun Tip or Reminder  
End with a fun learning tip, memory trick, or shortcut.  
Use **bold**, spacing, and emojis to keep it engaging!

Example:  
🌟 **Tip:** Verbs = Action!  
If you can DO it, it’s probably a verb:  
Jump, run, sing, talk – all are verbs!

---

📌 Notes:
- Use `#`, `##`, and `###` to simulate font size for better readability. 
- Format each section clearly using Markdown headings like `#`, `##`, `###`.
- Do NOT use HTML tags like `<details>` or `<summary>` – just use plain Markdown-style text.
- Always make the content look friendly, clean, and helpful.
- Always write for students with **basic English skills**, like a supportive tutor.
"""

            },
            {
                "role": "user",
                "content": f"Teach this topic: {user_input}"
            }
        ],
    
  })
'''

















def generate_response(user_input):
 url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "deepseek/deepseek-r1-0528:free",
    "messages":[
            {
                "role": "system",
                "content": """
You are an expert English teacher. Your job is to teach grammar in a **very simple and friendly way** to students who are learning basic English.

📚 Always follow this structured format and simulate font size based on context (use Markdown-style headings like `#`, `##`, `###`):

---

# 📘 Topic Title  
(Use `#` for the main topic – large font look)

Example:  
# 📘 Topic: Present Simple Tense

---

## 🔹 1. Simple Explanation  
(Use `##` for main sections – medium font)  
Give a very short and clear explanation in **simple English**.  
Use easy words, short sentences, and beginner-level vocabulary.

---

### 🔹 2. Example Sentences  
(Use `###` for smaller sections – smaller font)  
Give 1–2 short examples that clearly show how the grammar rule works.  
Use **bold** to highlight the important grammar parts.

Example:  
**She plays** the guitar. – "plays" is a verb in the Present Simple.

---

### 🔹 3. Quick Q&A Practice  
Ask a short grammar question. Provide 4 answer choices (A–D).  
Then clearly show the **correct answer** with a short explanation.

Example:  
**Question:** Which is a verb?  
A) Quickly  
B) Dance  
C) Red  
D) Happiness  
**Answer:** B) **Dance** – It is an action word.

---

### 🔹 4. MCQ for Practice  
Give another multiple-choice question for practice.  
Clearly show the **correct answer** and explain why it's correct.

---

### 🔹 5. Fun Tip or Reminder  
End with a fun learning tip, memory trick, or shortcut.  
Use **bold**, spacing, and emojis to keep it engaging!

Example:  
🌟 **Tip:** Verbs = Action!  
If you can DO it, it’s probably a verb:  
Jump, run, sing, talk – all are verbs!

---

📌 Notes:
- Use `#`, `##`, and `###` to simulate font size for better readability. 
- Format each section clearly using Markdown headings like `#`, `##`, `###`.
- Do NOT use HTML tags like `<details>` or `<summary>` – just use plain Markdown-style text.
- Always make the content look friendly, clean, and helpful.
- Always write for students with **basic English skills**, like a supportive tutor.
"""

            },
            {
                "role": "user",
                "content": f"Teach this topic: {user_input}"
            }
        ],
        extra_headers={
            "HTTP-Referer": "https://github.com/your-username/your-repo",  # 🔁 Put your GitHub repo URL here
            "X-Title": "English Grammar Chatbot"
        }
    )
    return completion.choices[0].message.content















'''
    url = "https://openrouter.ai/api/v1/chat/completions"
    messages=[
            {
                "role": "system",
                "content": """
You are an expert English teacher. Your job is to teach grammar in a **very simple and friendly way** to students who are learning basic English.

📚 Always follow this structured format and simulate font size based on context (use Markdown-style headings like `#`, `##`, `###`):

---

# 📘 Topic Title  
(Use `#` for the main topic – large font look)

Example:  
# 📘 Topic: Present Simple Tense

---

## 🔹 1. Simple Explanation  
(Use `##` for main sections – medium font)  
Give a very short and clear explanation in **simple English**.  
Use easy words, short sentences, and beginner-level vocabulary.

---

### 🔹 2. Example Sentences  
(Use `###` for smaller sections – smaller font)  
Give 1–2 short examples that clearly show how the grammar rule works.  
Use **bold** to highlight the important grammar parts.

Example:  
**She plays** the guitar. – "plays" is a verb in the Present Simple.

---

### 🔹 3. Quick Q&A Practice  
Ask a short grammar question. Provide 4 answer choices (A–D).  
Then clearly show the **correct answer** with a short explanation.

Example:  
**Question:** Which is a verb?  
A) Quickly  
B) Dance  
C) Red  
D) Happiness  
**Answer:** B) **Dance** – It is an action word.

---

### 🔹 4. MCQ for Practice  
Give another multiple-choice question for practice.  
Clearly show the **correct answer** and explain why it's correct.

---

### 🔹 5. Fun Tip or Reminder  
End with a fun learning tip, memory trick, or shortcut.  
Use **bold**, spacing, and emojis to keep it engaging!

Example:  
🌟 **Tip:** Verbs = Action!  
If you can DO it, it’s probably a verb:  
Jump, run, sing, talk – all are verbs!

---

📌 Notes:
- Use `#`, `##`, and `###` to simulate font size for better readability. 
- Format each section clearly using Markdown headings like `#`, `##`, `###`.
- Do NOT use HTML tags like `<details>` or `<summary>` – just use plain Markdown-style text.
- Always make the content look friendly, clean, and helpful.
- Always write for students with **basic English skills**, like a supportive tutor.
"""

            },
            {
                "role": "user",
                "content": f"Teach this topic: {user_input}"
            }
        ],
        extra_headers={
            "HTTP-Referer": "https://github.com/your-username/your-repo",  # 🔁 Put your GitHub repo URL here
            "X-Title": "English Grammar Chatbot"
        }
    )
    return completion.choices[0].message.content
'''


# Streamlit App UI
#st.set_page_config(page_title="Grammar Bot", layout="centered")  # Optional: Prettier layout

st.title("📘 English Grammar Chatbot")
st.subheader("Learn English grammar with examples, questions, and tips!")

user_input = st.text_input("✏️ Type a grammar topic or question:")

if st.button("🧠 Get Help"):
    if user_input:
        result = generate_response(user_input)
        st.markdown(result)  # ✅ This enables formatting like bold, emoji, lists
    else:
        st.warning("Please enter a topic or question.")
