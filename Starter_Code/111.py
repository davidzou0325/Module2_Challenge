import questionary

def save_qualifying_loans():
    """
    Prompt dialog to ask user if they want to save the qualifying loans information

    """
    answer = questionary.confirm('Would you like to save your qualifying loans in a csv file?').ask()
    message = "Sure!"

    if answer == True:
        message = "Your data is saved in qualifying_loan_list.csv, please check it."
        
    print (message)

save_qualifying_loans()