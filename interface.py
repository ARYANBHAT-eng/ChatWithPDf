import streamlit as st
import subprocess


def run_selected_file(selected_file):
    if selected_file == 'ChatWithPdf':
        subprocess.Popen(['streamlit', 'run', 'chatpdf.py'])
    elif selected_file == 'ChatWithWebsite':
        subprocess.Popen(['streamlit', 'run', 'chatwithurl.py'])
    else:
        st.error("Invalid selection")


def main():
    st.title('Choose an app you want to run \n 1. ChatWithPdf \n 2. ChatWithWebsite')
    selected_file = st.selectbox('Select File:', ['ChatWithPdf', 'ChatWithWebsite'])
    if st.button('Run Selected File'):
        run_selected_file(selected_file)


if __name__ == "__main__":
    main()
