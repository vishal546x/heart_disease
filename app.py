from flask import Flask , render_template,request
import pickle
import numpy as np

app=Flask(__name__)

with open ('heartt.pkl','rb') as file:
   model=pickle.load(file)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predi')
def prediction_page():
    return render_template("predi.html")

@app.route('/home')
def home_page():
    return render_template("index.html")
@app.route('/predict' ,methods=["POST"])
def predict():
   a1=request.form['ST_Slope']
   a2=request.form['ExerciseAngina']
   a3=request.form['ChestPainType']

   input_data=[[int(a1),int(a2),int(a3)]]

   #reshaped=np.array(input_data).reshape(1,-1)
   predict=model.predict(input_data)
   predict="Yes" if predict==1 else "NO"
   # return prediction
   return render_template("result.html",prediction=predict)


if __name__ == '__main__':
    app.run(debug=True)