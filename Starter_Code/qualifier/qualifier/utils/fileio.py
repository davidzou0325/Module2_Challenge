# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import questionary
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(qualifying_loans):
    """Save the qualified loans data into new CSV file.

    Args:
        save_csv (list of lists): the qualifying bank loans
    
    Returns:
        A list of lists that contains the rows of qualified loans data

    """
    # set the desinated file path and name
    answer = questionary.path("What's the path to save this csv file?").ask()
    csvpath = (answer + 'qualifying_loan_list.csv')
    # write the CSV file 
    with open (csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(qualifying_loans)
    return csvpath