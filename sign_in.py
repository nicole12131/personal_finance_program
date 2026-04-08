# CB 1st Log In Functions

# use hashlib for passwords

import hashlib
from saving_parsing import *

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
    sha256.update(password.encode("utf-8"))
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

def check_username(user_details):
    # to be called in a tkinter thing
    pass



def create_account(user_details,username,password):
    # all details are obtained from a tkinter window
    password = hash_password(password)
    print("Account created successfully.")
    create_user(username,password)
    

def log_in(user_details,username,password):
    # all details are obtained from
    for i in user_details:
        user = None
        if username.lower() == i.username:
            user = i
            break
        else:
            pass
    
    if hash_password(password) == user.password:
        return "Login succesful.",user
    else:
        return "Incorrect username or password",False