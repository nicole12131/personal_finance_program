# CB 1st Log In Functions

# use hashlib for passwords

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