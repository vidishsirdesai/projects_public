import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Loan Underwriter App</h1>"

# reading the trained model's pickle file
lgr_model = open("../artifacts/lgr_model.pkl", "rb")

# loading the classifier
classifier = pickle.load(lgr_model)

@app.route("/classify", methods = ["POST"])
def classify():
    classify_request = request.get_json()

    # upacking the json object
    loan_amnt = classify_request["loan_amnt"]
    term = classify_request["term"]
    int_rate = classify_request["int_rate"]
    annual_inc = classify_request["annual_inc"]
    dti = classify_request["dti"]
    open_acc = classify_request["open_acc"]
    pub_rec = classify_request["pub_rec"]
    revol_bal = classify_request["revol_bal"]
    revol_util = classify_request["revol_util"]
    total_acc = classify_request["total_acc"]
    initial_list_status = classify_request["initial_list_status"]
    mort_acc = classify_request["mort_acc"]
    pub_rec_bankrupticies = classify_request["pub_rec_bankrupticies"]
    grade = classify_request["grade"]
    home_ownership = classify_request["home_ownership"]
    verification_status = classify_request["verification_status"]
    purpose = classify_request["purpose"]
    application_type = classify_request["application_type"]
    zip_code = classify_request["zip_code"]

    # initializing categorical features that are encoded
    grade_B = 0
    grade_C = 0
    grade_D = 0
    grade_E = 0
    grade_F = 0
    grade_G = 0
    home_ownership_MORTGAGE = 0
    home_ownership_NONE = 0
    home_ownership_OTHER = 0
    home_ownership_OWN = 0
    home_ownership_RENT = 0
    verification_status_Source_Verified = 0
    verification_status_Verified = 0
    purpose_credit_card = 0
    purpose_debt_consolidation = 0
    purpose_educational = 0
    purpose_home_improvement = 0
    purpose_house = 0
    purpose_major_purchase = 0
    purpose_medical = 0
    purpose_moving = 0
    purpose_other = 0
    purpose_renewable_energy = 0
    purpose_small_business = 0
    purpose_vacation = 0
    purpose_wedding = 0
    application_type_INDIVIDUAL = 0
    application_type_JOINT = 0
    zip_code_05113 = 0
    zip_code_11650 = 0
    zip_code_22690 = 0
    zip_code_29597 = 0
    zip_code_30723 = 0
    zip_code_48052 = 0
    zip_code_70466 = 0
    zip_code_86630 = 0
    zip_code_93700 = 0

    # updating grade
    if grade == "B":
        grade_B = 1
    elif grade == "C":
        grade_C = 1
    elif grade == "D":
        grade_D = 1
    elif grade == "E":
        grade_E = 1
    elif grade == "F":
        grade_F = 1
    elif grade == "G":
        grade_G = 1

    # update home_ownership
    if home_ownership == "MORTGAGE":
        home_ownership_MORTGAGE = 1
    elif home_ownership == "NONE":
        home_ownership_NONE = 1
    elif home_ownership == "OTHER":
        home_ownership_OTHER = 1
    elif home_ownership == "OWN":
        home_ownership_OWN = 1
    elif home_ownership == "RENT":
        home_ownership_RENT = 1

    # update verification_status
    if verification_status == "Source Verified":
        verification_status_Source_Verified = 1
    elif verification_status == "Verified":
        verification_status_Verified = 1

    # update purpose
    if purpose == "credit_card":
        purpose_credit_card = 1
    elif purpose == "debt_consolidation":
        purpose_debt_consolidation = 1
    elif purpose == "educational":
        purpose_educational = 1
    elif purpose == "home_improvement":
        purpose_home_improvement = 1
    elif purpose == "house":
        purpose_house = 1
    elif purpose == "major_purchase":
        purpose_major_purchase = 1
    elif purpose == "medical":
        purpose_medical = 1
    elif purpose == "moving":
        purpose_moving = 1
    elif purpose == "other":
        purpose_other = 1
    elif purpose == "renewable_energy":
        purpose_renewable_energy = 1
    elif purpose == "small_business":
        purpose_small_business = 1
    elif purpose == "vacation":
        purpose_vacation = 1
    elif purpose == "wedding":
        purpose_wedding = 1
    
    # update application_type
    if application_type == "INDIVIDUAL":
        application_type_INDIVIDUAL = 1
    elif application_type == "JOINT":
        application_type_JOINT = 1

    # update zip_code
    if zip_code == "05113":
        zip_code_05113 = 1
    elif zip_code == "11650":
        zip_code_11650 = 1
    elif zip_code == "22690":
        zip_code_22690 = 1
    elif zip_code == "29597":
        zip_code_29597 = 1
    elif zip_code == "30723":
        zip_code_30723 = 1
    elif zip_code == "48052":
        zip_code_48052 = 1
    elif zip_code == "70466":
        zip_code_70466 = 1
    elif zip_code == "86630":
        zip_code_86630 = 1
    elif zip_code == "93700":
        zip_code_93700 = 1
    
    # scaling
    scaler = StandardScaler()
    training_data = pd.read_csv("../datasets/x_train.csv", header = 0)
    training_data.drop(columns = ["Unnamed: 0"], inplace = True)
    training_data_scaled = scaler.fit_transform(training_data)

    model_inputs = pd.DataFrame([[loan_amnt, term, int_rate, annual_inc, dti, open_acc, pub_rec, revol_bal, revol_util, total_acc, initial_list_status, mort_acc, pub_rec_bankrupticies, grade_B, grade_C, grade_D, grade_E, grade_F, grade_G, home_ownership_MORTGAGE, home_ownership_NONE, home_ownership_OTHER, home_ownership_OWN, home_ownership_RENT, verification_status_Source_Verified, verification_status_Verified, purpose_credit_card, purpose_debt_consolidation, purpose_educational, purpose_home_improvement, purpose_house, purpose_major_purchase, purpose_medical, purpose_moving, purpose_other, purpose_renewable_energy, purpose_small_business, purpose_vacation, purpose_wedding, application_type_INDIVIDUAL, application_type_JOINT, zip_code_05113, zip_code_11650, zip_code_22690, zip_code_29597, zip_code_30723, zip_code_48052, zip_code_70466, zip_code_86630, zip_code_93700]])

    # transforming the input data
    model_inputs = scaler.transform(model_inputs)

    # predict
    result = str(classifier.predict(model_inputs)[0])

    if result == "0":
        return {"Loan Status": "Not Approved"}
    else:
        return {"Loan Status": "Approved"}

if __name__ == "__main__":
    app.run(debug = True)
