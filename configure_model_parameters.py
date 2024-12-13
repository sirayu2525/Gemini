import google.generativeai as genai
import os
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set")
genai.configure(api_key=api_key)


model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
    "Tell me a story about a magic backpack.",
    generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1, #返される生成された回答の数を指定
        stop_sequences=["x"], #出力生成を停止する一連の文字列（最大 5 つ）を指定
        max_output_tokens=20, #候補に含めるトークンの最大数を設定
        temperature=1.0, #出力のランダム性を制御
    ),
)

print(response.text)
