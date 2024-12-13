import google.generativeai as genai
import os
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
# ユーザーが "Hello" と言う。
# モデルが "Great to meet you. What would you like to know?" と応答する。
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)
response = chat.send_message("I have 2 dogs in my house.", stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)
response = chat.send_message("How many paws are in my house?", stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)

print(chat.history)
