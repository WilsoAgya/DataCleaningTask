"""GLOCAL FOUNDATION: Data Cleaning Task (PY02)

REQUIREMENTS:
- Remove Duplicate Rows
- Trim Whitespace from strings
- Standardize capitalization
- validate email formats (using regex)

CLEAN DATA:
    - Load Data
    - Put data inside a dataframe
    - Identify columns
    """

import pandas as pd
import re
df = pd.read_csv('data/raw/practice.csv')


#Puts all values in first_name, and last_name to proper capitalization
#First letter is capitalized
def standardize_capitalization(x):
   for col in x[["first_name","last_name"]]:
        x[col] = x[col].str.capitalize()


#Removes duplicate rows
def remove_duplicate_rows(x):
    x = x.drop_duplicates(subset=['first_name', 'last_name'], keep='first')
    return x

#Handles proper email formatting
def email_format(x):
    print("EMAIL FORMATTING")
    #Remove whitespace
    #Gets rid of underscore, replaces with .
    #Replaces gmail with gmail.com
    #Puts email into lowercase()
    x['email'] = x['email'].str.replace(r"\s", "", regex=True)\
                         .str.replace("[_]", ".", regex=True)\
                         .str.replace("gmail","gmail.com",regex=True)\
                         .str.lower()
    #For all emails it concatenates values from first_name column with the rest of the email
    #Replaces everything before the first period with lowercase values from the first_name column
    x['email'] = x['first_name'].str.lower() + x['email'].str.replace(r'^[^.]+', '', regex=True)


#Removes whitespace for all columns
def remove_whitespace(x):
    for col in x:
        x[col] = x[col].str.strip()



print("----------RAW DATA--------------")
print(df)
remove_whitespace(df)
standardize_capitalization(df)
df = remove_duplicate_rows(df)
email_format(df)


print("----------CLEAN DATA-------------")
print(df)




