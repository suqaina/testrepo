import numpy as np
from flask import Flask, request, jsonify, render_template, redirect
from flask_bootstrap import Bootstrap
import pickle 


flask_app = Flask(__name__)
Bootstrap(flask_app)
file = open('model.pkl', 'rb')

# dump information to that file
data = pickle.load(file)
# model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["GET","POST"])
def predict():
    
    if request.method == "POST":
            float_features = [int(z) for z in request.form.values()]
            features = [np.array(float_features)]
            my_prediction = data.predict(features)
            return render_template("index.html", prediction = my_prediction)
    elif request.method == 'GET':
        return redirect('/')
    else:
        return 'Not a valid request method for this route'
                    


if __name__ == "__main__":
    flask_app.run(debug=True)