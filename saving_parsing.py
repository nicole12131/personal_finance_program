# CB 1st Saving & Loading Files

# define function load_details():
    # go through details file, load each row into into a list, return that list

# define function load_user(file_paths):
    # define function load_expenses(expense_path):
        # create an expenses list, use with open to open the file, go through file and load into a list, then return list

    # define function load_incomes(income_path):
        # create an incomes list, use with open to open the file, go through file and load into a list, then return list

    # define function load_savings(savings_path):
        # create an savings list, use with open to open the file, go through file and load into a list, then return list

# define function save_user(file_paths,data lists):
    # define funcion save_expenses(expense_path,expenses):
        # first, go through and sort list by date (most recent is first)
        # then, go through and write each dict in list to file (if we save them as objects, make sure they are turned into dicts)

    # define function save_incomes(income_path,expenses):
        # first, go through and sort list by date (most recent is first)
        # then, go through and write each dict in list to file (if we save them as objects, make sure they are turned into dicts)

    # functin save_savings(income_path,savings):
        # save each item in savings dict

# define function create_user():

    # define function make_paths():
        # set all of the files so they are in the documents folder
        # have the names be "document\\username_filetype.csv" or something like that
        # return filepaths

    # define function write_details(username, password, filepaths):
        # write hashed password, username, filepaths, and set currency to USD

    # define function init_expenses(expense_path):
        # create file with expense fieldnames, use expense_path

    # define function init_incomes(income_path):
        # create file with income fieldnames, use income_path

    # define function load_savings(savings_path):
        # create file with savings fieldnames, use savings_path

