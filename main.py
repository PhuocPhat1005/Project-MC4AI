import streamlit as st
import numpy as np

tab1, tab2, tab3, tab4 = st.tabs(["Danh sách", "Biểu đồ", "Phân nhóm", "Phân loại"])
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("Giới tính")
        choose1 = st.checkbox('Nam')
        choose2 = st.checkbox('Nữ')
    with col2:
        genre = st.radio("Khối lớp", ["Tất cả", "Lớp 10", "Lớp 11", "Lớp 12"])
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
    st.write("Số HS: ")
    st.write("GPA: cao nhất, thấp nhất, trung bình")
with tab2:
    tab_A, tab_B = st.tabs(["Số lượng HS", "Điểm"])
    
