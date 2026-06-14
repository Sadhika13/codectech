from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# Sample Training Data
data = {
    "tenure_months": [2, 5, 12, 24, 36, 48, 60, 3, 8, 18],
    "monthly_charges": [100, 90, 80, 70, 60, 50, 40, 110, 95, 75],
    "support_tickets": [8, 7, 5, 3, 2, 1, 0, 9, 6, 4],
    "churn": [1, 1, 1, 0, 0, 0, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df[["tenure_months", "monthly_charges", "support_tickets"]]
y = df["churn"]

model = RandomForestClassifier()
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        tenure = float(request.form["tenure"])
        charges = float(request.form["charges"])
        tickets = int(request.form["tickets"])

        prediction = model.predict([[tenure, charges, tickets]])

        if prediction[0] == 1:
            result = "⚠️ Customer is likely to Churn"
        else:
            result = "✅ Customer is likely to Stay"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
    
    