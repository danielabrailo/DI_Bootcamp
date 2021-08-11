import datetime

birthdate = input("What is your birthdate? Use format DD-MM-YYY: ")
dateFormat = datetime.datetime.strptime(birthdate, "%d-%m-%Y")
today = datetime.datetime.now()
currentYear = today.year
age = currentYear - (dateFormat.year)
candles = ("i" * age)
if age == 53:
    candles = "i" * 3
print(f'''
       __{candles}__
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
''')

