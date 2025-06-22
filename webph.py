from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "f4273c804026a7b48f255fc4e182134b"  # Replace this!

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        number = request.form["number"]
        url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={number}"
        try:
            res = requests.get(url)
            data = res.json()
            if data.get("valid"):
                result = {
                    "valid": "Yes ✅",
                    "country": data.get("country_name"),
                    "location": data.get("location"),
                    "carrier": data.get("carrier"),
                    "line_type": data.get("line_type")
                }
            else:
                result = {"valid": "❌ Invalid number"}
        except:
            result = {"valid": "⚠️ Error fetching data"}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
