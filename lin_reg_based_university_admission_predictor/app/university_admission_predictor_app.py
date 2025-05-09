from flask import Flask, request
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>University Admission Predictor App</h1>"

# reading the trained model's pickle file
lr_model = open("../artifacts/lr_model.pkl", "rb")

# loading the classifier
lr_model = pickle.load(lr_model)

@app.route("/predict", methods = ["POST"])
def predict():
    predict_request = request.get_json()

    gre_score = predict_request["gre_score"]
    toefl_score = predict_request["toefl_score"]
    university_rating = predict_request["university_rating"]
    sop = predict_request["sop"]
    lor = predict_request["lor"]
    cgpa = predict_request["cgpa"]
    research = predict_request["research"]

    # encoding
    if research == "Yes":
        research = 1
    else:
        research = 0

    # scaling the train data
    scaler = StandardScaler()
    training_data = pd.read_csv("../datasets/x_train.csv", header = 0)
    training_data.drop(columns = ["Unnamed: 0"], inplace = True)
    training_data_scaled = scaler.fit_transform(training_data)

    model_inputs = [[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]]

    # scaling the model_inputs
    model_inputs = scaler.transform(model_inputs)

    chance_of_admit = lr_model.predict(model_inputs)

    return {"chance_of_admit": chance_of_admit[0]}

if __name__ == "__main__":
    app.run(debug = True)
