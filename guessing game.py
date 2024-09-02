from random import randint
answer=randint(1,10)
while True:
    try:
        guess = int(input('guess a num between 1 to 10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('your right')
                break
        else:
            print('heyy print a number >0 or <11')
    except ValueError:
        print('please enter a num')



