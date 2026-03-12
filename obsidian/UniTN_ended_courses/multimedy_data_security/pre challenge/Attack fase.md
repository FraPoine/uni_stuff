# PSNR and WPSNR
### PSNR (Peak Signal-to-Noise Ratio)
Il **Peak Signal-to-Noise Ratio** (Rapporto Segnale/Rumore di Picco) è la misura più comune e semplice per quantificare la qualità di ricostruzione di un'immagine o di un video soggetti a compressione con perdita (_lossy compression_).
- **Scopo:** Misura il rapporto tra la massima potenza possibile di un segnale e la potenza del "rumore di corruzione" (l'errore introdotto dalla compressione o dall'elaborazione).
- **Formula:** È definito in decibel (dB) ed è calcolato tramite l'**Errore Quadratico Medio (MSE)** tra l'immagine originale e quella ricostruita.

La formula fondamentale è:

$$\text{PSNR} = 10 \log_{10} \left( \frac{\text{MAX}_I^2}{\text{MSE}} \right)$$
Dove:
* $\text{MAX}_I$: Il massimo valore possibile di un pixel.
* $\text{MSE}$: L'Errore Quadratico Medio, calcolato come:
$$\text{MSE} = \frac{1}{M \cdot N} \sum_{i=1}^{M} \sum_{j=1}^{N} [I(i, j) - K(i, j)]^2$$

Dove $I$ è l'immagine originale e $K$ è quella ricostruita, di dimensioni $M \times N$.

***
### WPSNR (Weighted Peak Signal-to-Noise Ratio)
Il **Weighted Peak Signal-to-Noise Ratio** (Rapporto Segnale/Rumore di Picco Pesato) è un'evoluzione del PSNR che cerca di superare il suo limite includendo elementi di **percezione visiva umana**.
- **Scopo:** È una versione modificata del PSNR in cui l'errore tra i pixel non è trattato in modo uniforme, ma viene **pesato** in base alla sua importanza per l'occhio umano.
- **Come funziona:** A differenza del PSNR, che assegna lo stesso peso all'errore in qualsiasi pixel, il WPSNR introduce una **funzione di ponderazione** (_weighting function_). Questa funzione:
    - Assegna un **peso maggiore** agli errori nelle aree dell'immagine a cui l'occhio è più sensibile (ad esempio, aree uniformi o con dettagli fini).   
    - Assegna un **peso minore** agli errori nelle aree a cui l'occhio è meno sensibile (ad esempio, le alte frequenze o aree di forte contrasto, a causa del fenomeno di _mascheramento visivo)_.
- **Vantaggio:** Il WPSNR è generalmente considerato una metrica di qualità **migliore** rispetto al PSNR per le immagini, poiché le sue valutazioni sono spesso più in linea con il **giudizio soggettivo** di un osservatore umano.

Il WPSNR utilizza una versione pesata dell'MSE, lo **Weighted Mean Squared Error (WMSE)**, dove $W(i, j)$ è la funzione di ponderazione percettiva.

$$\text{WPSNR} = 10 \log_{10} \left( \frac{\text{MAX}_I^2}{\text{WMSE}} \right)$$

Dove:
$$\text{WMSE} = \frac{\sum_{i=1}^{M} \sum_{j=1}^{N} W(i, j) \cdot [I(i, j) - K(i, j)]^2}{\sum_{i=1}^{M} \sum_{j=1}^{N} W(i, j)}$$

In sintesi, mentre il **PSNR** è una misura puramente matematica dell'errore di ricostruzione, il **WPSNR** tenta di essere una misura **percettivamente più rilevante**.

---
# Legal attacks
| Attacco                                  | Funzionamento Principale                                                          | Effetto sul Watermark                                                                                                              |
| :--------------------------------------- | :-------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| **AWGN** (Additive White Gaussian Noise) | Aggiunge rumore casuale (disturbo statistico) all'immagine.                       | Il rumore si sovrappone ai dati del watermark, **rendendo difficile l'estrazione** per correlazione.                               |
| **Blurring** (Sfocatura)                 | Applica un filtro (es. Gaussiano) per uniformare i pixel vicini.                  | Rimuove le componenti ad alta frequenza, **smussando e diluendo** il pattern del watermark.                                        |
| **Sharpening** (Nitidezza)               | Aumenta il contrasto e i dettagli sui bordi.                                      | Distorce il pattern del watermark **amplificando i disturbi** e le modifiche locali introdotte.                                    |
| **JPEG Compression**                     | Compressione con perdita di dati basata su DCT (Trasformata Discreta del Coseno). | Elimina i coefficienti meno significativi, spesso usati per nascondere il watermark, **causando la perdita** di parte del segnale. |
| **Resizing** (Ridimensionamento)         | Cambia le dimensioni (ingrandimento o riduzione) dell'immagine.                   | Distrugge la **sincronizzazione geometrica** e la mappatura tra il watermark e la griglia dei pixel.                               |
| **Median Filtering**                     | Sostituisce i pixel con il valore mediano dell'area circostante.                  | Efficace nell'eliminare le deviazioni isolate, **smorzando il segnale** del watermark.                                             |

---
# AWGN
**AWGN** è l'acronimo di **Additive White Gaussian Noise** (Rumore Bianco Gaussiano Additivo). Descrive un processo casuale che aggiunge una distorsione a un segnale o un'immagine.

### 1. Additivo (Additive)
Significa che il rumore viene semplicemente **sommato** all'immagine originale.

### 2. Bianco (White)
Significa che la potenza spettrale del rumore è **uniformemente distribuita** su tutte le frequenze. In altre parole, non c'è una frequenza spaziale che sia disturbata più di altre. Questo è simile alla luce bianca, che contiene tutte le lunghezze d'onda (frequenze) in pari misura.

### 3. Gaussiano (Gaussian)
Significa che i valori del rumore seguono una **distribuzione normale** (o gaussiana, spesso chiamata "a campana"). Questa distribuzione è caratterizzata principalmente da:
- **Media (μ):** Spesso impostata a zero.
- **Varianza (σ2) o Deviazione Standard (σ):** Definisce l'intensità o la potenza del rumore. Un σ più alto significa un rumore più intenso e una maggiore distorsione visiva.