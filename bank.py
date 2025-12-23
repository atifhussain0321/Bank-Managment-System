import time
import json

# Greeting From Bank
print("Welcome to HDFC Bank of India")

def instructions():
    time.sleep(1)
    print('''
    1. Create Account
    2. Check Balance
    3. Deposit Money
    4. Withdraw Money
    5. Transfer Money
    6. Update Account Details
    7. View Account Details
    8. Delete Account
    0. Exit Bank
      ''')
def password(a_holder):
    password_a = input("\nCreate a Strong Pin/Password :- ")
    a_holder["password"] = password_a        
    return a_holder

def save_account(data):
    try:
        with open("accounts.json","r") as file:
            accounts = json.load(file)
    except:
        accounts = []
    accounts.append(data)
    with open("accounts.json","w") as file:
        json.dump(accounts,file,indent=4)

def create_account(user_detials,eligiblity,age_user):
    if eligiblity == True:
        print("\nYou're Eligible to Create Account\n")
        accounts = ["Saving Account"]
        if age_user >= 18:
            accounts.append("Current Account")
        a = 1
        for i in accounts:
            print(f"{a}. {i}")
            a += 1
        user_account = int(input("\nIndex of You're Account Type :- ")) - 1
        if user_account == 1:
            user_detials["account"] = accounts[user_account]
        elif user_account == 0:
            user_detials["account"] = accounts[user_account]
        else:
            print("\n You Entered Invalid Number So, You're Account Type will be Saving as Default")
            user_detials["account"] = accounts[0]
        account_nu  = "#"  + user_detials["account"][0] + user_detials["name"][0].upper() + str(user_detials["age"])[0] + str(user_detials["aadhaar"])[1] + user_detials["pan"][2] + str(user_detials["mobile"])[3]
        print(f"\nCongratulation ðŸ˜Š, You're Account Number is {account_nu}.(Remember it) & IFSC Code is HDFC0001234")
        user_detials["account_no"] = account_nu
        details = password(user_detials)
        save_account(details)
        time.sleep(0.5)
        print("\nWelcome, to HDFC Family ðŸ‘‹")
        time.sleep(0.5)
        print(f"Dear {details["name"]}, You're Account is Sucessfully Created ðŸ˜‰.")
        time.sleep(1)
        work_order()
            
    else:
        print("\nYou're Not Eligible to Create Account")

def kyc(user_details):
    time.sleep(1)
    user_kyc = True
    print("\nYour KYC has been Started...")
    if len(user_details["name"]) > 4:
        time.sleep(1)
        print("\nYour Name is Valid âœ…")
    else:
        time.sleep(1)
        user_kyc = False
        print("\nYour Name is Invalid âŒ")
    if user_details["age"] > 0 and user_details["age"] < 70:
        time.sleep(1)
        print("Your Age is Valid âœ…")
    else:
        time.sleep(1)
        user_kyc = False
        print("Your Age is Invalid âŒ")
    if len(str(user_details["aadhaar"])) == 12:
        time.sleep(1)
        print("Your Aadhaar Number is Valid âœ…")
    else:
        time.sleep(1)
        user_kyc = False
        print("Your Aadhaar Number is Invalid âŒ")
    if len(user_details["pan"]) == 10:
        time.sleep(1)
        print("Your PAN Card is Valid âœ…")
    else:
        time.sleep(1)
        user_kyc = False
        print("Your PAN Card is Invalid âŒ")
    if len(str(user_details["mobile"])) == 10:
        time.sleep(1)
        print("Your Mobile Number is Valid âœ…")
    else:
        time.sleep(1)
        user_kyc = False
        print("Your Mobile Number is Invalid âŒ")
    if len(user_details["email"]) > 10:
        time.sleep(1)
        print("Your Email Id is Valid âœ…")
    else:
        time.sleep(1)
        user_kyc = False
        print("Your Email Id is Invalid âŒ")
    if len(user_details["address"]) > 5:
        time.sleep(1)
        print("Your Address is Valid âœ…")
    else:
        time.sleep(1)
        user_kyc = False
        print("Your Address is Invalid âŒ")
    if user_kyc == True:
        create_account(user_details,True,user_details["age"])
    else:
        create_account(user_details,False,0)


def user_credetials():
    time.sleep(1)
    print("\nWe're Processig to Create You're Account")
    name = input("\nYour name :- ")
    age = int(input("Your age :- "))
    aadhaar = int(input("Your aadhaar number :- "))
    pan = input("Your pan number :- ")
    mobile = int(input("Your mobile number :- "))
    email = input("Your email id :- ")
    address = input("Your aadress :- ")

    user = {
        "name": name,
        "age": age,
        "aadhaar": aadhaar,
        "pan": pan,
        "mobile": mobile,
        "email": email,
        "address": address,
        "balance": 0,
        "transactions": [],
        "password": "",
        "ifsc":"HDFC0001234"
    }
    kyc(user)
def check_balance():
    user = False
    password = ""
    account_num = input("Enter You're Account Number :- ")
    with open("accounts.json", "r") as file:
        accounts = json.load(file)
    for i in accounts:
        if account_num == i["account_no"]:
            pin = input("Enter the Password/Pin :- ")
            if pin == i["password"]:
                user = True
                print(f"\nDear {i["name"]}, You're Bank Balance is Rs.{i["balance"]} ðŸ˜€")
                print("\nNext What is my work sir,")
                work_order()
            else:
                print("Your Password is Wrong ðŸ˜­")
                print("\nNext What is my work sir,")
                work_order()
        else:
            print("Your Account Number is Worng ðŸ˜’")
            print("\nNext What is my work sir,")
            work_order()

def deposit():
    print("\nWe're Starting the Process of Deposit Money ðŸ§¾")
    time.sleep(1)
    account_num = input("You're Account Number :- ")
    with open("accounts.json", "r") as file:
        accounts = json.load(file)
    for i in accounts:
        if i["account_no"] == account_num:
            pin = input("Enter Your Pin/Passoword :- ")
            if pin == i["password"]:
                                    amount = int(input("Enter the amount that you wanna to deposit :- Rs."))
                                    i["balance"] += amount
                                    with open("accounts.json", "w") as file:
                                        json.dump(accounts, file,indent=4)
                                    print(f"Deposit Sucessfull, Now, Your Current Balance is Rs.{i["balance"]} ðŸ˜.")
                                    print("\nWhat is Your Next Order? ")
                                    work_order()
            else:
                print("\nSad, You're Pin/Password is wrong ðŸ˜­")
                print("\nWhat is Your Next Order? ")
                work_order()
        else:
            print("\nYou're Account Number is Worng ðŸ˜¢")
            print("\nWhat is Your Next Order? ")

def work_order():
    instructions()
    time.sleep(2)
    work = int(input("How can I help You? "))
    if work == 1:
        user_credetials()
    elif work == 0:
        exit()
    elif work == 2:
        check_balance()
    elif work == 3:
        deposit()


work_order()