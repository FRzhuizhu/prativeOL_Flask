from flask import Flask,render_template,flash,redirect,url_for

import json

app = Flask(__name__)
app.secret_key = 'frzhuizhu'

with open('sum.json','r',encoding='utf-8') as f:
    data = json.load(f)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route("/<int:id>")
def prative(id):
    item = data[id]
    html_data = {}
    html_data['qestion'] = str(id)+'、'+item['question']
    for i,opt in enumerate(item['options'] ):
        html_data['option'+chr(ord('A')+i)] = opt
    html_data['last'] = '/'+str(id-1)
    html_data['next'] = '/'+str(id+1)
    html_data['answer'] = '/'+str(id)+'/answer'
    print(html_data)
    return render_template('qestion.html',**html_data)

@app.route('/<int:id>/answer')
def answer(id):
    item = data[id]
    flash('正确答案：'+item['answer'])
    return redirect(url_for('prative',id = id))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)