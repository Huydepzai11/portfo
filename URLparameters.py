from flask import Flask,render_template,url_for, request,redirect
import csv
# render_template cho phep gui tep HTML
app=Flask(__name__)
print(__name__)

@app.route("/")
def my_home(): 
    return render_template('index.html')

@app.route("/<string:name_page>")
def component(name_page):
    return render_template(name_page)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer= csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



# @app.route("/index.html")
# def home(): 
#     return render_template('index.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/works.html")
# def work():
#     return render_template('works.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/components.html")
# def component():
#     return render_template('components.html')

# @app.route("/blog")
# def blog():
#     return "These are my thoughts on blogs"

# @app.route("/blog/2020/dogs")
# def blog2():
#     return "This is my dog"
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form(): 
    # return 'Form submitted'
    if request.method=='POST':
        data=request.form.to_dict()
        # print(data)

        # return 'formmm submitted'

        # write_to_file(data)
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong. Try again'
if __name__=="__main__":
    app.run() 