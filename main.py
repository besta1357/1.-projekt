"""projekt_1.py: první projekt do Engeto Online Python Akademie

author: Peter Šebest
email: psebest11@gmail.com
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
registrovani_uzivatele = {
    "bob" : 123,
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}
cara = "-" * 40
pocet_textu = (len(TEXTS))

uzivatel = input("username: ")
heslo = input("pasword: ")

if heslo.isnumeric():
  heslo = int(heslo)  
if uzivatel in registrovani_uzivatele and heslo == registrovani_uzivatele[uzivatel]:
  print(cara)
  print(f"Welcome to the app, {uzivatel} \nWe have {pocet_textu} texts to be analyzed. ")
  print(cara)
  vyber_textu = (input(f"Enter a number btw. 1 and {pocet_textu} to select: "))
  if vyber_textu.isnumeric():
     vyber_textu = int(vyber_textu)
     if vyber_textu < 1 or vyber_textu > pocet_textu:
          print("Invalid number, terminating the program...")
          exit()
          print(cara)               
  else:
      print("Invalid input, terminating the program...")
      exit()
      print(cara)
  print(cara)
elif uzivatel in registrovani_uzivatele and heslo != registrovani_uzivatele[uzivatel]:
  print("Invalid password, terminating the program...")
  exit()
  print(cara)  
else:
  print("unregistered user, terminating the program...")
  exit()

vycistena_slova = []
pocet_malych_slov = 0
pocet_velkych_slov = 0
pocet_cisel = 0
pocet_slov_s_velkym_pismenom = 0
#cisla_v_textu = []
pismena_ve_slovech = []
cisla_v_textu = [int(cisla) for cisla in TEXTS[vyber_textu - 1].split() if cisla.isnumeric()]
suma_cisel = sum(cisla_v_textu)
      
for slova in TEXTS[vyber_textu - 1].split():
    ciste_slovo = slova.strip(",.:;'")
    vycistena_slova.append(ciste_slovo)
    pocet_slov = len(vycistena_slova)    
    pocet_pismen_ve_slovech = len(ciste_slovo) #vytvori pocet pismen v jednotlivych slovech
    pismena_ve_slovech.append(pocet_pismen_ve_slovech) #vytvoreni listu s poctem pismen ve slovech    
    if slova.islower():
        pocet_malych_slov += 1      
    elif slova.isupper():
        pocet_velkych_slov += 1       
    elif slova.isnumeric():
        pocet_cisel += 1          
    for pismena in slova: #vytvori jenom prvni pismeno slova
        break        
    if pismena.isupper():
       pocet_slov_s_velkym_pismenom += 1      
print(f"Text number {vyber_textu} contains {pocet_slov} words.")
print(f"There are {pocet_malych_slov} lowercase words.")
print(f"There are {pocet_velkych_slov} uppercase words.")
print(f"There are {pocet_slov_s_velkym_pismenom - pocet_velkych_slov} titlecase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {suma_cisel}")

#nejdelsi_slovo = int(max(pismena_ve_slovech))

vyskyt_slov = {}
for cetnost in pismena_ve_slovech:
    if cetnost not in vyskyt_slov:
        vyskyt_slov[cetnost] = 1
    else:
        vyskyt_slov[cetnost] += 1
serazeny_vyskyt_slov = dict(sorted(vyskyt_slov.items()))
nejvyssi_cetnost = max(serazeny_vyskyt_slov.values())
print(cara)
print("LEN |".center(5) + "OCCURENCES".center(15) + "| NR.".center(10))
print(cara)

for delka_slova in serazeny_vyskyt_slov:
    print(f"{delka_slova: ^4}|{serazeny_vyskyt_slov[delka_slova]*"*": ^1}" +
          f"{" "*((nejvyssi_cetnost - serazeny_vyskyt_slov[delka_slova])+8)}" + 
          f"|{serazeny_vyskyt_slov[delka_slova]}")
print(cara)