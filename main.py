from flask import Flask, render_template, request ,json

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('TwoPage.html')

@app.route('/result',methods = ['POST','GET'])
def result():
   if request.method == 'POST':
    json_input = request.form['input2']
    parsed = json.loads(json_input)
    result = json.dumps(parsed, indent=6)
   return render_template("TwoPage.html",result=result)

if __name__ == '__main__':
   app.run(debug = True)