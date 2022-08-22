import pandas as pd

url = "https://raw.githubusercontent.com/seanneves/495/main/inventory_495%20Welland%20Ave_7_13_2022%20-%20Inventory%20Count%20Report.csv?token=GHSAT0AAAAAABX4DJ342YGMR3472VUUSOUUYYC23TA"

df = pd.read_csv(url)