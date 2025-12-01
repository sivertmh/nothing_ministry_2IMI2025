# Flask-prosjekt "The Ministry of Nothing" — Dokumentasjon

## 1. Forside

**Prosjekttittel:** The Ministry of Nothing

**Navn:** Sivert Mathisen Hansen

**Klasse:** 2IMI

**Dato startet:** 10. november 2025

**Kort beskrivelse av prosjektet:**

Jeg har lyst til å lage en slags nettbutikk for kulturmedia. Den lar deg kjøpe musikk, filmer, serier, bøker og spill (ikke online-spill). Målgruppen til denne nettsiden vil være de som liker kulturmedia og de som vil eie ting selv. Du kan gå inn på din egen bruker og få en oversikt over det du eier, sortert etter type media. Dette kan da lastes ned lokalt (imaginær funksjonalitet). Hvis flere enn manuellt lagt til brukerene

---

## 2. Systembeskrivelse

**Formål med applikasjonen:**

Formålet er å vise kompetanse innenfor temaet databaser, python og sql. Prosjektet har stor telling på karakteren dette skoleåret.

**Brukerflyt:**

Startsiden er en velkomstside og tilbyr online shopping av de forskjellige mediumene. Her kan du kjøpe ting (ingen faktisk betaling), deretter eier du de. En av lenkene på navbaren leder til brukersiden din, og du får en oversikt av eiendeler, sortert etter ulike kategorier (film, spill, bok, osv.). 

Dette gjelder bare hvis du har en bruker allerede. Hvis du ikke har bruker kan du gå til "/register" på nettsiden og fylle ut skjemaet som lager en.

**Teknologier brukt:**

- Python / Flask
- MariaDB
- HTML / CSS / JS

---

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø

Vi har en Raspberry Pi 4 vi har fått av skolen og bruker den som fysisk server. På den var Raspberry Pi OS 64-bit Lite installert.

### Nettverksoppsett

- Nettverksdiagram
- IP-adresser: 10.200.14.71 (rpi), 10.200.14.70 (skolepc)
- Porter: 22 (ssh)
- Brannmurregler: ufw allow 22

Eksempel:

    Klient → Waitress → MariaDB

### Tjenestekonfigurasjon

- systemctl / Supervisor
- Filrettigheter
- Miljøvariabler: DB_HOST, DB_USER, DB_PASSORD, DB_NAME

---

## 4. Prosjektstyring -- GitHub Projects (Kanban)

- To Do / In Progress / Done
- Issues
- Skjermbilde (valgfritt)

Refleksjon: Hvordan hjalp Kanban arbeidet?

---

## 5. Databasebeskrivelse

**Databasenavn: nothing_ministry**

**Tabeller:**

```sql
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| name     | varchar(255) | NO   |     | NULL    |                |
| surname  | varchar(255) | NO   |     | NULL    |                |
| username | varchar(255) | NO   | UNI | NULL    |                |
| email    | varchar(255) | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
```

**SQL-eksempel:**

```sql
CREATE TABLE user (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT NULL,
surname VARCHAR(255) NOT NULL,
username VARCHAR(255) NOT NULL UNIQUE,
email VARCHAR(255) NOT NULL);
```

---

## 6. Programstruktur

    nothing_ministry_2imi2025/
     ├── app.py
     ├── templates/
     ├── python/
     ├── static/
     └── .env

Databasestrøm:

    HTML → Flask → MariaDB → Flask → HTML-tabell

---

## 7. Kodeforklaring

Under er koden for en dynamisk brukerside.

```python
# varierende brukerside
@app.route("/u/<string:username>")
def show_user(username):
    mydb = get_connection()
    mycursor = mydb.cursor()

    # Henter brukernavn og id basert på brukernavn i url
    mycursor.execute("SELECT id, username FROM user WHERE username = %s", (username,))
    row = mycursor.fetchone()

    if row:
        user_id, username = row
        # henter "items" fra gjeldene bruker
        mycursor.execute("SELECT * FROM item WHERE user_id = %s", (user_id,))
        items = mycursor.fetchall()
    else:
        username = "User not found"
        items = []

    mydb.close()

    return render_template("user.html", username=username, item=items)
```

Forklaring:

1. Den kjører en sql-query mot databasen for å hente ut brukernavn og passord.

2. Bruker If-setning til å bare hente "items" bruker eier.

---

## 8. Sikkerhet og pålitelighet

- .env
- Miljøvariabler for hemmelig info
- Parameteriserte spørringer med %s ved queries
- Validering
- Feilhåndtering i python med try except

---

## 9. Feilsøking og testing

- Typiske feil
- Hvordan du løste dem
- Testmetoder

**Definering av tabeller på feil måte:**

- Feil rekkefølge slik at tabeller med FK blir laget før den den refererer til.

- Ikke kall en tabell for _order_, for det ser ut til å være en sql-kommando og førte til at tabell ikke ble laget. Jeg kalte den _receipt_ istdeden.

**SSH til pi stoppet å funke:**

- Jeg fikk feilen _"permission denied (public key)"_, for pi-en hadde blitt plutselig satt til å bare bruke ssh-key og ingen passord. Jeg fikset feilen ved å gå til filen _/etc/ssh/sshd_config_ og endre linjen _PasswordAuthentication_ til _yes_, det sto _no_ for meg.

**Kunne ikke pinge eller koble til Pi:**

- Viste seg å være et brannmurproblem. Dette hjalp:

```bash
sudo ufw allow from any to any proto
sudo ufw reload
```

- Dette åpner _proto_ i brannmuren, noe som fikset problemet med ping og tilkobling.

---

## 10. Konklusjon og refleksjon

- Hva lærte du?
- Hva fungerte bra?
- Hva ville du gjort annerledes?
- Hva var utfordrende?

---

## 11. Kildeliste

- w3schools
- flask.palletsprojects.com
- [ssh.com](https://www.ssh.com/academy/ssh/sshd_config)
