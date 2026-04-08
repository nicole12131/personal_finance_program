# CB 1st Log In Functions

# use hashlib for passwords

import hashlib

SPECIAL_CHARACTERS = set("!@#$%^&*()-_=+[]{}|:;'<>.,?/~`")

# define function hash_password():
    # to be honest, I have no idea how this code works. It was written by Warren Gibson, from another group project.
    # sha256 = hashlib.sha256()
    # sha256.update(item.encode("utf-8"))
    # return sha256.hexdigest()

# define function password_requirements(password):
    # set of requirments for password. first check is just a length requirement, then the 'if not any' goes through the password and sees if there are any characters of a specific kind in the password.

    # if len(password) < 12:
        # return False

    #if not any(c.islower() for c in password):
     #   return False

   # if not any(c.isupper() for c in password):
    #    return False

    #if not any(c.isdigit() for c in password):
     #   return False

#    if not any(c in SPECIAL_CHARACTERS for c in password):
 #       return False

  #  return True


# define function create_account():
    # account detalis are username and password
    # have user enter username, make sure there isn't already an account with that username
    # have user enter password, verify password with password_requirements
    # when creating account, first save to a CSV, then use information to create an object for account
    # make sure password is hashed when saved



# define function log_in():
    # have user enter username for their account
    # see if username actually exists in csv
    # if so, have user enter password
    # hash password and see if it matches the hashed password in the user csv

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(item.encode("utf-8"))
    return sha256.hexdigest()

def password_requirements(password):
    # set of requirments for password. first check is just a length requirement, then the 'if not any' goes through the password and sees if there are any characters of a specific kind in the password.

    if len(password) < 12:
        return False

    if not any(c.islower() for c in password):
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    if not any(c in SPECIAL_CHARACTERS for c in password):
        return False

    return True

def create_account(user_details):
    while True:
        username = input("Enter a username:\n")
        check = False
        for i in user_details:
            if i['username'] == username:
                check = True
                print("Username already exists. Please try again.")
                break
        
        if check == False:
            break

    while True:
        password = input("Enter a password (12 characters, uppercase and lowercase letters, numbers, and special characters):\n")
        if password_requirements(password):
            break
        else:
            print("Password does not meet the requirements. Please try again.")

    password = hash_password(password)
    print("Account created successfully.")
    # call create_user() from saving_parsing to create user csv and save details to csv, then create user object using details and return it

def log_in(user_details):
    username = input("Enter your username:\n")
    user = None
    for i in user_details:
        if i['username'] == username:
            user = i
            break

    if not user:
        print("Username not found.")
        return None

    password = input("Enter your password:\n")
    password = hash_password(password)

    if password == user['password']:
        print("Login successful.")
        return user
    else:
        print("Incorrect password.")
        return None