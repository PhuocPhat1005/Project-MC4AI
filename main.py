import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

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

st.title(':rainbow[BẢNG ĐIỂM LỚP PY4AI 09/2022]')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["**Danh sách**", "**Biểu đồ**", "**Phân nhóm**", "**Phân loại**", "**Điểm danh**"])
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Giới tính**")
        choose1 = st.checkbox('Nam')
        choose2 = st.checkbox('Nữ')
    with col2:
        radio = st.radio("**Khối lớp**", ["Tất cả", "Lớp 10", "Lớp 11", "Lớp 12"])
    with col3:
        option_1 = st.selectbox('**Phòng**', ['Tất cả', 'A114', 'A115'], placeholder = "Choose an option")
    with col4:
        option_2 = st.multiselect("**Buổi**", ["Sáng", "Chiều"], placeholder = "Choose an option")

    st.write("**Lớp chuyên**")

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
    
    cnt_1 = len(df[df['GENDER'].str.contains('M')])
    cnt_2 = len(df[df['GENDER'].str.contains('F')])
    count_reg_Y = len(df[df['REG-MC4AI'] == 'Y'])
    count_reg_U = len(df[df['REG-MC4AI'] == 'unknown'])
    
    if df is not None:
        students = len(df)
        maxGPA = df['GPA'].max()
        minGPA = df['GPA'].min()
        averageGPA = round(df['GPA'].mean(), 1)
        st.write('**Số HS** :', students, f' ({cnt_1} nam, {cnt_2} nữ)')
        st.write('**GPA** : cao nhất', maxGPA, ', thấp nhất ', minGPA, ', trung bình', averageGPA)
        st.write('**Số HS đăng ký tiếp lớp MC-4AI** :', count_reg_Y, ', **không đăng ký tiếp lớp MC4AI** : ', count_reg_U)
    st.dataframe(df)
    
with tab2:
    
    tab_A, tab_B = st.tabs(["**Số lượng HS**", "**Điểm**"])
    
    with tab_A:
        if(len(df)) != 0:
            # Draw the pie chart 1
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
            
            sizes = np.array(sizes)
            name_class = np.array(name_class)
            
            fig = px.pie(df, names = 'PYTHON-CLASS', title = 'BIỂU ĐỒ BIỂU DIỄN SỰ SO SÁNH SỐ LƯỢNG HỌC SINH TỪNG BUỔI HỌC')
            fig.update_layout(title_x=0.1, title_y=0.9)
            st.plotly_chart(fig)

            if len(sizes) == 1:
                st.success(f'**Kết luận**:\n\n- Chỉ có duy nhất một lớp học **{name_class[0]}** (100%).\n\n- Đây là thời điểm thích hợp nhiều người học hơn.', icon = "✍️")
            elif len(sizes) == 2:
                if (sizes[0] < sizes[1]):
                    st.success(f'**Kết luận**:\n\n- Có hai lớp học: **{name_class[0]}** và **{name_class[1]}** .\n\n- Ta thấy số lượng học sinh lớp **{name_class[0]}** ít hơn số lượng học sinh lớp **{name_class[1]}**.\n\n- Chứng tỏ học sinh có xu hướng học lớp **{name_class[1]}** nhiều hơn.', icon = "✍️")
                elif (sizes[0] > sizes[1]):
                    st.success(f'**Kết luận**:\n\n- Có hai lớp học: **{name_class[0]}** và **{name_class[1]}** .\n\n- Ta thấy số lượng học sinh lớp **{name_class[1]}** ít hơn số lượng học sinh lớp **{name_class[0]}**.\n\n- Chứng tỏ học sinh có xu hướng học lớp **{name_class[0]}** nhiều hơn.', icon = "✍️")
                elif (sizes[0] == sizes[1]):
                    st.success(f'**Kết luận**:\n\n- Có hai lớp học: **{name_class[0]}** và **{name_class[1]}** .\n\n- Ta thấy số lượng học sinh lớp **{name_class[0]}** bằng số lượng học sinh lớp **{name_class[1]}**.\n\n- Chứng tỏ giờ học là hợp lý, đáp ứng đủ nhu cầu của từng học sinh.', icon = "✍️")
            elif len(sizes) == 3:
                max_id = sizes.argmax()
                min_id = sizes.argmin()
                st.success(f'**Kết luận**:\n\n- Có ba lớp học: **{name_class[0]}**, **{name_class[1]}** và **{name_class[2]}** .\n\n- Lớp có số lượng học sinh học đông nhất là: **{name_class[max_id]}** ({sizes[max_id]} học sinh).\n\n- Lớp học có số lượng học sinh học ít nhất là: **{name_class[min_id]}** ({sizes[min_id]} học sinh).\n\n- Chứng tỏ học sinh có thời gian học lớp **{name_class[max_id]}** hơn các lớp còn lại, trong khi đó lại có xu hướng ít học lớp **{name_class[min_id]}**. Đồng thời, các lớp còn lại thì có số lưọng bình thường.', icon = "✍️")
            elif len(sizes) == 4:
                max_id = sizes.argmax()
                min_id = sizes.argmin()
                st.success(f'**Kết luận**:\n\n- Có bốn lớp học: **{name_class[0]}**, **{name_class[1]}**, **{name_class[2]}** và **{name_class[3]}** .\n\n- Lớp có số lượng học sinh học đông nhất là: **{name_class[max_id]}** ({sizes[max_id]} học sinh).\n\n- Lớp học có số lượng học sinh học ít nhất là: **{name_class[min_id]}** ({sizes[min_id]} học sinh).\n\n- Chứng tỏ học sinh có thời gian học lớp **{name_class[max_id]}** hơn các lớp còn lại, trong khi đó lại có xu hướng ít học lớp **{name_class[min_id]}**. Đồng thời, các lớp còn lại thì có số lượng bình thường.', icon = "✍️")
            
            # Draw the pie chart 2
            rank = []
            for i in df.index:
                c = df.loc[i, 'CLASS']
                if c[2:4] == 'CV':
                    rank.append('Văn')
                elif c[2:5] == 'CT1' or c[2:5] == 'CT2' or c[2:5] == 'CT3':
                    rank.append('Toán')
                elif c[2:4] == 'CL':
                    rank.append('Lý')
                elif c[2:4] == 'CH':
                    rank.append('Hóa')
                elif c[2:4] == 'CA':
                    rank.append('Anh')
                elif c[2:6] == 'CTIN':
                    rank.append('Tin')
                elif c[2:5] == 'CSD':
                    rank.append('Sử Địa')
                elif c[2:6] == 'CTRN':
                    rank.append('Trung Nhật')
                elif c[2:4] == 'TH' or c[2:4] == 'SN':
                    rank.append('TH / SN')
                elif c[2] == 'A' or c[2] == 'B':
                    rank.append('Khác')
                    
            df['CLASS-GROUP'] = rank
            fig = px.pie(df, names = 'CLASS-GROUP', title = 'BIỂU ĐỒ BIỂU DIỄN SỰ SO SÁNH SỐ LƯỢNG HỌC SINH TỪNG LỚP HỌC')
            fig.update_layout(title_x=0.1, title_y=0.9)
            st.plotly_chart(fig)
            
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
            
            if len(sizes_1) == 1:
                st.success(f'**Kết luận**:\n\n- Chỉ có duy nhất một loại đối tượng lớp học **{name_class_1[0]}** (100%).\n\n- Chứng tỏ các lớp học AI thu hút chủ yếu các học sinh của lớp **{name_class_1[0]}**.', icon = "✍️")
            elif len(sizes_1) == 2:
                if (sizes[0] < sizes[1]):
                    st.success(f'**Kết luận**:\n\n- Có hai loại đối tượng lớp học: **{name_class_1[0]}** và **{name_class_1[1]}** .\n\n- Ta thấy số lượng học sinh lớp **{name_class_1[0]}** ít hơn số lượng học sinh lớp **{name_class_1[1]}**.\n\n- Chứng tỏ các lớp học AI thu hút học sinh học lớp **{name_class_1[1]}** nhiều hơn.', icon = "✍️")
                elif (sizes[0] > sizes[1]):
                    st.success(f'**Kết luận**:\n\n- Có hai loại đối tượng lớp học: **{name_class_1[0]}** và **{name_class_1[1]}** .\n\n- Ta thấy số lượng học sinh lớp **{name_class_1[1]}** ít hơn số lượng học sinh lớp **{name_class_1[0]}**.\n\n- Chứng tỏ các lớp học AI thu hút học sinh học lớp **{name_class_1[0]}** nhiều hơn.', icon = "✍️")
                elif (sizes[0] == sizes[1]):
                    st.success(f'**Kết luận**:\n\n- Có hai loại đối tượng lớp học: **{name_class_1[0]}** và **{name_class_1[1]}** .\n\n- Ta thấy số lượng học sinh lớp **{name_class_1[0]}** bằng số lượng học sinh lớp **{name_class_1[1]}**.\n\n- Chứng tỏ các lớp học AI thu  hút học sinh đều nhau.', icon = "✍️")
            elif len(sizes_1) >= 3:
                max_id = np.argmax(sizes_1)
                min_id = np.argmin(sizes_1)
                st.success(f'**Kết luận**:\n\n- Lớp có số lượng học sinh học đông nhất là: **{name_class_1[max_id]}** ({sizes_1[max_id]} học sinh).\n\n- Lớp học có số lượng học sinh học ít nhất là: **{name_class_1[min_id]}** ({sizes_1[min_id]} học sinh).\n\n- Chứng tỏ học sinh học lớp **{name_class_1[max_id]}** yêu thích môn AI hơn các lớp còn lại, trong khi đó các học sinh học lớp **{name_class_1[min_id]}** lại không thích AI hơn. Đồng thời, các lớp còn lại thì có số lưọng học sinh yêu thích các lớp AI bình thường.', icon = "✍️")
            # Draw the pie chart 3
            conditions_2 = {
                'M': 'Nam',
                'F': 'Nữ'
            }
            
            df['GENDER'] = df['GENDER'].map(conditions_2)
            
            fig = px.pie(df, names = 'GENDER', title = 'BIỂU ĐỒ BIỂU DIỄN SỰ SO SÁNH SỐ LƯỢNG HỌC SINH NAM VÀ NỮ')
            fig.update_layout(title_x=0.1, title_y=0.9)
            st.plotly_chart(fig)
            
            if cnt_1 == 0:
                st.success(f'**Kết luận**:\n\n- Chỉ có duy nhất một giới tính **Nữ** (100%).\n\n- Chứng tỏ các lớp học AI thu hút nhiều học sinh **Nữ**.', icon = "✍️")
            elif cnt_2 == 0:
                st.success(f'**Kết luận**:\n\n- Chỉ có duy nhất một giới tính **Nam** (100%).\n\n- Chứng tỏ các lớp học AI thu hút nhiều học sinh **Nam**.', icon = "✍️")
            elif cnt_1 > cnt_2:
                st.success(f'**Kết luận**:\n\n- Có hai giới tính **Nữ** và **Nam**.\n\n- Số lượng học sinh **Nam** nhiều hơn số lượng học sinh **Nữ**.\n\n- Chứng tỏ các lớp học AI thu hút số lượng học sinh **Nam** đông đảo hơn.', icon = "✍️")
            elif cnt_1 < cnt_2:
                st.success(f'**Kết luận**:\n\n- Có hai giới tính **Nữ** và **Nam**.\n\n- Số lượng học sinh **Nữ** nhiều hơn số lượng học sinh **Nam**.\n\n- Chứng tỏ các lớp học AI thu hút số lượng học sinh **Nữ** đông đảo hơn.', icon = "✍️")
            elif cnt_1 == cnt_2:
                st.success(f'**Kết luận**:\n\n- Có hai giới tính **Nữ** và **Nam**.\n\n- Số lượng học sinh **Nam** bằng số lượng học sinh **Nữ**.\n\n- Chứng tỏ các lớp học AI thu hút số lượng học sinh **Nam** và **Nữ** đồng đều.', icon = "✍️")
        else:
            st.warning('**The DataFrame is empty !!!**', icon = "⚠️")
        
    with tab_B:
        if len(df) != 0:
            
            genre = st.radio("**Điểm từng thành phần**", ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "GPA"], horizontal = True)
            
            rank = []
            for i in df.index:
                c = df.loc[i, 'CLASS']
                if c[2:4] == 'CV':
                    rank.append('Văn')
                elif c[2:5] == 'CT1' or c[2:5] == 'CT2' or c[2:5] == 'CT3':
                    rank.append('Toán')
                elif c[2:4] == 'CL':
                    rank.append('Lý')
                elif c[2:4] == 'CH':
                    rank.append('Hóa')
                elif c[2:4] == 'CA':
                    rank.append('Anh')
                elif c[2:6] == 'CTIN':
                    rank.append('Tin')
                elif c[2:5] == 'CSD':
                    rank.append('Sử Địa')
                elif c[2:6] == 'CTRN':
                    rank.append('Trung Nhật')
                elif c[2:4] == 'TH' or c[2:4] == 'SN':
                    rank.append('TH / SN')
                elif c[2] == 'A' or c[2] == 'B':
                    rank.append('Khác')
                    
            df['CLASS-GROUP'] = rank
            
            for i in range(9):
                if genre == f'S{i + 1}':
                    fig = px.box(df, x = 'PYTHON-CLASS', y = f'S{i + 1}', color = 'GENDER', title = f'BIỂU ĐỒ BIỂU DIỄN SỰ SO SÁNH ĐIỂM SESSION {i + 1} GIỮA CÁC BUỔI HỌC')
                    fig.update_layout(title_x=0.1, title_y=0.9)
                    st.plotly_chart(fig)

                    fig1 = px.box(df, x = 'CLASS-GROUP', y = f'S{i + 1}', title = f'BIỂU ĐỒ BIỂU ĐIỄN SỰ SO SÁNH ĐIỂM SESSION {i + 1} GIỮA CÁC HỌC SINH TRONG LỚP')
                    fig1.update_layout(title_x=0.1, title_y=0.9)
                    st.plotly_chart(fig1)
                    
            if genre == 'GPA':
                fig = px.box(df, x = 'PYTHON-CLASS', y = 'GPA', color = 'GENDER', title = 'BIỂU ĐỒ BIỂU DIỄN SỰ SO SÁNH ĐIỂM GPA GIỮA CÁC BUỔI HỌC')
                fig.update_layout(title_x=0.1, title_y=0.9)
                st.plotly_chart(fig)

                fig1 = px.box(df, x = 'CLASS-GROUP', y = 'GPA', title = 'BIỂU ĐỒ BIỂU ĐIỄN SỰ SO SÁNH ĐIỂM GPA GIỮA CÁC HỌC SINH TRONG LỚP')
                fig1.update_layout(title_x=0.1, title_y=0.9)
                st.plotly_chart(fig1)                

        else:
            st.warning('**The DataFrame is empty !!!**', icon = "⚠️")