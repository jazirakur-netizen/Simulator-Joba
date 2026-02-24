import streamlit as st

# 1. Ойынның күйін (сахнасын) сақтау
if 'scene' not in st.session_state:
    st.session_state.scene = 'start'

# 2. Персонаждардың суреттеріне сілтеме (Осы жерге өз суреттеріңіздің сілтемесін қойыңыз)
# Мысалы: GitHub-қа жүктелген суреттер немесе интернеттегі сілтемелер
char_happy = "https://raw.githubusercontent.com/your-repo/happy_apple.png"
char_sad = "https://raw.githubusercontent.com/your-repo/sad_apple.png"
char_thinking = "https://raw.githubusercontent.com/your-repo/thinking_apple.png"

st.title("🍏 OBAL PRO: Эко-приключение")

# 3. Ойын логикасы (Сахналар)
if st.session_state.scene == 'start':
    st.image(char_thinking, width=300)
    st.write("### Эко-Көмекші: Сәлем! Менің атым — Алмабек. Біз бүгін Түркібастағы алмаларды құтқаруымыз керек. Дайынсың ба?")
    if st.button("Иә, бастайық!"):
        st.session_state.scene = 'question_1'
        st.rerun()

elif st.session_state.scene == 'question_1':
    st.image(char_thinking, width=300)
    st.write("### 1-сұрақ: Біздің зауытта 1000 кг алмадан 600 литр шырын шықты. Қалған 400 кг қалдықты не істейміз?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Қоқысқа тастаймыз 🗑️"):
            st.session_state.scene = 'wrong_answer'
            st.rerun()
    with col2:
        if st.button("Пектин аламыз 🧪"):
            st.session_state.scene = 'correct_answer'
            st.rerun()

elif st.session_state.scene == 'correct_answer':
    st.image(char_happy, width=300)
    st.success("### Керемет! Сен нағыз Эко-инженерсің! Пектин — өте бағалы өнім. Біз 'Обалдың' алдын алдық!")
    if st.button("Келесі деңгей"):
        st.session_state.scene = 'start' # Немесе келесі сұрақ
        st.rerun()

elif st.session_state.scene == 'wrong_answer':
    st.image(char_sad, width=300)
    st.error("### Ой... Бұл - ОБАЛ болды. Қалдықтарды тастау - үлкен шығын әрі экологияға зиян. Қайтадан көрейікші?")
    if st.button("Қайталау"):
        st.session_state.scene = 'question_1'
        st.rerun()
