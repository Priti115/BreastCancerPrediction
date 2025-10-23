from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect all 30 feature values from the form
    features = [
        request.form['radius_mean'],
        request.form['texture_mean'],
        request.form['perimeter_mean'],
        request.form['area_mean'],
        request.form['smoothness_mean'],
        request.form['compactness_mean'],
        request.form['concavity_mean'],
        request.form['concave_points_mean'],
        request.form['symmetry_mean'],
        request.form['fractal_dimension_mean'],
        request.form['radius_se'],
        request.form['texture_se'],
        request.form['perimeter_se'],
        request.form['area_se'],
        request.form['smoothness_se'],
        request.form['compactness_se'],
        request.form['concavity_se'],
        request.form['concave_points_se'],
        request.form['symmetry_se'],
        request.form['fractal_dimension_se'],
        request.form['radius_worst'],
        request.form['texture_worst'],
        request.form['perimeter_worst'],
        request.form['area_worst'],
        request.form['smoothness_worst'],
        request.form['compactness_worst'],
        request.form['concavity_worst'],
        request.form['concave_points_worst'],
        request.form['symmetry_worst'],
        request.form['fractal_dimension_worst']
    ]
    
    # Convert to numpy array
    np_features = np.asarray(features, dtype=np.float32)
    
    # Make prediction
    pred = model.predict(np_features.reshape(1, -1))

    output = ["Cancer Detected" if pred[0] == 1 else "No Cancer Detected"]
    return render_template('index.html', message=output)

if __name__ == '__main__':
    app.run(debug=True)