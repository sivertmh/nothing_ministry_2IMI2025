# Flask-prosjekt -- Dokumentasjon

## 1. Forside

**Prosjekttittel:** The Ministry of Nothing\
**Navn:** Sivert Mathisen Hansen\
**Klasse:** 2IMI\
**Dato startet:** 10. november 2025

**Kort beskrivelse av prosjektet:**\
*Skriv 2--4 setninger om hva applikasjonen gjør og hvilket tema den
bygger på.*

Jeg har lyst til å lage en slags nettbutikk for kulturmedia som lar deg kjøpe musikk, filmer, serier, bøker og spill. Målgruppen til denne nettsiden vil være de som liker kulturmedia og de som vil eie ting selv. Du kan gå inn på din egen bruker og få en oversikt over det du eier, og du kan laste det ned lokalt. Mange av disse funksjonene er imaginære, for jeg kan ikke nok til å lage det hele enda. Det jeg kan og skal gjøre er å manuellt legge in brukere og få en fin profilside til å vise hva du har kjøpt.

------------------------------------------------------------------------

## 2. Systembeskrivelse

**Formål med applikasjonen:**\

Formålet er å vise kompetanse innenfor temaet databaser, python og sql. Prosjektet har stor telling på karakteren dette skoleåret.

**Brukerflyt:**\
*Beskriv hvordan brukeren bruker løsningen -- fra startside til lagring
av data.*

**Teknologier brukt:**

-   Python / Flask
-   MariaDB
-   HTML / CSS / JS
-   (valgfritt) Docker / Nginx / Gunicorn / Waitress osv.

------------------------------------------------------------------------

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø

Vi har en Raspberry Pi 4 vi har fått av skolen og bruker den som fysisk server. På den er Raspberry Pi OS 64-bit Lite installert.

### Nettverksoppsett

-   Nettverksdiagram
-   IP-adresser
-   Porter
-   Brannmurregler

Eksempel:

    Klient → Waitress → MariaDB

### Tjenestekonfigurasjon

-   systemctl / Supervisor
-   Filrettigheter
-   Miljøvariabler

------------------------------------------------------------------------

## 4. Prosjektstyring -- GitHub Projects (Kanban)

-   To Do / In Progress / Done
-   Issues
-   Skjermbilde (valgfritt)

Refleksjon: Hvordan hjalp Kanban arbeidet?

------------------------------------------------------------------------

## 5. Databasebeskrivelse

**Databasenavn: nothing_ministry**

**Tabeller:**
\| Tabell \| Felt \| Datatype \| Beskrivelse \|
\|--------\|-------\|-----------\|--------------\| \| customers \| id \|
INT \| Primærnøkkel \| \| customers \| name \| VARCHAR(255) \| Navn \|
\| customers \| address \| VARCHAR(255) \| Adresse \|

**SQL-eksempel:**

``` sql
CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255)
);
```

------------------------------------------------------------------------

## 6. Programstruktur

    projektnavn/
     ├── app.py
     ├── templates/
     ├── static/
     └── .env

Databasestrøm:

    HTML → Flask → MariaDB → Flask → HTML-tabell

------------------------------------------------------------------------

## 7. Kodeforklaring

Forklar ruter og funksjoner (kort).

------------------------------------------------------------------------

## 8. Sikkerhet og pålitelighet

-   .env
-   Miljøvariabler
-   Parameteriserte spørringer
-   Validering
-   Feilhåndtering

------------------------------------------------------------------------

## 9. Feilsøking og testing

-   Typiske feil
-   Hvordan du løste dem
-   Testmetoder

------------------------------------------------------------------------

## 10. Konklusjon og refleksjon

-   Hva lærte du?
-   Hva fungerte bra?
-   Hva ville du gjort annerledes?
-   Hva var utfordrende?

------------------------------------------------------------------------

## 11. Kildeliste

-   w3schools
-   flask.palletsprojects.com
