import streamlit as st
import pandas as pd
import joblib
import base64
import gdown
from pathlib import Path


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


img = get_base64_image("assets/rumah.jpg")

st.set_page_config(
    page_title="Prediksi Harga Rumah",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(f"""
<style>
html, body, [class*="css"] {{
    font-family: "Segoe UI", "Inter", sans-serif;
}}

.stApp {{
    background:
        linear-gradient(rgba(241,245,242,0.80), rgba(241,245,242,0.80)),
        url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Lebarkan area utama supaya form tidak kecil di tengah layar */
section.main > div,
div[data-testid="stAppViewContainer"] .main .block-container,
.block-container {{
    max-width: 1380px !important;
    width: 88vw !important;
    margin: 0 auto !important;
    padding-top: 54px !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    padding-bottom: 40px !important;
}}

header[data-testid="stHeader"] {{
    background: transparent;
}}

#MainMenu, footer {{
    visibility: hidden;
}}

.hero-title {{
    text-align: center;
    font-size: 3.35rem;
    font-weight: 800;
    color: #1f2c24;
    letter-spacing: -0.03em;
    margin-bottom: 10px;
}}

.hero-subtitle {{
    text-align: center;
    font-size: 1.22rem;
    color: #35473b;
    margin-bottom: 34px;
    font-weight: 800;
}}

/* Perbesar kotak form/tabel */
div[data-testid="stVerticalBlockBorderWrapper"] {{
    background: rgba(231, 238, 232, 0.46) !important;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 26px !important;
    border: 1px solid rgba(179, 194, 183, 0.60) !important;
    box-shadow:
        0 22px 48px rgba(49, 66, 53, 0.12),
        inset 0 1px 0 rgba(255,255,255,0.32) !important;
    width: 100% !important;
    min-height: 410px !important;
    padding: 44px 56px 38px 56px !important;
}}

/* Tambahkan jarak antar kolom dan antar field agar form terasa penuh */
div[data-testid="stHorizontalBlock"] {{
    gap: 4.5rem !important;
}}

div[data-testid="column"] {{
    min-width: 0 !important;
}}

div[data-testid="stSelectbox"],
div[data-testid="stNumberInput"] {{
    width: 100% !important;
    margin-bottom: 24px !important;
}}

label, .stSelectbox label, .stNumberInput label {{
    color: #26382d !important;
    font-weight: 750 !important;
    font-size: 1.14rem !important;
    margin-bottom: 8px !important;
}}

/* Samakan ukuran dropdown Kota dengan semua input angka */
div[data-testid="stSelectbox"],
div[data-testid="stNumberInput"] {{
    width: 100% !important;
}}

div[data-testid="stSelectbox"] [data-baseweb="select"],
div[data-testid="stNumberInput"] [data-baseweb="input"] {{
    width: 100% !important;
}}

div[data-testid="stSelectbox"] [data-baseweb="select"] > div,
div[data-testid="stNumberInput"] [data-baseweb="input"],
div[data-testid="stNumberInput"] [data-baseweb="input"] > div {{
    background: rgba(245, 248, 245, 0.92) !important;
    border: 1px solid rgba(181, 194, 184, 0.90) !important;
    border-radius: 12px !important;
    min-height: 58px !important;
    height: 58px !important;
    box-shadow: 0 8px 20px rgba(49, 66, 53, 0.07) !important;
    display: flex !important;
    align-items: center !important;
}}

.stTextInput input,
.stNumberInput input,
div[data-testid="stNumberInput"] input {{
    min-height: 58px !important;
    height: 58px !important;
    color: #253228 !important;
    font-size: 1.08rem !important;
    font-weight: 550 !important;
    padding-left: 22px !important;
}}

div[data-testid="stSelectbox"] [data-baseweb="select"] span {{
    color: #253228 !important;
    font-size: 1.08rem !important;
    font-weight: 550 !important;
}}

div[data-testid="stNumberInput"] button {{
    height: 58px !important;
    min-height: 58px !important;
    min-width: 48px !important;
    font-size: 1.08rem !important;
}}

.stTextInput input:focus,
.stNumberInput input:focus,
[data-baseweb="input"]:focus-within,
[data-baseweb="select"] > div:focus-within {{
    border: 1px solid #6c8a73 !important;
    box-shadow: 0 0 0 2px rgba(108,138,115,0.16) !important;
}}

input::placeholder {{
    color: #7f9186 !important;
    opacity: 1 !important;
}}

/* Tombol dibuat lebih besar supaya proporsi halaman seimbang */
div.stButton {{
    display: flex;
    justify-content: flex-start;
    margin-top: 34px;
}}

div.stButton > button {{
    background: linear-gradient(135deg, #5f7d67, #4f6b56) !important;
    color: white !important;
    border: none !important;
    border-radius: 18px !important;
    min-height: 68px !important;
    min-width: 235px !important;
    padding: 1.12rem 3rem !important;
    font-size: 1.14rem !important;
    font-weight: 800 !important;
    box-shadow: 0 16px 30px rgba(79,107,86,0.28) !important;
    transition: all 0.25s ease !important;
}}

div.stButton > button:hover {{
    transform: translateY(-1px);
    box-shadow: 0 20px 36px rgba(79,107,86,0.32) !important;
    background: linear-gradient(135deg, #55715c, #435a49) !important;
}}

div[data-testid="stAlert"] {{
    background: rgba(250,235,228,0.88) !important;
    border: 1px solid rgba(210,154,132,0.35) !important;
    border-radius: 18px !important;
    padding: 18px 20px !important;
    margin-top: 18px !important;
}}

div[data-testid="stAlert"] p,
div[data-testid="stAlert"] span,
div[data-testid="stAlert"] div {{
    color: #8b4d3a !important;
    font-weight: 650 !important;
    font-size: 1.04rem !important;
}}

div[data-testid="stAlert"] svg {{
    display: none !important;
}}

/* Paksa tulisan pada dropdown Kota agar tetap hitam saat deploy */
div[data-testid="stSelectbox"] [data-baseweb="select"] *,
div[data-testid="stSelectbox"] [data-baseweb="select"] div,
div[data-testid="stSelectbox"] [data-baseweb="select"] input {{
    color: #253228 !important;
    -webkit-text-fill-color: #253228 !important;
    font-weight: 600 !important;
}}

div[data-testid="stSelectbox"] [data-baseweb="select"] input::placeholder {{
    color: #253228 !important;
    -webkit-text-fill-color: #253228 !important;
    opacity: 1 !important;
}}

div[data-testid="stSelectbox"] label {{
    color: #000000 !important;
}}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-title">Prediksi Harga Rumah</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Masukkan spesifikasi properti untuk estimasi harga</div>',
    unsafe_allow_html=True
)

MODEL_PATH = Path("model_terbaik_harga_rumah_rmse.pkl")
FILE_ID = "1q0HoJGAJapT2zzMe4ZAsQ7k0GcJI0ILV"

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        url = f"https://drive.google.com/uc?id={FILE_ID}"
        gdown.download(url, str(MODEL_PATH), quiet=False)

    return joblib.load(MODEL_PATH)

model = load_model()

daftar_kota = [
    "Jakarta Barat", "Jakarta Selatan", "Jakarta Timur",
    "Jakarta Utara", "Jakarta Pusat",
    "Bogor", "Depok", "Tangerang", "Bekasi"
]

with st.container(border=True):
    col1, col2 = st.columns(2, gap="large")

    with col1:
        kota = st.selectbox(
            "Kota",
            options=[None] + daftar_kota,
            format_func=lambda x: "Pilih kota" if x is None else x
        )

        kamar_tidur = st.number_input(
            "Kamar Tidur",
            min_value=1,
            step=1,
            value=None,
            placeholder="Masukkan jumlah kamar tidur"
        )

        kamar_mandi = st.number_input(
            "Kamar Mandi",
            min_value=1,
            step=1,
            value=None,
            placeholder="Masukkan jumlah kamar mandi"
        )

    with col2:
        garasi = st.number_input(
            "Garasi",
            min_value=0,
            step=1,
            value=None,
            placeholder="Masukkan jumlah garasi"
        )

        luas_tanah = st.number_input(
            "Luas Tanah (m²)",
            min_value=1,
            step=1,
            value=None,
            placeholder="Masukkan luas tanah"
        )

        luas_bangunan = st.number_input(
            "Luas Bangunan (m²)",
            min_value=1,
            step=1,
            value=None,
            placeholder="Masukkan luas bangunan"
        )

submit = st.button("Prediksi Harga", use_container_width=False)

if submit:
    if (
        kota is None or
        kamar_tidur is None or
        kamar_mandi is None or
        garasi is None or
        luas_tanah is None or
        luas_bangunan is None
    ):
        st.error("Tidak bisa melakukan prediksi. Silakan lengkapi semua input terlebih dahulu.")
    else:
        data = pd.DataFrame([{
            "Kota": kota,
            "Kamar Tidur": kamar_tidur,
            "Kamar Mandi": kamar_mandi,
            "Garasi": garasi,
            "Luas Tanah": luas_tanah,
            "Luas Bangunan": luas_bangunan
        }])

        pred = model.predict(data)[0]

        st.session_state["hasil_prediksi"] = pred
        st.session_state["input_data"] = data.iloc[0].to_dict()

        st.switch_page("pages/2_Hasil_Prediksi.py")