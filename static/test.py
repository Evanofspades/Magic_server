from flask import Flask, jsonify, request, render_template, redirect, url_for, send_file


app = Flask(__name__)





@app.route('/')
def hello_world():
    # return render_template("homee.html")
    return "<h1>Hello Nikos</h1>"





@app.route("/images/", methods=['GET', "POST"])
def imag():
    
    return redirect(url_for('static', filename="test1.jpg"))





@app.route("/image/", methods=['GET', "POST"])
def imagg():
    # return redirect(url_for('static', filename="test1.jpg"))
    return send_file("C:\\Users\ekouk\\PycharmProjects\\Magic_server\\static\\test1.jpg", as_attachment=True)





@app.route("/imageee/", methods=['GET', "POST"])
def imagsssg():
    image = url_for('static', filename='test1.jpg')
    # return redirect(url_for('static', filename="test1.jpg"))
    return render_template("imag.html", image=image)




# @app.route('/download')
# def download():
#     path = "C:\\Users\\ekouk\\PycharmProjects\\buget\\website\\static\\test.py"
#     return send_file(path, as_attachment=True)
#
#




if __name__ == '__main__':
    app.run(host="192.168.1.211", port="2525", debug=True)









#
# if __name__ == '__main__':
#     app.run(host="192.168.1.189", port="8800", debug=True)