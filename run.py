import os
from flask import Flask, g, redirect, render_template, request, url_for
from src.seikei import reshape_text, to_url

app = Flask(__name__, instance_relative_config=True)


@app.route('/test')
def test():
    return '<h1>this is test page<h1>'


@app.route("/", methods=("GET", "POST"))
def text_shaping():
    if request.method == "POST":
        text = reshape_text(request.form["text"])
        ret_url = to_url(text)
        #文字列を改行で分割
        text_list=text.splitlines()
        return render_template("result.html",url=ret_url, text=text_list)
    return render_template("form.html")

#app.run(host='0.0.0.0', debug=True)
app.run(host='0.0.0.0')


