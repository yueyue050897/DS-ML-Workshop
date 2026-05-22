import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.write("Yueyue")
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

st.markdown(''':rainbow[Jeerawadee Sungkasopon] ''')

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("💰 การทำความสะอาดข้อมูล"):
    st.switch_page("pages/clean_bytoon.py")
elif st.button("💰 แปลงข้อมูล"):
    st.switch_page("pages/clean_byyueyue.py")
elif st.button("💰 แปลงข้อมูลA"):
    st.switch_page("pages/clean_customers.py")
