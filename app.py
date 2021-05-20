from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sumbit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name_input = request.form['name_input']
        sex_input = request.form['sex_input']
        age_input =  request.form['age_input']
        bmi_input = request.form['bmi_input']
        children_input = request.form['children_input']
        smoker_input = request.form['smoker_input']
        user_insurance_cost = request.form['user_insurance_cost']
        
        
        
if __name__ == '__main__':
    app.run()

        
        




