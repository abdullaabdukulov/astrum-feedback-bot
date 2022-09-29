import json
from googleapiclient.discovery import build
from google.oauth2 import service_account
import datetime
# from oauth2client.service_account import ServiceAccountCredentials
from data.query_data import save_row

service_account_file = '/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/Google_servis_data.json'

SCOPES = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1rgfEQdRBtD-AXtu3kfAvTUEwe0qkOpY2RRLSsGDBlrw'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

# UPDATED_MESSAGES = [["bir"]]
# sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                       range=f"sheet1!A3", valueInputOption="USER_ENTERED",
#                       body={'values': UPDATED_MESSAGES}).execute()


# rows = [{"q_li": ["D", "E", "F"]}, {"n_li": ["G", "H", "I"]}, {"q_siz": ["J", "K", "L"]}]
# caty = ['A', "B", "C"]

with open('/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/save_row.json', 'r') as f:
    s = json.load(f)
    f.close()
sheets_num = s
# dataa = ["Otabek Astanov", "DS", "Namunali", "A"]


def google_sheet_add(data):
    for i in range(len(data)+2):
        if i == 0:
            updated = data[0]
            sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                  range=f"sheet1!A{sheets_num}", valueInputOption="USER_ENTERED",
                                  body={'values': [[updated]]}).execute()

        elif i == 1:
            updated = data[1]
            sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                  range=f"sheet1!B{sheets_num}", valueInputOption="USER_ENTERED",
                                  body={'values': [[updated]]}).execute()

        elif i == 2:
            updated = data[2]
            sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                  range=f"sheet1!C{sheets_num}", valueInputOption="USER_ENTERED",
                                  body={'values': [[updated]]}).execute()

        elif i == 3:
            updated = data[3]
            sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                  range=f"sheet1!D{sheets_num}", valueInputOption="USER_ENTERED",
                                  body={'values': [[updated]]}).execute()

        elif i == 4:
            updated = data[4]
            sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                  range=f"sheet1!E{sheets_num}", valueInputOption="USER_ENTERED",
                                  body={'values': [[updated]]}).execute()

        elif i == 5:
            updated = datetime.datetime.now().strftime("%Y-%m-%d")
            sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                  range=f"sheet1!F{sheets_num}", valueInputOption="USER_ENTERED",
                                  body={'values': [[updated]]}).execute()

    globals()["sheets_num"] += 1
    save_row(sheets_num)
