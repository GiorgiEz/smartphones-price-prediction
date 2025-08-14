import joblib
import pandas as pd


# Input: Galaxy S25 Ultra 512GB
actual_price = 1419
new_phone = {
    'brand_name': 'Samsung',
    'processor_brand': 'Qualcomm',
    'os': 'Android',
    'avg_rating': 8.0,
    '5G_or_not': 1,
    'num_cores': 8,
    'processor_speed': 4.47,
    'battery_capacity': 5000,
    'fast_charging': 45,
    'ram_capacity': 12,
    'internal_memory': 512,
    'screen_size': 6.9,
    'refresh_rate': 120,
    'num_rear_cameras': 4,
    'primary_camera_rear': 200,
    'primary_camera_front': 12,
    'extended_memory_available': 0,
    'resolution_height': 3120,
    'resolution_width': 1440
}

def predict():
    models = ["gradient_boosting_model", "random_forest_model"]

    for model_name in models:
        saved = joblib.load(f"../main/saved_models/{model_name}.pkl")
        model = saved["model"]
        encoding_maps = saved["maps"]
        encoding_type = saved.get("type", "frequency")

        df_new = pd.DataFrame([new_phone])

        if encoding_type == "frequency":
            for cat in encoding_maps:
                df_new[cat] = df_new[cat].map(encoding_maps[cat]).fillna(0)

        elif encoding_type == "one-hot":
            for cat, columns in encoding_maps.items():
                for col in columns:
                    category_value = col.split(f"{cat}_", 1)[1]
                    df_new[col] = (df_new[cat] == category_value).astype(int)
                df_new.drop(columns=[cat], inplace=True)

        df_new = df_new[saved["features"]]

        predicted_price = model.predict(df_new)[0]
        print(f"Model: {model_name}, Actual Price: {actual_price}, Predicted Price: {predicted_price}")



if __name__ == '__main__':
    predict()
