### **1. Multimedia Forensics & Tampering**

1. Che cosa si intende per **tampering detection** e in cosa si differenzia dalla **source identification**? Quali sono i due compiti principali (detection e localization)?
    - La tampering detection è un insieme di tecniche per capire se un media è stato alterato dopo l'acquisizione, si divide in 
	    - Forgery detection, binary decision if a media is real or synthetic
	    - Forgery Localization, heat-map production that show where the media is compromise 
	- the source identification instead aims to determine the origin of a media, and is on 3 level, devices class, brand/model and even individual devices

---

### **2. Tracce forensi: panoramica**

2. Classifica le tecniche di tampering detection in base al **livello di traccia** (pixel-level, fisico/geometrico, formato, semantico) e fai **almeno un esempio** per ciascun livello.
	1. Pixel level traces
		- based on local parameters of pixels and pipeline fingerprints
			- CFA
			- PRNU
			- median filtering
	2. physics and geometrical traces 
		- based on the physics of the scene 
			- shadows
			- light direction
			- Perspective geometry
	3. format based traces
		- JPEG compression
		- double or triple JPEG compression
	4. semantic level
		- coherence between location, date and content
    

---

### **3. CFA e Pixel-level traces**

3. Spiega perché il **Color Filter Array (CFA)** introduce **correlazioni periodiche** tra pixel e come queste possono essere sfruttate per **rilevare uno splicing**.
	- the CFA is a matrix on the sensor that, for every pixels, capture one of the three RGB value, the periodic pattern is needed for the interpolation part, in which every pixel get the missing values from the adjacent pixels. the most famous pattern is the Bayer one, in which in a 2 by 2 square there are 2 green, 1 red, 1 blue, this because the human eyes see much more tonality of green than the other two color.
	- if the periodic pattern went missing on some part of the media, its a trace of some manipulation of the media, and the CFA can be useful also for the Forgery individuation part, because the spot in which the periodic pattern is broken is the manipulated one.

4. Perché una regione manipolata può mostrare **assenza o incoerenza delle tracce CFA** rispetto al resto dell’immagine?
	- i think i already answer this question on the question before 
	- i think also that is important to specify that different models use different interpolation algorithms, and so its easy to spot some incoherence between the correlation of the pixels 
    

---

### **4. Filtraggi**

5. Perché operazioni come **filtro mediano** o **filtri morfologici** lasciano tracce rilevabili a livello forense? In che contesto vengono spesso utilizzati dai falsificatori?
	- Median filtering suppresses outliers and modifies fine textures and edges.
	- Morphological filters create unnaturally uniform or blocky structures.
	- they are often used by forgers to clean splicing boundaries and mask editing artifacts 
	- These operations leave detectable statistical signatures.

---

### **5. Illuminazione e ombre**

6. Qual è il **principio geometrico** alla base dell’analisi delle ombre nella tampering detection? Perché le rette ombra–oggetto devono intersecarsi nello stesso punto?
	- The physical principle is that **light travels in straight lines**. Therefore:
		- A point on an object,
		- The corresponding point on its shadow,
		- And the light source
	- are all cllinear
	- in the image plane, the projections of these lines should intersect at a single point corresponding to the 2D projection of the light source
	- inconsistent intersections indicate possible manipulation
    
7. Perché l’essere umano è **poco affidabile** nel valutare incoerenze di illuminazione e ombre? Collega la risposta al paper sul **caso Oswald**.
	- the lecture emphasizes that humans are poor at  judging lighting and shadow consistency, as confermed by perceptual studies
	- in the **Oswald case**, observers believed shadows indicated multiple light sources. However, this conclusion was based on perception alone. A proper geometric and physical analysis showed that the shadows were actually consistent with a single light source 
    

---

### **6. Caso di studio – Oswald**

8. Riassumi l’approccio usato nel paper di **Farid sul caso Oswald** per verificare l’autenticità della fotografia. Perché le ombre, apparentemente incoerenti, risultano invece fisicamente plausibili?
	- Farid’s approach:
		1. Build a **3D head model** of Oswald from mugshots (FaceGen).
		2. Combine it with a generic articulated body.
		3. Model the scene geometry (ground, fence, post).
		4. Adjust camera and **single distant light source (sun)**.
		5. Compare rendered shadows with the photograph.
	- Result:
		- Facial shadows and ground shadows match accurately.
		- Shadows that appear suspicious perceptually are physically consistent.
		
	- Conclusion: the photo shows **no evidence of tampering**; perceptual judgment is misleading.
---

### **7. Tecniche geometriche**

9. Spiega il modello di **proiezione prospettica** di una camera e distingui tra **parametri intrinseci** ed **estrinseci**.
	- The camera model includes:
		- **Intrinsic parameters (K)**: focal length, aspect ratio, skew, principal point.
		- **Extrinsic parameters (R, t)**: rotation and translation of the camera in the world.
	- Typically, modern cameras assume square pixels and zero skew, simplifying the intrinsic matrix.
	
10. Che cos’è un’**omografia** e in quale caso particolare della proiezione prospettica viene utilizzata?
    - A **homography** is a 3×3 projective transformation that maps:
		- Points lying on a **planar surface** in 3D
		- To their 2D image projections

	- It is a special case of perspective projection when all world points are coplanar (e.g., signs, billboards, facades).

---

### **8. Photo compositing**

11. Come può il **photo compositing** alterare i parametri intrinseci stimati di una camera? Spiega il ruolo del **punto principale** nel rilevare un’immagine composita.
    

---

### **9. Manipolazione del testo**

12. Perché il testo inserito su **cartelli o billboard** è difficile da falsificare in modo geometricamente corretto? Qual è l’idea chiave del metodo basato sulla **rettificazione tramite omografia**?
    
13. Come viene utilizzato l’**errore di ricostruzione (RMS)** per distinguere testo autentico da testo manipolato? Cosa rappresenta una soglia come **E = 1.5**?
    

---

### **10. JPEG e compressione**

14. Descrivi il processo di **quantizzazione JPEG** dei coefficienti DCT e spiega perché questa fase è la principale fonte di perdita di informazione.
    
15. Spiega il fenomeno della **double quantization**:
    

- perché compaiono **zeri periodici negli istogrammi**
    
- e perché il caso “prima compressione più forte, seconda più debole” è più facile da rilevare.
    
---

- Median and morphological filtering 