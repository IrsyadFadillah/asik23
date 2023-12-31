import numpy as np
import streamlit as st
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

dic = {0: {'name': 'Clams',
            'description': 'Kerang (Clams) adalah jenis hewan laut yang memiliki cangkang sebagai pelindung tubuhnya. Cangkang ini terdiri dari dua bagian yang dapat dibuka dan ditutup, yang disebut dengan istilah "valve." Tubuh kerang terletak di dalam cangkang dan biasanya terdiri dari jaringan lunak. Ada berbagai jenis kerang yang dapat ditemui di perairan laut, sungai, dan danau di seluruh dunia. Beberapa jenis kerang hidup di dalam cangkang tunggal, sementara yang lain memiliki cangkang ganda yang terdiri dari dua bagian yang saling terhubung. Cangkang kerang memiliki beragam bentuk, ukuran, dan warna tergantung pada spesiesnya. Kerang umumnya menggunakan cangkangnya sebagai perlindungan dari predator dan untuk menjaga kelembapan tubuh mereka. Beberapa spesies kerang adalah filter feeder, yang berarti mereka menyaring partikel makanan mikroskopis dari air dengan bantuan insang mereka. Selain memiliki nilai biologis sebagai bagian dari ekosistem laut, beberapa jenis kerang juga memiliki nilai ekonomis tinggi karena dagingnya yang dapat dimakan dan cangkangnya yang digunakan untuk berbagai keperluan, seperti kerajinan tangan atau bahan bangunan tradisional.'}, 
       1: {'name': 'Crabs', 
           'description': 'Kepiting (Crabs) adalah binatang anggota krustasea berkaki sepuluh dari upabangsa (infraordo) Brachyura, yang dikenal mempunyai "ekor" yang sangat pendek (bahasa Yunani: brachy = pendek, ura = ekor), atau yang perutnya (abdomen) sama sekali tersembunyi di bawah dada (thorax). Tubuh kepiting dilindungi oleh cangkang yang sangat keras, tersusun dari kitin, dan dipersenjatai dengan sepasang capit. Ketam adalah nama lain bagi kepiting. Kepiting terdapat di semua samudra dunia. Ada pula kepiting air tawar dan darat, khususnya di wilayah-wilayah tropis. Rajungan adalah kepiting yang hidup di perairan laut dan jarang naik ke pantai, sedangkan yuyu adalah kepiting penghuni perairan tawar (sungai dan danau). Kepiting beraneka ragam ukurannya, dari kepiting kacang, yang lebarnya hanya beberapa milimeter, hingga kepiting laba-laba Jepang, dengan rentangan kaki hingga 4 m'
           }, 
       2: {'name': 'Jelly_Fish',
            'description': 'Ubur-ubur (Jelly Fish) adalah sejenis binatang laut tak bertulang belakang yang termasuk dalam filum Cnidaria, ubur-ubur yang dimaksud di sini adalah hewan dari kelas Schypozoa, sehingga sering disebut ubur-ubur sejati agar tidak dibingungkan dengan hewan lain yang juga disebut ubur-ubur seperti: Ctenophora (ubur-ubur sisir) dan Cubozoa (ubur-ubur kotak). Sebagai anggota Cnidaria, mereka memiliki dua bentuk tubuh yaitu polip yang menempel di dasar laut dan medusa yang dapat berenang bebas dan berbentuk cangkir terbalik.'
            }, 
       3: {'name': 'Lobster', 
           'description': 'Lobster adalah jenis kepiting laut yang memiliki cangkang keras dan kaki yang kuat. Lobster dikenal dengan bentuk tubuhnya yang panjang dan runcing, serta cangkang yang keras dan kuat untuk melindungi tubuhnya. Lobster biasanya memiliki dua pasang kaki berjalan dan beberapa pasang kaki renang. Ciri khas lobster termasuk sepasang cakar yang kuat, yang digunakan untuk merobek makanan dan melindungi diri dari predator. Warna lobster bervariasi, termasuk warna-warna seperti coklat, hijau, biru, dan oranye. Saat dimasak, warna lobster bisa berubah menjadi merah cerah. Lobster adalah hewan pemangsa dan biasanya memakan berbagai jenis makanan, termasuk ikan kecil, moluska, dan invertebrata laut lainnya. Mereka juga memiliki sistem pencernaan yang cukup sederhana.'
           }, 
       4: {'name': 'Nudibranchs', 
           'description': 'Nudibranchs, atau yang sering disebut sebagai "kupu-kupu laut," adalah kelompok kecil dan indah dari moluska tanpa cangkang yang hidup di lingkungan laut. Mereka memukau pengamat dengan warna-warna cerah dan pola-pola yang menarik pada tubuh mereka. Nudibranchs dapat ditemukan di berbagai habitat laut, mulai dari terumbu karang hingga dasar laut. Yang membuat nudibranchs begitu unik adalah kemampuan mereka untuk memanfaatkan warna dari makanan yang mereka konsumsi, seperti spons laut atau hydroid, sehingga tubuh mereka menjadi sangat berwarna dan terkadang bersinar. Meskipun ukurannya kecil, nudibranchs sering kali menjadi objek studi ilmiah karena keberagaman dan kompleksitas adaptasi yang mereka tunjukkan. Mereka tidak memiliki cangkang pelindung dan sering kali bergantung pada pertahanan kimia atau kemampuan menyembunyikan diri untuk melindungi diri dari predator. Nudibranchs memainkan peran penting dalam ekosistem laut, serta menjadi daya tarik bagi penyelam dan pecinta alam laut yang menghargai keindahan dan keunikan makhluk ini.'
           }, 
       5: {'name': 'Octopus', 
           'description': 'Gurita, makhluk laut yang menakjubkan dan cerdas, adalah sejenis moluska yang termasuk dalam kelompok Cephalopoda. Gurita memiliki ciri-ciri khas berupa delapan lengan yang dilengkapi dengan tentakel dan cakar di ujungnya. Meskipun mereka tidak memiliki tulang belakang, gurita memiliki kemampuan luar biasa untuk menyesuaikan bentuk tubuh mereka dan menyembunyikan diri di berbagai lingkungan laut. Sistem saraf kompleks gurita memungkinkan mereka berpikir dan belajar dengan cepat, membuat mereka salah satu hewan laut yang paling cerdas. Gurita juga memiliki kemampuan mengeluarkan tinta untuk melarikan diri dari predator dan mengelola suhu tubuh mereka agar tetap sesuai dengan lingkungan sekitar. Mereka terkenal sebagai pemburu yang lihai, menggunakan tentakel mereka untuk menangkap mangsa seperti ikan, krustasea, dan moluska kecil. Gurita sering menjadi objek studi ilmiah karena tingkat kecerdasan dan perilaku kompleks mereka, sementara dalam budaya populer, gurita sering kali dianggap sebagai makhluk misterius yang menarik perhatian dan kagum banyak orang.'
           }, 
       6: {'name': 'Sea_Urchins', 
           'description': 'Babi laut (sea urchins), adalah jenis echinoderm yang hidup di dasar laut dan dikenal dengan ciri khasnya yang memiliki cangkang berbentuk bulat atau bundar, disebut test, yang dilapisi oleh duri-duri yang tajam. Meskipun memiliki penampilan yang sederhana, babi laut memiliki peran penting dalam ekosistem laut. Duri-duri mereka tidak hanya berfungsi sebagai perlindungan terhadap predator, tetapi juga membantu mereka bergerak dan merayap di dasar laut. Babi laut adalah hewan pemakan detritus, memakan sisa-sisa organik dan alga laut. Beberapa spesies babi laut juga memiliki sistem penghisap kecil yang memungkinkan mereka menempel pada substrat di dasar laut. Selain itu, mereka memiliki sistem saluran air, yang membantu dalam sirkulasi air dan pertukaran zat-zat yang diperlukan untuk fungsi tubuh mereka. Babi laut memiliki keanekaragaman spesies yang tinggi, dan warna serta ukuran duri mereka bervariasi antar spesies. Meskipun mungkin terlihat tidak bergerak dengan cepat, babi laut memiliki kemampuan adaptasi yang luar biasa terhadap perubahan lingkungan dan perannya yang beragam dalam ekosistem laut membuatnya menjadi subjek penelitian ilmiah yang penting.'
           }, 
       7: {'name': 'Shrimp', 
           'description': 'Udang laut, makhluk kecil yang hidup di perairan laut, adalah anggota kelompok crustacea yang dikenal dengan enam pasang kaki, eksoskeleton keras, dan bentuk tubuh yang kompak. Udang memiliki kepala yang terdiferensiasi dengan sepasang antena yang digunakan untuk merasakan lingkungan sekitar dan sepasang mata yang dapat mendeteksi cahaya. Meskipun mereka umumnya kecil, udang memiliki peran penting dalam rantai makanan laut. Beberapa spesies udang adalah pemangsa yang lihai, sementara yang lain adalah filter feeder yang menyaring partikel makanan dari air. Udang hidup di berbagai habitat, mulai dari perairan dangkal hingga kedalaman laut yang lebih dalam. Keberagaman spesies dan warna udang menciptakan pemandangan yang menarik di bawah air, dan banyak di antaranya memiliki nilai ekonomis tinggi sebagai hasil tangkapan perikanan. Beberapa spesies udang juga menjadi bahan baku penting dalam industri makanan dan dapat ditemukan dalam berbagai hidangan kuliner di seluruh dunia.'
           }, 
       8: {'name': 'Squid', 
           'description': 'Cumi-cumi (Squid) adalah kelompok hewan sefalopoda besar atau jenis moluska yang hidup di laut. Nama "Sefalopoda" dalam bahasa Yunani berarti "kaki kepala", hal ini karena kakinya yang terpisah menjadi sejumlah tangan yang melingkari kepala. Seperti semua sefalopoda, cumi-cumi dipisahkan dengan memiliki kepala yang berbeda. Akson besar cumi-cumi ini memiliki diameter 1 mm. Cumi-cumi banyak digunakan sebagai makanan. Cumi-cumi adalah salah satu hewan dalam golongan invertebrata (tidak bertulang belakang).Salah satu jenis cumi-cumi laut dalam, Heteroteuthis, adalah yang memiliki kemampuan memancarkan cahaya. Organ yang mengeluarkan cahaya itu terletak pada ujung suatu juluran panjang yang menonjol di depan. Hal ini disebabkan peristiwa luminasi yang terjadi pada cumi-cumi jenis ini. Heteroteuthis menyemprotkan sejumlah besar cairan bercahaya apabila dirinya merasa terganggu, proses ini sama seperti pada halnya cumi-cumi biasa yang menyemprotkan tinta.'
           }, 
       9: {'name': 'Starfish',
            'description': 'Bintang laut (starfish) adalah kelompok hewan laut yang memukau dengan keindahan dan keunikan mereka. Bintang laut memiliki tubuh berbentuk bintang dengan lima lengan, meskipun beberapa spesies dapat memiliki lebih dari itu. Cangkang luar mereka dilapisi dengan duri-duri kecil yang berfungsi sebagai perlindungan terhadap predator. Bintang laut memiliki sistem vaskular air yang unik, yang memungkinkan mereka untuk bergerak dan menjalani kehidupan laut mereka. Alat pengisap di bagian bawah tubuh mereka digunakan untuk memperlekak pada substrat di dasar laut, sementara tentakel di sekitar mulut mereka digunakan untuk menangkap mangsa. Beberapa spesies bintang laut adalah pemakan detritus, sementara yang lain adalah pemangsa aktif yang dapat membuka dan menyantap kerang atau hewan laut lainnya. Bintang laut juga memiliki kemampuan regenerasi yang luar biasa; jika salah satu lengan mereka rusak, mereka dapat memperbaharui dan tumbuh kembali. Keberagaman warna dan pola pada tubuh bintang laut membuatnya menjadi objek daya tarik bagi penyelam dan pengamat laut. Selain peran ekologisnya yang penting dalam mengendalikan populasi hewan laut lainnya, bintang laut juga memainkan peran estetis yang menarik dalam keindahan ekosistem bawah laut.'
            }}

model = load_model('Asik23-BenthosException101-83.48.h5')

def predict_label(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    pred_prob = model.predict(img_array)[0]
    pred_class = int(np.argmax(pred_prob))
    accuracy = pred_prob[pred_class] * 100  # Akurasi dalam persentase
    return dic[pred_class]['name'], dic[pred_class]['description'], accuracy

def main():
    st.set_page_config(page_icon="🌊")
    st.sidebar.success("Pilih halaman untuk berganti fitur")
    st.title("Benthos Species Classification")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Membuat folder "upload" jika belum ada
        if not os.path.exists("upload"):
            os.makedirs("upload")

        img_path = os.path.join("upload", "temp.jpg")
        with open(img_path, "wb") as f:
            f.write(uploaded_file.read())

        st.image(img_path, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Classifying...")

        predicted_class, class_description, accuracy = predict_label(img_path)
        st.success(f"The predicted species is: {predicted_class}")
        st.info(f"Accuracy: {accuracy:.2f}%")

        # Menambahkan deskripsi di paling bawah dengan format artikel
        st.markdown(f"## {predicted_class}")
        st.markdown(f"<div style='text-align: justify;'>{class_description}</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
