from google import genai
from flask import Flask, render_template, request

client = genai.Client(api_key="paste your key here")

app = Flask(__name__)

# maintain chat history
chat_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_message = request.form.get("message", "")
        
        # 1. Make the API call first to get the 'result'
        result = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are Chetanay AI.

You are Chetanay AI.

Rules:
- Answer in this exact format.
- Start with a relevant emoji.
- Use 2-5 relevant emojis naturally (🤖 🚀 📌 💡 ⚡ ✅ ❌ 📚).
- Keep answers under 100 words.
- Never use Markdown.
- Never use ###, **, or *.
- Never write long paragraphs.
- Use a short title.
- Then give 3-5 numbered points.
- Each point must be one short sentence.
- End with a one-line summary.

Example:

🐍 Python

1. 📖 Python is easy to learn.
2. 🤖 It is used for AI and machine learning.
3. 🌐 It builds websites and APIs.
4. ⚙️ It automates repetitive tasks.

💡 Summary:
Python is a beginner-friendly language used in many industries.

{user_message}
"""
        )
        
        # 2. Now extract the text from the result
        bot_reply = result.text
        
        # 3. Maintain chat history and update response
        chat_history.append({"user": user_message, "bot": bot_reply})
        response = bot_reply
        
    return render_template("index.html", response=response, chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)