#Store Account Management System

#Project Overview:
The Store Account Management System is a simple console-based application designed to help small store owners manage customer accounts efficiently. The system allows users to add customer accounts, view all accounts, and sort them based on different criteria such as name, balance, and last purchase date.

This project demonstrates fundamental programming concepts including data structures (lists and dictionaries), sorting algorithms, user input handling, and modular function design.

#Features:
1.Add New Account: Register customer details including name, phone number, account balance, and last purchase date
2.View All Accounts: Display complete list of all registered customer accounts
Sort by Name: Arrange accounts alphabetically by customer name
3.Sort by Balance: Display accounts ordered by balance amount (highest to lowest)
4.Sort by Last Purchase Date: View accounts sorted by their most recent purchase date
User-Friendly Menu: Simple console interface for easy navigation

#Technologies/Tools Used:
Programming Language: Python 3.x
Data Structures: Lists and Dictionaries
Sorting: Lambda functions with built-in sorted() method
Version Control: Git & GitHub
Prerequisites
Python 3.6 or higher installed on your system
Basic understanding of command-line interface


#Steps to Install & Run the Project
1. Clone the Repository
bash
git clone https://github.com/yourusername/store-account-management.git
cd store-account-management
2. Run the Program
bash
python store_account_system.py
3. Using the Application

The main menu will appear with numbered options:
Enter the number corresponding to your desired action
-Follow the on-screen prompts to add or view accounts
-Enter 6 to exit the program

#Instructions for Testing:

-Test Case 1: Adding Accounts
Select option 1 from the menu
Enter sample data:
Name: John Doe
Phone: 9876543210
Balance: 5000
Last Purchase Date: 2024-11-20
Repeat for multiple accounts

-Test Case 2: Viewing Accounts
After adding accounts, select option 2
Verify all account details are displayed correctly

-Test Case 3: Sorting Functionality
Select option 3 to test name sorting
Select option 4 to test balance sorting (descending order)
Select option 5 to test date sorting
Verify the order is correct in each case

-Test Case 4: Empty Account List
Run the program without adding accounts
Try view and sort options
Verify appropriate messages are displayed

-Test Case 5: Invalid Input Handling
Enter an invalid menu choice (e.g., 9 or a letter)
Verify error message is displayed
Verify program continues running

#Sample Usage
==============================
   STORE ACCOUNT SYSTEM
==============================
1. Add Account
2. View Accounts
3. Sort by Name
4. Sort by Balance
5. Sort by Last Purchase
6. Exit
Enter your choice: 1

--- Add New Account ---
Enter name: Alice Smith
Enter phone number: 9876543210
Enter balance: 7500
Enter last purchase date (YYYY-MM-DD): 2024-11-15
Account added successfully!

#Project Structure
store-account-management/
│
├── store_account_system.py    # Main application file
├── README.md                   # Project documentation
├── statement.md                # Problem statement and scope
└── requirements.txt            # Python dependencies (if any)

#Future Enhancements
1.Add update and delete account functionality
Implement search by name or phone number
Add data persistence using file storage or database
2.Include transaction history for each account
3.Add balance update (credit/debit) features
4.Implement input validation for phone numbers and dates
5.Create a graphical user interface (GUI)
Contributing
This is an educational project. Suggestions and improvements are welcome!

Author
Kashish A 
VITyarthi Student
kashish.25boe10152@vitbhopal.ac.in
