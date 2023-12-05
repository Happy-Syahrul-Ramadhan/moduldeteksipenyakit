import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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
    
    jenis_kelamin_colors = {'Laki-Laki': 'blue', 'Perempuan': 'red'}
    fig1 = px.bar(df, x='jenis_kelamin', color='jenis_kelamin', color_discrete_map=jenis_kelamin_colors, title='Persebaran Data Jenis Kelamin User')
    st.plotly_chart(fig1)


    st.text("\n\n\n\n")
    umur_counts = df['umur'].value_counts()

    fig = px.bar(x=umur_counts.index, y=umur_counts.values, 
             color=umur_counts.index, color_discrete_sequence=px.colors.qualitative.Set3,
             title='Jumlah User Berdasarkan Umur')

    fig.update_layout(
    xaxis_title='Umur',
    yaxis_title='Jumlah',
    showlegend=False  
)

    st.plotly_chart(fig)

if st.session_state.login and st.session_state.username_login != 'syahrul' or st.session_state.password_login != '123':
    st.title("ANDA LOGIN BUKAN SEBAGAI ADMIN !")
    local_image_path = 'bukanAdmin.png'
    st.image(local_image_path, width=420)