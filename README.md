# Online Banking System

This project is a Python-based Online Banking System that simulates core banking functionalities for customers and administrators. It is designed to run as a console application.

## Technologies Used

- **Programming Language:** Python
- **Standard Libraries:** File I/O, datetime
- **No external frameworks:** The system relies on Python's built-in capabilities

## Features

### Customer Features

- **Account Creation**  
  - Signup flow allows customers to create Checking, Saving, or Loan accounts.
  - Collects user details (username, password, name, address, CNIC).
  - Enforces minimum initial deposit and yearly account fee.

- **Login**
  - Customers can log in using their username and account number.

- **Account Types**
  - **Checking Account:** Allows deposits, withdrawals (with overdraft and credit limits), transaction history, and balance enquiry.
  - **Saving Account:** Supports deposits, withdrawals, interest calculations, transaction history, and balance enquiry.
  - **Loan Account:** Handles loan management, monthly debits, loan balance enquiry, account details, and transaction history.

- **Transactions**
  - Deposit and withdraw money from accounts.
  - View transaction history and account details.
  - E-statements available.

### Administrator Features

- **Admin Login**
  - Secure login using a password stored in a file.

- **User Management**
  - View all user details, individual user details, and transaction histories.

- **Account Controls**
  - Set parameters for accounts including credit limits, overdraft fees, saving account interest rates, loan account interest rates, and loan duration.

- **Reporting**
  - Access to administrator-specific reports and data.

## How It Works

- All account and transaction data are stored in text files.
- User interactions are handled via command-line prompts.
- Each account type is implemented as a Python class, encapsulating related methods.

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/baseer0767/Online_Banking_System
   cd Online_Banking_System
   ```

2. **Run the Application**
   ```bash
   python Banking_System.py
   ```

3. **Follow On-screen Prompts**
   - Choose to log in as Admin or Customer.
   - For new customers, complete the signup process.
   - Administrators can configure system parameters and review user data.

## File Structure

- `Banking_System.py`: Main application containing all logic.
- User and admin data are stored as `.txt` files generated at runtime.

## Notes

- This is a demonstration system and not intended for production use.
- Sensitive data is stored in plain text for educational purposes only.
- No external database is required.

## License

This project does not currently specify a license.

## Author

[baseer0767](https://github.com/baseer0767)
