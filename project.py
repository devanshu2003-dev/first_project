import random
import string
import os
import platform
def generate_random_string(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    random_string = ''.join(random.choice(characters) for _ in range(length))
    g = str(random_string)
    return g
def clear_screen():
        """Clears the console screen."""
        system = platform.system()
        if system == "Windows":
            os.system('cls')
        elif system == "Linux" or system == "Darwin":  # Darwin is macOS
            os.system('clear')
        else:
            print("h" * 100)  # Fallback: print many newlines
print("")
print("")
print("")
print("")
print("                     HELLO WELCOME TO THE BANKING MANAGEMENT SYSTEM        ")
print("")
print("")
print("")
print("")
print("")
print("                               FOR NEW USER                 ")
print("--------------------------")
print("   1.Create new account ")
print("--------------------------")
print("")
print("                 EXISTING USER / ALREADY HAVE AN ACCOUNT")
print("--------------------------")
print("   2.Login to your account ")
print("--------------------------")
print("")
print("   3.EXIT")
print("")
print("")
choice=int(input("Enter your choice : "))
if choice==1:
    clear_screen()
    print("")
    print("")
    print("")
    file1=open("Account.txt","a")
    name=input("Enter your fullname : ")
    age=input("Enter your age : ")
    address=input("Enter your address : ")
    contact=input("Enter your phone number : ")
    x= random.random() 
    accno=str(x*100000)
    length = 10  # Specify the desired length of the random string
    y = generate_random_string(length)
    print("Your Account No. is : ", accno)
    print("Your Password is : ", y)
    file1.write(name)
    file1.write("\n")
    file1.write(age)
    file1.write("\n")
    file1.write(address)
    file1.write("\n")
    file1.write(contact)
    file1.write("\n")
    file1.write(accno)
    file1.write("\n")
    file1.write(y)
    file1.write("\n")
    file1.close()
elif choice==2:
    print("")      
    print("")      
    print("")      
    print("")
    get1 = input("Enter Account Number : ")
    get2 = input(" Enter Password : ")
    with open("Account.txt", 'r') as file2:
        file_content = file2.read().strip()
    if get1==file_content or get2==file_content:
        print(" 1. Deposit Cash")
        print(" 2. Withdraw Cash")
        print(" 3. Balance ")
        get3=int(input("Enter your choice : "))
        if get3==1:
            file3 = open("Transcation.txt","a")
            dep=input("Enter the amount to be deposit : ")
            file3.write(dep)
            file3.close()
        if get3==2:
            file3 = open("Transcation.txt","a")
            withd=input("Enter the amount to be withdrawn : ")
            file3.write(withd)
            file3.close()    
            
              

