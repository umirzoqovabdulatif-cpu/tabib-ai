import streamlit as st
from streamlit_chat import message

# Sahifa sozlamalari (Tabib AI brendi)
st.set_page_config(
    page_title="Tabib AI — Sizning Raqamli Salomatlik Yordamchingiz",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (Interfeys dizayni) ---
st.markdown("""
<style>
    .stApp {
        background-color: #f0f4f8;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    h1, h2, h3, h4 {
        color: #0d47a1;
    }

    .stColumn {
        background-color: white;
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.04);
        border: 1px solid #e1e8ed;
    }

    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 1px solid #c8d6e5;
    }

    .medicine-card {
        border: 1px solid #e1e8ed;
        border-radius: 12px;
        padding: 12px;
        background-color: white;
        text-align: center;
        margin-bottom: 15px;
        transition: transform 0.2s;
    }
    .medicine-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border-color: #1e88e5;
    }
    .medicine-card img {
        border-radius: 8px;
        margin-bottom: 8px;
    }
    .medicine-price {
        font-weight: bold;
        color: #2e7d32;
        font-size: 1.05em;
    }

    .doctor-card {
        background-color: #f4f8fb;
        border-radius: 8px;
        padding: 10px;
        margin-top: 8px;
        border-left: 4px solid #1e88e5;
    }

    .nasiya-block {
        background-color: #ff9800;
        color: white;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        margin-top: 12px;
        font-weight: bold;
    }

</style>
""", unsafe_allow_html=True)

# --- Sarlavha ---
col_head1, col_head2 = st.columns([0.08, 0.92])
with col_head1:
    st.image("https://cdn-icons-png.flaticon.com/512/387/387561.png", width=55)
with col_head2:
    st.title("Tabib AI")
    st.write("Shifokorlar, Aptekalar va Bemorlarni birlashtiruvchi milliy platforma")

# --- Sahifani ikki ustunga bo'lish ---
col1, col2 = st.columns([1.2, 1], gap="large")

# ==========================================
# --- Chap Ustun (AI Diagnostika va Navigatsiya) ---
# ==========================================
with col1:
    st.markdown("<h2>🤖 Tabib AI Yordamchisi</h2>", unsafe_allow_html=True)
    
    st.text_input("", placeholder="🔍 Kasallik, shifokor yoki dori qidirish...", key="global_search")
    
    st.markdown("---")
    st.subheader("Bemor va AI Muloqoti")
    
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    
    chat_container = st.container()
    
    with chat_container:
        if not st.session_state['messages']:
            message("Salom! Men Tabib AI diagnostikaman. Qayeringiz og'riyapti? Shikoyatingizni aytsangiz, sizga to'g'ri shifokor va dorini topishga yordam beraman.", is_user=False, logo="https://cdn-icons-png.flaticon.com/512/387/387561.png")

        for i, (msg, is_user) in enumerate(st.session_state['messages']):
            if is_user:
                message(msg, is_user=True, key=f"msg_u_{i}")
            else:
                message(msg, is_user=False, key=f"msg_a_{i}", logo="https://cdn-icons-png.flaticon.com/512/387/387561.png", allow_html=True)

    with st.form("problem_form", clear_on_submit=True):
        problem_input = st.text_input("💬 Shikoyatingizni yozing...", placeholder="Masalan: Mening belim og'riyapti...")
        submit_button = st.form_submit_button("Yuborish")
        
        if submit_button and problem_input:
            st.session_state['messages'].append((problem_input, True))
            
            ai_reply = ""
            if "bel" in problem_input.lower():
                ai_reply = f"""
Beligiz qancha vaqtdan buyon ogriyapti? 

Men sizga <b>Jizzax vil Gallaorol tumani</b> Bolgoli kuchasidagi DOKTOR ALI yoki... Doktor FIRDAVS (5 yulduz) tavsiya beraman.

<div class="doctor-card">
  <b>⭐ Doktor Ali (Nevropatolog)</b><br>
  Lokatsiya: Bo'lg'oli ko'chasi 📍<br>
  Reyting: ⭐⭐⭐⭐⭐ (120 sharh)
</div>
<div class="doctor-card">
  <b>⭐ Doktor Firdavs (Travmatolog)</b><br>
  Lokatsiya: Yaqin atrofdagi shifoxona 📍<br>
  Reyting: ⭐⭐⭐⭐⭐ (98 sharh)
</div>

<div class="nasiya-block">
  💳 Tabib AI Nasiya:<br>
  Mablag'ingiz yetarli bo'lmasa, hozir tekinga oling — pulingiz bo'lganda bo'lib to'laysiz!
</div>
                """
            elif "bosh" in problem_input.lower():
                ai_reply = f"""
Bosh og'rig'i bo'yicha sizga eng yaqin tor mutaxassis: Doktor Barno Yusupovani tavsiya qilaman.

<div class="doctor-card">
  <b>⭐ Barno Yusupova (Nevropatolog)</b><br>
  Lokatsiya: Mintaqaviy tibbiyot markazi 📍<br>
  Reyting: ⭐⭐⭐⭐☆ (85 sharh)
</div>

<div class="nasiya-block">
  💳 Tabib AI Nasiya:<br>
  Kerakli dori va muolajalarni bo'lib to'lashga xarid qiling!
</div>
                """
            else:
                ai_reply = "Salom! Men Tabib AI diagnostikaman. Kasallingizni aytsangiz, sizga to'g'ri shifokor va dorilarni tavsiya qilaman."

            st.session_state['messages'].append((ai_reply, False))
            st.rerun()


# ==========================================
# --- O'ng Ustun (Dorilar Bo'limi) ---
# ==========================================
with col2:
    st.markdown("<h2>💊 Dorilar Bo'limi</h2>", unsafe_allow_html=True)
    st.text_input("", value="sitramon", placeholder="🔍 Dori qidirish...", key="medicine_search")

    dorilar = [
        {"nom": "Tsitramon P", "narx": "9.999 so'm", "rasm": "https://images.apteka.uz/products/TsITRAMON_P_N10_TAB_1_2.jpg"},
        {"nom": "Nurofen Ultra", "narx": "54.000 so'm", "rasm": "https://pharma.uz/upload/iblock/24d/f0e69eb74b3a6ff4176b6d274438139a.jpg"},
        {"nom": "Paratsetamol", "narx": "4.000 so'm", "rasm": "https://pharma.uz/upload/iblock/2b9/1c28f096_db5d_11ea_ae10_00155d01240c_06a4b2a8_16c8_11eb_ae1c_00155d01240c.jpg"},
        {"nom": "Vitrum C Plus", "narx": "99.999 so'm", "rasm": "https://images.apteka.uz/products/VITRUM_C_VITAMIN_PLUS_TSh_500MG_N60_1_2.jpg"},
        {"nom": "Aspirin Kardio", "narx": "15.000 so'm", "rasm": "https://images.apteka.uz/products/ASPIRIN_KARDIO_100MG_N28_1_2.jpg"},
        {"nom": "Ketanov", "narx": "12.500 so'm", "rasm": "https://images.apteka.uz/products/KETANOV_10MG_N20_TAB_1_2.jpg"},
    ]

    dori_cols = st.columns(3, gap="small")
    for i, dori in enumerate(dorilar):
        with dori_cols[i % 3]:
            st.markdown(f"""
            <div class="medicine-card">
                <img src="{dori['rasm']}" width="100" height="100">
                <h4 style="font-size:14px; margin:5px 0;">{dori['nom']}</h4>
                <p class="medicine-price">{dori['narx']}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Nasiyaga Olish 💳", key=f"buy_{i}", use_container_width=True):
                st.success(f"{dori['nom']} savatchaga qo'shildi!")

# ==========================================
# --- Pastki Navigatsiya Menyusi ---
# ==========================================
st.markdown("---")
menu_cols = st.columns(4, gap="small")
menu_items = [
    ("🏠 Bosh Sahifa"),
    ("➕ Shifokorlar"),
    ("💊 Dorilar"),
    ("👤 Profil")
]

for col, item in zip(menu_cols, menu_items):
    with col:
        if st.button(item, use_container_width=True, key=f"nav_{item}"):
            st.toast(f"{item} bo'limi")
