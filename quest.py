# Questo serve per definire la quest.
# Ogni quest ha un titolo, descrizione, stanza finale, mostri
# pyfiglet per ascii art

import random
import json

data = json.load(open("quest.json"))

def intro():
    storie = len(data)
    dado = random.randint(0, storie)
    print('La quest uscita è la n.', dado)
    titolo = data["quest"][dado]["titolo"]
    print('******************************\n', titolo,'\n******************************' )
    print('\n', data["quest"][dado]["descrizione"])


if __name__ == '__main__':
    intro()