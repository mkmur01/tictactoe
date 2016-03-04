import random
def printBoard():
    i = 0
    while i<9:
        if(i+1)%3==0:
            print(board[i])
            if(i+1)%9!=0:
                print("_____")
            else:
                print('---------------')
        else:
            print(board[i] + '|', end="")
        i+=1


def play(type, space):
    board[space-1] = type

def compPlay(type):
    comp=type
    open=[]
    better=[]
    best= []
    numOpen=0
    numBetter=0
    numBest=0
    defense=-1


    if board[0]!='X' and board[0]!='O':
        if((board[1]==comp and board[2]==comp) or (board[3]==comp and board[6]==comp) or (board[4]==comp and board[8]==comp)):

            return 0

        if((board[1]==human and board[2]==human) or (board[3]==human and board[6]==human) or (board[4]==human and board[8]==human)):

            defense=0


    if(board[1]!='X' and board[1]!='O'):

        if((board[0]==comp and board[2]==comp) or (board[4]==comp and board[7]==comp)):
            return 1

        if((board[0]==human and board[2]==human) or (board[4]==human and board[7]==human)):

            defense=1


    if(board[2]!='X' and board[2]!='O'):

        if((board[1]==comp and board[0]==comp) or (board[5]==comp and board[8]==comp) or (board[4]==comp and board[6]==comp)):

            return 2

        if((board[1]==human and board[0]==human) or (board[5]==human and board[8]==human)):

            defense=2


    if(board[3]!='X' and board[3]!='O'):

        if((board[4]==comp and board[5]==comp) or (board[0]==comp and board[6]==comp)):

            return 3

        if((board[4]==human and board[5]==human) or (board[0]==human and board[6]==human)):

            defense=3


    if(board[4]!='X' and board[4]!='O'):

        if((board[3]==comp and board[5]==comp) or
            (board[1]==comp and board[7]==comp) or
                    (board[0]==comp and board[8]==comp) or
                    (board[2]==comp and board[6]==comp)):

            return 4

        if((board[3]==human and board[5]==human) or
                    (board[1]==human and board[7]==human) or
                    (board[0]==human and board[8]==human) or
                    (board[2]==human and board[6]==human)):

            defense=4


    if(board[5]!='X' and board[5]!='O'):

        if((board[3]==comp and board[4]==comp) or (board[2]==comp and board[8]==comp)):

            return 5

        if((board[3]==human and board[4]==human) or (board[2]==human and board[8]==human)):

                defense=5


    if(board[6]!='X' and board[6]!='O'):

        if((board[7]==comp and board[8]==comp) or
                    (board[0]==comp and board[3]==comp) or
                    (board[4]==comp and board[2]==comp)):

            return 6

        if((board[7]==human and board[8]==human) or
                    (board[0]==human and board[3]==human) or
                    (board[4]==human and board[2]==human)):

            defense=6


    if(board[7]!='X' and board[7]!='O'):

        if((board[6]==comp and board[8]==comp) or (board[1]==comp and board[4]==comp)):

            return 7

        if((board[6]==human and board[8]==human) or (board[1]==human and board[4]==human)):

            defense=7


    if(board[8]!='X' and board[8]!='O'):

        if((board[6]==comp and board[7]==comp) or
                    (board[2]==comp and board[5]==comp) or
                    (board[4]==comp and board[0]==comp)):

            return 8

        if((board[6]==human and board[7]==human) or
                    (board[2]==human and board[5]==human) or
                    (board[4]==human and board[0]==human)):

            defense=8



    if(defense>-1):
        return defense
    if(board[0]!=human and board[0]!=comp):

        open.append(0)
        numOpen+=1
        if((board[1]==comp and board[2]!=human) or board[2]==comp and board[1]!=human):

            if((board[3]==comp and board[6]!=human) or board[6]==comp and board[3]!=human):

                best.append(0)
                numBest+=1

            else:

                better.append(0)
                numBetter+=1


        if((board[3]==comp and board[6]!=human) or board[6]==comp and board[3]!=human):

            better.append(0)
            numBetter+=1


    if(board[1]!=human and board[1]!=comp):

        open.append(1)
        numOpen+=1
        if((board[0]==comp and board[2]!=human) or board[2]==comp and board[0]!=human):

            if((board[4]==comp and board[7]!=human) or board[7]==comp and board[7]!=human):

                best.append(1)
                numBest+=1

            else:

                better.append(1)
                numBetter+=1


        if((board[4]==comp and board[7]!=human) or board[7]==comp and board[4]!=human):

            better.append(1)
            numBetter+=1


    if(board[2]!=human and board[2]!=comp):

        open.append(2)
        numOpen+=1
        if((board[1]==comp and board[0]!=human) or board[0]==comp and board[1]!=human):

            if((board[5]==comp and board[8]!=human) or board[8]==comp and board[5]!=human):

                best.append(2)
                numBest+=1

            else:

                better.append(2)
                numBetter+=1


        if((board[5]==comp and board[8]!=human) or board[8]==comp and board[5]!=human):

            better.append(2)
            numBetter+=1


    if(board[3]!=human and board[3]!=comp):

        open.append(3)
        numOpen+=1
        if((board[4]==comp and board[5]!=human) or board[5]==comp and board[4]!=human):

            if((board[0]==comp and board[6]!=human) or board[6]==comp and board[0]!=human):

                best.append(3)
                numBest+=1

            else:

                better.append(3)
                numBetter+=1


        if((board[0]==comp and board[6]!=human) or board[6]==comp and board[0]!=human):

            better.append(3)
            numBetter+=1


    if(board[4]!=human and board[4]!=comp):

        open.append(4)
        numOpen+=1
        if((board[3]==comp and board[5]!=human) or board[5]==comp and board[3]!=human):

            if((board[1]==comp and board[7]!=human) or board[7]==comp and board[1]!=human):

                best.append(4)
                numBest+=1

            else:

                better.append(4)
                numBetter+=1


        if((board[1]==comp and board[7]!=human) or board[7]==comp and board[1]!=human):

            better.append(4)
            numBetter+=1


    if(board[5]!=human and board[5]!=comp):

        open.append(5)
        numOpen+=1
        if((board[3]==comp and board[4]!=human) or board[4]==comp and board[3]!=human):

            if((board[2]==comp and board[8]!=human) or board[8]==comp and board[2]!=human):

                best.append(5)
                numBest+=1

            else:

                better.append(5)
                numBetter+=1


        if((board[2]==comp and board[8]!=human) or board[8]==comp and board[2]!=human):

            better.append(5)
            numBetter+=1


    if(board[6]!=human and board[6]!=comp):

        open.append(6)
        numOpen+=1
        if((board[7]==comp and board[8]!=human) or board[8]==comp and board[7]!=human):

            if((board[3]==comp and board[0]!=human) or board[0]==comp and board[3]!=human):

                best.append(6)
                numBest+=1

            else:

                better.append(6)
                numBetter+=1


        if((board[3]==comp and board[0]!=human) or board[0]==comp and board[3]!=human):

            better.append(6)
            numBetter+=1


    if(board[7]!=human and board[7]!=comp):

        open.append(7)
        numOpen+=1
        if((board[6]==comp and board[8]!=human) or board[8]==comp and board[6]!=human):

            if((board[1]==comp and board[4]!=human) or board[4]==comp and board[1]!=human):

                best.append(7)
                numBest+=1

            else:

                better.append(7)
                numBetter+=1


        if((board[1]==comp and board[4]!=human) or board[4]==comp and board[1]!=human):

            better.append(7)
            numBetter+=1


    if(board[8]!=human and board[8]!=comp):

        open.append(8)
        numOpen+=1
        if((board[6]==comp and board[7]!=human) or board[7]==comp and board[6]!=human):

            if((board[2]==comp and board[5]!=human) or board[5]==comp and board[2]!=human):

                best.append(8)
                numBest+=1

            else:

                better.append(8)
                numBetter+=1


        if((board[2]==comp and board[5]!=human) or board[5]==comp and board[2]!=human):

            better.append(8)
            numBetter+=1


    if(numBest>0):

        return best[random.randrange(numBest)]

    if(numBetter>0):
        return better[random.randrange(numBetter)]
    else:
        return open[random.randrange(numOpen)]

board = ['1','2','3','4','5','6','7','8','9']
human = ""
computer = ""
human = input("Would you like to be X or O")
while human != 'x' and human != 'o' and human != 'X' and human !="0":
    human = input("please enter X or O only")
if human == 'x':
    human ='X'
if human == 'X':
    computer = 'O'
if human == 'o':
    human = 'O'
if human == 'O':
    computer = 'X'


order = 0
space = 0
winner = 'd'

if human == 'O':
    order+=1

i = 0
while i<9:
    if (not((board[0]==board[1]and board[0]==board[2])or
    (board[3]==board[4]and board[3]==board[5])or
    (board[6]==board[7]and board[6]==board[8])or
    (board[0]==board[3]and board[0]==board[6])or
    (board[1]==board[4]and board[1]==board[7])or
    (board[2]==board[5]and board[2]==board[8])or
    (board[0]==board[4]and board[0]==board[8])or
    (board[2]==board[4]and board[2]==board[6]))):
        printBoard()

        if(i+order)%2==0:
            space = int(input("what space would you like to play?"))
            while not(space>0 and space<10):
                space = input("please enter a valid space")
            while str(board[space-1])=='X' or str(board[space-1])=='O':
                space = input("please enter a valid space")
            play(human, space)
        elif order == 0:
            play('O',compPlay('O')+1)
        else:
            play('X',compPlay('X')+1)

    elif((board[0]==human and board[1]==human and board[2]==human) or
    (board[3]==human and board[4]==human and board[5]==human) or
    (board[6]==human and board[7]==human and board[8]==human) or
    (board[0]==human and board[3]==human and board[6]==human) or
    (board[1]==human and board[4]==human and board[7]==human) or
    (board[2]==human and board[5]==human and board[8]==human) or
    (board[0]==human and board[4]==human and board[8]==human) or
    (board[2]==human and board[4]==human and board[6]==human)):
        winner='h'

    elif((board[0]==computer and board[1]==computer and board[2]==computer) or
    (board[3]==computer and board[4]==computer and board[5]==computer) or
    (board[6]==computer and board[7]==computer and board[8]==computer) or
    (board[0]==computer and board[3]==computer and board[6]==computer) or
    (board[1]==computer and board[4]==computer and board[7]==computer) or
    (board[2]==computer and board[5]==computer and board[8]==computer) or
    (board[0]==computer and board[4]==computer and board[8]==computer) or
    (board[2]==computer and board[4]==computer and board[6]==computer)):
        winner='c'
    i+=1


printBoard()
if winner == 'h':
    print("Congrats you win!")
elif winner == 'c':
    print("Sorry,  you lose.")
else:
    print("Cat game")
