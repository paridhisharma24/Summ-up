from flask import Flask, render_template, request, redirect
import json
from utils.summarizer import summarizer
# from utils.YoutubeTranscript import Generate_yt_transcript
from utils.ArticleTranscript import Generate_artc_transcript
# from utils.DataExtraction import 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Dashboard.html')


@app.route('/inp_summarization', methods=['POST', 'GET'])
def inp_summarization():
    text = request.form.get("input-text")
    summary = summarizer(text)
    return render_template("SummarizedDash.html", input=text, summary=summary)

# @app.route('/yt_link', methods=['POST', 'GET'])
# def yt_link():
#     youtube_link = request.form.get("myValue")
#     transcript = Generate_yt_transcript(youtube_link)
#     summary = summarizer(transcript)
#     return render_template("SummarizedDash.html",input=transcript,summary=summary)

@app.route('/article_link', methods=['POST', 'GET'])
def article_link():
    article_link=request.form.get("myValue")
    article = Generate_artc_transcript(article_link)
    summary = summarizer(article)
    return render_template("SummarizedDash.html",input=article,summary=summary)

# @app.route('/local_file', methods=['POST', 'GET'])
# def local_file():
#     file = request.files["myValue"]

#     return render_template("SummarizedDash.html")



if __name__ == '__main__':
    app.run(debug=True)