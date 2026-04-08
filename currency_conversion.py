# CB 1st Currency Conversion

from forex_python.converter import CurrencyRates
from currency_converter import CurrencyConverter
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
def update_currency(user_details):
    c = CurrencyRates()
    c_offline = CurrencyConverter()
    is_online = is_connected()
    while True:
        if is_online == False:
            print("You are currently offline. Currency conversion rates may be out of date.")
            new_currency = input("Enter the currency you want to change to (USD, EUR, GBP, etc.), or enter 'exit' to return:\n").upper()
            if new_currency == 'EXIT':
                break
            try:
                c_offline.convert(1, 'USD', new_currency)
            except:
                print("Invalid currency. Please try again.")
            else:
                user_details['currency'] = new_currency
                print(f"Currency updated to {new_currency}.")
                break
        else:
            new_currency = input("Enter the currency you want to change to (USD, EUR, GBP, etc.), or enter 'exit' to return:\n").upper()
            if new_currency == 'EXIT':
                break
            try:
                c.get_rate('USD', new_currency)
            except:
                print("Invalid currency. Please try again.")
            else:
                user_details['currency'] = new_currency
                print(f"Currency updated to {new_currency}.")
                break

def convert_currency():
    c = CurrencyRates()
    c_offline = CurrencyConverter()
    is_online = is_connected()
    from_currency = input("Enter the currency you want to convert from (USD, EUR, GBP, etc.):\n").upper()
    to_currency = input("Enter the currency you want to convert to (USD, EUR, GBP, etc.):\n").upper()
    amount = float(input("Enter the amount you want to convert:\n"))
    if is_online == False:
        print("You are currently offline. Currency conversion rates may be out of date.")
        try:
            converted_amount = c_offline.convert(amount, from_currency, to_currency)
            print("Converting amounts...")
        except:
            print("Invalid currency or conversion error. Please try again.")
            return
        else:
            print(f"{amount} {from_currency} is approximately {converted_amount:.2f} {to_currency}.")
            return
    else:
        try:
            converted_amount = c.convert(from_currency, to_currency, amount)
            print("Converting amounts...")
        except:
            print("Invalid currency or conversion error. Please try again.")
            return
        else:
            print(f"{amount} {from_currency} is approximately {converted_amount:.2f} {to_currency}.")
            return
        
convert_currency()