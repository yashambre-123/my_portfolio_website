from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__) # we use Flask class to instanciate the app . The name of app is __main__.

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def store_the_login_credentials(data):
    with open('database.csv',newline='',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer=csv.writer(database,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL)
        csv_writer.writerow([email,subject,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        data=request.form.to_dict()
        store_the_login_credentials(data)
        return redirect('/thankyou.html')
    else:
        return redirect('/made_a_error.html')

if __name__=='__main__':
    app.run(debug=True)
# 127.0.0.1 is the address of the laptop which we are working upon
# 5000 is the local host



