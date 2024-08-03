import itertools
def manual_count(character_amount):
    string = (input('Type anything: '))
    o = len(string) - 1
    count_char = (input('Type a character to find out the amount of it in the previous entered text: '))
    oo = len(count_char)
    while oo != 1:
        count_char = (input('Input a single character only!: '))
        oo = len(count_char)
    character_amount = 0
    ooo = 0

    for i in itertools.count():
        if string[ooo] == count_char:
            character_amount = character_amount + 1
            ooo = ooo + 1

        else:
            ooo = ooo + 1

        if ooo == o and character_amount == 0:
            print('Unfortunately we couldnt find the character you were looking for in the given text, please try again.')
            string = (input('Type anything: '))
            o = len(string) - 1
            count_char = (input('Type a character to find out the amount of it in the previous entered text: '))
            oo = len(count_char)
            while oo != 1:
                    count_char = (input('Input a single character only!: '))
                    oo = len(count_char)
            character_amount = 0
            ooo = 0
            i = o

        elif ooo == o:
             break
        
    return character_amount()  #vergavige es return saatebia vchalichob vax
        
        
manual_count()        
