# Gestione Appuntamenti

## Obiettivo
Ottimizzare l'agenda dello studio garantendo efficienza operativa e soddisfazione dei pazienti.

## Principi di Programmazione

### Regole Base

1. **Mai sovrapporre** appuntamenti sulla stessa poltrona
2. **Rispettare** le durate standard
3. **Prevedere** buffer tra appuntamenti complessi
4. **Bilanciare** il carico di lavoro
5. **Considerare** le preferenze dell'operatore

### Durate Standard

| Prestazione | Durata Minima | Durata Standard |
|-------------|---------------|-----------------|
| Prima visita | 30 min | 45 min |
| Visita controllo | 15 min | 20 min |
| Igiene | 45 min | 60 min |
| Otturazione semplice | 30 min | 45 min |
| Otturazione complessa | 45 min | 60 min |
| Devitalizzazione | 45 min | 60-90 min |
| Estrazione semplice | 20 min | 30 min |
| Estrazione complessa | 45 min | 60 min |
| Chirurgia | 60 min | 90+ min |
| Impronta protesi | 30 min | 45 min |
| Cementazione | 20 min | 30 min |
| Emergenza | 15 min | 30 min |

## Struttura dell'Agenda

### Fasce Orarie

```
MATTINA (09:00 - 13:00)
├── 09:00-09:30  Slot versatile
├── 09:30-10:30  Slot lungo (chirurgia, endo)
├── 10:30-11:00  Buffer/emergenze
├── 11:00-12:00  Slot lungo
└── 12:00-13:00  Slot versatile

POMERIGGIO (14:30 - 19:30)
├── 14:30-15:30  Slot lungo
├── 15:30-16:30  Slot lungo
├── 16:30-17:00  Buffer/emergenze
├── 17:00-18:00  Slot lungo
├── 18:00-19:00  Slot versatile
└── 19:00-19:30  Buffer chiusura
```

### Slot Riservati

| Tipo Slot | Orario Consigliato | Scopo |
|-----------|-------------------|-------|
| Emergenze | 10:30, 16:30 | Urgenze del giorno |
| Prima visita | Prima mattina/primo pomeriggio | Migliore accoglienza |
| Chirurgia | Mattina | Operatore più fresco |
| Bambini | Primo pomeriggio | Dopo la scuola |
| Lavoratori | Prima/ultima fascia | Compatibilità lavoro |

## Procedura di Prenotazione

### Nuovi Pazienti

1. **Raccogliere dati** essenziali
2. **Capire il motivo** della visita
3. **Proporre** slot prima visita (45 min)
4. **Confermare** l'appuntamento
5. **Inviare** conferma SMS/email

**Slot preferiti per prime visite:**
- 09:00 - 09:45
- 14:30 - 15:15

### Pazienti Esistenti

1. **Verificare** la cartella clinica
2. **Controllare** il piano di trattamento
3. **Identificare** la prestazione da programmare
4. **Selezionare** la durata corretta
5. **Proporre** disponibilità
6. **Confermare** l'appuntamento

### Urgenze

!!! warning "Gestione Urgenze"
    Le urgenze devono essere inserite negli slot dedicati. Se non disponibili, valutare l'inserimento in slot buffer.

**Criteri:**

| Urgenza | Tempistica |
|---------|------------|
| Dolore acuto | Stesso giorno |
| Trauma | Stesso giorno |
| Gonfiore | Stesso giorno |
| Protesi rotta | Entro 24h |
| Corona staccata | Entro 24h |
| Dolore moderato | Entro 48h |

## Regole per Tipologia di Appuntamento

### Chirurgia/Implantologia

- Programmare al mattino
- Prevedere tempo extra (buffer dopo)
- Verificare anamnesi aggiornata
- Confermare preparazione paziente

### Sedute Multiple

Per piani di trattamento complessi:

1. Programmare le sedute in sequenza logica
2. Rispettare tempi di guarigione
3. Evitare sedute ravvicinate impegnative
4. Considerare impegni del paziente

### Bambini

- Slot primo pomeriggio
- Sedute brevi (max 30 min)
- Buffer dopo per eventuale prolungamento
- Annotare età e comportamento

## Modifiche e Spostamenti

### Richiesta del Paziente

1. Verificare motivo
2. Proporre alternative
3. Aggiornare l'agenda
4. Inviare nuova conferma
5. Gestire lo slot liberato

### Richiesta dello Studio

1. Contattare il paziente tempestivamente
2. Scusarsi per il disagio
3. Proporre alternative convenienti
4. Documentare la comunicazione

## Ottimizzazione Agenda

### Evitare "Buchi"

- Utilizzare lista d'attesa
- Chiamare per anticipi
- Proporre slot adiacenti
- Contattare pazienti per recall

### Evitare Sovraccarico

- Non accettare "urgenze" fuori dagli slot
- Rispettare le durate
- Prevedere buffer
- Saper dire "no" con alternative

### Bilanciamento

```
ESEMPIO GIORNATA BILANCIATA

09:00  Prima visita (45 min) - Facile
09:45  Igiene (60 min) - Media
10:45  Buffer (15 min)
11:00  Endodonzia (60 min) - Impegnativa
12:00  Controllo (20 min) - Facile
12:20  Otturazione (40 min) - Media
---
14:30  Chirurgia (90 min) - Impegnativa
16:00  Buffer (30 min)
16:30  Igiene (60 min) - Media
17:30  Controllo (20 min) - Facile
17:50  Otturazione (40 min) - Media
18:30  Cementazione (30 min) - Facile
19:00  Buffer chiusura
```

## Documentazione

### Nel Gestionale

Per ogni appuntamento:

| Campo | Informazione |
|-------|--------------|
| Paziente | Anagrafica collegata |
| Data/Ora | Inizio appuntamento |
| Durata | Prevista |
| Operatore | Assegnato |
| Prestazione | Prevista |
| Note | Eventuali |
| Stato | Confermato/Da confermare |

### Statistiche

Monitorare periodicamente:

- Tasso di occupazione
- No-show rate
- Ritardi medi
- Prestazioni più richieste

## Responsabilità

| Ruolo | Compito |
|-------|---------|
| Segretaria | Programmazione, modifiche, conferme |
| Coordinatore | Supervisione, ottimizzazione, criticità |
| Operatori | Comunicare durate reali, esigenze |
