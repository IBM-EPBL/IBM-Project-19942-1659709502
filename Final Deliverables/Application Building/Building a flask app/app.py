
from os import stat
from flask import Flask, render_template, request, url_for, redirect
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
mymodel = pickle.load(open("model.pkl", "rb"))  # load model
myscaler = pickle.load(open("scaler.pkl", "rb"))


@app.route('/')  # url binding
def loadhome():
    return render_template("homepage.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template("prediction.html")


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    return redirect(url_for('form'))


@app.route('/submit', methods=['POST'])  # url binding
def user():
    Education = request.form["Education"]
    ApplicantIncome = request.form["ApplicantIncome"]
    Coapplicant = request.form["Co-applicant"]
    LoanAmount = request.form["LoanAmount"]
    LoanAmountTerm = request.form["Loan-Amount-Term"]
    CreditHistory = request.form["Credit-History"]
    dependents = request.form["dependents"]
    property = request.form["property"]
    if Education == "Graduate":
        se = 0
    else:
        se = 1
    if dependents == "0":
        s1, s2, s3, s4 = 0, 0, 0, 1
    elif dependents == "1":
        s1, s2, s3, s4 = 0, 0, 1, 0
    elif dependents == "2":
        s1, s2, s3, s4 = 0, 1, 0, 0
    elif dependents == "3+":
        s1, s2, s3, s4 = 1, 0, 0, 0
    if property == "Rural":
        sp1, sp2, sp3 = 0, 0, 1
    elif property == "Semi-urban":
        sp1, sp2, sp3 = 0, 1, 0
    elif property == "Urban":
        sp1, sp2, sp3 = 1, 0, 0
    # Education, Applicant Income, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, dependents(4), property(3)

    arrayofinputs = [[float(se), float(ApplicantIncome), float(Coapplicant), float(
        LoanAmount), float(LoanAmountTerm), float(CreditHistory), float(s1), float(s2), float(s3), float(s4), float(sp1), float(sp2), float(sp3)]]
    print(myscaler.transform(arrayofinputs))
    y = mymodel.predict(myscaler.transform(arrayofinputs))
    if str(y[0]) == '1':
        status = 'approved'
    else:
        status = 'rejected'
    return render_template("result.html", output="The Loan status is "+status)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
