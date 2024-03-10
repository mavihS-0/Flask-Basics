from flask import Flask,redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, QtCode'

@app.route('/pass/<int:score>')
def pass_(score):
    return 'Passed with score: %d' % score

#pass query parameters with url
@app.route('/query?score=<score>')
def query(score):
    return 'Passed with score: %d %d' % int(score) 

@app.route('/fail/<int:score>')
def fail(score):
    return 'Failed with score: %d' % score

@app.route('/result/<int:score>')
def result(score):
    if(score<40):
        return redirect(url_for('fail',score=score))
    else:
        return redirect(url_for('pass_',score=score))
    
if __name__=='__main__':
    app.run(debug=True)
