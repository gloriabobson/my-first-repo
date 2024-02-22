accountsAC1 = {"Name": "Gloria Sackey-Bobson", "Age": 10, "Account_bal": 0.32}
accountsAC2 = {"Name": "Kojo Sagoe", "Age": 14, "Account_bal": 35.00}

accounts = [accountsAC1, accountsAC2]

count = 1
for account in accounts:
    print(f"\nAccountAC{count}:")
    for account_details in account.items():
        print(f"{account_details[0]} : {account_details[1]}")
    print()