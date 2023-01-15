import pickle,json
import numpy as np

class laon_data():
    def __init__(self,Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,Loan_Amount_Term,Credit_History,Property_Area):
        self.Gender=Gender
        self.Married=Married
        self.Dependents=Dependents
        self.Education=Education
        self.Self_Employed=Self_Employed
        self.ApplicantIncome=ApplicantIncome
        self.CoapplicantIncome=CoapplicantIncome
        self.Loan_Amount_Term=Loan_Amount_Term
        self.Credit_History=Credit_History
        self.Property_Area=Property_Area

    def model_import(self):
        with open("Model.pickle","rb")as f:
            self.model=pickle.load(f)

        with open("Std_scale.pickle","rb")as f:
            self.std=pickle.load(f)

        with open("Column.json","r")as f:
            self.column_names=json.load(f)

    def output(self):
        self.model_import()
        arr=np.zeros(len(self.column_names["columns"]))

        arr[0]=self.Gender
        arr[1]=self.Married
        arr[2]=self.Dependents
        arr[3]=self.Education
        arr[4]=self.Self_Employed
        arr[5]=self.ApplicantIncome
        arr[6]=self.CoapplicantIncome
        arr[7]=self.Loan_Amount_Term
        arr[8]=self.Credit_History

        arr_val="Property_Area_"+self.Property_Area
        arr_index=self.column_names["columns"].index(arr_val)
        arr[arr_index]=1

        trans_data=self.std.transform([arr])
        pred=self.model.predict(trans_data)
        return pred