- Network routers \[A] \[B] \[C] \[D]
	- Man-In-The-Middle --> Weak authentication mechanisms
	- Unauthorized access --> Weak password or default credentials
	- DoS --> No rate limit or other DoS protections
- Firewall \[A] \[B] \[C] \[D]
	- Unauthorized Access --> Weak authentication, default credentials
	- Exploit misconfiguration --> Human error, poor logging
	- RCE in firewall's OS --> Bugs in firewalls software
- Communication protocols (e.g. WiFi) \[A] \[B] \[C] \[D]
	- Protocol bug exploitation --> Bugs in the protocol (e.g. possibility of buffer overflow)
	- Sniffing --> Lack or weak encryption
- Servers \[A] \[B] \[C] \[D]
	- Unauthorized Access --> Lack of proper authentication mechanism, e.g. weak credentials
	- Insiders threats --> intentional or unintentional misuse of the service
	- Malware infection --> Lack of anitvirus
- RF transceiver models  \[A] \[C] \[D]
	- Over the air update attacks --> No authetentication or verification on updates



- Onboard safety logic (microcontroller or flight controller) \[B] \[C]
	- Insecure failsafe activation --> Poor validation of command source or signal integrity
- Emergency handling UAV software \[B] \[C]
	- Unauthorized activation --> Weak authentication for emergency commands   
- Public key infrastructure (PKI) \[A] \[B] \[D]
	- Fake certificates issued --> Compromised CA private key
- Encryption libraries (e.g., AES, TLS) \[A] \[D]
	- Incorrect API usage --> Poor documentation or lack of misuse resistance
- Secure communication protocols (SSL/TLS, IPsec) \[A] \[D]
	- Brute-force login --> Weak passwords; no rate limiting or 2FA





- Navigation software stack \[B]
	- Command or data injection --> Lack of input sanitization
- Identity and access management systems \[A]
	- Password guessing or credential stuffing --> Poor password policies, no MFA
- Monitoring software \[B]
	- Buffer overflow --> Input validation errors

