This section should describe the summary of security problems identified for the scenario and explain which security controls you propose to mitigate these problems. This should be the summary of your analysis.

Proposta non per gruppi:

- Attacks to API for other info -> more checks/ authentication
    
- Attacks to communication channels -> authentication, encryption
    
- Attacks to protocols -> non so come risolvere ma sono tantini
    
- Attacks to the UTM system  

Provare ad ampliare la lista e dettagliare

Su gli asset gira e rigira gli attacchi sono gli stessi per categoria

Non tenerla per punti

---

This section summarizes the main security risks identified in the drone traffic management scenario and outlines the proposed security controls to mitigate them.

### 🌐 **1. Rete e connettività** v

Asset che permettono il collegamento tra i vari nodi del sistema.
- **Network switches**
- **Network routers**
- **Firewall**
- **Communication protocols (e.g. WiFi)**
- **RF transceiver models**
### 🔌 **2. Infrastruttura fisica e di alimentazione** V
Componenti che garantiscono l’alimentazione elettrica e la resilienza fisica del sistema.
- **Electrical infrastructure**
- **UPS (Uninterruptible Power Supply)**
- **Backup generators**
- **UAV hardware**
- **Antennas**
### ☁️ **3. Interfacce esterne e fonti dati** V
 Asset che forniscono dati da fonti esterne o li scambiano con enti terzi.
- **External weather API**
- **External GPS API**
- **APIs for real-time traffic feeds (from aviation authorities)** 
- **Regulatory databases**
	- Data loss or corruption
		- signature checks + redundant data source
	- Man-in-the-middle (MITM) 
		- difesa: 
			- secure protocol usage 
### 🔒 **4. Sicurezza, autenticazione e crittografia** V
Asset responsabili della protezione del sistema attraverso autenticazione, cifratura e gestione delle identità.
- **Identity and access management systems**
- **Public key infrastructure (PKI)**
- **Encryption libraries (e.g., AES, TLS)**
- **SecurCommunication protocols (e.g. WiFi)e communication protocols (SSL/TLS, IPsec)**
### 🧠 **5. Elaborazione, calcolo e logica interna**
Asset coinvolti nell’elaborazione locale (sia lato UAV sia lato UTM) e nella logica operativa.
- **UAVs internal processors**
- **Onboard safety logic (microcontroller or flight controller)**
- **Emergency handling UAV software**
- **Software libraries for path planning**
- **Navigation software stack**
- **Data analysis 

---



