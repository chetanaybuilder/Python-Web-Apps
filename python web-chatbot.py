from flask import Flask, render_template, request
from google import genai

client = genai.Client(api_key="paste_your_key_here")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    response = ""

    if request.method == "POST":

        user_input = request.form["message"]

        result = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        response = result.text

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)







