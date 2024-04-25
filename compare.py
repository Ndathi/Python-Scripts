import pandas as pd

# Load the CSV files into pandas DataFrames
df1 = pd.read_csv("./edd.csv")
df2 = pd.read_csv("./engage.csv")

# Convert email addresses to lowercase
df1['Member Email'] = df1['Member Email'].str.lower()
df2['Member Email'] = df2['Member Email'].str.lower()

# Compare email addresses and find those that are unique to each DataFrame
unique_emails_in_df1 = df1[~df1['Member Email'].isin(df2['Member Email'])]
unique_emails_in_df2 = df2[~df2['Member Email'].isin(df1['Member Email'])]

# Output the unique emails
print("Unique emails in parents at woodlandstar mailing list:")
print(unique_emails_in_df1['Member Email'])

print("\nUnique emails in engage contact list")
print(unique_emails_in_df2['Member Email'])
