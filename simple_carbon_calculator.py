import streamlit as st
import sqlite3
import base64
import pandas as pd
import io
import os
from datetime import date

st.set_page_config(layout="wide",page_title="CarbonWISE", page_icon="./media/carbon.ico")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def translucent_box(image_path):
    image_base64 = get_base64(image_path)
    st.markdown(
        f"""
        <div style="
            background-color: rgba(255, 255, 255, 0.7);
            border-radius: 10px;
            padding: 20px;
            width: 40%;
            margin: auto;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;">
            <img src="data:image/png;base64,{image_base64}" alt="Logo" style="max-width: 100%; height: auto;">
        </div>
        """,
        unsafe_allow_html=True
    )
translucent_box("./media/fix logo.png")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
background = get_base64("./media/6227145.jpg")

def set_background(image_path):
    background = get_base64(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{background}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
set_background("./media/6227145.jpg")

st.markdown(
    f"""
    <link rel="stylesheet" href="./style/style.css">
    """,
    unsafe_allow_html=True
)

# Buat halaman utama

left, middle, right = st.columns([2,3.5,2])
main, comps , result = middle.tabs([" ", " ", " "])


with open("./style/main.md", "r", encoding="utf-8") as main_page:
    content = main_page.read()
    st.markdown(f'<div class="translucent-box">{content}</div>', unsafe_allow_html=True)


def init_db():
    conn = sqlite3.connect("carbon_footprint.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS footprint_data (
            id INTEGER PRIMARY KEY,
            nama TEXT,
            tanggal TEXT,
            jejak_karbon REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(nama, tanggal, jejak_karbon):
    conn = sqlite3.connect("carbon_footprint.db")
    c = conn.cursor()
    c.execute("INSERT INTO footprint_data (nama, tanggal, jejak_karbon) VALUES (?, ?, ?)", (nama, tanggal, jejak_karbon))
    conn.commit()
    conn.close()

init_db()

# CSS style for translucent box
st.markdown("""
    <style>
    .translucent-box {
        background: rgba(255, 255, 255, 0.8); /* Putih transparan */
        padding: 20px;                       /* Padding dalam box */
        border-radius: 10px;                 /* Membuat sudut melengkung */
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Efek bayangan */
        font-family: Arial, sans-serif;      /* Gaya font */
        color: #333;                         /* Warna teks */
        text-align: center;                  /* Rata tengah teks */
        margin-top: 20px;                    /* Jarak dari elemen sebelumnya */
    }
    </style>
""", unsafe_allow_html=True)


# Tambahkan variabel untuk melacak apakah di halaman perhitungan
is_on_calculation_page = True


if is_on_calculation_page:
    st.title("Kalkulator Jejak Karbon Harian 🌍")

st.write("Yuk, cek jejak karbon harianmu dan liat seberapa besar dampak aktivitas kamu ke bumi, Let's glow up for the planet!🌱")

nama = st.text_input("Masukkan Nama Anda")
tanggal_input = st.date_input("Tanggal", value=date.today())

st.header("Transportasi")
car_km = st.slider("Jarak mengemudi mobil per hari (km)", 0, 100, 10)
motorcycle_km = st.slider("Jarak mengendarai motor per hari (km)", 0, 100, 10)
public_transport_hours = st.slider("Jam menggunakan transportasi umum per hari", 0, 10, 1)
st.header("Energi Rumah Tangga")
electricity_use = st.slider("Penggunaan listrik (kWh per hari)", 0, 50, 5)
lpg_use = st.slider("Penggunaan LPG (kg per hari)", 0.0, 3.0, 0.2)

include_diet = st.checkbox("Inklusi kontribusi diet")
if include_diet:
    st.header("Diet")
    diet_type = st.selectbox("Pilih jenis diet", ["Vegan", "Vegetarian", "Omnivora", "Pengonsumsi Daging Tinggi"])
else:
    diet_type = None

car_emission = car_km * 0.2
motorcycle_emission = motorcycle_km * 0.1 
public_transport_emission = public_transport_hours * 0.17  
electricity_emission = electricity_use * 0.527 
lpg_emission = lpg_use * 3 

if diet_type == "Vegan":
    diet_emission = 1.5 
elif diet_type == "Vegetarian":
    diet_emission = 2.0
elif diet_type == "Omnivora":
    diet_emission = 3.0
elif diet_type == "Pescatarrian":
    diet_emission = 4.5
else:
    diet_emission = 0 

total_emission = (car_emission + motorcycle_emission + public_transport_emission +
                  electricity_emission + lpg_emission + diet_emission)

st.header("Perkiraan Jejak Karbon Harian Anda")
st.markdown(f"""
    <div class="translucent-box">
        <h2>{total_emission:.2f} kg CO₂</h2>
        <p>Perkiraan jejak karbon harian Anda berdasarkan data yang dimasukkan.</p>
    </div>
""", unsafe_allow_html=True)

# Tombol untuk menyimpan data
if st.button("Simpan"):
    if nama:
        # Menyimpan data ke database
        save_to_db(nama, tanggal_input.strftime("%Y-%m-%d"), total_emission)

        # Menyimpan data ke CSV jika berhasil disimpan
        file_path = "carbon_footprint_data.csv"
        
        # Data baru yang akan dimasukkan
        data = {
            "Nama": [nama],
            "Tanggal": [tanggal_input.strftime("%Y-%m-%d")],
            "Jejak Karbon (kg CO2)": [total_emission]
        }

        # Membaca file CSV yang sudah ada jika ada
        if os.path.exists(file_path):
            # Jika ada, baca data yang ada ke dalam DataFrame
            existing_df = pd.read_csv(file_path)
            
            # Gabungkan dengan data baru
            df = pd.DataFrame(data)
            combined_df = pd.concat([existing_df, df], ignore_index=True)
            
            # Menghapus duplikasi berdasarkan kolom yang relevan
            combined_df = combined_df.drop_duplicates(subset=["Nama", "Tanggal", "Jejak Karbon (kg CO2)"], keep="last")
        else:
            # Jika tidak ada, buat DataFrame baru
            combined_df = pd.DataFrame(data)

        # Menyimpan gabungan data ke dalam file CSV
        combined_df.to_csv(file_path, index=False)

        # Mengonversi DataFrame menjadi file CSV dalam bentuk byte
        csv = combined_df.to_csv(index=False)
        csv_file = io.StringIO(csv)

        st.success(
            "Data berhasil disimpan!\n\n"
            "Terima kasih sudah menggunakan CarbonWISE untuk mengukur jejak karbonmu.\n\n"
            "Data-data ini nantinya akan diambil dan diolah untuk membantu menciptakan bumi yang lebih baik."
        )

        

        # Menambahkan tombol unduh di Streamlit
        st.download_button(
            label="Download CSV",
            data=csv_file.getvalue(),
            file_name="carbon_footprint_data.csv",
            mime="text/csv"
        )

    else:
        st.error("Harap masukkan nama Anda sebelum menyimpan.")

# Menambahkan pesan tambahan setelah tombol "Simpan"
st.markdown(f"""
    <div class="translucent-box">
        <p>Jangan Lupa di Simpan yaa, setelah itu kamu bisa cek jejak karbon teman-teman yang lain. Yuk, cek jejak karbon orang lain! Biar makin semangat jaga bumi bareng-bareng! 🌍💚 Lihat seberapa besar impact yang bisa kita kurangi, biar bumi tetap kece buat generasi kita. Let’s keep it sustainable, fam! 💪✨ #GoGreen #SaveThePlanet #JejakKarbon.</p>
    </div>
""", unsafe_allow_html=True)