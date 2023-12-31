import streamlit as st 

def main():
    st.set_page_config(page_icon="🌊")
    st.sidebar.success("Pilih halaman untuk berganti fitur")
    st.title("Kontak kami")
    st.header(":mailbox: Kirim kritik dan saran kepada tim kami :)")


    contact_form = """ 
    <form action="https://formsubmit.co/irsfadill11@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nama" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Kritik dan Saran"></textarea>
        <button type="submit">Kirim</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    
    local_css("style/style.css")



if __name__ == '__main__':
    main()
