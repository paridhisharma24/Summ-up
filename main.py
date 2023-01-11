from flask import Flask, render_template, request, redirect
import json
from summarizer import summarizer

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Dashboard.html')


@app.route('/inp_summarization', methods=['POST', 'GET'])
def inp_summarization():
        text = request.form.get("input-text")
        summary = summarizer(text)
        return render_template("SummarizedDash.html", input=text, summary=summary)


if __name__ == '__main__':
    app.run(debug=True)