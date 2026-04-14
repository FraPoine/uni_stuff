## 1. Conditional probability: idea intuitiva
La probabilità condizionata risponde a domande del tipo:
- **qual è la probabilità che succeda E, sapendo che è già successo F?**
Si scrive:
$$
P(E\ |\ F)
$$
Si legge: **probabilità di E dato F**.
quando osservi F, entri nel “mondo” in cui F è già accaduto, quindi il tuo spazio dei possibili risultati si restringe.
#### Intuizione chiave
Prima guardavi tutto lo spazio campionario.  
Dopo aver osservato F, guardi solo la parte compatibile con F.

Quindi la domanda cambia da:
- “quanto è probabile E in generale?”
a
- “quanto è probabile E **dentro** il sottoinsieme F?”

---
## 2. Formula della conditional probability
la formula fondamentale è
$$
P(E\ |\ F) = \frac{P(E\ and\ F)}{P(F)}
$$
purchè $P(F) > 0$
#### Perché ha senso
- $(E \text{ and } F)$: probabilità che succedano entrambi
- $P(F)$: probabilità del “nuovo universo” in cui stai ragionando
Quindi stai prendendo la parte di F in cui accade anche E, e la confronti con tutto F.

---
## 3. Esempio intuitivo semplice
immagina un mazzo di carte.
sia 
- E la carta è una figura
- F la carta è di cuori
Allora:
$$
P(E\ |\ F)
$$
vuol dire: tra le carte di cuori, qual è la frazione di figure?
Non stai più guardando tutto il mazzo, ma solo le 13 carte di cuori. Questo è esattamente il senso del condizionamento.

---
## 4. Esempio del PDF: raccomandazione di film
Il PDF fa un esempio stile Netflix:
- E: l’utente guarda un certo film
- F: l’utente ha guardato Amélie
La domanda non è più la probabilità “assoluta” che guardi il film E, ma la probabilità che lo guardi **sapendo** che ha già guardato F. Il punto del PDF è che osservare F cambia l’informazione che hai sull’utente, quindi può far salire o scendere la probabilità di E.

Questa è l’idea più importante della conditional probability:  
**nuova evidenza → nuove probabilità**.

---
## 5. Il paradigma del condizionamento
Il PDF insiste su un’idea molto bella: quando condizioni su un evento, entri in un nuovo universo, ma **le regole della probabilità restano valide**.
Quindi, se condizioni sempre sullo stesso evento G, continuano a valere versioni “condizionate” delle formule note:
$$
\begin{matrix}
	0 ≤ P(E\ |\ G) ≤ 1 \\
	P(S\ |\ G) = 1
\end{matrix}
$$
Se E e F sono **mutuamente esclusivi**, allora:
$$
P(E \ or \ F \ | \ G) = P(E\ |\ G) + P(F\ |\ G)
$$
e anche il complemento diventa 
$$
P(E^c \ | \ G) = 1 - P(E\ |\ G)
$$
Il messaggio è: **il condizionamento non rompe la teoria; cambia solo il contesto**.

---
## 6. Conditioning on multiple events
Il PDF mostra anche che puoi condizionare su più eventi:
$$
P(E∣F,G)
$$che si legge: probabilità di E, dato che sono successi sia F sia G, 
e si scrive la formula:
$$
P(E∣F,G) = \frac{P(E\ and\ F\ |\ G)}{P(F∣G)}
$$
Questo serve a ricordarti che puoi aggiungere informazione progressivamente.

---
# Independence
## 7. Idea intuitiva di independence
Due eventi sono indipendenti se sapere che uno è successo **non cambia** la tua credenza sull’altro. Il PDF lo definisce proprio così.
Formalmente
$$
P(E\ |\ F) = P(E)
$$
Questa è la definizione concettuale migliore: **osservare F non ti dà informazione utile su E.**
### Esempio classico
- primo lancio di dado
- secondo lancio di dado
Il risultato del primo non cambia ciò che pensi del secondo, quindi gli eventi collegati ai due lanci sono indipendenti.
---
## 8. Formula dell’indipendenza
Il PDF introduce anche la forma equivalente:
$$
P(E\ and\ F)=P(E)P(F)
$$
Questa formula non è una definizione separata “magica”: viene dalla conditional probability. Se infatti
$$
P(E∣F) = \frac{P(E\ and\ F)}{P(F)}
$$e l’indipendenza dice che $P(E \mid F) = P(E)$, allora ottieni:
$$
P(E \ and\ F) = P(E)P(F)
$$
#### Interpretazione
Per eventi indipendenti, la probabilità che accadano entrambi si ottiene moltiplicando.

---
## 9. Attenzione: independence non è mutual exclusion
Questa è una distinzione fondamentale.
#### Mutually exclusive
Vuol dire che i due eventi **non possono accadere insieme**:
$$
P(E\ and \ F) = 0
$$
#### Independent
Vuol dire che sapere che succede uno **non cambia** la probabilità dell’altro:
$$
P(E \mid F) = P(E)
$$
**Sono concetti diversissimi.**

Anzi, per eventi con probabilità positiva, essere mutuamente esclusivi implica in genere **dipendenza**, non indipendenza. Perché se sai che F è accaduto, allora E non può più accadere. Quindi la tua credenza su E cambia drasticamente.

---
## 10. Independence è simmetrica
Il PDF sottolinea che l’indipendenza è simmetrica:
- se E è indipendente da F
- allora F è indipendente da E
cioè:
$$
P(E \mid F) = P(E) \iff P(F \mid E) = P(F)
$$
---
## 11. Independence di più eventi
Per più eventi, il PDF scrive che la generalized independence richiede che per ogni sottoinsieme di eventi valga il prodotto delle probabilità. In forma semplice, per eventi indipendenti E1, ..., En:
$$
P(E_1,\dots,E_n)=\prod_{i=1}^{n} P(E_i)
$$
#### Esempio del PDF
5 lanci indipendenti di moneta, probabilità di 5 teste:
$$
(\frac12)^5 = 0,03125
$$
perché ogni lancio è indipendente dagli altri.

---
## 12. Come si stabilisce l’indipendenza
Il PDF dice due cose importanti:
La prima: idealmente la mostri matematicamente, verificando che
$$
P(E \mid F) = P(E)
$$
oppure
$$
P(E\ and \ F) = P(E)P(F)
$$
La seconda: nella pratica, soprattutto con dati reali, l’indipendenza perfetta spesso non esiste davvero, ma viene **assunta** come modello utile. Questo succede continuamente in machine learning e statistica.

***l’indipendenza spesso non è “verità assoluta”, ma una assunzione semplificatrice.***

---
## 13. Independence and complements
Il PDF mostra anche che se A e B sono indipendenti, allora lo sono anche certe combinazioni coi complementi, per esempio A e B^c.

---
# Conditional independence

## 14. Che cos’è
Due o più eventi possono essere indipendenti **solo dopo aver fissato una certa informazione di contesto**. Questo si chiama **conditional independence**.

Per esempio, il PDF scrive che $E1​,E2​,E3$​ sono condizionatamente indipendenti dato F se:
$$
P(E1​,E2​,E3​∣F)=P(E1​∣F)P(E2​∣F)P(E3​∣F)
$$
### Intuizione
Una volta che sai F, le dipendenze residue tra gli eventi spariscono.
Questo concetto è centralissimo in AI, graphical models e Bayes nets.

---
## 15. Warning molto importante del PDF
Il PDF mette anche un warning fondamentale:
- eventi dipendenti possono diventare indipendenti dopo aver condizionato
- eventi indipendenti possono diventare dipendenti dopo aver condizionato
Quindi **independence** e **conditional independence** non sono la stessa cosa.

---
# Legame con la probabilità di “and”
## 16. Eventi indipendenti
Il PDF poi collega independence alla probabilità dell’“and”
Se E e F sono indipendenti, allora:
$$
P(E\ and\ F)=P(E)P(F)
$$
Questo è il modo più semplice di calcolare probabilità congiunte quando c’è indipendenza.

---
## 17. Eventi dipendenti: chain rule
Se invece gli eventi **non** sono indipendenti, devi usare la chain rule:
$$
P(E\ and\ F)=P(E \mid F)P(F)
$$
oppure equivalentemente:
$$
P(E\ and\ F)=P(F \mid E)P(E)
$$
Questa formula è nel PDF come regola generale per il caso dipendente.
#### Intuizione
Per avere sia E sia F:
- prima succede F
- poi, dato F, deve succedere anche E
Quidni:
probabilità totale=probabilità  di F x probabilità di E dato F

---
## 18. Generalizzazione della chain rule
Per più eventi, il PDF scrive:
$$
P(E_1​,\dots,E_n​)=P(E_1​)P(E_2​∣E_1​)\dots P(E_n​∣E_1​,\dots,E_n−1​)
$$
Questa formula è molto importante perché mostra come scomporre una probabilità complessa in pezzi più gestibili.

----
# Come capire tutto insieme

## 19. La relazione concettuale tra i pezzi
Puoi pensare così:
#### Conditional probability
serve a dire coma cambia la probabilità di E quando so F?
#### Independence
è il caso speciale in cui la risposta è: non cambia niente
cioè $P(E \mid F) = P(E)$

#### chain rule 
serve a dire come calcolo $P(E\ and\ F)$?
in generale
$$
P(E \mid F) = P(E)
$$
quindi
$$
P(E\ and\ F) = P(E)P(F)
$$
Questo è il collegamento logico principale di tutto il blocco.

---
# Errori Tipici
## 20. Gli errori più comuni

#### 1. Confondere independence con mutual exclusion
Sono quasi opposti come significato.
#### 2. Scrivere sempre $P(E\ and\ F) = P(E)P(F)$
Questo vale **solo** se gli eventi sono indipendenti.
#### 3. Dimenticare che condizionare cambia lo spazio
$P(E)$ e $P(E \mid F)$ sono quantità diverse.
#### 4. Pensare che independence implichi automaticamente conditional independence
Non è vero in generale.
#### 5. Pensare che conditional independence implichi independence assoluta
Anche questo non è vero.

---
## Formula sheet essenziale

### 21. Le formule da ricordare

**Probabilità condizionata**
$$
P(E \mid F) = \frac{P(E \cap F)}{P(F)}, \qquad P(F) > 0
$$
**Chain rule**
$$
P(E \cap F) = P(E \mid F)\,P(F)
$$
Equivalentemente,
$$
P(E \cap F) = P(F \mid E)\,P(E)
$$
**Se \(E\) e \(F\) sono indipendenti**
$$
P(E \mid F) = P(E)
$$
$$
P(E \cap F) = P(E)\,P(F)
$$
**Per più eventi**
$$
P(E_1 \cap E_2 \cap \cdots \cap E_n)
=
P(E_1)\,P(E_2 \mid E_1)\,P(E_3 \mid E_1 \cap E_2)\cdots P(E_n \mid E_1 \cap \cdots \cap E_{n-1})
$$
**Se \(E_1, E_2, \dots, E_n\) sono condizionalmente indipendenti dato \(F\)**
$$
P(E_1 \cap E_2 \cap \cdots \cap E_n \mid F)
=
\prod_{i=1}^{n} P(E_i \mid F)
$$
Tutte queste relazioni sono nella sezione del PDF su conditional probability, independence e probability of and.
