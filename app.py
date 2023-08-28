from flask import Flask,render_template,url_for,redirect,request
import csv
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

@app.route('/submit_form', methods = ['GET','POST'])
def form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_data_csv(data)
            message = 'Form Submitted, We will get in touch to you shortly!!'
            return render_template('thankyou.html',message=message)
        except:
            message = "DID NOT SAVE DATA TO DATABASE."
            return render_template('thankyou.html',message=message)
    else:
        message = "FORM NOT SUBMITTED"
        return render_template('thankyou.html',message=message)
    
def write_data_csv(data):
    email = data['email']
    subject = data['subject']
    message = data["message"]
    with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])

# if __name__ == "__main__":
#     app.run(debug=True, host="127.0.0.1", port=5000)
   