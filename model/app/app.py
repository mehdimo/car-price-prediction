from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

from featurizer import Featurizer

# declare constants
HOST = '0.0.0.0'
PORT = 8081

# initialize flask application
app = Flask(__name__)
CORS(app)

def load_artifacts():
    model_gbr_path = "../model_objects/model_gbr.pkl"
    mileage_sclaer_path = "../model_objects/mileage_sclaer.pkl"
    all_columns_path = "../model_objects/all_columns.pkl"
    with open(model_gbr_path, 'rb') as f:
        gbr_model = pickle.load(f)

    with open(mileage_sclaer_path, 'rb') as f:
        mileage_scalar = pickle.load(f)

    with open(all_columns_path, 'rb') as f:
        all_cols = pickle.load(f)

    return gbr_model, mileage_scalar, all_cols

name_map = {
    "manufacturer": "Manufacturer",
    "model": "Model",
    "year": "Prod. year",
    "mileage": "Mileage",
    "engine": "Engine volume"
}
def rename_columns(input):
    renamed = {}
    for k in input:
        new_key = name_map[k]
        renamed[new_key] = input[k]
    return renamed

@app.route('/api/train', methods=['GET'])
def train():
    return "Not Implemented."

@app.route('/api/predict', methods=['POST'])
def predict():
    # get car object from request
    X = request.get_json()
    res = X
    X = rename_columns(X)
    model, mi_scaler, all_cols = load_artifacts()
    fz = Featurizer(mileage_scaler=mi_scaler, all_cols=all_cols)
    X = fz.get_features(X)
    df_test = pd.Series(X)
    X_test = df_test.values.reshape(1, -1)
    pred = model.predict(X_test)

    res["prediction"] = int(pred[0])
    return jsonify(res)

if __name__ == '__main__':
    # run web server
    app.run(host=HOST,
            debug=True,  # automatic reloading enabled
            port=PORT)
