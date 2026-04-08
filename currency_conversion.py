# CB 1st Currency Conversion

from forex_python.converter import CurrencyRates
from currency_converter import CurrencyConverter
import customtkinter as CTk
import socket





# download forex-python, and currencyconverter for when offline

# define function update_currency():
    # have user input what currency they want to change their currency to (this is across the entire program, not just a quick conversion)

    # check that currency entered is a valid currency

    # check if user is online or not (look up something for this)

    # if user is online
        # use forex python to convert currency, change currency in user csv to input currency (numbers are still stored is USD, but when printed, use conversion to find out actual amount)
    # if user is offline
        # use currencyconverter, but first ask user if they want to proceed, as conversions may be out of date
        # if user wants to continue, change currency in user csv to input currency (though, correct amounts will still be saved in user CSV, it will just possibly display wrong on frontend)

# define function convert_currency():
    # have user input what currency they want to convert from, and what currency they want to convert to

    # have user input amount to convert to

    # if user is online, just show converted amount using forexpython

    # if user is offline, show converted amount using currencyconverter, though add note stating that amount may be inaccurate, as user is offline

def is_connected():
    try:
        # Connect to Google's public DNS server on port 53 (DNS)
        # 1.1.1.1 or 8.8.8.8 are reliable targets
        socket.create_connection(("1.1.1.1", 53), timeout=3)
        return True
    except OSError:
        return False


# Note: Update these so they will work with a tkinter GUI.  It will take an input from the GUI, and return a value for the GUI to display. 
# For all of these, use CTkEntry items to get the text input. For the general_conversion_menu, use OptionMenu.
def update_currency_offline(user_details,new_currency):
    
    c_offline = CurrencyConverter()
    try:
        c_offline.convert(1, 'USD', new_currency)
    except:
        return "Invalid currency. Please try again."
    else:
        user_details.currency = new_currency
        return f"Currency updated to {new_currency}."
                
        
def update_currency_online(user_details,new_currency):
            c = CurrencyRates()
            try:
                c.get_rate('USD', new_currency)
            except:
                return "Invalid currency. Please try again."
            else:
                user_details.currency = new_currency
                return f"Currency updated to {new_currency}."
                
def convert_currency_offline(from_cur,to_cur,amount):
    c_offline = CurrencyConverter()
    try:
        converted_amount = c_offline.convert(amount, from_cur, to_cur)
    except:
        return "Invalid currency or conversion error. Please try again."
        
    else:
        return f"{amount} {from_cur} is approximately {converted_amount:.2f} {to_cur}."
        
        

def convert_currency_online(from_cur,to_cur,amount):
    c = CurrencyRates()
    try:
        converted_amount = c.convert(amount, from_cur, to_cur)
    except:
        return "Invalid currency or conversion error. Please try again."
        
    else:
        return f"{amount} {from_cur} is approximately {converted_amount:.2f} {to_cur}."

def update_cur_menu(is_connected,app):
    # create a customtk window
    # check if user if online, if so, use update_currency_online, if not, use update_currency_offline
    # create a text input boxes so user can enter what they want to change their currency too
    pass


def convert_menu(is_connected,app):
    # create a customtk window
    # check if user is online, if so, use convert_currency_online, if not, use convert_currency_offline
    # print out returned string on window
    
    pass

def general_conversion_menu():
    # create a customtk window
    # check if user is online, if not, print note saying that currency rates my be out of date
    # create a few buttons allowing user to choose whether they want to just convert currencies or update their currenct currency
    # based on user choice, call one of the menus
    app = CTk.CTk()
    app.title("Conversion Options")
    app.geometry("500x500")

    label = CTk.CTkLabel(app, text="",fg_color = "transparent").pack()
    connection = is_connected()
    if connection == False:
        label.configure(text = "You are currently disconnected from the internet. Conversion rates may be out of date.").pack()
    else:
        pass
    
    def update_command(update_button):
        update_button.configure(text="This button works.")

    def convert_command(convert_button):
        convert_button.configure(text = "This button works.")

    update_button = CTk.CTkButton(app,text="Update Current Currency",fg_color="blue")
    update_button.configure(command = convert_command(update_button))

    convert_button = CTk.CTkButton(app,text="Convert Currencies")
    convert_button.configure(command = convert_command(convert_button),fg_color="blue")
    
    update_button.pack()
    convert_button.pack()
    app.mainloop()


general_conversion_menu()