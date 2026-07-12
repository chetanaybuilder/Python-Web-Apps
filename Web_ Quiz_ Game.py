from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "chetanay"

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        score = 0

        q1 = request.form["q1"]
        q2 = request.form["q2"]

        if q1 == "4":
            score += 1

        if q2.lower() == "india":
            score += 1
        return f"your score is {score}"
 
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

    



  

