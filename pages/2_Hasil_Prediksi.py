import streamlit as st
import base64
import os


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def format_miliar(angka):
    miliar = angka / 1_000_000_000
    return f"{miliar:.2f}".replace(".", ",") + " miliar rupiah"


def format_rupiah(angka):
    return f"Rp {angka:,.0f}"


def kategori_rumah(luas_bangunan):
    if luas_bangunan < 60:
        return "kecil"
    elif luas_bangunan < 120:
        return "sedang"
    return "besar"


def slug_kota(kota):
    return kota.lower().replace(" ", "_")


def pilih_gambar_rumah(data):
    kota = data["Kota"]
    luas_bangunan = data["Luas Bangunan"]

    ukuran = kategori_rumah(luas_bangunan)
    nama_kota = slug_kota(kota)

    path_utama = f"assets/{nama_kota}_{ukuran}.jpg"
    fallback_1 = f"assets/default_{ukuran}.jpg"
    fallback_2 = "assets/default.jpg"
    fallback_3 = "assets/rumah.jpg"

    if os.path.exists(path_utama):
        return path_utama, ukuran
    if os.path.exists(fallback_1):
        return fallback_1, ukuran
    if os.path.exists(fallback_2):
        return fallback_2, ukuran
    if os.path.exists(fallback_3):
        return fallback_3, ukuran

    return None, ukuran


img = get_base64_image("assets/rumah.jpg")

st.set_page_config(
    page_title="Hasil Prediksi",
    layout="centered",
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

.block-container {{
    max-width: 980px;
    padding-top: 2rem;
    padding-bottom: 3.2rem;
}}

header[data-testid="stHeader"] {{
    background: transparent;
}}

#MainMenu, footer {{
    visibility: hidden;
}}

h1 {{
    text-align: center;
    margin-bottom: 1.7rem !important;
    color: #1f2c24;
    letter-spacing: -0.03em;
    font-weight: 800 !important;
    font-size: 3rem !important;
}}

.section-title {{
    font-size: 1.35rem;
    font-weight: 800;
    margin-top: 0.6rem;
    margin-bottom: 0.9rem;
    color: #223127;
    letter-spacing: -0.01em;
}}

.card {{
    background: rgba(248, 250, 248, 0.92);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 38px 28px;
    border-radius: 24px;
    text-align: center;
    box-shadow:
        0 18px 42px rgba(49, 66, 53, 0.12),
        inset 0 1px 0 rgba(255,255,255,0.35);
    border: 1px solid rgba(176, 190, 179, 0.55);
    margin-bottom: 28px;
}}

.price-main {{
    font-size: 3rem;
    font-weight: 800;
    color: #1f2c24;
    letter-spacing: -0.03em;
    margin-bottom: 6px;
}}

.price-sub {{
    font-size: 1rem;
    color: #5f7064;
    font-weight: 600;
}}

.stImage {{
    background: transparent !important;
    margin-top: -2px !important;
}}

.stImage > div {{
    background: transparent !important;
    padding: 0 !important;
}}

img {{
    border-radius: 18px !important;
}}

[data-testid="stImageCaption"] {{
    text-align: center !important;
    color: #6b7b70 !important;
    font-size: 0.96rem !important;
    margin-top: 10px !important;
    font-weight: 500 !important;
}}

.spec-card {{
    background: rgba(248, 250, 248, 0.90);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 18px 18px;
    border-radius: 24px;
    box-shadow:
        0 16px 36px rgba(44, 62, 47, 0.12),
        inset 0 1px 0 rgba(255,255,255,0.42);
    border: 1px solid rgba(170, 184, 173, 0.55);
    margin-top: 6px;
}}

.spec-row {{
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    gap: 20px;
    padding: 18px 20px;
    margin-bottom: 12px;
    border-radius: 16px;
    background: linear-gradient(145deg, rgba(251,252,251,0.98), rgba(232,238,233,0.92));
    border: 1px solid rgba(180, 194, 183, 0.65);
    box-shadow:
        8px 8px 18px rgba(161, 173, 164, 0.25),
        -6px -6px 14px rgba(255,255,255,0.72),
        inset 0 1px 0 rgba(255,255,255,0.75);
}}

.spec-row:last-child {{
    margin-bottom: 0;
}}

.spec-label {{
    color: #4f6255;
    font-size: 1.02rem;
    font-weight: 600;
    letter-spacing: 0.01em;
}}

.spec-value {{
    color: #1f2c24;
    font-size: 1.06rem;
    font-weight: 800;
    text-align: right;
}}

.back-wrap {{
    display: flex;
    justify-content: flex-start;
    margin-top: 22px;
}}

div.stButton > button {{
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.86rem 1.45rem !important;
    font-weight: 700 !important;
    box-shadow:
        0 14px 28px rgba(37,99,235,0.28),
        inset 0 1px 0 rgba(255,255,255,0.18) !important;
}}

div.stButton > button:hover {{
    background: linear-gradient(135deg, #1d4ed8, #1e40af) !important;
    box-shadow:
        0 18px 34px rgba(37,99,235,0.34),
        inset 0 1px 0 rgba(255,255,255,0.18) !important;
}}

div[data-testid="stVerticalBlock"] > div:empty {{
    display: none !important;
}}

hr {{
    display: none !important;
}}
</style>
""", unsafe_allow_html=True)

if "hasil_prediksi" not in st.session_state or "input_data" not in st.session_state:
    st.warning("Belum ada data prediksi.")
    if st.button("← Kembali"):
        st.switch_page("streamlit_app.py")
    st.stop()

pred = st.session_state["hasil_prediksi"]
data = st.session_state["input_data"]

harga_rp = pred * 1_000_000
gambar_rumah, ukuran_rumah = pilih_gambar_rumah(data)

st.title("Hasil Prediksi Harga Rumah")

st.markdown('<div class="section-title">Estimasi Harga</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="card">
    <div class="price-main">{format_rupiah(harga_rp)}</div>
    <div class="price-sub">({format_miliar(harga_rp)})</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Gambaran Model Rumah</div>', unsafe_allow_html=True)

if gambar_rumah:
    st.image(
        gambar_rumah,
        caption=f"Ilustrasi rumah {ukuran_rumah} di wilayah {data['Kota']}",
        use_container_width=True
    )
else:
    st.info("Gambar tidak ditemukan")

st.markdown('<div class="section-title">Spesifikasi Properti</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="spec-card">
    <div class="spec-row">
        <div class="spec-label">Kota</div>
        <div class="spec-value">{data['Kota']}</div>
    </div>
    <div class="spec-row">
        <div class="spec-label">Kamar Tidur</div>
        <div class="spec-value">{data['Kamar Tidur']}</div>
    </div>
    <div class="spec-row">
        <div class="spec-label">Kamar Mandi</div>
        <div class="spec-value">{data['Kamar Mandi']}</div>
    </div>
    <div class="spec-row">
        <div class="spec-label">Garasi</div>
        <div class="spec-value">{data['Garasi']}</div>
    </div>
    <div class="spec-row">
        <div class="spec-label">Luas Tanah</div>
        <div class="spec-value">{data['Luas Tanah']} m²</div>
    </div>
    <div class="spec-row">
        <div class="spec-label">Luas Bangunan</div>
        <div class="spec-value">{data['Luas Bangunan']} m²</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="back-wrap">', unsafe_allow_html=True)
if st.button("← Kembali ke Halaman Input"):
    st.switch_page("streamlit_app.py")
st.markdown('</div>', unsafe_allow_html=True)