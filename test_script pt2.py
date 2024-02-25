#test_script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import sqlite3
import gdown

# Replace 'FILE_ID' with the actual ID of your Google Drive file
file_id = '11oVU31DCeiNbCucAhBZlJxsKHoubXsa1'

# Google Drive API endpoint to download the file
url = f'https://drive.google.com/uc?id={file_id}'



file = gdown.download(url,output="FPA_FOD_20221014.sqlite")

# Convert the downloaded file bytes to a BytesIO object
# file_in_memory = BytesIO(file_bytes)

conn=sqlite3.connect(file)

df=pd.read_sql_query('SELECT * FROM Fires',conn,index_col='OBJECTID')

with open('data_na.pkl','wb') as f : 
    df_na = pd.DataFrame(df.isna().sum())
    df_na.reset_index(inplace=True)
    df_na.columns = ['Column_Name', 'NaN_Count']
    pickle.dump(df_na.isna().sum(),f)


if __name__ == "__main__" : 
    None