from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    name = "chetanay"
    age = 15
    dream = "europe"
    skills = [
        "python",
        "java",
        "c++"
    ]
    projects = True
    return render_template('index.html', name=name, age=age, dream=dream, skills=skills,projects=projects)
if __name__ == '__main__':
    app.run(debug=True)
    
