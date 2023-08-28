from flask import Flask,render_template,url_for
app = Flask(__name__)


print(__name__)
   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/work')
def work():
    return render_template('work.html')

# if __name__ == "__main__":
#     app.run(debug=True, host="127.0.0.1", port=5000)
   