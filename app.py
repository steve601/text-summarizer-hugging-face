from flask import Flask,request,render_template
from transformers import pipeline

app = Flask(__name__)

def sumarize_text(article):
    classifier = pipeline("summarization")
    result = classifier(article,min_length=50,max_length=200,do_sample=False)
    return result[0]['summary_text']

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def do_prediction():
    a = request.form.get('user_text')
    msg = sumarize_text(a)
    
    return render_template('index.html',text=msg)

if __name__ == "__main__":
    app.run(debug=True)
    