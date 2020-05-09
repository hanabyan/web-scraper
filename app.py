from flask import Flask, render_template
import scraper

app = Flask(__name__)

@app.route('/')
def index():
    content = scraper.get_midtrans_payment_method()
    return render_template("base.html", data=content)

if __name__ == "__main__":
    app.run(debug=True)