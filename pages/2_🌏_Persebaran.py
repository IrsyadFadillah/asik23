import streamlit as st
from streamlit_folium import folium_static
import folium
from streamlit_gsheets import GSheetsConnection

def main():
    st.set_page_config(page_icon="🌊")
    st.sidebar.success("Pilih halaman untuk berganti fitur")
    st.title("Persebaran Kawasan Konservasi Perairan")

    # Establishing a Google Sheets connection
    conn = st.connection("gsheets", type=GSheetsConnection)

    # Fetching data from Google Sheets
    existing_data = conn.read(worksheet="Pengelolaan", usecols=['Jenis', 'NamaKawasan', 'Lat', 'Lon'], ttl=5)
    existing_data = existing_data.dropna(how="all")

    # Inisialisasi peta menggunakan folium
    m = folium.Map()
    folium.TileLayer('openstreetmap', location=[1.850838, 116.654750], zoom_start=4).add_to(m)
    folium.TileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', name='CartoDB DarkMatter', attr="CartoDB.DarkMatter", show=False).add_to(m)
    folium.TileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', name='Esri World Imagery', attr="Esri", show=False).add_to(m)

    kkp3k = folium.FeatureGroup(name="KKP3K").add_to(m)
    kkm = folium.FeatureGroup(name="KKM").add_to(m)
    kkp = folium.FeatureGroup(name="KKP").add_to(m)

    for index, row in existing_data.iterrows():
        jenis = row['Jenis']
        nama_kawasan = row['NamaKawasan']
        coordinates = (row['Lat'], row['Lon'])
        
        if jenis == 'KKP3K':
            folium.Marker(location=coordinates, popup=folium.Popup(nama_kawasan, parse_html=True, max_width=100)).add_to(kkp3k)
        elif jenis == 'KKM':
            folium.Marker(location=coordinates, popup=folium.Popup(nama_kawasan, parse_html=True, max_width=100)).add_to(kkm)
        elif jenis == 'KKP':
            folium.Marker(location=coordinates, popup=folium.Popup(nama_kawasan, parse_html=True, max_width=100)).add_to(kkp)

    # Menambahkan fit_bounds
    m.fit_bounds(m.get_bounds())

    # Menambahkan FeatureGroup ke dalam LayerControl
    folium.LayerControl().add_to(m)

    # Menampilkan peta di dalam streamlit
    folium_static(m)

    # Menambahkan judul dan subjudul
    st.header("Artikel: Persebaran Kawasan Konservasi Perairan")
    st.subheader("Pentingnya Konservasi Perairan untuk Lingkungan dan Ekosistem")

    # Menambahkan artikel atau deskripsi panjang
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer euismod elit nec sapien
        laoreet, vel cursus leo ultrices. Sed a justo vel quam facilisis feugiat. Proin vel elit
        vitae velit aliquet efficitur. Mauris dignissim nisi ut nisl efficitur, et venenatis nulla
        lacinia. Nullam bibendum eros eget elit sagittis, vitae auctor elit feugiat.

        Duis sit amet semper est. Fusce aliquet urna eu ligula auctor fringilla. Integer fermentum
        risus vel quam fermentum, ac blandit dolor tincidunt. Curabitur id purus eget urna
        vestibulum cursus. Mauris non metus quis risus dictum mattis. Fusce euismod elit eget
        justo tincidunt, ut dapibus ex tempor. Vestibulum tincidunt augue eu libero interdum
        sollicitudin.

        ... (Tambahkan artikel panjang sesuai kebutuhan Anda)
    """)

if __name__ == '__main__':
    main()
