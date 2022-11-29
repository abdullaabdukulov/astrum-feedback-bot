from pathlib import Path
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent


def df_data():
    service_account_file = f'{BASE_DIR}/data/Google_servis_data.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
    SAMPLE_SPREADSHEET_ID = '1rgfEQdRBtD-AXtu3kfAvTUEwe0qkOpY2RRLSsGDBlrw'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range='sheet1').execute()
    values = result.get('values', [])
    df = pd.DataFrame(values[1:], columns=values[0])
    df.Ball = df.Ball.astype("int")
    df.Yonalish = df.Yonalish = df.Yonalish.apply(lambda x: 'Data Science' if x == 'DS' else ('Software Engineering' if x == 'SE' else 'Full Stack'))
    df["Soni"] = 1

    return df.to_csv('../data/feedback.csv')


# for a in df_data():
#     if a[1] == 'DS':
#         result_2['ds_mentors'].append(a[0])
#     elif a[1] == 'SE':
#         result_2['se_mentors'].append(a[0])
#     elif a[1] == 'FS':
#         result_2['fs_mentors'].append(a[0])

# DS = df_data()[df_data()['Yonalish'] == 'Data Science']['Name'].unique()
# SE = df_data()[df_data()['Yonalish'] == 'Software Engineering']['Name'].unique()
# FS = df_data()[df_data()['Yonalish'] == 'Full Stack']['Name'].unique()
df_data()