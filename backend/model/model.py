
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

data = pd.read_csv("../../data/sample_generated.csv")

X = data.drop("Salary", axis=1)
y = data["Salary"]

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(), ['Job Title', 'Location', 'Education'])
], remainder='passthrough')

pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])

pipeline.fit(X, y)
joblib.dump(pipeline, "salary_model.pkl")
