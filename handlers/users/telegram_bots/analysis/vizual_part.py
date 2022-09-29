from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import plotly.express as px


def df_data():
    service_account_file = '/Users/student/Desktop/bot/My_Mentor_feedback_bot/handlers/users/telegram_bots/analysis/Google_servis_data.json'
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
    df.Yonalish = df.Yonalish = df.Yonalish.apply(lambda x: 'Data Science' if x == 'DS' else ('Software Engineering' if x == 'SE' else 'Full Stack'))
    return df


def umumit_analitika():
    # 1) ummumiy analitika
    fig = px.histogram(df_data(), y="Yonalish", color="Feedback", barmode="group", width=1000, height=600,
                       title="Bu Yo'nalishlarning olgan feedbaklari")
    fig1 = px.histogram(df_data(), x='Yonalish', y="Ball", width=600, height=650, title="Bu yo'nalishlarni umumiy balli")
    fig.write_image("/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/umumiy/yonalish/all.png")
    fig1.write_image("/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/umumiy/yonalish/all2.png")

# umumit_analitika()
# df_data()


def data_science_analitika(name):
    # name = "Komiljon Xamidjonov"
    yonalish = df_data()[df_data().Yonalish == "Data Science"]
    mentor = yonalish[yonalish.Name == name]
    fig = px.histogram(mentor, y="Name", color="Feedback", barmode="group", width=1000, height=600,
                       title=f"Bu {name} olgan feedbaklari")
    mentor['ball'] = 1
    fig2 = px.pie(values=mentor.ball, names=mentor.Sabab, title=f'{name}ning kammentariyalar analizi')
    fig.write_image(f'/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/directions/data_science/{name}_1.png')
    fig2.write_image(f'/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/directions/data_science/{name}_2.png')

# data_science_analitika('Komiljon Xamidjonov')


def full_stack_analitika(name):
    yonalish = df_data()[df_data().Yonalish == "Full Stack"]
    mentor = yonalish[yonalish.Name == name]
    fig = px.histogram(mentor, y="Name", color="Feedback", barmode="group", width=1000, height=600,
                       title=f"Bu {name} olgan feedbaklari")
    mentor['ball'] = 1
    fig2 = px.pie(values=mentor.ball, names=mentor.Sabab, title=f'{name}ning kammentariyalar analizi')
    fig.write_image(f'/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/directions/full_stack/{name}_1.png')
    fig2.write_image(f'/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/directions/full_stack/{name}_2.png')


def soft_engineer_analitika(name):
    yonalish = df_data()[df_data().Yonalish == "Software Engineering"]
    mentor = yonalish[yonalish.Name == name]
    fig = px.histogram(mentor, y="Name", color="Feedback", barmode="group", width=1000, height=600,
                       title=f"Bu {name} olgan feedbaklari")
    mentor['ball'] = 1
    fig2 = px.pie(values=mentor.ball, names=mentor.Sabab, title=f'{name}ning kammentariyalar analizi')
    fig.write_image(f'/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/directions/software/{name}_1.png')
    fig2.write_image(f'/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/directions/software/{name}_2.png')


def mentors_analysis(direction):
    yonalish = df_data()[df_data().Yonalish == direction]
    fig = px.histogram(yonalish, y="Name", color="Feedback", barmode="group", width=1000, height=600,
                       title=f"Bu {direction} mentorlarning olgan feedbaklari")
    fig1 = px.histogram(yonalish, x='Name', y="Ball", width=600, height=650, title=f"Bu {direction} mentorlarning umumiy balli")
    fig.write_image(f'/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/umumiy/mentor/{direction}.png')
    fig1.write_image(f'/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/umumiy/mentor/{direction}_1.png')

mentors_analysis('Data Science')