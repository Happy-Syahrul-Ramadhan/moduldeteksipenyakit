import streamlit as st

if 'login' not in st.session_state:
    st.session_state.login = False

if st.session_state.login:
    # Fungsi untuk membuat tautan ke API WhatsApp
    def create_whatsapp_link(phone_number, message):
        base_url = "https://wa.me/"
        phone_number = str(phone_number).replace("+", "").replace(" ", "").replace("-", "")
        whatsapp_link = f"{base_url}{phone_number}?text={message}"
        return whatsapp_link
    
    def whatsappLink2(phone_number2, message):
        base_url = "https://wa.me/"
        phone_number2 = str(phone_number2).replace("+", "").replace(" ", "").replace("-", "")
        whatsapp_link2 = f"{base_url}{phone_number2}?text={message}"

        return whatsapp_link2
    

    st.title("ISI PESAN UNTUK BERKONSULTASI DENGAN KAMI")

    # Form untuk memasukkan dan pesan
    message = st.text_area("Masukkan pesan:")
    phone_number = "+6285658763990"
    phone_number2 = "+6281298497106"

    # Tombol untuk mengarahkan ke API WhatsApp
    if st.button("Kirim Pesan via WhatsApp"):
        if phone_number and message:
            whatsapp_link = create_whatsapp_link(phone_number, message)
            whatsapp_link2 = whatsappLink2(phone_number2, message)
            st.success(f"Berhasil mengarahkan ke WhatsApp. Buka di WhatsApp ( Admin1 ) ({whatsapp_link})")
            st.success(f"Berhasil mengarahkan ke WhatsApp. Buka di WhatsApp ( Admin2 ) ({whatsapp_link2})")
        else:
            st.warning("Harap isi pesan terlebih dahulu.")
else:
    st.title("Anda Harus Login Terlebih Dahulu !!!")
    local_image_path = 'bukanAdmin.png'
    st.image(local_image_path, width=420)





