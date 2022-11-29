from pathlib import Path
import streamlit as st
from st_aggrid import AgGrid
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import schedule


BASE_DIR = Path(__file__).resolve().parent.parent


def update_data():
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

    return df.to_csv(f'{BASE_DIR}/data/feedback.csv')


schedule.every().day.at("00:00").do(update_data)


def df_data():
    return pd.read_csv(f'{BASE_DIR}/data/feedback.csv')


st.set_page_config(layout="wide")


def add_navigator():
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)

    st.markdown(""" 
   <nav class="navbar navbar-expand-lg navbar-dark" class="navbar navbar-dark bg-dark" style="background-color: #3498DB;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
    <a class="navbar-brand" href="http://172.20.16.8:8505/" onclick="window.open("http://172.20.16.8:8505/"); return false;" class="text-dark">Home</a>
    <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
      <li class="nav-item active">
        <a class="navbar-brand" class="text-primary" href="https://t.me/MyMentorsFeedbackAnalysis_bot">Telegram <span class="sr-only">(current)</span></a>
      </li>
    </ul>
  </div>
</nav>
    """, unsafe_allow_html=True)


def entry(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# def select_types():
def show_title():
    st.sidebar.header("Parametrlarni sozlash")
    st.markdown("<h1 style='text-align: center; color: #0000FF; font-weight: bold;'>Astrum Mentorlarining Feedbacklari Analitikasi</h1>",
                unsafe_allow_html=True)


def show_mentors_list():
    global fs, ds, ds_mentos, yonalishs, fs_mentos, se_mentos, ds_mentors, fs_mentors, se_mentors
    fields = (
        "Tanlash",
        "Umumiy analitika",
        "Data Science",
        "Full Stack",
        "Software Engineering",
    )
    ds_mentors = df_data()[df_data()['Yonalish'] == 'Data Science']['Name'].unique()

    fs_mentors = df_data()[df_data()['Yonalish'] == 'Full Stack']['Name'].unique()

    se_mentors = df_data()[df_data()['Yonalish'] == 'Software Engineering']['Name'].unique()

    time_of_analysis = (
        "Oylik analitika",
    )

    yonalishs = st.sidebar.selectbox("Yo'nalish tanlash:", fields)
    if yonalishs == "Data Science":
        ds_mentos = st.sidebar.selectbox('Mentor tanlash:', options=ds_mentors)
    elif yonalishs == "Full Stack":
        fs_mentos = st.sidebar.selectbox('Mentor tanlash:', options=fs_mentors)
    elif yonalishs == "Software Engineering":
        se_mentos = st.sidebar.selectbox('Mentor tanlash:', options=se_mentors)

    time = st.sidebar.selectbox("Vaqtni tanlash:", time_of_analysis)


# def add_logo(logo_path, width, height):
#     logo = Image.open(logo_path)
#     modified_logo = logo.resize((width, height))
#     return modified_logodef add_logo(logo_path, width, height):
#     logo = Image.open(logo_path)
#     modified_logo = logo.resize((width, height))
#     return modified_logo


# print(df)


def hisobot():
    st.header('Mentorlar statistikasi')
    # df = df.set_index(df["Date"],drop=True)
    return df_data()


def hisobot_lot(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def analysis():
    if yonalishs == 'Umumiy analitika':
        # 1) ummumiy analitika
        fig = px.histogram(df_data(), y="Yonalish", color="Feedback", barmode="group", width=1000, height=600,
                           title="Bu Yo'nalishlarning olgan feedbaklari")

        # 1) ummumiy analitika
        fig1 = px.histogram(df_data(), x='Yonalish', y="Ball", width=600, height=650,
                            title="Bu yo'nalishlarni umumiy balli")
        st.plotly_chart(fig, use_container_width=True)
        st.plotly_chart(fig1, use_container_width=True)

    for n in range(len(ds_mentors)):
        # 3 Yo'nalish tanlaganda
        try:
            if ds_mentos == ds_mentors[n]:
                mentor = df_data()[df_data().Yonalish == "Data Science"][
                    df_data()[df_data().Yonalish == "Data Science"].Name == ds_mentors[n]]
                if ds_mentos == "Umumiy analitika":
                    fig3 = px.histogram(df_data()[df_data().Yonalish == "Data Science"], y="Name", color="Feedback",
                                        barmode="group",
                                        width=1000, height=600,
                                        title="Bu Mentorlarning olgan feedbaklari")
                    st.plotly_chart(fig3, use_container_width=True)

                    fig1 = px.histogram(df_data()[df_data().Yonalish == "Data Science"], x='Name', y="Ball", width=600,
                                        height=650,
                                        title="Bu Mentorlarning umumiy balli")
                    st.plotly_chart(fig1, use_container_width=True)
                else:
                    fig = px.histogram(mentor, y="Name", color="Feedback", barmode="group", width=1000, height=600,
                                       title="Bu Mentorlarning olgan feedbaklari")
                    st.plotly_chart(fig, use_container_width=True)

                    fig1 = px.pie(values=mentor.Soni, names=mentor.Sabab, title='Bu Mentorning olgan kammentlarni')
                    st.plotly_chart(fig1, use_container_width=True)

        except:
            pass

    for n in range(len(se_mentors)):
        # 3 Yo'nalish tanlaganda
        try:
            if se_mentos == se_mentors[n]:
                mentor = df_data()[df_data().Yonalish == "Software Engineering"][
                    df_data()[df_data().Yonalish == "Software Engineering"].Name == se_mentors[n]]
                if se_mentos == "Umumiy analitika":
                    fig3 = px.histogram(df_data()[df_data().Yonalish == "Software Engineering"], y="Name", color="Feedback",
                                        barmode="group",
                                        width=1000, height=600,
                                        title="Bu Mentorlarning olgan feedbaklari")
                    st.plotly_chart(fig3, use_container_width=True)

                    fig1 = px.histogram(df_data()[df_data().Yonalish == "Software Engineering"], x='Name', y="Ball", width=600,
                                        height=650,
                                        title="Bu Mentorlarning umumiy balli")
                    st.plotly_chart(fig1, use_container_width=True)
                else:
                    fig = px.histogram(mentor, y="Name", color="Feedback", barmode="group", width=1000, height=600,
                                       title="Bu Mentorlarning olgan feedbaklari")
                    st.plotly_chart(fig, use_container_width=True)

                    fig1 = px.pie(values=mentor.Soni, names=mentor.Sabab, title='Bu Mentorning olgan kammentlarni')
                    st.plotly_chart(fig1, use_container_width=True)
        except:
            pass
    # print(fs_mentors)
    for n in range(len(fs_mentors)):
        # 3 Yo'nalish tanlaganda
        try:
            if fs_mentos == fs_mentors[n]:
                mentor = df_data()[df_data().Yonalish == "Full Stack"][
                    df_data()[df_data().Yonalish == "Full Stack"].Name == fs_mentors[n]]
                if fs_mentos == "Umumiy analitika":
                    fig3 = px.histogram(df_data()[df_data().Yonalish == "Full Stack"], y="Name", color="Feedback",
                                        barmode="group",
                                        width=1000, height=600,
                                        title="Bu Mentorlarning olgan feedbaklari")
                    st.plotly_chart(fig3, use_container_width=True)

                    fig1 = px.histogram(df_data()[df_data().Yonalish == "Full Stack"], x='Name', y="Ball", width=600,
                                        height=650,
                                        title="Bu Mentorlarning umumiy balli")
                    st.plotly_chart(fig1, use_container_width=True)
                else:
                    fig = px.histogram(mentor, y="Name", color="Feedback", barmode="group", width=1000, height=600,
                                       title="Bu Mentorlarning olgan feedbaklari")
                    st.plotly_chart(fig, use_container_width=True)

                    fig1 = px.pie(values=mentor.Soni, names=mentor.Sabab, title='Bu Mentorning olgan kammentlarni')
                    st.plotly_chart(fig1, use_container_width=True)
        except:
            pass


def main():
    st.markdown("<h1 style='text-align: left; color: Blue;'><b>Astrum</b></h1>", unsafe_allow_html=True)
    # my_logo = add_logo(logo_path="image.jpg", width=230, height=300)
    # st.sidebar.image(my_logo)
    add_navigator()
    show_title()
    selection = st.sidebar.radio('Menu', options=['Home', 'Hisobot datasi', 'Hisobot vizualizatsiyasi'])
    if selection == "Hisobot statistikasi":
        lott = hisobot_lot("https://assets4.lottiefiles.com/packages/lf20_kitlgxkw.json")
        st_lottie(
            lott,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            height=400,
            width=900,
            key=None,
        )
    if selection == "Hisobot datasi":
        df = hisobot()
        AgGrid(df, height=700, fit_columns_on_grid_load=True)

    if selection == "Hisobot vizualizatsiyasi":
        show_mentors_list()

    if selection == "Hisobot vizualizatsiyasi":
        with st.sidebar.form(key='columns_in_form'):
            submitted = st.form_submit_button('Submit')
        if submitted:
            analysis()

    if selection == "Home":
        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("https://avatars.mds.yandex.net/get-altay/2363990/2a0000017c2652da3e09db45ef6e50c0432a/XXXL");
        background-size:cover;
        background-position: cover;
        background-repeat: no-repeat;
        background-attachment: local;
        }}
        [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}
        [data-testid="stToolbar"] {{
        right: 2rem;
        }}
        </style>
        """

        st.markdown(page_bg_img, unsafe_allow_html=True)


main()
