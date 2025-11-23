# -------------------------------------------------------
# SIMPLE STORE ACCOUNT MANAGEMENT SYSTEM
# -------------------------------------------------------

accounts = []   # This will store all accounts as dictionaries


# --------------------- ADD ACCOUNT ----------------------
def add_account():
    print("\n--- Add New Account ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    balance = float(input("Enter balance: "))
    last_date = input("Enter last purchase date (YYYY-MM-DD): ")

    acc_id = len(accounts) + 1  # Auto-increment ID

    account = {
        "id": acc_id,
        "name": name,
        "phone": phone,
        "balance": balance,
        "last_purchase": last_date
    }

    accounts.append(account)
    print("Account added successfully!")


# --------------------- VIEW ACCOUNTS --------------------
def view_accounts():
    if not accounts:
        print("No accounts found!")
        return

    print("\n--- All Accounts ---")
    for acc in accounts:
        print(acc["id"], acc["name"], acc["phone"], acc["balance"], acc["last_purchase"])


# --------------------- SORT BY NAME ----------------------
def sort_by_name():
    if not accounts:
        print("No accounts to sort.")
        return

    sorted_list = sorted(accounts, key=lambda x: x["name"])

    print("\n--- Accounts Sorted by Name ---")
    for acc in sorted_list:
        print(acc["id"], acc["name"], acc["balance"])


# --------------------- SORT BY BALANCE -------------------
def sort_by_balance():
    if not accounts:
        print("No accounts to sort.")
        return

    sorted_list = sorted(accounts, key=lambda x: x["balance"], reverse=True)

    print("\n--- Accounts Sorted by Balance (High to Low) ---")
    for acc in sorted_list:
        print(acc["id"], acc["name"], acc["balance"])


# ----------------- SORT BY LAST PURCHASE DATE ------------
def sort_by_last_purchase():
    if not accounts:
        print("No accounts to sort.")
        return

    sorted_list = sorted(accounts, key=lambda x: x["last_purchase"], reverse=True)

    print("\n--- Accounts Sorted by Last Purchase Date ---")
    for acc in sorted_list:
        print(acc["id"], acc["name"], acc["last_purchase"])


# --------------------------- MENU -------------------------
def show_menu():
    print("\n==============================")
    print("   STORE ACCOUNT SYSTEM")
    print("==============================")
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Sort by Name")
    print("4. Sort by Balance")
    print("5. Sort by Last Purchase")
    print("6. Exit")


# --------------------- MAIN PROGRAM LOOP ------------------
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_account()
    elif choice == "2":
        view_accounts()
    elif choice == "3":
        sort_by_name()
    elif choice == "4":
        sort_by_balance()
    elif choice == "5":
        sort_by_last_purchase()
    elif choice == "6":
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")