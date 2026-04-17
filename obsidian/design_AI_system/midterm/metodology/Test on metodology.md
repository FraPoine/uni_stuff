Queste sono le mie risposte, mi riesci comuqnque a dare una micro spiegazione sulle risposte?
## Parte A
### 1 C
Il **test set** serve per la **valutazione finale del modello**.
- training → imparare
- validation → scegliere hyperparameters
- test → risultato finale
### 2 B
Il **validation set** serve per scegliere:
- modello migliore
- valore di k nel kNN
- profondità albero
- learning rate
- altri hyperparameters
### 3 C
Se guardi troppe volte il test set, inizi a fare scelte che funzionano bene **solo su quel test set**.
### 4 Non ricordo, riescia rispiegarmele tutte in breve
Quando le classi sono sbilanciate, per esempio:
- 95% negativi
- 5% positivi
un classificatore stupido che predice sempre la classe più frequente può già ottenere accuracy alta.
**majority class classifier**
Se 95 persone su 100 sono negative:
predico sempre “negative”  
→ accuracy = 95%
Sembra ottimo, ma in realtà il modello è pessimo.
### 5 Non ricordo, me le riesci a spiegare tutte
Quando i **falsi negativi costano molto**, la metrica più importante è **recall**.
Diagnosi tumore:
Se una persona malata viene classificata sana → gravissimo
Quello è un **false negative**
Quindi vogliamo trovare più positivi possibile.
La recall misura proprio questo:
quanti veri positivi sono riuscito a trovare?
## Parte B
mi riesci ad aggiungere anche la definizione di precision, recall e accuracy?
Precision: --> tra tutti quelli che il modello ha detto positivi, quanti lo sono davvero?
Recall --> tra tutti i veri positivi presenti, quanti ne ho trovati?
Accuracy --> percentuale totale di predizioni corrette
### 6 0.8
### 7 0.89
### 8 0.85
## Parte C
### 9 mi riesci a dare tu la deifnizione di bias e variance
Bias --> Errore dovuto a un modello **troppo semplice**
	associato ad underfitting
Variance --> Errore dovuto a un modello **troppo complesso e sensibile al rumore**
	associato ad overfitting
- **high bias = too simple**
- **high variance = too complex**
### 10 mi riesci a dare la definizione Generalization gap
È la differenza tra performance su training e validation/test
gap=accuracy(train)​−accuracy(validation)
Se il gap è grande:
	il modello va molto bene sul training  
	ma peggio sui nuovi dati
Questo indica **overfitting**


# Test 2
ricordati di darmi comunque sempre una breve definizione
## Parte A 
### 1 B
Il **training set** è il dataset usato per addestrare il modello.
### 2 B
La **cross-validation** divide il training set in più parti (folds) e ripete training + validation più volte.
### 3 C
accuracy È la percentuale totale di classificazioni corrette.
### 4 B
**ridurre la complessità / aggiungere regolarizzazione**
Per ridurla, in generale:
- modello più semplice
- albero meno profondo
- regolarizzazione
- aumentare k in kNN
### 5 non ricordo, mi dici quale e mi spieghi il perchè
Il ROC space usa:
- **FPR** = false positive rate
- **TPR** = true positive rate
Il miglior classificatore è: in alto a sinistra
Perché vogliamo:
- TPR alto
- FPR basso
## Parte B
### 6 0.59
la precision è tra tutti i positivi predetti, quanti sono davvero positivi?
### 7 0.91
recall quanti veri positivi ho trovato?
### 8 0.55
Accuracy --> predizioni giuste su quelle totali
## Parte C

### 9 quando il modello è troppo abituato agli stessi dati e si comporta male con dati nuovi
### 10 quando c'è un problema di class imbalance
La recall si usa quando è importante **non perdere i positivi**.
### Esempi
- diagnosi tumore
- frodi
- spam detection
In questi casi spesso c’è anche **class imbalance**.