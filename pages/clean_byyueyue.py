import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# --- Page Config ---
st.set_page_config(layout='wide', page_title='Cat Clean App 🐱', page_icon='🐱')

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    .main { background-color: #fff5f8; }
    h1 { color: #d33682; }
    .stButton>button { background-color: #ff69b4; color: white; border-radius: 20px; }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.title("🐱 Meow Data Cleaning Workshop")
st.markdown("### ยินดีต้อนรับสู่แอปทำความสะอาดข้อมูลสุดน่ารัก 🐾")

# --- File Uploader ---
uploaded_file = st.file_uploader("อัปโหลดไฟล์ CSV ของคุณที่นี่ (เมี๊ยว~)", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("อัปโหลดไฟล์สำเร็จแล้วนะเมี๊ยว! 🐾")

    # Sidebar Tools
    st.sidebar.header("🐾 เมนูจัดการข้อมูล")
    if st.sidebar.button("ทำความสะอาดข้อมูลทันที!"):
        # 1. Handle Duplicates
        df = df.drop_duplicates()
        
        # 2. Inconsistent Data (Basic Standardize)
        if 'Region' in df.columns:
            df['Region'] = df['Region'].str.strip().str.upper()
        
        # 3. Missing Data
        df = df.fillna(df.median(numeric_only=True))

        st.balloons()
        st.write("### ✅ ข้อมูลที่ทำความสะอาดเสร็จแล้ว (Cleaned Data)")
        st.dataframe(df.style.highlight_max(axis=0, color='#ffc0cb'))

        # Summary
        col1, col2 = st.columns(2)
        col1.metric("จำนวนแถวทั้งหมด", f"{len(df)} แถว", "🐱")
        col2.metric("จำนวนคอลัมน์", len(df.columns))

        # Download Button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 ดาวน์โหลดไฟล์ที่สะอาดแล้ว (CSV)",
            data=csv,
            file_name='cat_cleaned_data.csv',
            mime='text/csv',
        )
    else:
        st.write("### 🐾 ข้อมูลต้นฉบับ (Raw Data)")
        st.dataframe(df.head(10))

else:
    st.info("กรุณาอัปโหลดไฟล์เพื่อเริ่มใช้งานนะเมี๊ยว~ 🐱")
