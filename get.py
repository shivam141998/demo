from flask import Flask,request

app=Flask(__name__)

@app.route('/login',methods=['GET'])

def login():
    uname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=='shivam' and password=='ibm':
        return 'Welcome %s' %uname
    else:
        return "Wrong Credentials"
    
if __name__=='__main__':
    app.run(debug=False)