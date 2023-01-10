from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Minor.html')

# @app.route('/ProcessUserinfo/<string:userinfo>',methods=['POST'] )
# def ProcessUserinfo(userinfo):
#     userinfo=json.loads( userinfo)
#     username=userinfo
#     print()
#     print (username)
#     print()
#     return( '/' )
@app.route('/anything',methods=['POST', 'GET'])
def anything():
        text=request.form.get("myValue")
        return render_template("abc.html", text=text)
@app.route('/anything1',methods=['POST', 'GET'])
def anything1():
        text1=request.form.get("HEYHEY")
        return render_template("abc.html", text=text1)
if __name__ == '__main__':
    app.run(debug=True)