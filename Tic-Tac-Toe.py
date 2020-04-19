
global stop
stop = 0
#enumerate() is a built in function. It simply returns the index value of a list element along with the list element.
def game_board(row=0 , column=0 , player=0):
    print("   0  1  2")
    if player !=0:
        game[row][column] = player
    for count , row in enumerate(game):
        print(count , row)


def winner_declare(current_game):
    #for horizontal
    for row in current_game:
        sum1 = 0
        for item in range(0 , len(row)):
            sum1 = sum1 + row[item]
            if row[item]==0:
                sum1 = 0.5
        if sum1%len(row)==0 and sum1!=0:
            print(row)
            print("Player" , int(sum1/len(row)) ,  "is the Winner By Horizontal Rule")
            return 1

    #for vertical
    i = 0
    for row in current_game:
        sum2 = 0
        for item in range(0 , len(row)):
            sum2 = sum2 + current_game[item][i]
            if current_game[item][i]==0:
                sum2 = 0.5
            

        if sum2%len(row)==0 and sum2!=0:
            print("Player" , int(sum2/len(row)) ,  "is the Winner By Vertical Rule")
            return 1
        i = i+1

    #for first diagonal
    sum3 = 0
    for item in range(0 , len(current_game)):
        sum3 = sum3 + current_game[item][item]
        if current_game[item][item]==0:
            sum3 = 0.5

    if sum3%len(current_game)==0 and sum3!=0:
        print("Player" , int(sum3/len(row)) ,  "is the Winner By 1st Diagonal Rule")
        return 1


    #for second diagonal
    sum4= 0
    for j in range(0 , len(current_game)):
        sum4 = sum4 + current_game[j][-(j+1)]
        if current_game[j][-(j+1)]==0:
            sum4 = 0.5

    if sum4%len(current_game)==0 and sum4!=0:
        print("Player" , int(sum4/len(row)) ,  "is the Winner By 2nd Diagonal Rule")
        return 1



play = True
game = [[0 , 0 , 0] , [0 , 0 , 0] , [0 , 0 , 0]]
print("   0  1  2")
for count , row in enumerate(game):
    print(count , row)
while play:
    try:
        '''players = [1 , 0]
        choice = 1
        for me in range(100):
            current_player = choice
            player_choice = players[current_player] + 1
            print("Current Player" , "=" , player_choice)
            choice = 1 - current_player 

           '''
        for me in range(100):
            row_choice = int(input("Enter row you want to choose? (0 , 1 , 2)"))
            column_choice = int(input("Enter column you want to choose? (0 , 1 , 2)"))
            player_choice = int(input("Which player are you? (1 or 2)"))
            game_board(row_choice , column_choice , player_choice)
            x = winner_declare(game)
            if x==1:
                break
            play = False
    except:
        print("Please enter appropriate row/column or player")
        flag = 1
        
    
    

'''
def ver(current_game):
    i = 0
    new = []
    for row in current_game:
        sum = 0
        for item in range(0 , len(row)):
            sum = sum + current_game[item][i]
            

        if sum%len(row)==0 and sum!=0:
            print("winner By Vertical Rule")
        i = i+1

def first_diagonal(current_game):
    sum = 0
    for item in range(0 , len(current_game)):
        sum = sum + current_game[item][item]

    if sum%len(current_game)==0 and sum!=0:
        print("Winner By 1st Diagonal Rule")



def second_diagonal(current_game):
    sum= 0
    for i in range(0 , len(current_game)):
        sum = sum + current_game[i][-(i+1)]

    if sum%len(current_game)==0 and sum!=0:
        print("Winner By 2nd Diagonal Rule")
   
                
hori(game)
ver(game)
first_diagonal(game)
second_diagonal(game)
'''






#While calling the function in any where in the code. The position of arguments doesn't matter only if all the arguments are positional.
#First argument in the function declaring section can be called at last in the calling section.
#USe global keyword to make a variable declared inside a function global so that it could be accessed from any part of the code
#strip() removes all the whitespace present in a string
#In the print statement or in a variable we can put {} curly braces where we can add values later. It works as %d in C programming. We have to use format() to add value later to the var.
# In set if you want to add single item add() method can be used and to add multiple items we should use update() method.
#Sets are unordered and unindexed
#Dictionaries are changeable , unordered and indexed
#dictionaries are indexed with the keyNames not with the 0,1,2 and all that.
#clear method empties the entire dictionary.
#strings are immutable.
#we cannot change the object itself but we can modify the elements of the object.
#Try and Except is a method to prevent the error messages in the program if any error comes to the code. Code inside try if brings out any error instead of error messages code inside except executes.
#finally keyword in error handling just runs code inside irrespective of whatever the error is.
#raise keyword is used to raise an error ourselves where we tend to.
#reversed() is a function that completely reverses the elements in a list. It doesn't give the list. To get the reversed list we have to use list(reversed(required_list)).





 







    





