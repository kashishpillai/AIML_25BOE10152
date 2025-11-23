#Project Statement

#Problem Statement
Small retail store owners often struggle with managing customer accounts manually using paper-based systems or basic spreadsheets. This leads to several challenges:

1.Inefficient Data Management: Difficulty in organizing and retrieving customer information quickly
2.Time-Consuming Operations: Manual sorting and searching through records wastes valuable time
3.Data Loss Risk: Paper-based records are prone to damage, loss, or misplacement
4.Limited Analysis Capability: Hard to identify high-value customers or track purchase patterns
4.Scalability Issues: As the customer base grows, manual management becomes increasingly impractical

Store owners need a simple, reliable, and efficient system to maintain customer account records, track balances, and analyze customer behavior without requiring extensive technical knowledge or expensive software solutions.

#Scope of the Project
The Store Account Management System is designed to provide a lightweight, console-based solution for managing customer accounts in small to medium-sized retail stores.

-In-Scope Features:
1.Customer account creation with essential details (name, phone, balance, last purchase date)
2.Comprehensive account viewing functionality
3.Multi-criteria sorting capabilities (by name, balance, purchase date)
4.Simple menu-driven interface requiring no technical expertise
5.Data organization using efficient data structures

#Out-of-Scope (Future Enhancements):
1.Database integration for persistent storage
2.Multi-user access and authentication
3.Transaction history tracking
4.Graphical user interface (GUI)
5.Advanced reporting and analytics
6.Payment processing integration
7.SMS/Email notifications

#Target Users
-Primary Users:
1.Small Retail Store Owners: Independent shop owners managing 50-500 customer accounts
2.Store Managers: Personnel responsible for day-to-day customer relationship management
3.Sales Staff: Employees who need quick access to customer information during sales

#User Characteristics:
1.Basic computer literacy (can operate keyboard and read screen)
2.Limited or no programming knowledge
3.Need quick, reliable access to customer information
4.Prefer simple, straightforward interfaces
5.Work in fast-paced retail environments

#Use Case Scenarios:
1.A grocery store owner wants to identify customers with high outstanding balances
2.A clothing store manager needs to find customers who haven't purchased recently for promotional outreach
3.A pharmacy owner wants to maintain organized records of regular customers
4.Sales staff need to quickly check customer account status during checkout

#High-Level Features
1. Account Management
Add New Account: Register customer with name, phone number, initial balance, and last purchase date
Auto-ID Generation: Automatic assignment of unique customer IDs
Data Validation: Ensures all required fields are captured
2. Information Retrieval
View All Accounts: Display complete customer database in a readable format
Quick Access: Instant retrieval of all customer records
Formatted Output: Clear presentation of customer information
3. Data Organization & Sorting
Alphabetical Sorting: Organize customers by name for easy lookup
Balance-Based Sorting: Identify high-value customers (highest to lowest balance)
Date-Based Sorting: Track customer engagement through last purchase dates
Flexible Sorting: Multiple sorting options available without data modification
4. User Interface
Menu-Driven Navigation: Simple numbered menu for all operations
Clear Instructions: User prompts guide through each operation
Error Handling: Graceful handling of invalid inputs
Exit Option: Clean program termination
5. Technical Features
I/n-Memory Storage: Fast data access using Python lists and dictionaries
Modular Design: Separate functions for each operation
Scalable Architecture: Easy to extend with additional features
No External Dependencies: Runs with standard Python installation

#Success Criteria
The project will be considered successful if it:

1.Allows users to add and view customer accounts without errors
2.Provides accurate sorting functionality across all criteria
3.Handles invalid inputs gracefully without crashing
4.Offers intuitive navigation requiring minimal training
5.Demonstrates proper programming practices and code organization
