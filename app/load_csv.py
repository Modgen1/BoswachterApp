import pandas as pd

fdw = pd.read_csv("../raw_data/fdw_monitoring.csv", sep=';')
fdw.to_excel('fdw_monitoring.xlsx')
print(fdw)