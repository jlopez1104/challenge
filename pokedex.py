pokedex={}
pokemon ={'Pikachu':'60 Hp',
'charzard':'120 Hp',
'nidoran':'70 Hp',
'Mewto':'140 Hp',
'muk':'100 Hp'}
while True
    print("/nMenu")
    print("1. To add a pokemon")
    print("2. change Hp of a pokemon in pokedex")
    print("3. Check to see if pokemon is in the pokedex")
    print("4. Exit")
    choice = input("please enter in number(1/2/3/4): ")
    if choice == 1:

    elif choice == 2:
        hp 
    elif choice == 3:
        n = input('enter a pokemon:')
        if n in pokemon:
            print('in list. HP  of pokemon is: ',pokemon[n])
        else:
            print('not found')
