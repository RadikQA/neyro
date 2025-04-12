from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TOGETHER_API_URL = "https://api.together.ai/v1/chat/completions"

@app.route("/api/message", methods=["POST"])
def message():
    data = request.get_json()
    user_message = data.get("message")
    mode = data.get("mode", "chat")  # по умолчанию обычный режим

    if mode == "reflect":
        system_prompt = (
            "Ты поддерживающий собеседник. "
            "Твоя задача — мягко переформулировать реплики пользователя так, "
            "чтобы они прозвучали с большей заботой, осознанностью и эмпатией. "
            "Говори с теплом и уважением. Если в сообщении есть тревога или резкость — смягчи. "
            "Вопросы задавай только если они помогают углубить диалог."
        )
    else:
        system_prompt = "Ты поддерживающий собеседник."

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(TOGETHER_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
