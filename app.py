from flask import Flask, render_template, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        print("URL received:", url)
        domain = urlparse(url).netloc
        print("Domain extracted:", domain)

        
        trusted_domains = ["google.com", "facebook.com", "github.com", "openai.com"]

        if domain in trusted_domains:
            result = "✅ Legitimate URL"
        else:
            result = " Suspicious URL"

        print("Result generated:", result)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
