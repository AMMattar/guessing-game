#reminding myself the all ways to conctinating p.s spelling are completely wrong but who cares ;(
#youtuber = 'Ahmed Mamdouh Mattar'
#print('subscribe to '+ youtuber)
#print('subscribe to {}'.format(youtuber))
#print(f'subscribe to {youtuber}')
import random

def guss(x):
    comp = random.randint(1, x)
    human_guss = 0
    while human_guss != comp:
        human_guss = int(input(f"what do you think my nyumber is? it's between 1 and {x}: "))
        if human_guss < comp:
            print('sorry, guess again too low')
        elif human_guss > comp:
            print('sorry, guess again too high')
    print(f"congrats you have guessed the correct number {comp}, good job!")


def com_guss(x):
    low = 1
    high = x
    feed_back = ""
    while feed_back != "c":  #and low != high
        if low != high:
            guess = guess = random.randint(low, high)
        else:
            guess = low
        feed_back = input(f'is my guess {guess} high(h), low(l), or correct(c)?: ').lower()
        if feed_back == "h":
            high = guess -1
        elif feed_back == "l":
            low = guess +1
    print(f"yay, I did it, i know your number {guess}")

print('Lets play a game together, guess my number')
guss(10)
print("now is my turn to guess")
com_guss(20)
