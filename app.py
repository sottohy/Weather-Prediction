import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import math

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0])
    return render_template('web.html', prediction_text="Tomorrow's temperature will be {}°F.".format(output))

if __name__ == '__main__':
    app.run()