from flask import Flask, render_template

app = Flask(__name__, template_folder="../app/templates", static_folder="../app/static")

@app.route("/")
def home():
    return render_template("index.html")

# required for vercel
def handler(request):
    return app