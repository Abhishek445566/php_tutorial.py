from flask import Flask

app=Flask(__name__)

@app.route("/")
  def tutorial():
    return f"<h1>hello</h1>"
