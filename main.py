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
    #Puts email into lowercase()
    x['email'] = x['email'].str.replace("[_-]", ".", regex=True)\
                         .str.lower()
    #For all emails it concatenates values from first_name column with the rest of the email
    #Proper format for email: Gets values from first column, converts it to lowercase, then replaces any spaces,punctuation, and non-word characters with nothing
    x['email'] = (x['first_name'].str.lower().str.replace(r'\W+', '', regex=True) +
                  '.' +
    #Same format goes for appending the last name part of the email
                  x['last_name'].str.lower().str.replace(r'\W+', '', regex=True) +
                  '@gmail.com')


#Removes whitespace for all columns
def remove_whitespace(x):

    for col in x:
        x[col] = x[col].str.strip()



print("----------RAW DATA--------------")
print(df)
df = df.dropna(subset=['first_name', 'last_name'])
remove_whitespace(df)
standardize_capitalization(df)
df = remove_duplicate_rows(df)
email_format(df)


print("----------CLEAN DATA-------------")
print(df)

#Write DataFrame to new CSV file
df.to_csv('updated_clean_practice.csv',index=False)




