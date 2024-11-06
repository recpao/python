# Qui si decide che succede..
#tieni il conto delle stanze, 12 + finale

import random

def area():
    x = random.randint(1,6)
    if x <= 3:
        print ('Incontro! Preparati alla lotta')
    elif x == 4 or x == 5:
        print('Sta per accadere un evento!')
    else:
        print('Sei fortunato, la stanza è vuota')




if __name__ == '__main__':
    print('Aree\n')
    area()