from flask import Flask, render_template

app = Flask(__name__)

# Initialize sample data for banks.html(replace with actual db tables data)
def init_banks_db():
    sample_banks = [
        {'Bank_Code': 101, 'Bank_Name': 'State Bank of India', 'Address': '123 Main Street, Connaught Place', 'City': 'New Delhi'},
        {'Bank_Code': 102, 'Bank_Name': 'HDFC Bank', 'Address': '456 Financial District, Bandra Kurla Complex', 'City': 'Mumbai'},
        {'Bank_Code': 103, 'Bank_Name': 'ICICI Bank', 'Address': '789 Electronic City', 'City': 'Bangalore'},
        {'Bank_Code': 104, 'Bank_Name': 'Axis Bank', 'Address': '321 Salt Lake', 'City': 'Kolkata'},
        {'Bank_Code': 105, 'Bank_Name': 'Punjab National Bank', 'Address': '654 MG Road', 'City': 'Chennai'},
        {'Bank_Code': 106, 'Bank_Name': 'Bank of Baroda', 'Address': '987 Cyber City', 'City': 'Gurugram'},
        {'Bank_Code': 107, 'Bank_Name': 'Canara Bank', 'Address': '753 Civil Lines', 'City': 'Jaipur'},
        {'Bank_Code': 108, 'Bank_Name': 'Union Bank of India', 'Address': '159 Boat Club Road', 'City': 'Pune'}
    ]
    return sample_banks

# Initialize sample data for employees.html (replace with actual db tables data)
def init_employee_db():
    sample_employees = [
        {'Emp_ID': 1001, 'Emp_Name': 'Rajesh Kumar', 'Mobile_No': '9876543210', 'Address': '42 Green Park, New Delhi', 'Bank_Code': 101},
        {'Emp_ID': 1002, 'Emp_Name': 'Priya Sharma', 'Mobile_No': '8765432109', 'Address': '15 Juhu Beach Road, Mumbai', 'Bank_Code': 102},
        {'Emp_ID': 1003, 'Emp_Name': 'Amit Patel', 'Mobile_No': '7654321098', 'Address': '78 MG Road, Bangalore', 'Bank_Code': 103},
        {'Emp_ID': 1004, 'Emp_Name': 'Neha Singh', 'Mobile_No': '6543210987', 'Address': '123 Park Street, Kolkata', 'Bank_Code': 104},
        {'Emp_ID': 1005, 'Emp_Name': 'Vikram Reddy', 'Mobile_No': '5432109876', 'Address': '56 Anna Salai, Chennai', 'Bank_Code': 105},
        {'Emp_ID': 1006, 'Emp_Name': 'Kavita Gupta', 'Mobile_No': '4321098765', 'Address': '89 Cyber Hub, Gurugram', 'Bank_Code': 106},
        {'Emp_ID': 1007, 'Emp_Name': 'Rahul Verma', 'Mobile_No': '3210987654', 'Address': '34 Civil Lines, Jaipur', 'Bank_Code': 107},
        {'Emp_ID': 1008, 'Emp_Name': 'Ananya Joshi', 'Mobile_No': '2109876543', 'Address': '67 FC Road, Pune', 'Bank_Code': 108}
    ]
    return sample_employees

@app.route('/')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/banks')
def banks():
    return render_template('banks.html', banks=init_db())

@app.route('/employees')
def employees():
    return render_template('employees.html', employees=init_employee_db())
if __name__ == '__main__':
    app.run(debug=True)