# example.py
import streamlit as st
import pandas as pd

st.title('黑蛋，您好！')
uploaded_csv = st.file_uploader('選擇您要上傳的CSV檔')

if uploaded_csv is not None:
    df = pd.read_csv(uploaded_csv)
    st.header('您所上傳的CSV檔內容：')
    st.dataframe(df)

 