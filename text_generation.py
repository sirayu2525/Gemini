import google.generativeai as genai
import os
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.", stream=True)
# デフォルトでは、モデルはテキスト生成プロセス全体が完了した後にレスポンスを返します。
# 結果全体を待たずに、ストリーミングを使用して部分的な結果を処理することで、インタラクションを高速化できます。
for chunk in response:
    print(chunk.text)
    print("_" * 80)