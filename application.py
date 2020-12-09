
# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

application = Flask(__name__) # initializing a flask app
# app=application
@application.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@application.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            crim= float(request.form['crim'])
            zn = float(request.form['zn'])
            indus = float(request.form['indus'])
            chas = float(request.form['chas'])
            nox = float(request.form['nox'])
            rm = float(request.form['rm'])
            age = float(request.form['age'])
            dis = float(request.form['dis'])
            rad = float(request.form['rad'])
            tax = float(request.form['tax'])
            ptratio = float(request.form['ptratio'])
            b = float(request.form['b'])
            lstat = float(request.form['lstat'])
            filename = 'finalized_assignment_model2.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	application.run(debug=True) # running the app