u1 = ""
p1 = ""
#####
def SignUp():
    global u1,p1
    u1 = input("New Username: ")
    p1 = input("New Password: ")
    print("")
    cp1 = input("Confirm New Password: ")

    if p1 == cp1 and u1 != None and p1 != None and cp1 != None:
        print("")
        print("Sign Up: Successfull")
        print("")
        LogIn()
    else:
        print("")
        print("Sign Up: Failed!")

def LogIn():
    if u1 == "" and p1 == "":
        print("")
        print("You have to Sign Up first!")
        print("")
        SignUp()
    else:
        u2 = input("Username: ")
        p2 = input("Password: ")
        if u2 == u1 and p2 == p1:
            a = "Successfull"
        else:
            a = "Failed!"
        print("")
        print(f"Log In: {a}")
#####
q = input("1.Log In\n2.Sign Up\n\nSelect one option: ")

if q == "1":
    LogIn()
elif q == "2":
    SignUp()
else:
    print("")
    print("Error!")