from flask import Flask,render_template
from Gesture_Controller import GestureController

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/home')
def home():
    gc1 = GestureController()
    gc1.start()


    




if __name__ == '__main__':
    app.run(debug=True)
