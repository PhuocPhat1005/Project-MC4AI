import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


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

st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')

tab1, tab2, tab3, tab4 = st.tabs(["Danh sách", "Biểu đồ", "Phân nhóm", "Phân loại"])
with tab1:
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
    filter_conditions = {
        0: df['CLASS'].str[2:4].isin(['CV']),
        1: df['CLASS'].str[2:5].isin(['CT1', 'CT2', 'CT3']),
        2: df['CLASS'].str[2:4].isin(['CL']),
        3: df['CLASS'].str[2:4].isin(['CH']),
        4: df['CLASS'].str[2:4].isin(['CA']),
        5: df['CLASS'].str[2:6].isin(['CTIN']),
        6: df['CLASS'].str[2:5].isin(['CSD']),
        7: df['CLASS'].str[2:6].isin(['CTRN']),
        8: df['CLASS'].str[2:4].isin(['TH', 'SN']),
        9: df['CLASS'].str[2].isin(['A', 'B'])
    }
    
    num_true = sum(labels)

    if num_true == 1:
        index = labels.index(True)
        df = df[filter_conditions[index]]
    elif num_true == 2:
        indices = [i for i, label in enumerate(labels) if label]
        df = df[filter_conditions[indices[0]] | filter_conditions[indices[1]]]
    elif num_true == 3:
        indices = [i for i, label in enumerate(labels) if label]
        df = df[filter_conditions[indices[0]] | filter_conditions[indices[1]] | filter_conditions[indices[2]]]
    elif num_true == 4:
        indices = [i for i, label in enumerate(labels) if label]
        df = df[filter_conditions[indices[0]] | filter_conditions[indices[1]] | filter_conditions[indices[2]] | filter_conditions[indices[3]]]
    elif num_true == 5:
        indices = [i for i, label in enumerate(labels) if label]
        df = df[filter_conditions[indices[0]] | filter_conditions[indices[1]] | filter_conditions[indices[2]] | filter_conditions[indices[3]] | filter_conditions[indices[4]]]
    elif num_true == 6:
        indices = [i for i, label in enumerate(labels) if label]
        df = df[filter_conditions[indices[0]] | filter_conditions[indices[1]] | filter_conditions[indices[2]] | filter_conditions[indices[3]] | filter_conditions[indices[4]] | filter_conditions[indices[5]]]
    elif num_true == 7:
        indices = [i for i, label in enumerate(labels) if label]
        df = df[filter_conditions[indices[0]] | filter_conditions[indices[1]] | filter_conditions[indices[2]] | filter_conditions[indices[3]] | filter_conditions[indices[4]] | filter_conditions[indices[5]] | filter_conditions[indices[6]]]
    elif num_true == 8:
        indices = [i for i, label in enumerate(labels) if label]
        df = df[filter_conditions[indices[0]] | filter_conditions[indices[1]] | filter_conditions[indices[2]] | filter_conditions[indices[3]] | filter_conditions[indices[4]] | filter_conditions[indices[5]] | filter_conditions[indices[6]] | filter_conditions[indices[7]]]
    elif num_true == 9: 
        indices = [i for i, label in enumerate(labels) if label]
        df = df[filter_conditions[indices[0]] | filter_conditions[indices[1]] | filter_conditions[indices[2]] | filter_conditions[indices[3]] | filter_conditions[indices[4]] | filter_conditions[indices[5]] | filter_conditions[indices[6]] | filter_conditions[indices[7]] | filter_conditions[indices[8]]]
    elif num_true == 10:
        indices = [i for i, label in enumerate(labels) if label]
        df = df[filter_conditions[indices[0]] | filter_conditions[indices[1]] | filter_conditions[indices[2]] | filter_conditions[indices[3]] | filter_conditions[indices[4]] | filter_conditions[indices[5]] | filter_conditions[indices[6]] | filter_conditions[indices[7]] | filter_conditions[indices[8]] | filter_conditions[indices[9]]]
        
    cnt_1 = 0
    cnt_2 = 0
    for i in df.index:
        c = df.loc[i, 'GENDER']
        if c == 'M':
            cnt_1 += 1
        elif c == 'F':
            cnt_2 += 1
            
    if df is not None:
        students = len(df)
        maxGPA = df['GPA'].max()
        minGPA = df['GPA'].min()
        averageGPA = round(df['GPA'].mean(), 1)
        st.write('Số HS:', students, f' ({cnt_1} nam, {cnt_2} nữ)')
        st.write('GPA: cao nhất', maxGPA, ', thấp nhất ', minGPA, ', trung bình', averageGPA)
        
    st.dataframe(df)
    
with tab2:
    
    tab_A, tab_B = st.tabs(["Số lượng HS", "Điểm"])
    
    with tab_A:
        count_114S = len(df[df['PYTHON-CLASS'] == '114-S'])
        count_114C = len(df[df['PYTHON-CLASS'] == '114-C'])
        count_115S = len(df[df['PYTHON-CLASS'] == '115-S'])
        count_115C = len(df[df['PYTHON-CLASS'] == '115-C'])
        
        chart_1 = [count_114S, count_114C, count_115S, count_115C]
        name_class = []
        sizes = []
        conditions = {
            0: '114-S',
            1: '114-C',
            2: '115-S',
            3: '115-C'
        }
        
        for i in range(len(chart_1)):
            if chart_1[i] != 0:
                name_class.append(conditions[i])
                sizes.append(chart_1[i])
        
        fig, ax = plt.subplots(figsize = (6, 6))
        ax.pie(sizes, autopct='%1.1f%%', startangle = 90)
        ax.axis('equal')
        plt.legend(name_class, prop = {'size': 7}, loc = "upper right")
        plt.title('BIỂU ĐỒ BIỂU DIỄN SỰ SO SÁNH SỐ LƯỢNG HỌC SINH TỪNG BUỔI HỌC')
        st.pyplot(fig)
         
        conditions_1 = {
            0: 'Chuyên Văn',
            1: 'Chuyên Toán',
            2: 'Chuyên Lý',
            3: 'Chuyên Hóa',
            4: 'Chuyên Anh',
            5: 'Chuyên Tin',
            6: 'Chuyên Sử Địa',
            7: 'Chuyên Trung Nhật',
            8: 'Tích Hợp / Song Ngữ',
            9: 'Khác'
        }

        name_class_1 = []
        sizes_1 = []

        count_0 = len(df[df['CLASS'].str[2:4].isin(['CV'])])
        count_1 = len(df[df['CLASS'].str[2:5].isin(['CT1', 'CT2', 'CT3'])])
        count_2 = len(df[df['CLASS'].str[2:4].isin(['CL'])])
        count_3 = len(df[df['CLASS'].str[2:4].isin(['CH'])])
        count_4 = len(df[df['CLASS'].str[2:4].isin(['CA'])])
        count_5 = len(df[df['CLASS'].str[2:6].isin(['CTIN'])])
        count_6 = len(df[df['CLASS'].str[2:5].isin(['CSD'])])
        count_7 = len(df[df['CLASS'].str[2:6].isin(['CTRN'])])
        count_8 = len(df[df['CLASS'].str[2:4].isin(['TH', 'SN'])])
        count_9 = len(df[df['CLASS'].str[2].isin(['A', 'B'])])

        for i in range(len(conditions_1)):
            if locals()[f'count_{i}'] != 0:
                name_class_1.append(conditions_1[i])
                sizes_1.append(locals()[f'count_{i}'])
                
        fig, ax = plt.subplots(figsize = (6, 6))
        ax.pie(sizes_1, autopct = '%1.1f%%' , startangle = 90)
        ax.axis('equal')
        if len(name_class_1) == 1:
            plt.legend(name_class_1, prop={'size': 7}, loc='upper right')
        elif len(name_class_1) == 2:
            plt.legend(name_class_1, prop={'size': 6}, loc='upper right')
        elif len(name_class_1) == 3:
            plt.legend(name_class_1, prop={'size': 6}, loc='upper right')
        elif len(name_class_1) == 4:
            plt.legend(name_class_1, prop={'size': 6}, loc='upper right')
        elif len(name_class_1) == 5:
            plt.legend(name_class_1, prop={'size': 6}, loc='upper right')
        plt.title('BIỂU ĐỒ BIỂU DIỄN SỰ SO SÁNH SỐ LƯỢNG HỌC SINH TỪNG LỚP HỌC')
        st.pyplot(fig)