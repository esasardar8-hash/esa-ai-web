from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# ڕێکخستنی کلیلەکە
os.environ["GOOGLE_API_KEY"] = os.environ.get("GOOGLE_API_KEY", "")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# لێرەدا بە زۆر وەشانی v1 دیاری دەکەین بۆ ئەوەی کێشەی v1beta نەمێنێت
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash'
)

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")
        
        # ناردنی نامە بۆ مۆدێلەکە
        response = model.generate_content(user_message)
        
        return jsonify({"reply": response.text})
    except Exception as e:
        # ئەگەر هەڵەیەک هەبوو، لێرە پیشانی بدە
        return jsonify({"error": str(e)}), 500

app.debug = True
