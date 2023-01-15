from flask import Flask,request,url_for,redirect,render_template
from function import laon_data

app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    data=request.form

    Gender=float(data["Gender"])
    Married=float(data["Married"])
    Dependents=float(data["Dependents"])
    Education=float(data["Education"])
    Self_Employed=float(data["Self_Employed"])
    ApplicantIncome=float(data["ApplicantIncome"])
    CoapplicantIncome=float(data["CoapplicantIncome"])
    LoanAmount=float(data["LoanAmount"])
    Loan_Amount_Term=float(data["Loan_Amount_Term"])
    Credit_History=float(data["Credit_History"])
    Property_Area=data["Property_Area"]

    input_data=[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,Loan_Amount_Term,Credit_History,Property_Area]

    final_op=laon_data(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,Loan_Amount_Term,Credit_History,Property_Area).output()

    return render_template("index.html",result=final_op)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)