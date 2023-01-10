from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Minor.html')

@app.route('/ProcessUserinfo/<string:userinfo>',methods=['POST'] )
def ProcessUserinfo(userinfo):
    userinfo=json.loads( userinfo)
    username=userinfo
    print()
    print (username)
    print()
    return( '/' )

if __name__ == '__main__':
    app.run(debug=True)