pokedex={}
pokemon ={'Pikachu': 60,
'charzard':120,
'nidoran':70,
'Mewto':140,
'muk':100}
while True
    print("/nMenu")
    print("1. To add a pokemon")
    print("2. change Hp of a pokemon in pokedex")
    print("3. Check to see if pokemon is in the pokedex")
    print("4. Exit")
    choice = input("please enter in number(1/2/3/4): ")
    if choice == 1:
        name = input('enter pokemon name: ')
        Hp = int(input('Enter pokemon Hp'))
        pokemon[name]=Hp
        print (pokemon)
    elif choice == 2:
        name = input('enter pokemon name: ')
        Hp = int(input('Enter pokemon Hp'))
        pokemon[name]=Hp
        print (pokemon)

    elif choice == 3:
        name = input('enter a pokemon:')
        if n in pokemon:
            print('in list. HP  of pokemon is: ',pokemon[name])
        else:
            print('not found')
