from flask import Flask, render_template

app = Flask("primeira_entrega")
@app.route("/")
def ola_mundo():
    return render_template("index.html"), 200
app.run()