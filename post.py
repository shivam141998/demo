from flask import Flask,request

app=Flask(__name__)

@app.route('/login',methods=['POST'])

def login():
    uname=request.form['uname']
    password=request.form['pass']
    if uname=='shivam' and password=='ibm':
        return 'Welcome %s' %uname
    else:
        return "Wrong Credentials"
    
if __name__=='__main__':
    app.run(debug=False)