from flask import Flask, render_template, request

from flask import Flask, render_template, request
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
)

spam_keywords = [
    "win money",
    "free gift",
    "click here",
    "lottery",
    "congratulations",
    "claim prize",
    "urgent",
    "limited offer",
    "cash reward",
    "free"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/check', methods=['POST'])
def check():

    name = request.form['name']
    age = request.form['age']
    occupation = request.form['occupation']
    email_text = request.form['email']

    email_lower = email_text.lower()

    spam_score = 0

    for word in spam_keywords:
        if word in email_lower:
            spam_score += 1

    if spam_score >= 2:
        result = "🚨 SPAM EMAIL"
        color = "#ffb3c6"
    else:
        result = "✅ SAFE EMAIL"
        color = "#c7f9cc"

    return render_template(
        'result.html',
        name=name,
        age=age,
        occupation=occupation,
        email=email_text,
        result=result,
        color=color
    )

if __name__ == '__main__':
    app.run(debug=True)
    











