import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if 'login' not in st.session_state:
    st.session_state.login = False

if st.session_state.login == False:
    st.title("Silahkan Login Sebagai Admin Untuk Mengakses Halaman ini")
    st.session_state.username_login = 'gandum'
    st.session_state.password_login = '123'


if (st.session_state.username_login == 'syahrul' and st.session_state.password_login == '123'):
    st.markdown("<h1 style='text-align: center;'>Admin Dashboard</h1>", unsafe_allow_html=True)
    df = pd.read_csv("user_data.csv")
    st.write("Data User :")
    st.dataframe(df)

    
    st.markdown("<h1 style='text-align: center;'>Dashboard Analysis</h1>", unsafe_allow_html=True)
    
    fig, ax = plt.subplots()
    sns.countplot(x='jenis_kelamin', hue='jenis_kelamin', data=df, ax=ax)
    ax.set_xlabel('Jenis Kelamin')
    ax.set_ylabel('Jumlah')
    ax.set_title('Persebaran Data Jenis Kelamin User')
    st.pyplot(fig)


    st.text("\n\n\n\n")
    fig, ax = plt.subplots()
    sns.countplot(x='umur', hue='umur', data=df, ax=ax)
    ax.set_xlabel('Umur')
    ax.set_ylabel('Jumlah')
    ax.set_title('Persebaran Data Umur User')
    st.pyplot(fig)

if st.session_state.login and st.session_state.username_login != 'syahrul' or st.session_state.password_login != '123':
    st.title("ANDA LOGIN BUKAN SEBAGAI ADMIN !")
    local_image_path = 'bukanAdmin.png'
    st.image(local_image_path, width=420)