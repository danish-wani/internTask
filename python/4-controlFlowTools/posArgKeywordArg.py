def cheeseshop(kind,*arguments,**keywords):
    print(kind)

    for arg in arguments:
        print(arg)
    print(40 * '-')

    for keys in keywords:
        print(keys)



cheeseshop('burger','its very runny sir', 'its really very very runny sir',shopkeeper='michael',client='john',sketch='cheese shop sketch')
