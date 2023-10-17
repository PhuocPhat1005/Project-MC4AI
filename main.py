import streamlit as st
import numpy as np
import pandas as pd

# Xử lý và loại bỏ giá trị NULL trong dataframe
df = pd.read_csv('py4ai-score.csv')
df['S1'].fillna(0, inplace=True)
df['S2'].fillna(0, inplace=True)
df['S3'].fillna(0, inplace=True)
df['S4'].fillna(0, inplace=True)
df['S5'].fillna(0, inplace=True)
df['S6'].fillna(0, inplace=True)
df['S7'].fillna(0, inplace=True)
df['S8'].fillna(0, inplace=True)
df['S9'].fillna(0, inplace=True)
df['S10'].fillna(0, inplace=True)
df['BONUS'].fillna(0, inplace=True)
df['REG-MC4AI'].fillna('unknown', inplace=True)
    

tab1, tab2, tab3, tab4 = st.tabs(["Danh sách", "Biểu đồ", "Phân nhóm", "Phân loại"])
with tab1:
    st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("Giới tính")
        choose1 = st.checkbox('Nam')
        choose2 = st.checkbox('Nữ')
    with col2:
        radio = st.radio("Khối lớp", ["Tất cả", "Lớp 10", "Lớp 11", "Lớp 12"])
    with col3:
        option_1 = st.selectbox('Phòng', ['Tất cả', 'A114', 'A115'], placeholder = "Choose an option")
    with col4:
        option_2 = st.multiselect("Buổi", ["Sáng", "Chiều"], placeholder = "Choose an option")

    st.write("Lớp chuyên")

    col5, col6, col7, col8, col9 = st.columns(5)
    with col5:
        choose3 = st.checkbox("Văn")
        choose4 = st.checkbox("Toán")
    with col6:
        choose5 = st.checkbox("Lý")
        choose6 = st.checkbox("Hóa")
    with col7:
        choose7 = st.checkbox("Anh")
        choose8 = st.checkbox("Tin")
    with col8:
        choose9 = st.checkbox("Sử Địa")
        choose10 = st.checkbox("Trung Nhật")
    with col9:
        choose11 = st.checkbox("TH/SN")
        choose12 = st.checkbox("Khác")
        
    if choose1 and choose2:
        df = df
    elif choose1:
        df = df[df['GENDER'].str.contains('M')]
    elif choose2:
        df = df[df['GENDER'].str.contains('F')]

    if radio == 'Tát cả':
        df = df
    elif radio == 'Lớp 10':
        df = df[df['CLASS'].str.startswith('10')]
    elif radio == 'Lớp 11':
        df = df[df['CLASS'].str.startswith('11')]
    elif radio == 'Lớp 12':
        df = df[df['CLASS'].str.startswith('12')]
    
    if option_1 == 'Tất cả':
        df = df
    elif option_1 == 'A114':
        df = df[df['PYTHON-CLASS'].str.startswith('114')]
    elif option_1 == 'A115':
        df = df[df['PYTHON-CLASS'].str.startswith('115')]
        
    if (option_2 == ['Sáng', 'Chiều']) or (option_2 == ['Chiều', 'Sáng']):
        df = df
    elif option_2 == ['Sáng']:
        df = df[df['PYTHON-CLASS'].str.contains('S')]
    elif option_2 == ['Chiều']:
        df = df[df['PYTHON-CLASS'].str.contains('C')]
        
        
    labels = [choose3, choose4, choose5, choose6, choose7, choose8, choose9, choose10, choose11, choose12]
    m = len(labels)
    true = []
    
    for i in range(m):
        if (labels[i] == True):
            true.append(i)
            
    for i in range(len(true)):
        if (true[i] == 0):
            df = df[df['CLASS'].str[2:4] == 'CV']
        if (true[i] == 1):
            df = df[df['CLASS'].str[2:5].isin(['CT1', 'CT2'])]
        if (true[i] == 2):
            df = df[df['CLASS'].str[2:4] == 'CL']
        if (true[i] == 3):
            df = df[df['CLASS'].str[2:4] == 'CH']
        if (true[i] == 4):
            df = df[df['CLASS'].str[2:4] == 'CA']
        if (true[i] == 5):
            df = df[df['CLASS'].str[2:6] == 'CTIN']
        if (true[i] == 6):
            df = df[df['CLASS'].str[2:5] == 'CSD']
        if (true[i] == 7):
            df = df[df['CLASS'].str[2:6] == 'CTRN']
        if (true[i] == 8):
            df = df[df['CLASS'].str[2:4].isin(['TH', 'SN'])]
        if (true[i] == 9):
            df = df[df['CLASS'].str[2].isin(['A', 'B'])]        
        
    st.dataframe(df)
    
with tab2:
    tab_A, tab_B = st.tabs(["Số lượng HS", "Điểm"])
    
