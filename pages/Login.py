import streamlit as st
import pandas as pd
import hashlib


# inisialisasi state
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
            user_data = pd.DataFrame(columns=['username', 'password'])
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
    def register(username, password):
        user_data = read_csv()

        # Memeriksa apakah username sudah ada
        if username in user_data['username'].values:
            st.success("**Username sudah digunakan. Silakan pilih username lain.**")
            return

        # Menambahkan pengguna baru
        hashed_password = hash_password(password)
        new_user = pd.DataFrame({'username': [username], 'password': [hashed_password]})
        user_data = pd.concat([user_data, new_user], ignore_index=True)

        # Menyimpan data ke file CSV
        write_csv(user_data)
        st.session_state.login = True
        st.success("**Register berhasil.**")

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
            st.success("**Login gagal. Periksa kembali username dan password.**")

    # Tampilan Streamlit
    st.title("Login dan Register")

    # Pilihan antara register dan login
    option = st.radio("Pilih opsi:", ("Register", "Login"))

    # Form untuk register
    if option == "Register":
        st.subheader("Register")
        username_reg = st.text_input("Username:")
        password_reg = st.text_input("Password:", type="password")
        if st.button("Register"):
            register(username_reg, password_reg)

    # Form untuk login
    elif option == "Login":
        st.subheader("Login")
        st.session_state.username_login = st.text_input("Username:")
        st.session_state.password_login = st.text_input("Password:", type="password")
        if st.button("Login"):
            login(st.session_state.username_login, st.session_state.password_login)
