from flask import Flask, request, render_template,jsonify
import pickle as pk
import numpy as np

# Flask constructor
application = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@application.route('/via_postman', methods=["POST"])
def request_by_postman():
    if request.method == "POST":
        # ting input with name = fname in HTML json
        presentprice = request.json["presentprice"]
        # ting input with name = lname in HTML json
        KmsDriven = float(request.json["KmsDriven"])
        Past_Owners = float(request.json["Past_Owners"])
        age = float(request.json["Age"])
        Transmission = request.json["Transmission"]
        SellerType = request.json["SellerType"]
        fueltype = request.json["fueltype"]
        filename = 'finalized_model.pk'
        loaded_model = pk.load(open(filename, 'rb'))
        if Transmission=="Manual":
            man=1;
            aut0=0;
        else:
            man=0;
            aut0=1;

        if SellerType == "Individual":
            indi=1
        else:
            indi=0

        if fueltype == "Petrol":
            petrol = 1
            diesel=0
        elif fueltype == "Disel":
            petrol=0
            diesel=1
        else :
            petrol=0
            diesel=0

        predictionresult = loaded_model.predict([[presentprice,KmsDriven,Past_Owners,age,diesel,petrol,indi,man]])

        result="selling price is " + str(np.round(predictionresult[0],decimals=2)) + "Lakhs"
        return jsonify(result)
    #return render_template("index.html")


if __name__ == '__main__':
    application.run(debug=True)