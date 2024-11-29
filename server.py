from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/link')
def contact():
    return render_template('link.html')

@app.route('/kryptys')
def kryptys():
    return render_template('kryptys.html')

@app.route('/101')
def m101():
    return render_template('101.html')
@app.route('/101A')
def m101a():
    return render_template('101a.html')

@app.route('/110')
def m110():
    return render_template('110.html')
@app.route('/111')
def m111():
    return render_template('111.html')
@app.route('/117')
def m117():
    return render_template('117.html')
@app.route('/118')
def m118():
    return render_template('118.html')
@app.route('/122')
def m122():
    return render_template('122.html')
@app.route('/124')
def m124():
    return render_template('124.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)