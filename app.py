from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'bank_management_secret_key'  # Required for flashing messages

# Login required decorator for protecting routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_id' not in session:
            flash('Please log in to access this page', 'error')
            return redirect(url_for('index', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

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
        'total_transactions': sum(payment['Payment_Amount'] for payment in payments) / 100000  # Convert to Lakhs
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
    # This would typically be replaced with database operations
    global employees_data
    return employees_data

# Storage for employees (simulating a database)
employees_data = [
    {'Emp_ID': 1001, 'Emp_Name': 'Rajesh Kumar', 'Mobile_No': '9876543210', 'Address': '42 Green Park, New Delhi', 'Bank_Code': 101},
    {'Emp_ID': 1002, 'Emp_Name': 'Priya Sharma', 'Mobile_No': '8765432109', 'Address': '15 Juhu Beach Road, Mumbai', 'Bank_Code': 102},
    {'Emp_ID': 1003, 'Emp_Name': 'Amit Patel', 'Mobile_No': '7654321098', 'Address': '78 MG Road, Bangalore', 'Bank_Code': 103},
    {'Emp_ID': 1004, 'Emp_Name': 'Neha Singh', 'Mobile_No': '6543210987', 'Address': '123 Park Street, Kolkata', 'Bank_Code': 104},
    {'Emp_ID': 1005, 'Emp_Name': 'Vikram Reddy', 'Mobile_No': '5432109876', 'Address': '56 Anna Salai, Chennai', 'Bank_Code': 105},
    {'Emp_ID': 1006, 'Emp_Name': 'Kavita Gupta', 'Mobile_No': '4321098765', 'Address': '89 Cyber Hub, Gurugram', 'Bank_Code': 106},
    {'Emp_ID': 1007, 'Emp_Name': 'Rahul Verma', 'Mobile_No': '3210987654', 'Address': '34 Civil Lines, Jaipur', 'Bank_Code': 107},
    {'Emp_ID': 1008, 'Emp_Name': 'Ananya Joshi', 'Mobile_No': '2109876543', 'Address': '67 FC Road, Pune', 'Bank_Code': 108}
]

# Initialize sample data for customers.html (replace with actual db tables data)
def init_customers_db():
    # This would typically be replaced with database operations
    global customers_data
    return customers_data

# Define global variable for customers_data
customers_data = [
    {'Cust_ID': 2001, 'F_Name': 'Aditya', 'L_Name': 'Sharma', 'Mobile_No': '9988776655', 'E_Mail': 'aditya.sharma@email.com', 'Address': '78 Rajouri Garden, New Delhi'},
    {'Cust_ID': 2002, 'F_Name': 'Sneha', 'L_Name': 'Mehta', 'Mobile_No': '8877665544', 'E_Mail': 'sneha.mehta@email.com', 'Address': '23 Andheri West, Mumbai'},
    {'Cust_ID': 2003, 'F_Name': 'Karan', 'L_Name': 'Malhotra', 'Mobile_No': '7766554433', 'E_Mail': 'karan.m@email.com', 'Address': '45 Koramangala, Bangalore'},
    {'Cust_ID': 2004, 'F_Name': 'Meera', 'L_Name': 'Banerjee', 'Mobile_No': '6655443322', 'E_Mail': 'meera.b@email.com', 'Address': '12 Lake Town, Kolkata'},
    {'Cust_ID': 2005, 'F_Name': 'Rohan', 'L_Name': 'Desai', 'Mobile_No': '5544332211', 'E_Mail': 'rohan.d@email.com', 'Address': '34 T Nagar, Chennai'},
    {'Cust_ID': 2006, 'F_Name': 'Pooja', 'L_Name': 'Agarwal', 'Mobile_No': '4433221100', 'E_Mail': 'pooja.a@email.com', 'Address': '56 Sector 29, Gurugram'},
    {'Cust_ID': 2007, 'F_Name': 'Arjun', 'L_Name': 'Singh', 'Mobile_No': '3322110099', 'E_Mail': 'arjun.s@email.com', 'Address': '89 Malviya Nagar, Jaipur'},
    {'Cust_ID': 2008, 'F_Name': 'Nisha', 'L_Name': 'Patil', 'Mobile_No': '2211009988', 'E_Mail': 'nisha.p@email.com', 'Address': '32 Kothrud, Pune'}
]

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
    global loans_data
    return loans_data

loans_data = [
        {'Loan_No': 3001, 'Amount': 250000.00, 'Cust_ID': 2001, 'Customer_Name': 'Aditya Sharma'},
        {'Loan_No': 3002, 'Amount': 500000.00, 'Cust_ID': 2003, 'Customer_Name': 'Karan Malhotra'},
        {'Loan_No': 3003, 'Amount': 750000.00, 'Cust_ID': 2005, 'Customer_Name': 'Rohan Desai'},
        {'Loan_No': 3004, 'Amount': 100000.00, 'Cust_ID': 2007, 'Customer_Name': 'Arjun Singh'},
        {'Loan_No': 3005, 'Amount': 300000.00, 'Cust_ID': 2002, 'Customer_Name': 'Sneha Mehta'},
        {'Loan_No': 3006, 'Amount': 450000.00, 'Cust_ID': 2004, 'Customer_Name': 'Meera Banerjee'},
        {'Loan_No': 3007, 'Amount': 175000.00, 'Cust_ID': 2006, 'Customer_Name': 'Pooja Agarwal'},
        {'Loan_No': 3008, 'Amount': 125000.00, 'Cust_ID': 2008, 'Customer_Name': 'Nisha Patil'}
    ]


# Initialize sample data for accounts.html (replace with actual db tables data)
def init_accounts_db():
    # This would typically be replaced with database operations
    global accounts_data
    return accounts_data

accounts_data = [
        {'Account_No': 5001, 'balance': 25000.50, 'Cust_ID': 2001},
        {'Account_No': 5002, 'balance': 78456.75, 'Cust_ID': 2002},
        {'Account_No': 5003, 'balance': 12500.00, 'Cust_ID': 2003},
        {'Account_No': 5004, 'balance': 456789.25, 'Cust_ID': 2004},
        {'Account_No': 5005, 'balance': 9870.45, 'Cust_ID': 2005},
        {'Account_No': 5006, 'balance': 34567.89, 'Cust_ID': 2006},
        {'Account_No': 5007, 'balance': 78956.23, 'Cust_ID': 2007},
        {'Account_No': 5008, 'balance': 123456.78, 'Cust_ID': 2008}
    ]
    

# Initialize sample data for branches.html (replace with actual db tables data)
def init_branches_db():
    # This would typically be replaced with database operations
    global branches_data
    return branches_data

# Storage for branches (simulating a database)
branches_data = [
    {'Branch_Code': 201, 'Branch_Name': 'Main Branch - Delhi', 'Address': '123 Connaught Place, New Delhi', 'Bank_Code': 101},
    {'Branch_Code': 202, 'Branch_Name': 'Corporate Branch - Mumbai', 'Address': '456 Bandra Kurla Complex, Mumbai', 'Bank_Code': 102},
    {'Branch_Code': 203, 'Branch_Name': 'Tech Park Branch', 'Address': '789 Electronic City, Bangalore', 'Bank_Code': 103},
    {'Branch_Code': 204, 'Branch_Name': 'East Kolkata Branch', 'Address': '321 Salt Lake Sector V, Kolkata', 'Bank_Code': 104},
    {'Branch_Code': 205, 'Branch_Name': 'T Nagar Branch', 'Address': '654 Anna Salai, Chennai', 'Bank_Code': 105},
    {'Branch_Code': 206, 'Branch_Name': 'Cyber City Branch', 'Address': '987 DLF Phase 3, Gurugram', 'Bank_Code': 106},
    {'Branch_Code': 207, 'Branch_Name': 'Pink City Branch', 'Address': '753 MI Road, Jaipur', 'Bank_Code': 107},
    {'Branch_Code': 208, 'Branch_Name': 'Koregaon Park Branch', 'Address': '159 FC Road, Pune', 'Bank_Code': 108}
]

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
def index():
    return render_template('index.html')

@app.route('/admin_login', methods=['POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Your database connection and query here
        # Example:
        # connection = db_connection()
        # cursor = connection.cursor()
        # cursor.execute("SELECT admin_id, username, password FROM admins WHERE username = %s", (username,))
        # admin = cursor.fetchone()
        
        # For demonstration purposes (replace with actual DB check)
        # In reality, you would never store plaintext passwords
        # You should use password hashing (e.g., bcrypt)
        admin = None
        if username == "admin" and password == "password":  # Replace with actual DB check
            admin = {"admin_id": 1, "username": "admin"}
        
        if admin:
            # Store admin info in session
            session['admin_id'] = admin['admin_id']
            session['username'] = admin['username']
            return redirect(url_for('dashboard'))
        else:
            # Return to index with error
            return render_template('index.html', error="Invalid username or password")
    
    return redirect(url_for('index'))

@app.route('/admin_signup', methods=['POST'])
def admin_signup():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        
        # Check if username already exists
        # connection = db_connection()
        # cursor = connection.cursor()
        # cursor.execute("SELECT username FROM admins WHERE username = %s", (username,))
        # existing_admin = cursor.fetchone()
        
        # For demonstration (replace with actual DB check)
        existing_admin = None  # Check if username exists in your DB
        
        if existing_admin:
            return render_template('index.html', signup_error="Username already exists")
        
        # Insert new admin into database
        # In production, hash the password before storing
        # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # cursor.execute(
        #     "INSERT INTO admins (username, name, email, phone, password) VALUES (%s, %s, %s, %s, %s)",
        #     (username, name, email, phone, hashed_password)
        # )
        # connection.commit()
        # admin_id = cursor.lastrowid
        
        # For demonstration
        admin_id = 2  # This would be the new admin's ID from your DB
        
        # Log the user in after signup
        session['admin_id'] = admin_id
        session['username'] = username
        
        return redirect(url_for('dashboard'))
    
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Clear session
    session.pop('admin_id', None)
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    stats = calculate_dashboard_stats()
    return render_template('dashboard.html', stats=stats)

@app.route('/banks')
def banks():
    banks_data = init_banks_db()
    
    # Get search query and sort parameter from request
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', '')
    
    # Filter banks based on search query across all columns
    filtered_banks = banks_data
    if search_query:
        filtered_banks = [bank for bank in banks_data if any(
            str(value).lower().find(search_query.lower()) != -1 
            for key, value in bank.items()
        )]
    
    # Sort banks based on sort parameter
    if sort_by in ['Bank_Code', 'Bank_Name', 'Address', 'City']:
        filtered_banks = sorted(filtered_banks, key=lambda x: str(x[sort_by]))
    
    return render_template('banks.html', banks=filtered_banks, search_query=search_query, sort_by=sort_by)

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
    # Get the branches data
    branches_data = init_branches_db()
    
    # Get search query and sort parameter from request
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', '')
    
    # Filter branches based on search query across all columns
    filtered_branches = branches_data
    if search_query:
        filtered_branches = [branch for branch in branches_data if any(
            str(value).lower().find(search_query.lower()) != -1 
            for key, value in branch.items()
        )]
    
    # Sort branches based on sort parameter
    if sort_by in ['Branch_Code', 'Branch_Name', 'Address', 'Bank_Code']:
        filtered_branches = sorted(filtered_branches, key=lambda x: str(x[sort_by]))
    
    return render_template('branches.html', branches=filtered_branches, search_query=search_query, sort_by=sort_by)

# Route for adding a branch
@app.route('/add_branch', methods=['POST'])
def add_branch():
    global branches_data
    if request.method == 'POST':
        new_branch = {
            'Branch_Code': int(request.form['Branch_Code']),
            'Branch_Name': request.form['Branch_Name'],
            'Address': request.form['Address'],
            'Bank_Code': int(request.form['Bank_Code'])
        }
        
        # Check if branch code already exists
        for branch in branches_data:
            if branch['Branch_Code'] == new_branch['Branch_Code']:
                flash('Branch code already exists', 'error')
                return redirect(url_for('branches'))
        
        # Add the new branch
        branches_data.append(new_branch)
        flash('Branch added successfully', 'success')
        return redirect(url_for('branches'))

# Route for updating a branch
@app.route('/update_branch', methods=['POST'])
def update_branch():
    global branches_data
    if request.method == 'POST':
        branch_code = int(request.form['Branch_Code'])
        branch_name = request.form['Branch_Name']
        address = request.form['Address']
        bank_code = int(request.form['Bank_Code'])
        
        for branch in branches_data:
            if branch['Branch_Code'] == branch_code:
                branch['Branch_Name'] = branch_name
                branch['Address'] = address
                branch['Bank_Code'] = bank_code
                break
        
        flash('Branch updated successfully', 'success')
        return redirect(url_for('branches'))

# Route for deleting a branch
@app.route('/delete_branch', methods=['POST'])
def delete_branch():
    global branches_data
    if request.method == 'POST':
        branch_code = int(request.form['Branch_Code'])
        
        # Find the branch with the given code and remove it
        branches_data = [branch for branch in branches_data if branch['Branch_Code'] != branch_code]
        
        flash('Branch deleted successfully', 'success')
        return redirect(url_for('branches'))

@app.route('/employees')
def employees():
    # Get the employees data
    employees_data = init_employee_db()
    
    # Get search query and sort parameter from request
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', '')
    
    # Filter employees based on search query across all columns
    filtered_employees = employees_data
    if search_query:
        filtered_employees = [employee for employee in employees_data if any(
            str(value).lower().find(search_query.lower()) != -1 
            for key, value in employee.items()
        )]
    
    # Sort employees based on sort parameter
    if sort_by in ['Emp_ID', 'Emp_Name', 'Mobile_No', 'Address', 'Bank_Code']:
        filtered_employees = sorted(filtered_employees, key=lambda x: str(x[sort_by]))
    
    return render_template('employees.html', employees=filtered_employees, search_query=search_query, sort_by=sort_by)

# Route for adding an employee
@app.route('/add_employee', methods=['POST'])
def add_employee():
    global employees_data
    if request.method == 'POST':
        new_employee = {
            'Emp_ID': int(request.form['Emp_ID']),
            'Emp_Name': request.form['Emp_Name'],
            'Mobile_No': request.form['Mobile_No'],
            'Address': request.form['Address'],
            'Bank_Code': int(request.form['Bank_Code'])
        }
        
        # Check if employee ID already exists
        for employee in employees_data:
            if employee['Emp_ID'] == new_employee['Emp_ID']:
                flash('Employee ID already exists', 'error')
                return redirect(url_for('employees'))
        
        # Add the new employee
        employees_data.append(new_employee)
        flash('Employee added successfully', 'success')
        return redirect(url_for('employees'))

# Route for updating an employee
@app.route('/update_employee', methods=['POST'])
def update_employee():
    global employees_data
    if request.method == 'POST':
        emp_id = int(request.form['Emp_ID'])
        emp_name = request.form['Emp_Name']
        mobile_no = request.form['Mobile_No']
        address = request.form['Address']
        bank_code = int(request.form['Bank_Code'])
        
        for employee in employees_data:
            if employee['Emp_ID'] == emp_id:
                employee['Emp_Name'] = emp_name
                employee['Mobile_No'] = mobile_no
                employee['Address'] = address
                employee['Bank_Code'] = bank_code
                break
        
        flash('Employee updated successfully', 'success')
        return redirect(url_for('employees'))

# Route for deleting an employee
@app.route('/delete_employee', methods=['POST'])
def delete_employee():
    global employees_data
    if request.method == 'POST':
        emp_id = int(request.form['Emp_ID'])
        
        # Find the employee with the given ID and remove it
        employees_data = [employee for employee in employees_data if employee['Emp_ID'] != emp_id]
        
        flash('Employee deleted successfully', 'success')
        return redirect(url_for('employees'))

@app.route('/customers')
def customers():
    # Get the customers data
    customers_data = init_customers_db()  # Replace with your actual data source
    
    # Get search query and sort parameter from request
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', '')
    
    # Filter customers based on search query across all columns
    filtered_customers = customers_data
    if search_query:
        filtered_customers = [customer for customer in customers_data if any(
            str(value).lower().find(search_query.lower()) != -1 
            for key, value in customer.items()
        )]
    
    # Sort customers based on sort parameter
    if sort_by in ['Cust_ID', 'F_Name', 'L_Name', 'Mobile_No', 'E_Mail', 'Address']:
        filtered_customers = sorted(filtered_customers, key=lambda x: str(x[sort_by]))
    
    return render_template('customers.html', customers=filtered_customers, search_query=search_query, sort_by=sort_by)

# Route for adding a customer
@app.route('/add_customer', methods=['POST'])
def add_customer():
    global customers_data
    if request.method == 'POST':
        new_customer = {
            'Cust_ID': int(request.form['Cust_ID']),
            'F_Name': request.form['F_Name'],
            'L_Name': request.form['L_Name'],
            'Mobile_No': request.form['Mobile_No'],
            'E_Mail': request.form['E_Mail'],
            'Address': request.form['Address']
        }
        
        # Check if customer ID already exists
        for customer in customers_data:
            if customer['Cust_ID'] == new_customer['Cust_ID']:
                flash('Customer ID already exists', 'error')
                return redirect(url_for('customers'))
        
        # Add the new customer
        customers_data.append(new_customer)
        flash('Customer added successfully', 'success')
        return redirect(url_for('customers'))

# Route for updating a customer
@app.route('/update_customer', methods=['POST'])
def update_customer():
    global customers_data
    if request.method == 'POST':
        cust_id = int(request.form['Cust_ID'])
        f_name = request.form['F_Name']
        l_name = request.form['L_Name']
        mobile_no = request.form['Mobile_No']
        e_mail = request.form['E_Mail']
        address = request.form['Address']
        
        for customer in customers_data:
            if customer['Cust_ID'] == cust_id:
                customer['F_Name'] = f_name
                customer['L_Name'] = l_name
                customer['Mobile_No'] = mobile_no
                customer['E_Mail'] = e_mail
                customer['Address'] = address
                break
        
        flash('Customer updated successfully', 'success')
        return redirect(url_for('customers'))

# Route for deleting a customer
@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    global customers_data
    if request.method == 'POST':
        cust_id = int(request.form['Cust_ID'])
        
        # Find the customer with the given ID and remove it
        customers_data = [customer for customer in customers_data if customer['Cust_ID'] != cust_id]
        
        flash('Customer deleted successfully', 'success')
        return redirect(url_for('customers'))

@app.route('/transactions')
def transactions():
    payments = init_payments_db()
    # Calculate summary metrics
    total_amount = sum(payment['Payment_Amount'] for payment in payments)
    latest_date = max(payment['Payment_Date'] for payment in payments)
    return render_template('transactions.html', payments=payments, total_amount=total_amount, latest_date=latest_date)

@app.route('/loans')
def loans():
    global loans_data
    # Calculate summary metrics
    total_amount = sum(loan['Amount'] for loan in loans_data)
    avg_amount = round(total_amount / len(loans_data), 2) if loans_data else 0
    # Get the loans data
    loans_data = init_loans_db()  # Replace with your actual data source
    
    # Get search query and sort parameter from request
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', '')
    
    # Filter loans based on search query across all columns
    filtered_loans = loans_data
    if search_query:
        filtered_loans = [loan for loan in loans_data if any(
            str(value).lower().find(search_query.lower()) != -1 
            for key, value in loan.items()
        )]
    
    # Sort loans based on sort parameter
    if sort_by in ['Loan_No', 'Amount', 'Cust_ID', 'Customer_Name']:
        filtered_loans = sorted(filtered_loans, key=lambda x: str(x[sort_by]))
    
    return render_template('loans.html', loans=filtered_loans, search_query=search_query, sort_by=sort_by, total_amount=total_amount, avg_amount=avg_amount)

@app.route('/accounts')
def accounts():
    # Get the accounts data
    accounts_data = init_accounts_db()  # Replace with your actual data source
    
    # Get search query and sort parameter from request
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', '')
    
    # Filter accounts based on search query across all columns
    filtered_accounts = accounts_data
    if search_query:
        filtered_accounts = [account for account in accounts_data if any(
            str(value).lower().find(search_query.lower()) != -1
            for key, value in account.items()
        )]
    
    # Sort accounts based on sort parameter
    if sort_by in ['Account_No', 'balance', 'Cust_ID']:
        # For balance column, convert to float for proper numeric sorting
        if sort_by == 'balance':
            filtered_accounts = sorted(filtered_accounts, key=lambda x: float(str(x[sort_by]).replace('₹', '').replace(',', '')))
        else:
            filtered_accounts = sorted(filtered_accounts, key=lambda x: str(x[sort_by]))
    
    return render_template('accounts.html', accounts=filtered_accounts, search_query=search_query, sort_by=sort_by)

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

# Route for adding a loan
@app.route('/add_loan', methods=['POST'])
def add_loan():
    global loans_data
    if request.method == 'POST':
        new_loan = {
            'Loan_No': int(request.form['Loan_No']),
            'Amount': float(request.form['Amount']),
            'Cust_ID': int(request.form['Cust_ID']),
            'Customer_Name': request.form['Customer_Name']
        }
        
        # Check if loan number already exists
        for loan in loans_data:
            if loan['Loan_No'] == new_loan['Loan_No']:
                flash('Loan number already exists', 'error')
                return redirect(url_for('loans'))
        
        # Add the new loan
        loans_data.append(new_loan)
        flash('Loan added successfully', 'success')
        return redirect(url_for('loans'))

# Route for updating a loan
@app.route('/update_loan', methods=['POST'])
def update_loan():
    global loans_data
    if request.method == 'POST':
        loan_no = int(request.form['Loan_No'])
        amount = float(request.form['Amount'])
        cust_id = int(request.form['Cust_ID'])
        customer_name = request.form['Customer_Name']
        
        for loan in loans_data:
            if loan['Loan_No'] == loan_no:
                loan['Amount'] = amount
                loan['Cust_ID'] = cust_id
                loan['Customer_Name'] = customer_name
                break
        
        flash('Loan updated successfully', 'success')
        return redirect(url_for('loans'))

# Route for deleting a loan
@app.route('/delete_loan', methods=['POST'])
def delete_loan():
    global loans_data
    if request.method == 'POST':
        loan_no = int(request.form['Loan_No'])
        
        # Find the loan with the given number and remove it
        loans_data = [loan for loan in loans_data if loan['Loan_No'] != loan_no]
        
        flash('Loan deleted successfully', 'success')
        return redirect(url_for('loans'))

# Route for adding an account
@app.route('/add_account', methods=['POST'])
def add_account():
    global accounts_data
    if request.method == 'POST':
        new_account = {
            'Account_No': int(request.form['Account_No']),
            'balance': float(request.form['balance']),
            'Cust_ID': int(request.form['Cust_ID'])
        }
        
        # Check if account number already exists
        for account in accounts_data:
            if account['Account_No'] == new_account['Account_No']:
                flash('Account number already exists', 'error')
                return redirect(url_for('accounts'))
        
        # Add the new account
        accounts_data.append(new_account)
        flash('Account added successfully', 'success')
        return redirect(url_for('accounts'))

# Route for updating an account
@app.route('/update_account', methods=['POST'])
def update_account():
    global accounts_data
    if request.method == 'POST':
        account_no = int(request.form['Account_No'])
        balance = float(request.form['balance'])
        cust_id = int(request.form['Cust_ID'])
        
        for account in accounts_data:
            if account['Account_No'] == account_no:
                account['balance'] = balance
                account['Cust_ID'] = cust_id
                break
        
        flash('Account updated successfully', 'success')
        return redirect(url_for('accounts'))

# Route for deleting an account
@app.route('/delete_account', methods=['POST'])
def delete_account():
    global accounts_data
    if request.method == 'POST':
        account_no = int(request.form['Account_No'])
        
        # Find the account with the given number and remove it
        accounts_data = [account for account in accounts_data if account['Account_No'] != account_no]
        
        flash('Account deleted successfully', 'success')
        return redirect(url_for('accounts'))
    
    
if __name__ == '__main__':
    app.run(debug=True)