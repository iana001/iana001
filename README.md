# Keylogger Python

Acest script Python este un keylogger care capturează apăsările de taste și le trimite prin email. Folosește biblioteca `pynput` pentru a asculta evenimentele de tastatură și biblioteca `smtplib` pentru a trimite emailuri cu datele capturate.

## Descriere

- **Funcționalitate**: Înregistrează apăsările de taste ale utilizatorului și le stochează într-un fișier text (`keyfile.txt`). După apăsarea tastei Enter, scriptul trimite conținutul fișierului la adresa de email specificată.

- **Biblioteci utilizate**:
  - `pynput`: pentru a captura evenimentele de tastatură.
  - `smtplib`: pentru a trimite emailuri.

## Configurare

1. **Instalare dependențe**:
   Asigurați-vă că aveți instalată biblioteca `pynput`. O puteți instala folosind pip:
   ```bash
   pip install pynput
# Configurare și Utilizare

## Configurare Email

Înlocuiți valorile `your_email@example.com` și `your_email_password` cu adresa și parola dvs. de email. Acestea sunt necesare pentru autentificarea și trimiterea emailurilor.
email_address = "your_email@example.com"  # Adresa de email destinatar
email_password = "your_email_password"  # Parola pentru adresa de email
## Executare Script

Rulați scriptul pentru a începe înregistrarea apăsărilor de taste. Scriptul va asculta evenimentele de tastatură și va trimite datele prin email când tasta Enter este apăsată.
```bash
python keylogger.py ```

## Funcționalitate

- **send_email(subject, body)**: Trimite un email cu subiectul și corpul specificat.
- **clear_and_write_to_file(logKey)**: Resetează și scrie textul curent în fișierul de logare.
- **keyPressed(key)**: Captură apăsările de taste și le adaugă în fișierul de logare.
- **on_release(key)**: Trimiterea emailului cu datele capturate atunci când tasta Enter este apăsată.

## Măsuri de protecție și etică

### Protejarea Utilizatorilor

1. **Consimțământ**: Asigurați-vă că aveți permisiunea explicită a utilizatorilor înainte de a utiliza sau distribui acest script. Utilizarea keyloggerelor fără consimțământ este ilegală și neetică.
2. **Utilizare Responsabilă**: Folosiți acest script doar în scopuri educaționale și pentru securitatea propriilor dispozitive. Nu utilizați keyloggere pentru a compromite securitatea altor persoane.

### Măsuri de Securitate

1. **Parola Email**: Nu stocați parola emailului direct în codul sursă. Utilizați variabile de mediu sau un sistem de gestionare a secretelor pentru a proteja informațiile sensibile.
2. **Securitate Email**: Utilizați un serviciu de email care oferă autentificare în doi pași pentru a spori securitatea contului utilizat pentru trimiterea emailurilor.
3. **Protecția Fișierelor**: Asigurați-vă că fișierele care stochează datele capturate sunt protejate și accesibile doar de către persoane autorizate. Luați în considerare criptarea fișierelor care conțin informații sensibile.

## Note Legale

Utilizarea keyloggerelor poate încălca legislația privind protecția vieții private și confidențialitatea datelor. Respectați toate legile și reglementările aplicabile în jurisdicția dvs. înainte de a utiliza acest script.

**Atenție**: Utilizarea acestui script în scopuri neautorizate poate avea consecințe legale grave. Utilizați-l cu responsabilitate și doar în scopuri legale și etice.
