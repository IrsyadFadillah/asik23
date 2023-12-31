import streamlit as st 
from streamlit_gsheets import GSheetsConnection
import pandas as pd

def main():
    st.set_page_config(page_icon="🌊")
    st.sidebar.success("Pilih halaman untuk berganti fitur")
    st.title("Pengelolaan")
    # Display Title and Description
    st.markdown("Masukkan detail data baru di bawah ini.")

    # Establishing a Google Sheets connection
    conn = st.connection("gsheets", type=GSheetsConnection)

    # Fetch existing data
    existing_data = conn.read(worksheet="Pengelolaan", usecols=list(range(8)), ttl=5)
    existing_data = existing_data.dropna(how="all")

    # List of Business Types and Products
    KONSERVASI_TYPES = [
        "KKP3K",
        "KKM",
        "KKP",
        
    ]
    STATUS_PENETAPAN = [
        "PENETAPAN MKP",
        "PENCADANGAN",
        "PENCADANGAN (PROSES PENETAPAN) ",
        
    ]
    PROVINSI = [
        "Nanggroe Aceh Darussalam", "Sumatera Utara", "Sumatera Selatan", "Sumatera Barat", "Bengkulu", "Riau", "Kepulauan Riau", "Jambi", "Lampung", "Bangka Belitung", "Kalimantan Barat", "Kalimantan Tengah", "Kalimantan Selatan", "Kalimantan Timur", "Kalimantan Utara", "Banten" , "DKI Jakarta", "Jawa Barat", "Jawa Tengah", "Daerah Istimewa Yogyakarta", "Jawa Timur", "Bali", "Nusa Tenggara Barat", "Nusa Tenggara Timur", "Gorontalo", "Sulawesi Barat", "Sulawesi Tengah", "Sulawesi Utara", "Sulawesi Tenggara", "Sulawesi Selatan", "Maluku", "Maluku Utara", "Papua", "Papua Barat", "Papua Tengah", "Papua Selatan", "Papua Pegunungan", "Papua Barat Daya"
    ]
    WPP_RI = [
        "WPP 571", "WPP 572", "WPP 573", "WPP 711", "WPP 712", "WPP 713", "WPP 714", "WPP 715", "WPP 716", "WPP 717", "WPP 718"
    ]
    # Onboarding New Form
    action = st.selectbox(
    "Choose an Action",
    [
        "Tambah Data Baru",
        "Ubah Data",
        "Lihat Semua Data",
        "Hapus Data"
    ],  
    )

    if action == "Tambah Data Baru":
        st.markdown("Masukan data baru pada kolom dibawah.")
        with st.form(key="Entry_form"):
            Jenis_konservasi = st.selectbox("Jenis Konservasi*", options=KONSERVASI_TYPES, index=None)
            Nama_Kawasan = st.text_input(label="Nama Kawasan*")
            Luas_HA = st.text_input(label="Luas (HA)")
            Status_penetapan = st.selectbox("Status Penetapan", options=STATUS_PENETAPAN, index=None)
            Provinsii = st.selectbox("Provinsi", options=PROVINSI, index=None)
            WPPi = st.selectbox("WPP", options=WPP_RI, index=None)
            latitude = st.number_input(label="Latitude*", format="%.6f")
            longitude = st.number_input(label="Longitude*", format="%.6f")

            st.markdown("**required*")
            submit_button = st.form_submit_button(label="Kirim Detail Data")

            if submit_button:
                if not Jenis_konservasi or not Nama_Kawasan:
                    st.warning("Pastikan semua bidang wajib diisi.")
                elif existing_data["NamaKawasan"].str.contains(Nama_Kawasan).any():
                    st.warning("Data dengan nama perusahaan ini sudah ada.")
                else:
                    konservasi_data = pd.DataFrame(
                        [
                            {
                                "Jenis": Jenis_konservasi,
                                "NamaKawasan": Nama_Kawasan,
                                "Luas(HA)": Luas_HA,
                                "StatusPenetapan": Status_penetapan,
                                "Provinsi": Provinsii,
                                "WPP": WPPi,
                                "Lat" : format(latitude, ".6f"),
                                "Lon" : format(longitude, ".6f"),
                            }
                        ]
                    )
                    updated_df = pd.concat([existing_data, konservasi_data], ignore_index=True)
                    conn.update(worksheet="Pengelolaan", data=updated_df)
                    st.success("Data berhasil disimpan!")

    elif action == "Ubah Data":
        st.markdown("Pilih dan ubah data pada kolom dibawah.")

        konservasi_to_update = st.selectbox(
            "Pilih Nama Kawasan Untuk diedit", options=existing_data["NamaKawasan"].tolist()
        )
        konservasi_data = existing_data[existing_data["NamaKawasan"] == konservasi_to_update].iloc[
            0
        ]

        with st.form(key="update_form"):
            Jenis_konservasi = st.selectbox("Jenis Konservasi*", options=KONSERVASI_TYPES, index=None)
            Nama_Kawasan = st.text_input(label="Nama Kawasan*")
            Luas_HA = st.text_input(label="Luas (HA)")
            Status_penetapan = st.selectbox("Status Penetapan", options=STATUS_PENETAPAN, index=None)
            Provinsii = st.selectbox("Provinsi", options=PROVINSI, index=None)
            WPPi = st.selectbox("WPP", options=WPP_RI, index=None)
            latitude = st.number_input(label="Latitude*", format="%.6f")
            longitude = st.number_input(label="Longitude*", format="%.6f")
            st.markdown("**required*")
            update_button = st.form_submit_button(label="Perbarui Detail Data")

            if update_button:
                if not Jenis_konservasi or not Nama_Kawasan:
                    st.warning("Pastikan semua bidang wajib diisi.")
                else:
                    # Removing old entry
                    existing_data.drop(
                        existing_data[
                            existing_data["NamaKawasan"] == konservasi_to_update
                        ].index,
                        inplace=True,
                    )
                    # Creating updated data entry
                    updated_konservasi_data = pd.DataFrame(
                        [
                            {
                                "Jenis": Jenis_konservasi,
                                "NamaKawasan": Nama_Kawasan,
                                "Luas(HA)": Luas_HA,
                                "StatusPenetapan": Status_penetapan,
                                "Provinsi": Provinsii,
                                "WPP": WPPi,
                                "Lat" : format(latitude, ".6f"),
                                "Lon" : format(longitude, ".6f"),
                            }
                        ]
                    )
                    # Adding updated data to the dataframe
                    updated_df = pd.concat(
                        [existing_data, updated_konservasi_data], ignore_index=True
                    )
                    conn.update(worksheet="Pengelolaan", data=updated_df)
                    st.success("Data berhasil di-update!")

    # View All Datas
    elif action == "Lihat Semua Data":
        st.dataframe(existing_data)

    # Delete Data
    elif action == "Hapus Data":
        konservasi_to_delete = st.selectbox(
            "Pilih Data yang Akan Dihapus", options=existing_data["NamaKawasan"].tolist()
        )

        if st.button("Delete"):
            existing_data.drop(
                existing_data[existing_data["NamaKawasan"] == konservasi_to_delete].index,
                inplace=True,
            )
            conn.update(worksheet="Pengelolaan", data=existing_data)
            st.success("Data berhasil dihapus!")
    
    
if __name__ == '__main__':
    main()
