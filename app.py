from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
@app.route('/', methods = ['GET','POST'])
def index():

    result=request.form.to_dict()
    #print(result)
    return render_template('landingpage.html')
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')