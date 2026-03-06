import requests
import base64

URL = "http://mercury.picoctf.net:56136/"

def flip(byte_value, bit_pos):
    return byte_value ^ (1 << bit_pos)

def generate_cookies(original_cookie: str):
    cookie = base64.b64decode(base64.b64decode(original_cookie))
    cookies = []
    for c in range(len(cookie)):
        for bit in range(8):
            f = flip(cookie[c], bit).to_bytes(1)
            new = cookie[:c] + f + cookie[c+1:]
            cookies.append(base64.b64encode(base64.b64encode(new)).decode())

    return cookies

def bit_flip_attack():
    original_cookie = requests.get(URL, allow_redirects=False).cookies['auth_name']
    cookies = generate_cookies(original_cookie)

    for cookie in cookies:
        response = requests.get(URL,
        cookies={ "auth_name": cookie })

        print(response)
        if 'Cannot decode cookie.' not in response.text:
            print(response.content)
            print(cookie)
            break

bit_flip_attack()