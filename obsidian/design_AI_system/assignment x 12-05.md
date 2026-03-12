the workflow is:  
1. pick a use case (summarization, entity extraction etc) and a data example (a web page, a book,....)  
2. write a prompt to do what you want to do, so given the input, the LLM gives you an output.  
3. then, write a "judge prompt" given the input and output, you ask the LLM: did my other prompt work well?

used:
- claude haiku 4.5
- question:
	- at this web page u can find the list of all pokemon [https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number)
	- can u provide me the number of pokemon for every type? if a pokemon has two types u can add 1 to evey type of that pokemon

answer

- did my previous prompt work well
Yes, your previous prompt worked really well! It was clear and specific:

1. **You provided a direct source** - You gave me the exact URL to fetch, which is much more efficient than asking me to search broadly
2. **You clearly stated what you wanted** - "provide me the number of pokemon for every type"
3. **You explained the counting method** - "if a pokemon has two types u can add 1 to every type of that pokemon" - this made it unambiguous how to handle dual-types

The prompt was concise and easy to understand. The only minor challenge was that the webpage had a very large HTML table, so I needed to fetch it and process the data, but that's not a flaw in your prompt—it's just the nature of working with that kind of data.

If you wanted to be even more specific in the future, you could optionally mention:

- Whether you want it sorted by count (highest to lowest)
- Whether you want it as a table, list, or chart
- If you want percentages or other statistics

But honestly, your original prompt was already excellent and didn't really need any of those additions. It communicated exactly what you needed! 👍


---
which properties has a good summary?
think in a json way

{
  "summary_quality_parameters": {
    "coverage": {
      "description": "Quanto il riassunto include le idee e gli eventi principali del libro",
      "criteria": [
        "presenza dei temi principali",
        "inclusione degli eventi o argomenti chiave",
        "rappresentazione delle parti fondamentali della trama o tesi"
      ]
    },
    "accuracy": {
      "description": "Quanto il contenuto del riassunto è fedele al testo originale",
      "criteria": [
        "assenza di informazioni inventate",
        "correttezza dei fatti o degli eventi",
        "coerenza con il significato originale"
      ]
    },
    "conciseness": {
      "description": "Capacità di condensare il contenuto senza ridondanze",
      "criteria": [
        "assenza di dettagli secondari",
        "assenza di ripetizioni",
        "densità informativa elevata"
      ]
    },
    "coherence": {
      "description": "Fluidità logica e leggibilità del riassunto",
      "criteria": [
        "ordine logico degli eventi o delle idee",
        "connessioni chiare tra le frasi",
        "struttura narrativa o argomentativa comprensibile"
      ]
    },
    "structure": {
      "description": "Organizzazione interna del riassunto",
      "criteria": [
        "introduzione del contesto o del tema",
        "sviluppo delle idee principali",
        "eventuale conclusione o risultato"
      ]
    },
    "relevance": {
      "description": "Percentuale di informazioni presenti nel riassunto che sono realmente importanti",
      "criteria": [
        "presenza di informazioni centrali",
        "assenza di dettagli marginali",
        "focus sui concetti chiave"
      ]
    },
    "compression_ratio": {
      "description": "Rapporto tra lunghezza del riassunto e lunghezza del testo originale",
      "example": "0.05"
    },
    "readability": {
      "description": "Facilità di comprensione del riassunto",
      "criteria": [
        "frasi chiare",
        "vocabolario appropriato",
        "assenza di ambiguità"
      ]
    }
  }
}