from flask import Flask, jsonify, request, render_template, redirect, url_for, send_file
from datetime import datetime, timedelta
import threading
import time
import os


app = Flask(__name__)





@app.route('/')
def hello_world():
    # return render_template("homee.html")
    return "<h1>Hello Nikos</h1>"


@app.route("/test")
def hello():
    os.system("python3 headless.py")

    
    return "<h2>Done</h2>"





@app.route("/logout/", methods=['GET', "POST"])
def Login_to_WW():
    global sec

    if request.method == "GET":

        return render_template("logout.html")

    min = request.form['min']

    sec = float(min) * 60


    c_time = datetime.now()
    l_time = c_time + timedelta(minutes=int(min))
    l_time = datetime.strftime(l_time, "%H:%M")


    threading.Thread(target=thr).start()

    
    return f"<h4>{min} min left.</h4>" \
           f"<h2>You will logout at {l_time}.</h2>"


def thr():
    print("start")
    time.sleep(sec)
    print("done")
    # os.system("python3 log_out.py")




@app.route("/logintow/")
def Login_to_WwwW():

    return "<h1> Set time for the log-out</h1>"






@app.route("/images/", methods=['GET', "POST"])
def imag():
    
    return redirect(url_for('static', filename="test1.jpg"))





@app.route("/image/", methods=['GET', "POST"])
def imagg():
    # return redirect(url_for('static', filename="test1.jpg"))
    return send_file("C:\\Users\\ekouk\\PycharmProjects\\buget\\website\\static\\test1.jpg", as_attachment=True)





@app.route("/imageee/", methods=['GET', "POST"])
def imagsssg():
    image = url_for('static', filename='test1.jpg')
    # return redirect(url_for('static', filename="test1.jpg"))
    return render_template("imag.html", image=image)




@app.route('/download')
def download():
    path = "C:\\Users\\ekouk\\PycharmProjects\\buget\\website\\static\\test1.jpg"
    return send_file(path, as_attachment=True)






if __name__ == '__main__':
    app.run(host="0.0.0.0", port="2323", debug=True)









#
# if __name__ == '__main__':
#     app.run(host="192.168.1.189", port="8800", debug=True)