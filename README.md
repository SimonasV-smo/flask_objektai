# Sporto Varžybų Rezultatų Puslapis

## Aprašymas
Ši Flask aplikacija leidžia atvaizduoti sporto varžybų rezultatus, įskaitant komandų statistikas, bei suteikia galimybę pridėti, redaguoti ir trinti rungtynių duomenis. Ji skirta analizuoti komandų pasirodymus, rodyti laimėjimų skaičių, pelnytus taškus ir dar daugiau.

**Pagrindinės funkcijos:**
- Rungtynių rezultatų lentelė su redagavimo ir trynimo funkcijomis.
- Paieškos laukelis, leidžiantis ieškoti rezultatų pagal komandų pavadinimus ar datą.
- Forma, skirta pridėti naujas rungtynes.
- Statistikos puslapis, kuriame rodomos komandos pozicijos, laimėjimai ir pelnyti taškai.

---

## Kaip Paleisti Aplikaciją

### 1. Parsisiųskite Projektą
Parsisiųskite `app.zip` failą iš GitHub arba kitos saugyklos ir išpakuokite jį savo kompiuteryje.

### 2. Įkelkite projektą į PyCharm arba VSCode
Atidarykite išpakuotą projektą savo mėgstamoje IDE, pvz., PyCharm arba Visual Studio Code.

### 3. Įdiekite reikalavimus
Atidarykite terminalą IDE aplinkoje ir įveskite šią komandą, kad įdiegtumėte reikiamas bibliotekas:

```bash
pip install -r requirements.txt
```
Tai automatiškai įdiegs visas priklausomybes, kurios reikalingos aplikacijai veikti, pvz., Flask, SQLAlchemy ir kitas.

### 4. Paleiskite aplikaciją
Paleiskite Flask serverį terminale naudodami komandą:

```bash
flask run
```
Atidarykite naršyklę ir įveskite adresą:
```bash
http://127.0.0.1:5000/
```