# Breast Cancer Prediction Web App 🎗️

This is a **Flask-based Machine Learning Web App** that predicts whether a tumor is benign or malignant using key medical parameters from the breast cancer dataset. You can access the live app here:

👉 [Live App on Render](https://breastcancerprediction-o014.onrender.com/)

---

## 🔍 Objective
To build a web-based predictive model that classifies breast cancer tumors as either **malignant** (cancerous) or **benign** (non-cancerous) based on diagnostic features computed from digitized images of a breast mass.

---

## 📊 Dataset Description

We used the **Breast Cancer Wisconsin (Diagnostic) Data Set** from UCI Machine Learning Repository. The dataset contains **569 instances** and **30 real-valued input features**, along with a diagnosis label.

---

## 📑 Columns Description

| Feature Name             | Description |
|-------------------------|-------------|
| `id`                    | Unique identifier (not used in prediction) |
| `diagnosis`             | Target label: B (Benign) or M (Malignant) |
| `radius_mean`           | Mean of distances from center to points on the perimeter |
| `texture_mean`          | Standard deviation of gray-scale values |
| `perimeter_mean`        | Mean size of the perimeter |
| `area_mean`             | Mean area of the cell nuclei |
| `smoothness_mean`       | Mean of local variation in radius lengths |
| `compactness_mean`      | Mean of perimeter² / area - 1.0 |
| `concavity_mean`        | Mean of severity of concave portions of the contour |
| `concave points_mean`   | Mean number of concave portions of the contour |
| `symmetry_mean`         | Mean symmetry of the cell shape |
| `fractal_dimension_mean`| Mean of fractal dimension (coastline approximation) |
| `radius_se`             | Standard error of the radius |
| `texture_se`            | Standard error of texture |
| `perimeter_se`          | Standard error of perimeter |
| `area_se`               | Standard error of area |
| `smoothness_se`         | Standard error of smoothness |
| `compactness_se`        | Standard error of compactness |
| `concavity_se`          | Standard error of concavity |
| `concave points_se`     | Standard error of concave points |
| `symmetry_se`           | Standard error of symmetry |
| `fractal_dimension_se`  | Standard error of fractal dimension |
| `radius_worst`          | Worst (largest) radius |
| `texture_worst`         | Worst texture |
| `perimeter_worst`       | Worst perimeter |
| `area_worst`            | Worst area |
| `smoothness_worst`      | Worst smoothness |
| `compactness_worst`     | Worst compactness |
| `concavity_worst`       | Worst concavity |
| `concave points_worst`  | Worst concave points |
| `symmetry_worst`        | Worst symmetry |
| `fractal_dimension_worst`| Worst fractal dimension |

---

## 🧠 Machine Learning Model

- 🔍 **Logistic Regression** was used as the core classification algorithm.
- 📊 Preprocessing involved:
  - Handling missing values (if any)
  - Label encoding (`diagnosis`: B → 0, M → 1)
  - Feature scaling
- 🧪 Train-test split: 80/20
- ✅ Achieved **~97% accuracy** on the test set.

---

## 🚀 Deployment

- 🧩 **Flask** used for backend Python logic.
- 🎨 **HTML/CSS** for front-end interface.
- 🌍 Deployed on **Render.com** as a public web service.
- 🧪 Users can input medical data manually and get predictions in real time.

---

## 📝 Project Structure

