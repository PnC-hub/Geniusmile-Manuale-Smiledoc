# Recall Pazienti

## Obiettivo
Garantire la continuità delle cure richiamando sistematicamente i pazienti per controlli periodici e igiene professionale.

## Importanza del Recall

### Benefici per il Paziente

- Prevenzione patologie
- Diagnosi precoce
- Mantenimento salute orale
- Risparmio economico (prevenzione vs cura)

### Benefici per lo Studio

- Fidelizzazione pazienti
- Occupazione agenda costante
- Revenue ricorrente
- Migliori outcome clinici

## Tipologie di Recall

| Tipo | Frequenza Standard | Target |
|------|-------------------|--------|
| Igiene | 6 mesi | Tutti i pazienti |
| Controllo | 6-12 mesi | Tutti i pazienti |
| Parodontale | 3-4 mesi | Pazienti parodontali |
| Ortodontico | Secondo piano | Pazienti orto |
| Post-chirurgico | Variabile | Post interventi |
| Implantare | 6 mesi | Portatori impianti |

## Frequenze Personalizzate

### Valutazione Rischio

| Rischio | Frequenza Igiene | Frequenza Controllo |
|---------|------------------|---------------------|
| Basso | 12 mesi | 12 mesi |
| Medio | 6 mesi | 6 mesi |
| Alto | 3-4 mesi | 6 mesi |

### Fattori di Rischio

**Alto rischio:**

- Parodontite attiva/trattata
- Fumatori
- Diabetici
- Scarsa igiene domiciliare
- Cariorecettività elevata

## Procedura di Recall

### Impostazione nel Gestionale

Per ogni paziente definire:

| Campo | Valore |
|-------|--------|
| Tipo recall | Igiene/Controllo/Altro |
| Frequenza | Mesi |
| Data prossimo | Automatica |
| Canale preferito | SMS/Tel/Email |
| Note | Particolarità |

### Flusso di Comunicazione

```
DATA RECALL RAGGIUNTA
         │
         ▼
    PRIMO CONTATTO
    (SMS automatico)
         │
    ┌────┴────┐
Risponde     Non risponde
    │              │
    ▼              ▼
Prenota      SECONDO CONTATTO
             (7 giorni dopo)
                   │
              ┌────┴────┐
         Risponde     Non risponde
              │              │
              ▼              ▼
          Prenota      TERZO CONTATTO
                       (Telefonata)
                            │
                       ┌────┴────┐
                  Risponde     Non risponde
                       │              │
                       ▼              ▼
                   Prenota      Segnare come
                               "Non raggiunto"
                               Riprovare tra 30gg
```

## Messaggi di Recall

### SMS Recall Igiene

```
Studio Smiledoc: Gentile [Nome], sono passati 6 mesi
dalla sua ultima igiene. È tempo di un controllo!
Prenoti al 06 90623936 o risponda a questo messaggio.
```

### SMS Recall Controllo

```
Studio Smiledoc: Gentile [Nome], è passato un anno
dall'ultimo controllo. La prevenzione è importante!
Ci chiami al 06 90623936 per un appuntamento.
```

### Email Recall

```
Oggetto: È tempo del suo controllo periodico

Gentile [Nome],

sono trascorsi [X] mesi dalla sua ultima visita presso
il nostro studio.

La prevenzione è la migliore cura: un controllo
periodico permette di individuare eventuali problemi
prima che diventino più seri e costosi da trattare.

La invitiamo a contattarci per fissare un appuntamento:
📞 06 90623936
📧 info@smiledoc.it

La aspettiamo!

Cordiali saluti
Studio Dentistico Smiledoc
```

### Script Telefonico

> "Buongiorno Sig./Sig.ra [Nome], sono [Nome] dello Studio Smiledoc. La chiamo perché sono passati [X] mesi dalla sua ultima [igiene/visita] e volevamo invitarla a programmare un controllo. Ha disponibilità nelle prossime settimane?"

## Gestione Risposte

### Paziente Prenota

1. Fissare appuntamento
2. Aggiornare data prossimo recall
3. Inviare conferma

### Paziente Rifiuta/Rimanda

1. Chiedere (senza insistere) il motivo
2. Proporre periodo alternativo
3. Annotare in cartella
4. Impostare nuovo recall futuro

### Paziente Irraggiungibile

1. Documentare i tentativi
2. Segnare come "non raggiunto"
3. Riprovare dopo 30 giorni
4. Dopo 3 cicli: valutare se continuare

## Monitoraggio

### KPI Recall

| Indicatore | Formula | Obiettivo |
|------------|---------|-----------|
| Tasso invio | Recall inviati / Recall programmati | 100% |
| Tasso risposta | Risposte / Recall inviati | > 40% |
| Tasso prenotazione | Prenotati / Recall inviati | > 30% |
| Tasso presentazione | Presentati / Prenotati | > 90% |

### Report Mensile

```
REPORT RECALL - Mese: __________

Recall programmati: ____
Recall inviati: ____ (___%)
Risposte ricevute: ____ (___%)
Appuntamenti fissati: ____ (___%)
Presentati: ____ (___%)

Pazienti non raggiunti: ____
Pazienti che hanno rifiutato: ____

Azioni necessarie:
________________________________
```

## Pazienti "Persi"

### Identificazione

Pazienti senza appuntamenti da oltre 18 mesi.

### Recupero

1. Campagna dedicata
2. Messaggio personalizzato
3. Eventuale incentivo (visita gratuita)
4. Follow-up telefonico

### Messaggio Recupero

```
Studio Smiledoc: Gentile [Nome], non la vediamo da tempo!
La invitiamo per una visita di controllo gratuita.
Prenoti al 06 90623936. La aspettiamo!
```

## Responsabilità

| Ruolo | Compito |
|-------|---------|
| Sistema | Invio automatico SMS/Email |
| Segreteria | Telefonate, gestione risposte |
| Coordinatore | Monitoraggio KPI, azioni correttive |
| Operatore | Impostazione frequenza recall in cartella |
