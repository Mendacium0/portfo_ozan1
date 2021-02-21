from flask import Flask, render_template, url_for, request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
# dinamik olarak diğer sekmeler ayarlandı.

# database e yazma
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email},{subject},{message}')
        # databse.txt yazmak için olan
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])





@app.route('/submit_form', methods=['POST', 'GET'])
# post = browser save info, get= browser sent info
def submit_form():
    if request.method == 'POST':
        # html sayfasında GFET ya da POST kullanmamıza göre
        try:
            data = request.form.to_dict()
            # tüm datayı dictionary olarak tutan method
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save the database :('
    else:
        return 'something went wrong. Try Again!'
