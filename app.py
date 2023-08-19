from flask import Flask
app = Flask(__name__)


print(__name__)
   

@app.route('/')
def Fun():
    return 'Hello world,m'

@app.route('/about')
def about():
    return 'Runner'


# if __name__ == "__main__":
#     app.run(debug=True, host="127.0.0.1", port=5000)
   