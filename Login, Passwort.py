# Einleitung: In diesem Program können Sie Ihr Passwort eingeben und es für Sie überprüfen, ob es richtig ist. Wenn Sie das korrekte Passwort eingegeben haben, bergrüsst es Sie mit "Herzlich Willkommen". Ist es jedoch das falsche Passwort, gibt das Program als Rückmeldung: "Passwort nicht korrekt". Sie können das Passwort aber natürlich nach Belieben verändern.
# Feature: 

# Revlexion: Ich habe gelernt, dass Programmiersprachen viel komplexer aufgebaut sind, als ich mir vorgestelt habe. Ich habe gelernt, dass man praktisch alles Programmieren kann. Über Einkaufslisten, zu Logins bis zu den Notendurchschnittberecher. 


# Dieses Programm fragt nach ihrem Passwort, das sie korekkt eingebe muss.
# Es wird nach ihrem Login gefragt
x = input("Login eingeben: ")
# wenn ihr Login "Strudel123" ist, sagt der Code dir "Herzlich Willkommen"
if x == "Strudel123":
    print("Herzlich Willkommen")
# wenn das Login nicht "Strudel123" ist, sagt der Code dir "Passwort nicht korrekt"
else: 
    print("Passwort nicht korrekt")
