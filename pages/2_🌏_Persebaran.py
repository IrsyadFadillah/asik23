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
        Sejak dikeluarkannya Peraturan Pemerintah No. 60 Tahun 2007 tentang Konservasi Sumber
        Daya Ikan dan Undang-Undang No. 27 Tahun 2007 tentang Pengelolaan Wilayah Pesisir dan
        Pulau-pulau Kecil, sejumlah Kawasan Konservasi Perairan (KKP) dan Kawasan Konservasi
        Pesisir dan Pulau-Pulau Kecil (KKP3K), telah didirikan hampir di seluruh wilayah Indonesia.
        Hingga tahun 2013 tercatat sebanyak 99 KKP/KKP3K telah dibentuk dengan luas total
        11.069.263 ha. KKP/KKP3K yang dibentuk tersebut meliputi Kawasan Konservasi Perairan
        Nasional (KKPN), Kawasan Konservasi Perarain Daerah (KKPD) / Kawasan Konservasi
        Pesisir dan Pulau-Pulau Kecil Daerah (KKP3KD) dengan berbagai kategori. Jika ditambah
        dengan kawasan konservasi yang pendiriannya mengacu pada UU No. 5 Tahun 1990 tentang
        Konservasi Sumber Daya Hayati dan Ekosistemnya (sebanyak 32 KKP dengan total luas
        4.694.947 ha), maka secara keseluruhan telah didirikan 131 KKP di Indonesia dengan
        total luas 15.764.211 ha.
             
        KKP didefinisikan sebagai kawasan perairan yang dilindungi, dikelola dengan sistem zonasi,
        untuk mewujudkan pengelolaan sumber daya ikan dan lingkungannya secara berkelanjutan
        (PP 60/2007). Secara umum KKP didefinisikan sebagai kawasan yang diperuntukkan dan dikelola
        baik secara formal maupun tidak formal agar dalam jangka panjang untuk dapat melindungi
        sumberdaya alam berikut jasa-jasa ekosistem dan nilai-nilai budayanya (IUCN-WCPA, 2008).
        Untuk mewujudkan tujuan pembentukan KKP tersebut, maka diperlukan upaya pengelolaan
        secara efektif. KKP dapat dikelola dengan lebih efektif dengan cara berjejaring. Jejaring yang dirancang
        dengan baik memberikan hubungan spasial penting yang diperlukan untuk memelihara proses-proses
        ekosistem dan keterkaitannya, serta meningkatkan kelentingan (resilience) dengan cara 
        memperkecil resiko jika terjadi bencana-bencana lokal, perubahan iklim, kegagalan pengelolaan
        atau masalah lain. Dengan demikian, kawasan konservasi yang berjejaring akan membantu
        menjamin kelestarian populasi jangka panjang secara lebih baik jika dibandingkan satu kawasan
        konservasi saja (NRC, 2002).
             
        Sebagian dari KKP di Indonesia memiliki keterkaitan antara satu dengan lainnya. Faktor
        keterkaitan tersebut disebabkan adanya hubungan secara biofisik, sosial-budaya-ekonomi dan/
        atau tata kelola. Keterkaitan satu KKP dengan KKP lainnya dapat mempengaruhi keberhasilan
        pengelolaan kawasan konservasi yang saling terkait tersebut. Sebagai contoh suatu KKP yang
        mengalami kerusakan terumbu karang dapat dibantu pemulihannya oleh KKP lainnya yang
        kondisi terumbu karangnya masih terjaga, melalui arus laut yang menghubungkan kedua kawasan
        tersebut. Saat ini diberbagai tempat di Indonesia tengah diinisiasi pembentukan jejaring KKP. Untuk
        mendapatkan gambaran serta memahami bagaimana proses dan aspek keterkaitan dalam
        pembentukan jejaring-jejaring KKP tersebut, maka disusun profil jejaring KKP.
             
        Kategori KKP menurut Permen No. 17 Tahun 2008 terdiri atas Kawasan Konservasi Pesisir &
        Pulau Pulau Kecil (KKP3K), Kawasan Konservasi Maritim (KKM), dan Kawasan Konservasi
        Perairan (KKP). Jika dirinci, KKP3K terdiri dari Suaka Pesisir, Suaka Pulau Kecil, Taman Pesisir,
        dan Taman Pulau Kecil. KKM terdiri dari Perlindungan Adat Maritim dan Perlindungan Budaya
        Maritim. KKP terdiri dari Taman Nasional Perairan, Taman Wisata Perairan, Suaka Alam Perairan,
        dan Suaka Perikanan. Upaya pengembangan KKP di berbagai negara dilandasi oleh kemanfaatan KKP yang mencakup
        multi aspek. Roberts & Hawkins (2000) menyusun daftar manfaat KKP, yaitu (i) melindungi
        eksploitasi populasi dan memperbaiki produksi benih yang akan membantu restoking untuk
        daerah penangkapan ikan, (ii) mendukung usaha perikanan, yaitu dengan adanya spillover ikan
        dewasa dan juvenil ke daerah penangkapan ikan, (iii) menyediakan perlindungan terhadap
        spesies-spesies yang sensitif terhadap kegiatan penangkapan, (iv) mencegah kerusakan habitat
        dan membantu tahap pemulihan habitat, (v) memelihara keanekaragaman dengan cara
        membantu pengembangan komunitas biologi alami yang berbeda dengan yang ada di daerah
        penangkapan, serta (vi) membantu pemulihan ekosistem yang rusak oleh gangguan dari manusia
        dan alam.

        ... (Tambahkan artikel panjang sesuai kebutuhan Anda)
    """)

if __name__ == '__main__':
    main()
