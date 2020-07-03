from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
  def index():
    names=["Alice","bob","charlie"]
    return render_template("indexy.html",names=names)
