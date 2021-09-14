from googletrans import Translator

translator = Translator()
translations = translator.translate(["Bonjour", "Au revoir", "Bienvenue", "A bientôt"])
for word in translations:
    print(word.origin, ':', word.text)