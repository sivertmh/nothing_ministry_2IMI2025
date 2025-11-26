# Flask-prosjekt -- Dokumentasjon

## 1. Forside

**Prosjekttittel:** The Ministry of Nothing
**Navn:** Sivert Mathisen Hansen
**Klasse:** 2IMI
**Dato startet:** 10. november 2025

**Kort beskrivelse av prosjektet:**

Jeg har lyst til å lage en slags nettbutikk for kulturmedia. Den lar deg kjøpe musikk, filmer, serier, bøker og spill (ikke online-spill). Målgruppen til denne nettsiden vil være de som liker kulturmedia og de som vil eie ting selv. Du kan gå inn på din egen bruker og få en oversikt over det du eier, og du kan laste det ned lokalt. Mange av disse funksjonene er imaginære, for jeg kan ikke nok til å lage det hele enda. Det jeg kan og skal gjøre er å manuellt legge in brukere og få en fin profilside til å vise hva du har kjøpt.

------------------------------------------------------------------------

## 2. Systembeskrivelse

**Formål med applikasjonen:**

Formålet er å vise kompetanse innenfor temaet databaser, python og sql. Prosjektet har stor telling på karakteren dette skoleåret.

**Brukerflyt:**
*Beskriv hvordan brukeren bruker løsningen -- fra startside til lagring
av data.*

Startsiden er velkommer og tilbyr online shopping av de forskjellige mediumene. Her kan du kjøpe ting (legge til ditt bibliotek). En av lenkene på navbaren leder til brukersiden din, hvor du får en oversikt av eiendeler, sortert i ulike kategorier (film, spill, bok, osv.). 

**Teknologier brukt:**

-   Python / Flask
-   MariaDB
-   HTML / CSS / JS
-   (valgfritt) Docker / Nginx / Gunicorn / Waitress osv.

------------------------------------------------------------------------

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø

Vi har en Raspberry Pi 4 vi har fått av skolen og bruker den som fysisk server. På den var Raspberry Pi OS 64-bit Lite installert.

### Nettverksoppsett

-   Nettverksdiagram
-   IP-adresser: 10.200.14.71 (rpi), 10.200.14.70 (skolepc)
-   Porter: 22 (ssh)
-   Brannmurregler: ufw allow 22

Eksempel:

    Klient → Waitress → MariaDB

### Tjenestekonfigurasjon

-   systemctl / Supervisor
-   Filrettigheter
-   Miljøvariabler: DB_HOST, DB_USER, DB_PASSORD, DB_NAME

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

+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| name     | varchar(255) | NO   |     | NULL    |                |
| surname  | varchar(255) | NO   |     | NULL    |                |
| username | varchar(255) | NO   | UNI | NULL    |                |
| email    | varchar(255) | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+

**SQL-eksempel:**

``` sql
CREATE TABLE user (
id INT AUTO_INCREMENT PRIMARY KEY, 
name VARCHAR(255) NOT NULL, 
surname VARCHAR(255) NOT NULL, 
username VARCHAR(255) NOT NULL UNIQUE,
email VARCHAR(255) NOT NULL);
```

------------------------------------------------------------------------

## 6. Programstruktur

    nothing_ministry_2imi2025/
     ├── app.py
     ├── templates/
     ├── python/
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
-   Miljøvariabler for hemmelig info
-   Parameteriserte spørringer med %s
-   Validering
-   Feilhåndtering i python med try except

------------------------------------------------------------------------

## 9. Feilsøking og testing

-   Typiske feil
-   Hvordan du løste dem
-   Testmetoder

**Definering av tabeller på feil måte:**

- Feil rekkefølge slik at tabeller med FK blir laget før den den refererer til.

- Ikke kall en tabell for *order*, for det ser ut til å være en sql-kommando og førte til at tabell ikke ble laget. Jeg kalte den *receipt* istdeden.

**SSH til pi stoppet å funke:**

- Jeg fikk feilen *"permission denied (public key)"*, for pi-en hadde blitt plutselig satt til å bare bruke ssh-key og ingen passord. Jeg fikset feilen ved å gå til filen */etc/ssh/sshd_config* og endre linjen *PasswordAuthentication* til *yes*, det sto *no* for meg.

**Kunne ikke pinge eller koble til Pi:**

- Viste seg å være et brannmurproblem. Dette hjalp:

```bash
sudo ufw allow from any to any proto
sudo ufw reload
```
- Dette åpner *proto* i brannmuren, noe som fikset problemet med ping og tilkobling.

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
- [ssh.com](https://www.ssh.com/academy/ssh/sshd_config)
