from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = request.form['input_data']
    features_list = features.split(',')
    np_features = np.asarray(features_list, dtype=np.float32)
    pred = model.predict(np_features.reshape(1, -1))

    output = ["Cancer Detected" if pred[0] == 1 else "No Cancer Detected"]
    return render_template('index.html', message=output)
    

#python main
import os
if __name__ == '__main__':

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


