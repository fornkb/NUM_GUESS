##©NKB
import random
print('''
Welcome to NUM_GUESS!!
NUM_GUESS is a mathematical number guessing game!!
(press enter key to continue)''')
simply=input()
print('''You will be guessing a random number which can be guessed\nby the given hints!!
Enter Y below to ENTER the game,N to quit!!''')
enter=(input("Enter Y/N: ")).upper()
if enter == "Y":
    print('''Now enter which difficulty level you want to play the game in!!
Easy/Medum/Hard''')
    mode=(input("Enter easy/medium/hard: ")).lower()
    if mode=="easy":
        print("EASY LEVEL")
        num=random.randint(1,100)
        for div in range(1,9):
            if num%div==0:
                a=div
        if a==1:
            print("The number is prime")
        else:
            print("The number is divisible by",a)
        pal=str(num)
        if pal==pal[::-1]:
            print("Number is Palindrome!")
        for btwn in range(0,112,16):
            if num in range(btwn,btwn+16):
                print("The number is between",btwn,"and",btwn+16)
        for i in range(3):
            guess=int(input("Now,Guess the number: "))
            if guess == num:
                print("Well Congrats!,Seems like you won the game!!")
                break
            elif i==2:
                print("The correct number was",num)
            elif i==1:
                sum1=0
                for x in str(num):
                    sum1+=int(x)
                print("Sum of digits=",sum1,"\nThis is your last chance,try again!")
            else:
                print("Uh oh,try again!!",(2-i),"chances left")
        print("GAME OVER!")
        simply=input()
    elif mode=="medium":
        print("MEDIUM LEVEL")
        num=random.randint(1,500)
        for div in range(1,9):
            if num%div==0:
                a=div
        if a==1:
            print("The number is prime")
        else:
            print("The number is divisible by",a)
        pal=str(num)
        if pal==pal[::-1]:
            print("Number is Palindrome!")
        for btwn in range(0,500,20):
            if num in range(btwn,btwn+20):
                print("The number is between",btwn,"and",btwn+20)
        for i in range(3):
            guess=int(input("Now,Guess the number: "))
            if guess == num:
                print("congrats!,You won the game!!")
                break
            elif i==2:
                print("The correct number was",num)
            elif i==1:
                sum1=0
                for x in str(num):
                    sum1+=int(x)
                print("Sum of digits=",sum1,"\nThis is your last chance,try again!")
            else:
                print("Uh oh,try again!!",(2-i),"chances left")
        print("GAME OVER!")
        simply3=input()
    elif mode =="hard":
        print("HARD LEVEL")
        num=random.randint(1,1020)
        for div in range(1,9):
            if num%div==0:
                a=div
        if a==1:
            print("The number is prime")
        else:
            print("The number is divisible by",a)
        pal=str(num)
        if pal==pal[::-1]:
            print("Number is Palindrome!")
        for btwn in range(0,1020,30):
            if num in range(btwn,btwn+30):
                print("The number is between",btwn,"and",btwn+30)
        for i in range(3):
            guess=int(input("Now,Guess the number: "))
            if guess == num:
                print("congrats!,You won the game!!")
                break
            elif i==2:
                print("The correct number was",num)
            elif i==1:
                sum1=0
                for x in str(num):
                    sum1+=int(x)
                print("Sum of digits=",sum1,"\nThis is your last chance,try again!")
            else:
                print("Uh oh,try again!!",(2-i),"chances left")
        print("GAME OVER!")
        simply=input()
    else:
        print("INVALID INPUT")
    
else:
    print("Thank you!")
    simply=input()
##©NKB

