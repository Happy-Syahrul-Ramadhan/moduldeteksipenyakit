import streamlit as st

# t.title('Selamat Datang di Modul Untuk Mendeteksi Jenis Penyakit')

local_image_path = 'doctor.png'

col1, col2 = st.columns(2)

col2.image(local_image_path, width=420)
col1.markdown("<h1 style='text-align: center; margin-top='10px'>Modul Deteksi Penyakit</h1>", unsafe_allow_html=True)
col1.write("Modul ini adalah modul yang mampu menganalisis berbagai jenis data penyakit, mulai dari gambaran medis hingga parameter klinis, dengan akurasi tinggi. Selain itu, penggunaan modul ini dapat mempercepat proses diagnostik, memberikan respon cepat terhadap kondisi kesehatan, dan pada akhirnya meningkatkan hasil perawatan pasien.")