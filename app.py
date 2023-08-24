from flask import Flask,render_template
app = Flask(__name__)


print(__name__)
   

@app.route('/')
def Fun():
    return render_template('/static/html/index.html')

@app.route('/about')
def about():
    return 'Runner'


# if __name__ == "__main__":
#     app.run(debug=True, host="127.0.0.1", port=5000)
   