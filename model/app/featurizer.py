import pandas as pd

class Featurizer:
    def __init__(self, mileage_scaler, all_cols):
        self.mileage_scaler = mileage_scaler
        self.all_cols = all_cols

    def get_features(self, inp: dict) -> dict:
        df_test = pd.DataFrame([inp])
        df_test['Manufacturer'] = df_test['Manufacturer'].astype('category')
        df_test['Model'] = df_test['Model'].astype('category')
        df_test['Engine volume'] = df_test['Engine volume'].astype('category')
        X = df_test["Mileage"].values.reshape(-1, 1)
        scaledX = self.mileage_scaler.transform(X)
        df_test["Mileage"] = scaledX
        categorical_columns = ["Manufacturer", "Model", "Engine volume"]
        df_encoded = pd.get_dummies(df_test, columns=categorical_columns)
        record = df_encoded.to_dict(orient="records")[0]
        features = {}
        for col in self.all_cols:
            if col not in df_encoded.columns:
                features.update({col: 0})
            else:
                features.update({col: record[col]})

        return features
