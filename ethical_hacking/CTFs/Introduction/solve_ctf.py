import requests

#url = "http://cyberchallenge.disi.unitn.it:7900/api/get"
#url = "http://cyberchallenge.disi.unitn.it:7900/api/head_request_123"
#url = "http://cyberchallenge.disi.unitn.it:7900/api/post_456_request"
#url = "http://cyberchallenge.disi.unitn.it:7900/api/cookie"
#url = "http://cyberchallenge.disi.unitn.it:7900/api/query"
url = "http://cyberchallenge.disi.unitn.it:7900/api/header_78_9"


# Fai la richiesta POST
response = requests.get(url, headers={"X-Secret": "this_is_the_secret_header"})

# Stampa la risposta
print("Status Code:", response.status_code)
print("Response Content:", response.text)