# CB 1st Currency Conversion

# download forex-python, and currencyconverter for when offline

# define function update_currency():
    # have user input what currency they want to change their currency to (this is across the entire program, not just a quick conversion)

    # check that currency entered is a valid currency

    # check if user is online or not (look up something for this)

    # if user is online
        # use forex python to convert currency, change currency in user csv to input currency (numbers are still stored is USD, but when printed, use conversion to find out actual amount)
    # if user is offline
        # use currencyconverter, but first ask user if they want to proceed, as conversions may be out of date
        # if user wants to continue, change currency in user csv to input currency (though, correct amounts will still be saved in user CSV, it will just possibly display wrong on userend)

# define function convert_currency():
    # have user input what currency they want to convert from, and what currency they want to convert to

    # have user input amount to convert to

    # if user is online, just show converted amount using forexpython

    # if user is offline, show converted amount using currencyconverter, though add note stating that amount may be inaccurate, as user is offline