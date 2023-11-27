import streamlit as st
import pandas as pd

if 'login' not in st.session_state:
    st.session_state.login = False

if st.session_state.login == False:
    st.title("Silahkan Login Sebagai Admin Untuk Mengakses Halaman ini")
    st.session_state.username_login = 'gandum'
    st.session_state.password_login = '123'


if (st.session_state.username_login == 'syahrul' and st.session_state.password_login == '123'):
    st.title("Admin Dashboard")
    df = pd.read_csv("user_data.csv")
    st.write("Data User :")
    st.dataframe(df)

if st.session_state.login and st.session_state.username_login != 'syahrul' or st.session_state.password_login != '123':
    st.title("ANDA LOGIN BUKAN SEBAGAI ADMIN !")