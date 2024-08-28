import requests
import json
import pandas as pd
import datetime
from datetime import date
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

def umeed(df):
    url = "https://nrlm.gov.in/nrlmwebservice/services/jammukashmir/data"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(response.text)
    # print(data)
    df=pd.DataFrame(data)
    # print(df)
    # print(df.dtypes)
    df['data_sync_date']=pd.Timestamp.now().strftime("%d/%m/%Y %H:%M:%S")
    # print(df.columns)
    # print(df.head())
    return(df)