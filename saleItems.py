# Libraries needed for importing from github
import pandas as pd
import requests
import io

# Username of your GitHub account

username = 'seanneves'

# Personal Access Token (PAO) from your GitHub account

token = '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'

# Creates a re-usable session object with your creds in-built

github_session = requests.Session()
github_session.auth = (username, token)
    
# Downloading the csv file from your GitHub

url = "https://raw.githubusercontent.com/seanneves/495/main/inventory_495%20Welland%20Ave_7_13_2022%20-%20Inventory%20Count%20Report.csv?token=GHSAT0AAAAAABX4DJ342YGMR3472VUUSOUUYYC23TA" # Make sure the url is the raw version of the file on GitHub
download = github_session.get(url).content

# Reading the downloaded content and making it a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe to make sure everything is good

print (df.head())