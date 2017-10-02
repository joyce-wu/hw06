'''
Joyce Wu
SoftDev1 pd07
HW06 -- Echo Echo Echo
2017-10-02
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def intro(): #default page with login info
    return render_template("login.html")

@app.route("/result", methods=["POST"])
def ret():
    dic = request.form #saves immutable dictionary
    meth = request.method #saves method
    #returns all variables and puts it into the template
    return render_template("result.html", username=dic["username"], method=meth)

if __name__ == "__main__":
    app.debug = True
    app.run()
