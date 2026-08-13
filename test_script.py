from database import get_accounts

all_accounts = get_accounts()
for i in all_accounts:
    print(i)