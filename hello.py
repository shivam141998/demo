from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Externship Program."

if __name__=='__main___':
    app.run(debug=True)
    
