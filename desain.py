import streamlit as st

st.set_page_config(page_title="Kerangka Web Prediksi Harga Rumah", layout="wide")

st.markdown("""
<style>
.stApp {
    background: #ffffff;
}

.block-container {
    max-width: 1400px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

.page-title {
    text-align: center;
    font-size: 28px;
    font-weight: 800;
    color: #1f2937;
    margin-bottom: 10px;
}

.page-subtitle {
    text-align: center;
    font-size: 15px;
    color: #4b5563;
    margin-bottom: 22px;
}

.col-wrap-left {
    padding-right: 28px;
}

.col-wrap-right {
    padding-left: 28px;
}

.box {
    border-radius: 16px;
    padding: 14px 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}

.box-title {
    font-size: 14px;
    font-weight: 700;
    color: rgba(0,0,0,0.58);
    margin-bottom: 10px;
}

.box-center {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: rgba(0,0,0,0.30);
    font-weight: 700;
    line-height: 1.4;
}

.input-box {
    background: #dbeafe;
    height: 330px;
}

.input-box .box-center {
    height: 270px;
    font-size: 22px;
}

.button-box {
    background: #bfdbfe;
    width: 42%;
    min-width: 220px;
    height: 95px;
}

.button-box .box-center {
    height: 48px;
    font-size: 20px;
}

.price-box {
    background: #fde68a;
    height: 135px;
}

.price-box .box-center {
    height: 78px;
    font-size: 24px;
}

.image-box {
    background: #fecaca;
    height: 110px;
}

.image-box .box-center {
    height: 54px;
    font-size: 20px;
}

.spec-box {
    background: #ddd6fe;
    height: 260px;
}

.spec-box .box-center {
    height: 205px;
    font-size: 24px;
}

.caption {
    text-align: center;
    margin-top: 14px;
    font-size: 15px;
    font-weight: 700;
    color: #374151;
}
</style>
""", unsafe_allow_html=True)

left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown('<div class="col-wrap-left">', unsafe_allow_html=True)

    st.markdown('<div class="page-title">Halaman Input Prediksi Harga Rumah</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Bagian untuk memasukkan spesifikasi properti</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="box input-box">
        <div class="box-title">Form Input</div>
        <div class="box-center">Input Spesifikasi Rumah</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="box button-box">
        <div class="box-title">Aksi</div>
        <div class="box-center">Tombol Prediksi</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="col-wrap-right">', unsafe_allow_html=True)

    st.markdown('<div class="page-title">Halaman Hasil Prediksi Harga Rumah</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Bagian untuk menampilkan hasil estimasi dan detail properti</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="box price-box">
        <div class="box-title">Hasil Estimasi</div>
        <div class="box-center">Estimasi Harga</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="box image-box">
        <div class="box-title">Visualisasi</div>
        <div class="box-center">Gambaran Model Rumah</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="box spec-box">
        <div class="box-title">Ringkasan Properti</div>
        <div class="box-center">Spesifikasi Properti</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="caption">Gambar. Kerangka Antarmuka Web Prediksi Harga Rumah</div>',
    unsafe_allow_html=True
)