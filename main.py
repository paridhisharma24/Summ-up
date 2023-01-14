from flask import Flask, render_template, request,flash
import json
from utils.summarizer import summarizer
from utils.YoutubeTranscript import Generate_yt_transcript
from utils.ArticleTranscript import Generate_artc_transcript
from werkzeug.utils import secure_filename
import io
import PyPDF2
from docx import Document
import os


# from utils.DataExtraction import 
app = Flask(__name__)
app.secret_key = "abc"  

@app.route('/')
def index():
    return render_template('Dashboard.html')


@app.route('/inp_summarization', methods=['POST', 'GET'])
def inp_summarization():
    text = request.form.get("input-text")
    summary = summarizer(text)
    return render_template("SummarizedDash.html", input=text, summary=summary)


@app.route('/yt_link', methods=['POST', 'GET'])
def yt_link():
    youtube_link = request.form.get("link")
    transcript = Generate_yt_transcript(youtube_link)
    summary = summarizer(transcript)
    return render_template("SummarizedDash.html",input=transcript,summary=summary)


@app.route('/article_link', methods=['POST', 'GET'])
def article_link():
    article_link=request.form.get("link")
    article = Generate_artc_transcript(article_link)
    summary = summarizer(article)
    return render_template("SummarizedDash.html",input=article,summary=summary)


@app.route('/local_file', methods=['POST', 'GET'])
def local_file():
    file = request.files["link"]
    format = file.filename.split(".")[-1]
    if format == "txt":
        w = io.TextIOWrapper(file, encoding='utf-8')
        input = w.read()
        summary = summarizer(input)
        return render_template("SummarizedDash.html", input=input, summary=summary)
    elif format == "pdf":
        a = PyPDF2.PdfReader(file)
        #Getting The Number of Pages in PDF
        # pg_no = a.getNumPages()
        pg_no = len(a.pages)
        text = ""
        #Reading and Extracting The Data of PDF Page Wise
        for i in range(pg_no):
            text += a.pages[i].extract_text()
            # text += a.getPage(i).extractText()
        summary = summarizer(text)
        return render_template("SummarizedDash.html", input=text, summary=summary)

    elif format == "doc" or format=="docx":
        doc_obj = open(file,"rb")
        doc_reader = Document(doc_obj)
        data = ""
        for i in doc_reader.paragraphs:
            data += i.text+"\n"
        summary = summarizer(data)
        return render_template("SummarizedDash.html", input=data, summary=summary)

    else:
        flash("You Entered An Invalid File Type.")
        return render_template("Dashboard.html")



if __name__ == '__main__':
    app.run(debug=True) 