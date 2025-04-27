from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'bank_management_secret_key'  # Required for flashing messages

# to calculate information being showed on the main dashboard page
def calculate_dashboard_stats():
    # Get data from all tables
    banks = init_banks_db()
    branches = init_branches_db()
    customers = init_customers_db()
    accounts = init_accounts_db()
    employees = init_employee_db()
    payments = init_payments_db()
    
    # Calculate stats
    stats = {
        'total_banks': len(banks),
        'total_branches': len(branches),
        'total_customers': len(customers),
        'total_accounts': len(accounts),
        'total_employees': len(employees),
        'total_transactions': sum(payment['Payment_Amount'] for payment in payments) / 10000000  # Convert to Crores
    }
    return stats

# Initialize sample data for banks.html (replace with actual db tables data)
def init_banks_db():
    # This would typically be replaced with database operations
    global banks_data
    return banks_data

# Storage for banks (simulating a database)
banks_data = [
    {'Bank_Code': 101, 'Bank_Name': 'State Bank of India', 'Address': '123 Main Street, Connaught Place', 'City': 'New Delhi'},
    {'Bank_Code': 102, 'Bank_Name': 'HDFC Bank', 'Address': '456 Financial District, Bandra Kurla Complex', 'City': 'Mumbai'},
    {'Bank_Code': 103, 'Bank_Name': 'ICICI Bank', 'Address': '789 Electronic City', 'City': 'Bangalore'},
    {'Bank_Code': 104, 'Bank_Name': 'Axis Bank', 'Address': '321 Salt Lake', 'City': 'Kolkata'},
    {'Bank_Code': 105, 'Bank_Name': 'Punjab National Bank', 'Address': '654 MG Road', 'City': 'Chennai'},
    {'Bank_Code': 106, 'Bank_Name': 'Bank of Baroda', 'Address': '987 Cyber City', 'City': 'Gurugram'},
    {'Bank_Code': 107, 'Bank_Name': 'Canara Bank', 'Address': '753 Civil Lines', 'City': 'Jaipur'},
    {'Bank_Code': 108, 'Bank_Name': 'Union Bank of India', 'Address': '159 Boat Club Road', 'City': 'Pune'}
]

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

# Initialize sample data for customers.html (replace with actual db tables data)
def init_customers_db():
    sample_customers = [
        {'Cust_ID': 2001, 'F_Name': 'Aditya', 'L_Name': 'Sharma', 'Mobile_No': '9988776655', 'E_Mail': 'aditya.sharma@email.com', 'Address': '78 Rajouri Garden, New Delhi'},
        {'Cust_ID': 2002, 'F_Name': 'Sneha', 'L_Name': 'Mehta', 'Mobile_No': '8877665544', 'E_Mail': 'sneha.mehta@email.com', 'Address': '23 Andheri West, Mumbai'},
        {'Cust_ID': 2003, 'F_Name': 'Karan', 'L_Name': 'Malhotra', 'Mobile_No': '7766554433', 'E_Mail': 'karan.m@email.com', 'Address': '45 Koramangala, Bangalore'},
        {'Cust_ID': 2004, 'F_Name': 'Meera', 'L_Name': 'Banerjee', 'Mobile_No': '6655443322', 'E_Mail': 'meera.b@email.com', 'Address': '12 Lake Town, Kolkata'},
        {'Cust_ID': 2005, 'F_Name': 'Rohan', 'L_Name': 'Desai', 'Mobile_No': '5544332211', 'E_Mail': 'rohan.d@email.com', 'Address': '34 T Nagar, Chennai'},
        {'Cust_ID': 2006, 'F_Name': 'Pooja', 'L_Name': 'Agarwal', 'Mobile_No': '4433221100', 'E_Mail': 'pooja.a@email.com', 'Address': '56 Sector 29, Gurugram'},
        {'Cust_ID': 2007, 'F_Name': 'Arjun', 'L_Name': 'Singh', 'Mobile_No': '3322110099', 'E_Mail': 'arjun.s@email.com', 'Address': '89 Malviya Nagar, Jaipur'},
        {'Cust_ID': 2008, 'F_Name': 'Nisha', 'L_Name': 'Patil', 'Mobile_No': '2211009988', 'E_Mail': 'nisha.p@email.com', 'Address': '32 Kothrud, Pune'}
    ]
    return sample_customers

# Initialize sample data for transactions.html (replace with actual db tables data)
def init_payments_db():
    sample_payments = [
        {'Payment_No': 5001, 'Payment_Date': '2025-04-15', 'Payment_Amount': 25000.00},
        {'Payment_No': 5002, 'Payment_Date': '2025-04-17', 'Payment_Amount': 13500.00},
        {'Payment_No': 5003, 'Payment_Date': '2025-04-18', 'Payment_Amount': 7800.50},
        {'Payment_No': 5004, 'Payment_Date': '2025-04-20', 'Payment_Amount': 32600.75},
        {'Payment_No': 5005, 'Payment_Date': '2025-04-22', 'Payment_Amount': 9450.25},
        {'Payment_No': 5006, 'Payment_Date': '2025-04-24', 'Payment_Amount': 15700.00},
        {'Payment_No': 5007, 'Payment_Date': '2025-04-25', 'Payment_Amount': 28350.50},
        {'Payment_No': 5008, 'Payment_Date': '2025-04-26', 'Payment_Amount': 4275.80}
    ]
    return sample_payments

# Initialize sample data for loans.html (replace with actual db tables data)
def init_loans_db():
    # Using customer IDs from the customers sample data for reference
    sample_loans = [
        {'Loan_No': 3001, 'Amount': 250000.00, 'Cust_ID': 2001, 'Customer_Name': 'Aditya Sharma'},
        {'Loan_No': 3002, 'Amount': 500000.00, 'Cust_ID': 2003, 'Customer_Name': 'Karan Malhotra'},
        {'Loan_No': 3003, 'Amount': 750000.00, 'Cust_ID': 2005, 'Customer_Name': 'Rohan Desai'},
        {'Loan_No': 3004, 'Amount': 100000.00, 'Cust_ID': 2007, 'Customer_Name': 'Arjun Singh'},
        {'Loan_No': 3005, 'Amount': 300000.00, 'Cust_ID': 2002, 'Customer_Name': 'Sneha Mehta'},
        {'Loan_No': 3006, 'Amount': 450000.00, 'Cust_ID': 2004, 'Customer_Name': 'Meera Banerjee'},
        {'Loan_No': 3007, 'Amount': 175000.00, 'Cust_ID': 2006, 'Customer_Name': 'Pooja Agarwal'},
        {'Loan_No': 3008, 'Amount': 125000.00, 'Cust_ID': 2008, 'Customer_Name': 'Nisha Patil'}
    ]
    return sample_loans

# Initialize sample data for accounts.html (replace with actual db tables data)
def init_accounts_db():
    sample_accounts = [
        {'Account_No': 5001, 'balance': 25000.50, 'Cust_ID': 2001},
        {'Account_No': 5002, 'balance': 78456.75, 'Cust_ID': 2002},
        {'Account_No': 5003, 'balance': 12500.00, 'Cust_ID': 2003},
        {'Account_No': 5004, 'balance': 456789.25, 'Cust_ID': 2004},
        {'Account_No': 5005, 'balance': 9870.45, 'Cust_ID': 2005},
        {'Account_No': 5006, 'balance': 34567.89, 'Cust_ID': 2006},
        {'Account_No': 5007, 'balance': 78956.23, 'Cust_ID': 2007},
        {'Account_No': 5008, 'balance': 123456.78, 'Cust_ID': 2008}
    ]
    return sample_accounts

# Initialize sample data for branches.html (replace with actual db tables data)
def init_branches_db():
    sample_branches = [
        {'Branch_Code': 201, 'Branch_Name': 'Main Branch - Delhi', 'Address': '123 Connaught Place, New Delhi', 'Bank_Code': 101},
        {'Branch_Code': 202, 'Branch_Name': 'Corporate Branch - Mumbai', 'Address': '456 Bandra Kurla Complex, Mumbai', 'Bank_Code': 102},
        {'Branch_Code': 203, 'Branch_Name': 'Tech Park Branch', 'Address': '789 Electronic City, Bangalore', 'Bank_Code': 103},
        {'Branch_Code': 204, 'Branch_Name': 'East Kolkata Branch', 'Address': '321 Salt Lake Sector V, Kolkata', 'Bank_Code': 104},
        {'Branch_Code': 205, 'Branch_Name': 'T Nagar Branch', 'Address': '654 Anna Salai, Chennai', 'Bank_Code': 105},
        {'Branch_Code': 206, 'Branch_Name': 'Cyber City Branch', 'Address': '987 DLF Phase 3, Gurugram', 'Bank_Code': 106},
        {'Branch_Code': 207, 'Branch_Name': 'Pink City Branch', 'Address': '753 MI Road, Jaipur', 'Bank_Code': 107},
        {'Branch_Code': 208, 'Branch_Name': 'Koregaon Park Branch', 'Address': '159 FC Road, Pune', 'Bank_Code': 108}
    ]
    return sample_branches

# Initialize sample data for account_types.html (replace with actual db tables data)
def init_account_types_db():
    sample_account_types = [
        {'Account_No': 5001, 'Type': 'Savings_Account'},
        {'Account_No': 5002, 'Type': 'Current_Account'},
        {'Account_No': 5003, 'Type': 'Savings_Account'},
        {'Account_No': 5004, 'Type': 'Current_Account'},
        {'Account_No': 5005, 'Type': 'Savings_Account'},
        {'Account_No': 5006, 'Type': 'Current_Account'},
        {'Account_No': 5007, 'Type': 'Savings_Account'},
        {'Account_No': 5008, 'Type': 'Current_Account'}
    ]
    return sample_account_types

## Initialize sample data for loan_payments.html (replace with actual db tables data)
def init_loan_payments_db():
    # Creating sample data that references the loans from init_loans_db()
    sample_loan_payments = [
        {'Loan_No': 3001, 'Payment_No': 1, 'Loan_Amount': 50000.00, 'Customer_Name': 'Aditya Sharma'},
        {'Loan_No': 3001, 'Payment_No': 2, 'Loan_Amount': 50000.00, 'Customer_Name': 'Aditya Sharma'},
        {'Loan_No': 3001, 'Payment_No': 3, 'Loan_Amount': 50000.00, 'Customer_Name': 'Aditya Sharma'},
        {'Loan_No': 3002, 'Payment_No': 1, 'Loan_Amount': 100000.00, 'Customer_Name': 'Karan Malhotra'},
        {'Loan_No': 3002, 'Payment_No': 2, 'Loan_Amount': 100000.00, 'Customer_Name': 'Karan Malhotra'},
        {'Loan_No': 3003, 'Payment_No': 1, 'Loan_Amount': 150000.00, 'Customer_Name': 'Rohan Desai'},
        {'Loan_No': 3004, 'Payment_No': 1, 'Loan_Amount': 33333.33, 'Customer_Name': 'Arjun Singh'},
        {'Loan_No': 3004, 'Payment_No': 2, 'Loan_Amount': 33333.33, 'Customer_Name': 'Arjun Singh'},
        {'Loan_No': 3004, 'Payment_No': 3, 'Loan_Amount': 33333.34, 'Customer_Name': 'Arjun Singh'},
        {'Loan_No': 3005, 'Payment_No': 1, 'Loan_Amount': 75000.00, 'Customer_Name': 'Sneha Mehta'},
        {'Loan_No': 3005, 'Payment_No': 2, 'Loan_Amount': 75000.00, 'Customer_Name': 'Sneha Mehta'},
        {'Loan_No': 3006, 'Payment_No': 1, 'Loan_Amount': 150000.00, 'Customer_Name': 'Meera Banerjee'},
        {'Loan_No': 3007, 'Payment_No': 1, 'Loan_Amount': 87500.00, 'Customer_Name': 'Pooja Agarwal'},
        {'Loan_No': 3008, 'Payment_No': 1, 'Loan_Amount': 62500.00, 'Customer_Name': 'Nisha Patil'},
        {'Loan_No': 3008, 'Payment_No': 2, 'Loan_Amount': 62500.00, 'Customer_Name': 'Nisha Patil'}
    ]
    return sample_loan_payments


@app.route('/')
@app.route('/dashboard')
def dashboard():
    stats = calculate_dashboard_stats()
    return render_template('dashboard.html', stats=stats)

@app.route('/banks')
def banks():
    return render_template('banks.html', banks=init_banks_db())

# route for adding a bank
@app.route('/add_bank', methods=['POST'])
def add_bank():
    global banks_data
    if request.method == 'POST':
        new_bank = {
            'Bank_Code': int(request.form['Bank_Code']),
            'Bank_Name': request.form['Bank_Name'],
            'Address': request.form['Address'],
            'City': request.form['City']
        }
        
        # checking if bank code already exists
        for bank in banks_data:
            if bank['Bank_Code'] == new_bank['Bank_Code']:
                flash('Bank code already exists', 'error')
                return redirect(url_for('banks'))
        
        # Add the new bank
        banks_data.append(new_bank)
        flash('Bank added successfully', 'success')
        return redirect(url_for('banks'))

# New route for updating a bank
@app.route('/update_bank', methods=['POST'])
def update_bank():
    global banks_data
    if request.method == 'POST':
        bank_code = int(request.form['Bank_Code'])
        bank_name = request.form['Bank_Name']
        address = request.form['Address']
        city = request.form['City']
        
        for bank in banks_data:
            if bank['Bank_Code'] == bank_code:
                bank['Bank_Name'] = bank_name
                bank['Address'] = address
                bank['City'] = city
                break
        
        flash('Bank updated successfully', 'success')
        return redirect(url_for('banks'))

# New route for deleting a bank
@app.route('/delete_bank', methods=['POST'])
def delete_bank():
    global banks_data
    if request.method == 'POST':
        bank_code = int(request.form['Bank_Code'])
        
        # Find the bank with the given code and remove it
        banks_data = [bank for bank in banks_data if bank['Bank_Code'] != bank_code]
        
        flash('Bank deleted successfully', 'success')
        return redirect(url_for('banks'))

@app.route('/branches')
def branches():
    return render_template('branches.html', branches=init_branches_db())

@app.route('/employees')
def employees():
    return render_template('employees.html', employees=init_employee_db())

@app.route('/customers')
def customers():
    return render_template('customers.html',customers=init_customers_db())

@app.route('/transactions')
def transactions():
    payments = init_payments_db()
    # Calculate summary metrics
    total_amount = sum(payment['Payment_Amount'] for payment in payments)
    latest_date = max(payment['Payment_Date'] for payment in payments)
    return render_template('transactions.html', payments=payments, total_amount=total_amount, latest_date=latest_date)

@app.route('/loans')
def loans():
    loans_data = init_loans_db()
    # Calculate summary metrics
    total_amount = sum(loan['Amount'] for loan in loans_data)
    avg_amount = round(total_amount / len(loans_data), 2) if loans_data else 0
    return render_template('loans.html', loans=loans_data, total_amount=total_amount, avg_amount=avg_amount)

@app.route('/accounts')
def accounts():
    return render_template('accounts.html', accounts=init_accounts_db())

@app.route('/account_types')
def account_types():
    account_types_data = init_account_types_db()
    
    # Calculate summary metrics
    savings_count = sum(1 for account in account_types_data if account['Type'] == 'Savings_Account')
    current_count = sum(1 for account in account_types_data if account['Type'] == 'Current_Account')
    
    return render_template('account_types.html', 
                           account_types=account_types_data,
                           savings_count=savings_count,
                           current_count=current_count)

@app.route('/loan_payments')
def loan_payments():
    loan_payments_data = init_loan_payments_db()
    
    # Calculate summary metrics
    unique_loans = set(payment['Loan_No'] for payment in loan_payments_data)
    unique_loans_count = len(unique_loans)
    
    # Calculate average payments per loan
    if unique_loans_count > 0:
        avg_payments_per_loan = round(len(loan_payments_data) / unique_loans_count, 2)
    else:
        avg_payments_per_loan = 0
    
    return render_template('loan_payments.html', 
                          loan_payments=loan_payments_data,
                          unique_loans_count=unique_loans_count,
                          avg_payments_per_loan=avg_payments_per_loan)


if __name__ == '__main__':
    app.run(debug=True)