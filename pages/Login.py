import streamlit as st
import pandas as pd
import hashlib
import re

# Inisialisasi state
if 'pagelogin' not in st.session_state:
    st.session_state.pagelogin = False

if st.session_state.pagelogin:
    st.title("Anda sudah login silahkan cek gejala yg anda rasakan")
    if st.button("Logout"):
        st.session_state.pagelogin = False
        st.session_state.login = False

else:
    # Fungsi untuk membaca data pengguna dari file CSV
    def read_csv():
        try:
            user_data = pd.read_csv('user_data.csv')
        except FileNotFoundError:
            user_data = pd.DataFrame(columns=['username', 'nomor_hp', 'umur', 'password'])
        return user_data

    # Fungsi untuk menulis data pengguna ke file CSV
    def write_csv(data):
        data.to_csv('user_data.csv', index=False)

    # Fungsi untuk melakukan hashing password
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Fungsi untuk mengecek password
    def check_password(input_password, hashed_password):
        return hash_password(input_password) == hashed_password

    # Fungsi untuk registrasi pengguna
    def register(username, nomor_hp, umur, password):
        user_data = read_csv()

        # Memeriksa apakah username sudah ada (case-insensitive)
        if username.lower() in user_data['username'].str.lower().values:
            st.warning("**Username sudah digunakan. Silakan pilih username lain.**")
            return

        # Validasi Nomor HP (minimal 10 digit)
        if not re.match(r'^\d{10,}$', str(nomor_hp)):
            st.warning("**Nomor HP tidak valid. Pastikan minimal 10 digit angka.**")
            return

        # Validasi Umur (hanya angka)
        if not umur.isdigit():
            st.warning("**Umur harus berupa angka.**")
            return

        # Menambahkan pengguna baru
        hashed_password = hash_password(password)
        new_user = pd.DataFrame({'username': [username], 'nomor_hp': [nomor_hp], 'umur': [umur], 'password': [hashed_password]})
        user_data = pd.concat([user_data, new_user], ignore_index=True)

        # Menyimpan data ke file CSV
        write_csv(user_data)
        st.session_state.login = True
        st.success("**Registrasi berhasil. Silakan login.**")

    # Fungsi untuk login pengguna
    def login(username, password):
        st.session_state.username_login = username
        st.session_state.password_login = password
        user_data = read_csv()

        # Memeriksa apakah username dan password cocok
        if any((user_data['username'] == st.session_state.username_login) & (user_data['password'] == hash_password(st.session_state.password_login))):
            st.success("**Login berhasil.**")
            st.session_state.login = True
            st.session_state.pagelogin = True

        else:
            st.warning("**Login gagal. Periksa kembali username dan password.**")

    # Tampilan Streamlit
    st.title("Login dan Register")

    # Pilihan antara register dan login
    option = st.radio("Pilih opsi:", ("Register", "Login"))

    # Form untuk register
    if option == "Register":
        st.subheader("Register")
        username_reg = st.text_input("Username:")
        nomor_hp_reg = st.text_input("Nomor HP:")
        umur_reg = st.text_input("Umur:")
        password_reg = st.text_area("Password:")

        # Validasi Nomor HP dan Umur saat registrasi
        if st.button("Register"):
            if not username_reg or not password_reg or not nomor_hp_reg or not umur_reg:
                st.warning("**Semua kolom harus diisi.**")
            else:
                register(username_reg, nomor_hp_reg, umur_reg, password_reg)
                # Clear sensitive information after submission
                st.session_state.username_reg = ""
                st.session_state.password_reg = ""

    # Form untuk login
    elif option == "Login":
        st.subheader("Login")
        st.session_state.username_login = st.text_input("Username:")
        st.session_state.password_login = st.text_input("Password:", type="password")
        if st.button("Login"):
            login(st.session_state.username_login, st.session_state.password_login)
