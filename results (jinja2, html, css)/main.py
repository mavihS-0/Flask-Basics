from flask import Flask,redirect, url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        english=float(request.form['english'])
        total=int((maths+science+english)/3)
        return redirect(url_for('result',score=total))


# @app.route('/result/<int:score>')
# def result(score):
#     if(score<40):
#         return render_template('fail.html',score1=score)
#     else:
#         return render_template('pass.html',score2=score)

@app.route('/result/<int:score>')
def result(score):
    d1={}
    if(score<40):
        d1['Score']= score
        d1['Result']='Fail'

    else:
        d1['Score']= score
        d1['Result']='Pass'
    
    return render_template('result.html',result=d1)
if __name__=='__main__':
    app.run(debug=True)