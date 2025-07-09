import streamlit as st
import os

# Tạo các cột nút và hiển thị
coll, col2, col3, col4, col5 = st.columns(5)
col6, col7 = st.columns([2, 1])

def play_audio(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as audio:
            st.audio(audio, format='audio/wav')
    else:
        st.error(f"Không tìm thấy file âm thanh: {file_path}")

def show_image(image_path, caption):
    if os.path.exists(image_path):
        st.image(image_path, caption=caption)
    else:
        st.error(f"Không tìm thấy hình ảnh: {image_path}")

with coll:
    b1 = st.button('Con mèo')
with col2:
    b2 = st.button('Con chó')
with col3:
    b3 = st.button('Con khỉ')
with col4:
    b4 = st.button('Đại bàng')
with col5:
    b5 = st.button('Con gà')

if b1:
    with col6:
        st.write('Âm thanh')
        play_audio('sound/cat.wav')

        st.write('Video')
        st.video('https://www.youtube.com/watch?v=W86cTIoMv2U')
    with col7:
        show_image('img/cat.jpg', 'Con mèo')

if b2:
    with col6:
        st.write('Âm thanh')
        play_audio('sound/dog.wav')

        st.write('Video')
        st.video('https://www.youtube.com/watch?v=zb9l63Nm9zU')
    with col7:
        show_image('img/dog.jpg', 'Con chó')

if b3:
    with col6:
        st.write('Âm thanh')
        play_audio('sound/monkey.wav')

        st.write('Video')
        st.video('https://www.youtube.com/watch?v=icd_ob8UWgQ')
    with col7:
        show_image('img/monkey.jpg', 'Con khỉ')

if b4:
    with col6:
        st.write('Âm thanh')
        play_audio('sound/eagle.wav')

        st.write('Video')
        st.video('https://www.youtube.com/watch?v=1ryv1u2yXCk')
    with col7:
        show_image('img/eagle.jpg', 'Đại bàng')

if b5:
    with col6:
        st.write('Âm thanh')
        play_audio('sound/chicken.wav')

        st.write('Video')
        st.video('https://youtu.be/SNSr8ti3Y4A')
    with col7:
        show_image('img/chicken.jpg', 'Con gà')
