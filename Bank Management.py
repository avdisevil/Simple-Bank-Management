print('''     Welcome To VSA Online Banking Management
***************************************************''')
data_user={'Shifin':'7382'}
#Dictionary Containing The UserNames And The Respective Pin Number

data_history=""

bal=0
deposit_user=0
deposit_user2=0
deposit_user3=0
deposit_user4=0
a=1
b=1
c=1
d=1
e=1
f=1
g=1
h=1
i=1
j=0
m=1
n=1
x=1
y=1
z=1

while a==1:
    option=input('''Enter 'Login' To Login Into Your Profile
Enter 'Register' To Start A New Account
---->  ''')
    if option=='Login' or option=='login':
        login_name=input("Enter Your UserName: ")
        login_pin=input("Enter Your 4-Digit Pin Number: ")
        address_user=print("Enter Your Address: ")
        if login_name in data_user and data_user[login_name]==login_pin:
            print("You Have Successfully Logged Into Your Account")
            a=a+1
        else:
            print("The Given UserName Or Pin Number Is Wrong")
    elif option=='Register' or option=='register':
        c=1
        while c==1:
            login_name=input("Enter Your Username: ")
            login_pin=input("Enter Your 4-digit Pin Number: ")
            if len(login_pin)==4 and login_pin.isdigit():
                if login_pin not in data_user.values():
                    bal=int(input("Enter Your Amount To Be Deposited (Minimum Of Rupees 500 Should Be Deposited) : "))
                    c+=1
                    b=1
                    while b==1:
                        if bal>=500:
                            print("Your New Account Has Been Created")
                            data_user[login_name]=login_pin
                            print("PREVIEW: ")
                            print("User Name: ", login_name)
                            print("Pin Number: ", login_pin)
                            print("Balance Remaining: ", bal)
                            a+=1
                            b+=1
                            c+=1
                        else:
                            print("Minimum Requirement Of Deposit Amount Is Not Fulfilled")
                            a+=1
                else:
                    print("The Given Pin Already Exists")
                    print("Try Again")
                    a+=1
            else:
                print("The Given Pin Code Is Invalid")
                a+=1
                c=1
    else:
        print("The Given Option Is Incorrect")
        print("Try Again")

# Displays The Main Menu For The User To Choose From...

while y==1:
    print("MAIN MENU: ")
    option2= input('''Enter 'A' For Balance Inquiry
Enter 'B' For Withdrawal
Enter 'C' For Deposits
Enter 'D' For Transaction Details
Enter 'E' For Options To Edit User Profile
Enter 'P' For Viewing Your Profile
Enter 'F' For Logging Out
--->  ''')
    if option2 == 'E' or option2 == 'e':
        print("You Have Chosen To Edit Your Profile")
        print("Enter Your Current UserName And Pin Number For Verification")
        variable1 = input("UserName: ")
        variable2 = input("Pin Number: ")
        if data_user[variable1] == variable2:
            print("The Verification Was Successful")
            n=1
            while n==1:
                login_name = input("Enter Your New UserName: ")
                login_pin = input("Enter Your New Pin Number: ")
                if login_pin.isdigit() and len(login_pin)==4:
                    data_user[login_name] = login_pin
                    del data_user[variable1]
                    print("PREVIEW: ")
                    print("Username: ", login_name)
                    print("Pin Number: ", login_pin)
                    print("Balance: ", bal)
                    n+=1
                else:
                    print("The Pin Should Contain 4 Digits.")
                    print("Try Again")
                    n=1
        else:
            print("No Such User Name/Pin Number Exists")

        z=1
        while z==1:
            print("Enter 'M' To Go Back To The Main Menu")
            print("Enter 'Q' To Exit")
            option3 = input("--->")
            if option3 == 'M' or option3 == 'm':
                y=1
                z+=1
            elif option3=='Q' or option3=='q':
                print("Thank You For Using VSA Banking Management System")
                print("See You Soon!")
                y+=1
                z+=1
            else:
                print("You Have Entered An Incorrect Option")
                print("Try Again")



    elif option2 == 'A' or option2 == 'a':
        print("You Have Chosen To View Your Balance Amount")
        print("Balance: ", bal)
        z=1
        while z==1:
            print("Enter 'M' To Go Back To The Main Menu")
            print("Enter 'Q' To Exit")
            option4 = input("--->")
            if option4 == 'M' or option4 == 'm':
                y=1
                z+=1
            elif option4 == 'Q' or option4 == 'q':
                print("Thank You For Using VSA Banking Management System")
                print("See You Soon!")
                y+=1
                z+=1
            else:
                print("You Have Entered An Incorrect Option")
                print("Try Again")

    elif option2 == 'C' or option2 == 'c':
        print("You Have Chosen To Deposit Money")
        e=1
        while e==1:
            print("Enter '1' For A Fixed Deposit")
            print("Enter '2' For Depositing In Savings Account")
            option8=input("--->")
            if option8=='1':
                print("You Have Chosen For A Fixed Deposit")
                print("FIXED DEPOSIT:")
                print('''For 1 Year Of Fixed Deposit, Enter Option '1' 
For 3 Years Of Fixed Deposit, Enter Option '2' 
For 5 Years Of Fixed Deposit, Enter Option '3' 
For 10 Years Of Fixed Deposit, Enter Option '4' 
To Go Back, Enter Option '5' ''')
                option9=input("--->")
                d=1
                while d==1:
                    if option9=='1':
                        print("Fixed Deposit For 1 Year: ")
                        print("Interest Rate --- 5%")
                        interest1=5
                        option10=input('''Enter 'B' To Go Back
Enter 'C' To Continue: ''')
                        f=1
                        while f==1:
                            if option10=='B' or option10=='b':
                                f+=1
                                d+=1
                            elif option10=='C' or option10=='c':
                                g=1
                                while g==1:
                                    print("Enter The Amount Of Money For Fixed Deposit (Minimum Amount Of 500): ")
                                    option11=input("--->")
                                    option11_1=int(option11)
                                    if option11.isdigit() and option11_1>=500:
                                        print("The Amount Has Been Successfully Deposited")
                                        print("Your Amount Of Money In 1 Year: ",option11_1*interest1)
                                        deposit_user +=option11_1
                                        g+=1
                                        f+=1
                                        d+=1
                                        e+=1
                                        z = 1
                                        while z == 1:
                                            print("Enter 'M' To Go Back To The Main Menu")
                                            print("Enter 'Q' To Exit")
                                            option7 = input("--->")
                                            if option7 == 'M' or option7 == 'm':
                                                y = 1
                                                z += 1
                                            elif option7 == 'Q' or option7 == 'q':
                                                print("Thank You For Using VSA Banking Management System")
                                                print("See You Soon!")
                                                y += 1
                                                z += 1
                                            else:
                                                print("You Have Entered An Incorrect Option")
                                                print("Try Again")
                                    else:
                                        print("The Given Value Is Invalid")
                                        print("Try Again")
                            else:
                                print("The Given Input Is Wrong")
                                print("Try Again")
                    elif option9=='2':
                        print("Fixed Deposit For 3 Years: ")
                        print("Interest Rate --- 5.5%")
                        interest2 = 5.5
                        option10 = input('''Enter 'B' To Go Back
Enter 'C' To Continue: ''')
                        f = 1
                        while f == 1:
                            if option10 == 'B' or option10 == 'b':
                                f += 1
                                d += 1
                            elif option10 == 'C' or option10 == 'c':
                                g = 1
                                while g == 1:
                                    print("Enter The Amount Of Money For Fixed Deposit (Minimum Amount Of 500): ")
                                    option11 = input("--->")
                                    option11_1=float(option11)
                                    if option11.isdigit() and option11_1 >= 500:
                                        print("The Amount Has Been Successfully Deposited")
                                        print("Your Amount Of Money In 3 Years: ", option11_1*interest2)
                                        deposit_user2 +=option11_1
                                        g += 1
                                        f += 1
                                        d += 1
                                        e += 1
                                        z = 1
                                        while z == 1:
                                            print("Enter 'M' To Go Back To The Main Menu")
                                            print("Enter 'Q' To Exit")
                                            option7 = input("--->")
                                            if option7 == 'M' or option7 == 'm':
                                                y = 1
                                                z += 1
                                            elif option7 == 'Q' or option7 == 'q':
                                                print("Thank You For Using VSA Banking Management System")
                                                print("See You Soon!")
                                                y += 1
                                                z += 1
                                            else:
                                                print("You Have Entered An Incorrect Option")
                                                print("Try Again")
                                    else:
                                        print("The Given Value Is Invalid")
                                        print("Try Again")
                            else:
                                print("The Given Input Is Wrong")
                                print("Try Again")
                    elif option9=='3':
                        print("Fixed Deposit For 5 Years: ")
                        print("Interest Rate --- 5.8%")
                        interest3 = 5.8
                        option10 = input('''Enter 'B' To Go Back
Enter 'C' To Continue: ''')
                        f = 1
                        while f == 1:
                            if option10 == 'B' or option10 == 'b':
                                f += 1
                                d += 1
                            elif option10 == 'C' or option10 == 'c':
                                g = 1
                                while g == 1:
                                    print("Enter The Amount Of Money For Fixed Deposit (Minimum Amount Of 500): ")
                                    option11 = input("--->")
                                    option11_1=float(option11)
                                    if option11.isdigit() and option11_1 >= 500:
                                        print("The Amount Has Been Successfully Deposited")
                                        print("Your Amount Of Money In 5 Years: ", option11_1 * interest3)
                                        deposit_user3 +=option11_1
                                        g += 1
                                        f += 1
                                        d += 1
                                        e += 1
                                        z = 1
                                        while z == 1:
                                            print("Enter 'M' To Go Back To The Main Menu")
                                            print("Enter 'Q' To Exit")
                                            option7 = input("--->")
                                            if option7 == 'M' or option7 == 'm':
                                                y = 1
                                                z += 1
                                            elif option7 == 'Q' or option7 == 'q':
                                                print("Thank You For Using VSA Banking Management System")
                                                print("See You Soon!")
                                                y += 1
                                                z += 1
                                            else:
                                                print("You Have Entered An Incorrect Option")
                                                print("Try Again")
                                    else:
                                        print("The Given Value Is Invalid")
                                        print("Try Again")
                            else:
                                print("The Given Input Is Wrong")
                                print("Try Again")
                    elif option9=='4':
                        print("Fixed Deposit For 3 Years: ")
                        print("Interest Rate --- 6%")
                        interest4 = 6
                        option10 = input('''Enter 'B' To Go Back
Enter 'C' To Continue: ''')
                        f = 1
                        while f == 1:
                            if option10 == 'B' or option10 == 'b':
                                f += 1
                                d += 1
                            elif option10 == 'C' or option10 == 'c':
                                g = 1
                                while g == 1:
                                    print("Enter The Amount Of Money For Fixed Deposit (Minimum Amount Of 500): ")
                                    option11 = input("--->")
                                    option11_1=int(option11)
                                    if option11.isdigit() and option11_1 >= 500:
                                        print("The Amount Has Been Successfully Deposited")
                                        print("Your Amount Of Money In 10 Years: ", option11_1 * interest4)
                                        deposit_user4 +=option11_1
                                        g += 1
                                        f += 1
                                        d += 1
                                        e += 1
                                        z = 1
                                        while z == 1:
                                            print("Enter 'M' To Go Back To The Main Menu")
                                            print("Enter 'Q' To Exit")
                                            option7 = input("--->")
                                            if option7 == 'M' or option7 == 'm':
                                                y = 1
                                                z += 1
                                            elif option7 == 'Q' or option7 == 'q':
                                                print("Thank You For Using VSA Banking Management System")
                                                print("See You Soon!")
                                                y += 1
                                                z += 1
                                            else:
                                                print("You Have Entered An Incorrect Option")
                                                print("Try Again")
                                    else:
                                        print("The Given Value Is Invalid")
                                        print("Try Again")
                            else:
                                print("The Given Input Is Wrong")
                                print("Try Again")
                    elif option9=='5':
                        d+=1
                        e+=1
                    else:
                        print("The Given Input Is Wrong")
                        print("Try Again")
            elif option8=='2':
                print("You Have Chosen To Deposit Money In Your Savings Account")
                i=1
                while i==1:
                    option12=input("Enter The Amount Of Money To Be Deposited: ")
                    if option12.isdigit():
                        option12_1=int(option12)
                        print("The Amount Has Been Successfully Deposited In Your Account")
                        bal+=option12_1
                        j+=1
                        j_1=str(j)
                        option12_2=str(option12_1)
                        data_history+=j_1
                        data_history=data_history+". Amount Deposited : "+option12_2
                        data_history+="\n"
                        i+=1
                    else:
                        print("The Given Value Is Incorrect")
                        print("Try Again")
                e +=1
                z = 1
                while z == 1:
                    print("Enter 'M' To Go Back To The Main Menu")
                    print("Enter 'Q' To Exit")
                    option7 = input("--->")
                    if option7 == 'M' or option7 == 'm':
                        y = 1
                        z += 1
                    elif option7 == 'Q' or option7 == 'q':
                        print("Thank You For Using VSA Banking Management System")
                        print("See You Soon!")
                        y += 1
                        z += 1
                    else:
                        print("You Have Entered An Incorrect Option")
                        print("Try Again")
            else:
                print("You Have Entered An Incorrect Option")
                print("Try Again")
                e=1

    elif option2=='B' or option2=='b':
        print("You Have Chosen To Withdraw From Your Account")
        print("Your Balance: ",bal)
        m=1
        while m==1:
            option5=input("Enter The Amount To Be Withdrawn: ")
            option5_5=int(option5)
            if option5.isdigit():
                if option5_5<=bal:
                    bal-=option5_5
                    print("The Withdrawal From Your Account Has Been Successful!")
                    j+=1
                    j_2=str(j)
                    option5_5_6=str(option5_5)
                    data_history+=j_2
                    data_history+=". Amount Withdrawn: "+option5_5_6
                    data_history+="\n"
                    print("Your Remaining Balance: ",bal)
                    m+=1
                else:
                    print("The Given Value To Be Withdrawn Is Greater Than The Balance Amount.")
                    print("Try Again")
            else:
                print("The Given Amount Is Wrong")
                print("Try Again")
        z = 1
        while z == 1:
            print("Enter 'M' To Go Back To The Main Menu")
            print("Enter 'Q' To Exit")
            option7 = input("--->")
            if option7 == 'M' or option7 == 'm':
                y = 1
                z += 1
            elif option7 == 'Q' or option7 == 'q':
                print("Thank You For Using VSA Banking Management System")
                print("See You Soon!")
                y += 1
                z += 1
            else:
                print("You Have Entered An Incorrect Option")
                print("Try Again")
    elif option2=='P' or option2=='p':
        print("You Have Chosen To View Your Bank Profile")
        print("UserName: ", login_name)
        print("Pin Number: ", login_pin)
        print("Balance Amount: ",bal)
        if deposit_user>0:
            print("Fixed Deposit Amount (For 1 Year): ",deposit_user)
        if deposit_user2>0:
            print("Fixed Deposit Amount (For 3 Years): ",deposit_user2)
        if deposit_user3>0:
            print("Fixed Deposit Amount (For 5 Years): ",deposit_user3)
        if deposit_user4>0:
            print("Fixed Deposit Amount (For 10 Years: ",deposit_user4)
        z = 1
        while z == 1:
            print("Enter 'M' To Go Back To The Main Menu")
            print("Enter 'Q' To Exit")
            option7 = input("--->")
            if option7 == 'M' or option7 == 'm':
                y = 1
                z += 1
            elif option7 == 'Q' or option7 == 'q':
                print("Thank You For Using VSA Banking Management System")
                print("See You Soon!")
                y += 1
                z += 1
            else:
                print("You Have Entered An Incorrect Option")
                print("Try Again")

    elif option2=='D' or option2=='d':
        print("You Have Chosen To View Your Transaction Details")
        print(data_history)
        z = 1
        while z == 1:
            print("Enter 'M' To Go Back To The Main Menu")
            print("Enter 'Q' To Exit")
            option7 = input("--->")
            if option7 == 'M' or option7 == 'm':
                y = 1
                z += 1
            elif option7 == 'Q' or option7 == 'q':
                print("Thank You For Using VSA Banking Management System")
                print("See You Soon!")
                y += 1
                z += 1
            else:
                print("You Have Entered An Incorrect Option")
                print("Try Again")
    elif option2=='F' or option2=='f':
        print("You Have Chosen To Log Out")
        print("Thank You For Using VSA Banking Management System")
        print("See You Soon!")
        y+=1
