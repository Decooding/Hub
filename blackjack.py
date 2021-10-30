koloda = [2,3,4,6,7,8,9,10,11] *4

import random
random.shuffle(koloda)

print('Сыграем игру Блэк Джек?')
diller = random.randint(1,21)
count = 0
current = koloda.pop()
count += current
current = koloda.pop()
count += current
print('Ваша карта:', count)

while True:
    dialog = input('Брать карту?')
    if dialog == "Y":
        current = koloda.pop()
        count += current
        print('Ваша карта:',count)
    else:
        if count > diller:
            print('Поздравляю, ваша карта', count, "больше, чем карта диллера" , diller)

            exit()
        else:
            print("Kарта диллера" , diller, 'больше,чем ваша карта', count,)
            exit()
    if count == 21:
        print('Поздравляю! У вас 21!)')
    elif count > 21:
        print('Вы проиграли! Сумма карт больше 21(')
        exit()
    elif diller == 21:
        print('Етит колтитЬ! Вы проиграли! Карта Диллера 21(')
          
    
