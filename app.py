from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html") 

@app.route("/ml/<ticker>")
def mlticker(ticker):
    return render_template(f"{ticker.upper()}.html") 

@app.route("/ml/images/<file_name>")
def images(file_name):
    return send_from_directory( "static/images/", file_name) 


if __name__ == "__main__":
    app.run(debug=True)