import streamlit as st

# 1. СЕССИЯ КҮЙІН БАСҚАРУ
if 'scene' not in st.session_state:
    st.session_state.scene = 'start'

# 2. СУРЕТ СІЛТЕМЕЛЕРІ (Түзетілген RAW сілтемелер)
char_happy = "https://raw.githubusercontent.com/jazirakur-netizen/Simulator-Joba/main/Gemini_Generated_Image_qf6dyfqf6dyfqf6d.png"
char_sad = "https://raw.githubusercontent.com/jazirakur-netizen/Simulator-Joba/main/Gemini_Generated_Image_3kb34w3kb34w3kb3.png"
char_thinking = "https://raw.githubusercontent.com/jazirakur-netizen/Simulator-Joba/main/Gemini_Generated_Image_2r8rs52r8rs52r8r.png"

st.title("🍏 OBAL PRO: Эко-инженер жолы")

# Тексерілген жоба мазмұны бойынша дайын сұрақ-жауап.
with st.expander("✦ Танымдық көмекші", expanded=False):
    st.caption("Дайын тақырыптық түсіндірмелер. Еркін сөйлесетін ЖИ чат емес. Ойындағы жауапты өзіңіз таңдаңыз.")
    _helper_answers = {
        "Алманы ысырапсыз пайдалану": "Алманы өңдеу кезінде қалған бөліктерін бірден қоқыс деп қарастырмаймыз. Оларды қайта өңдеу мүмкіндігін бағалау — жобаның негізгі бағыты. Нақты технологияны шикізат құрамы мен өндірістік жағдайға қарай тексеру қажет.",
        "Пектин туралы": "Ойында пектин алманы қайта өңдеуден алынатын өнім ретінде қарастырылады. Өнімнің қасиеті мен шығымы өңдеу тәсіліне байланысты. Технологиялық деректерді жобаның дереккөздерімен салыстырыңыз.",
        "Түсім мен таза пайда": "Түсім = сатылған өнім көлемі × бірлік бағасы. Таза пайда = жалпы түсім − барлық шығын. Түсім мен таза пайда бір көрсеткіш емес. Ойындағы есепті осы айырмашылықты ескеріп орындаңыз.",
        "Обал және ұқыптылық": "«Обал» ұғымы қолдағы игілікті қадірлеуге және ысырап жасамауға бағыттайды. Жобада ол ресурсты ұқыпты пайдалану және қалдықты азайту идеясымен байланыстырылған.",
        "Ойыннан қалай өтемін?": "Әр кезеңдегі сұрақты оқып, шешімнің табиғатқа және өндіріске ықпалын ойластырыңыз. Қателескенде қайта бастауға болады. Бұл көмекші дайын жауап кілтін бермейді.",
        "Модель нәтижесіне сене аламын ба?": "Оқу моделінің нәтижесі енгізілген болжамдарға тәуелді. Баға, өнім шығымы және шығындар өзгерсе, нәтиже де өзгереді. Оқу есебі нақты кәсіпорын табысына кепілдік бермейді."
    }
    _helper_topic = st.selectbox("Тақырыпты таңдаңыз", list(_helper_answers), key="alma_helper_topic")
    st.info(_helper_answers[_helper_topic])



# 3. ОЙЫН САХНАЛАРЫ
# --- БАСТАУ ---
if st.session_state.scene == 'start':
    st.image(char_thinking, width=400)
    st.write("### Бағбан: Сәлем! Түлкібас бақтарында алма пісті. Бірақ оны ысырапсыз өңдеу үшін бізге білім керек. Дайынсың ба?")
    if st.button("Әрине, бастаймыз!"):
        st.session_state.scene = 'q1'
        st.rerun()

# --- 1-СҰРАҚ: ЭКОЛОГИЯ ---
elif st.session_state.scene == 'q1':
    st.image(char_thinking, width=400)
    st.write("### 1-кезең: Алманы өңдеген соң 40% қалдық қалады. Оны не істейміз?")
    if st.button("Өртеп жібереміз"): st.session_state.scene = 'wrong'; st.rerun()
    if st.button("Қайта өңдеп, пайда табамыз"): st.session_state.scene = 'q2'; st.rerun()

# --- 2-СҰРАҚ: ХИМИЯ ---
elif st.session_state.scene == 'q2':
    st.image(char_happy, width=400)
    st.success("Дұрыс! Қалдықтан біз Пектин аламыз.")
    st.write("### 2-кезең: Пектин дегеніміз не?")
    if st.button("Табиғи сорбент және қоюлатқыш"): st.session_state.scene = 'q3'; st.rerun()
    if st.button("Жай ғана қант түрі"): st.session_state.scene = 'wrong'; st.rerun()

# --- 3-СҰРАҚ: ЭКОНОМИКА ---
elif st.session_state.scene == 'q3':
    st.image(char_happy, width=400)
    st.write("### 3-кезең: Егер 1 кг пектин 8000 тг болса, 5 кг пектин қанша табыс әкеледі?")
    if st.button("40 000 теңге"): st.session_state.scene = 'q4'; st.rerun()
    if st.button("20 000 теңге"): st.session_state.scene = 'wrong'; st.rerun()

# --- 4-СҰРАҚ: ТЕХНОЛОГИЯ (BRIX) ---
elif st.session_state.scene == 'q4':
    st.image(char_thinking, width=400)
    st.write("### 4-кезең: Алма шырынының сапасын (қант мөлшерін) немен өлшейміз?")
    if st.button("Термометрмен"): st.session_state.scene = 'wrong'; st.rerun()
    if st.button("Рефрактометрмен (Brix)"): st.session_state.scene = 'q5'; st.rerun()

# --- 5-СҰРАҚ: ОБАЛ ФИЛОСОФИЯСЫ ---
elif st.session_state.scene == 'q5':
    st.image(char_thinking, width=400)
    st.write("### 5-кезең: Жапондардың 'Моттайнай' философиясы біздің қай ұғымға ұқсас?")
    if st.button("Обал болады"): st.session_state.scene = 'q6'; st.rerun()
    if st.button("Береке"): st.session_state.scene = 'wrong'; st.rerun()

# --- 6-СҰРАҚ: ФИНАЛДЫҚ ШЕШІМ ---
elif st.session_state.scene == 'q6':
    st.image(char_happy, width=400)
    st.write("### 6-кезең: Соңғы сұрақ! OBAL PRO жобасының басты мақсаты не?")
    if st.button("Тек ақша табу"): st.session_state.scene = 'wrong'; st.rerun()
    if st.button("Қалдықсыз өндіріс және таза табиғат"): st.session_state.scene = 'win'; st.rerun()

# --- ЖЕҢІС ---
elif st.session_state.scene == 'win':
    st.image(char_happy, width=400)
    st.balloons()
    st.success("### ҚҰТТЫҚТАЙМЫН! Сен нағыз ЭКО-ИНЖЕНЕРСІҢ! 🏆")
    st.write("Сен барлық кезеңнен өтіп, Түлкібас алмаларын обал болудан құтқардың!")
    if st.button("Ойынды қайта бастау"):
        st.session_state.scene = 'start'
        st.rerun()

# --- ҚАТЕЛЕСУ ---
elif st.session_state.scene == 'wrong':
    st.image(char_sad, width=400)
    st.error("### Өкінішті... Бұл жолы ОБАЛ болды.")
    st.write("Қате шешім өндіріске зиян келтірді. Бағбан мұңайып қалды.")
    if st.button("Қайтадан көрейінші"):
        st.session_state.scene = 'start'
        st.rerun()
     
