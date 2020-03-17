#   automate the boring stuff, chapter 3 practice project
#   The Collatz Sequence

#   imports


def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            return number
            print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            return number
            print(number)
            print('We hit 1!!')





def main():
    print('Enter number:')
    number = int(input())
    print('You entered ' + str(number) + ' as your starting number.')

    print(collatz(number))
        



main()
