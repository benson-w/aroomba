# import the Flask class from the flask module
from flask import Flask, render_template, request
import numpy as np
import cv2
import take_pic

# create the application object
app = Flask(__name__)

# # use decorators to link the function to a url
# @app.route('/', methods=['POST', 'GET'])
# def home():
#     message = None
#     render_template('index.html')
#     if request.method == 'POST':
#         datafromjs = request.form['mydata']
#         result = "return this"
#         resp = make_response('{"response": '+result+'}')
#         resp.headers['Content-Type'] = "application/json"
#
#         take_pic()
#
#         return resp
#     execfile("take_pic.py")
#     execfile("search.py --index index.csv --query queries/snapshot.png --result-path dataset")
#     # return
#     #return "Hello, World!"  # return a string

@app.route('/', methods=['POST', 'GET'])
def home():
    cap = cv2.VideoCapture(1) # video capture source camera (Here webcam of laptop)
    ret,frame = cap.read() # return a single frame in variable `frame`
    cv2.imwrite('/Users/benson/Desktop/vacation-image-search-engine/queries/snapshot.png',frame)
    return render_template('index.html')

# Call take_pic()
@app.route('/takepic', methods=['POST', 'GET'])
def pythontakepicture():
    message = None
    if request.method == 'POST':
        return render_template('index.html', take_pic())
        # datafromjs = request.form['mydata']
        # result = "return this"
        # resp = make_response('{"response": '+result+'}')
        # resp.headers['Content-Type'] = "application/json"
        # #take_pic()
        # return "hi"

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
