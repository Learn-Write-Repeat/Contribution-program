from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('loan_model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        user_inputs = []
        values_list = ['gender', 'married', 'dependants', 'education', 'self',
                       'app_income', 'coapp_income', 'loan_amt', 'loan_term',
                       'credit', 'location']
        for value in values_list:
            user_inputs.append(int(request.form.get(value)))
        user_inputs = np.array(user_inputs)
        user_inputs = user_inputs.reshape(1, -1)
        output = model.predict(user_inputs)
    
    if output == 1:
        return render_template('home.html', output="You are eligible for the loan!!")
    elif output == 0:
        return render_template('home.html', output="Sorry, you are not eligible to get the loan.")


if __name__ == "__main__":
    app.run(debug=True)
