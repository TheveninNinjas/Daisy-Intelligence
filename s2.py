### original code
import copy
from random import choice

class square:
    def __init__(self,ID,val):
        self.ID = ID
        self.value = val
        self.bigSq = self._getbigSq() #board number
        self.smallSq = self._getsmallSq() #ID with a board
    def _getbigSq(self):
        #return 3*int(self.ID/27) + int((self.ID%9)/3)
        return int(self.ID/9)
    def _getsmallSq(self):
        return self.ID%9

def findValidMoves(squares,nextsquare):
    vm = []
    for i in range(81):
        if squares[i].bigSq==nextsquare or nextsquare>8:  #Have to play in the next square, unless you can play anywhere
            if squares[i].value == 0: #Square must be empty
                if isBoardWon(getBigBoard(squares,squares[i].bigSq))==0: #Can't play in a won board; ==0 means not win yet
                    if not isBoardFull(getBigBoard(squares,squares[i].bigSq)): #Can't play in a full board
                        vm.append(i)
    return vm


def isBoardWon(squares):
    #Input: squares = 8 item list of squares 
    #Output: 0 if not win, 1 if 1 won, 2 if 2 won
    def compareSquares(squares,s1,s2,s3,v):
        if squares[s1]==squares[s2] and squares[s1]==squares[s3] and squares[s1]==v:
            return True
        else:
            return False
    if compareSquares(squares,0,1,2,1): return 1
    if compareSquares(squares,0,1,2,2): return 2
    if compareSquares(squares,3,4,5,1): return 1
    if compareSquares(squares,3,4,5,2): return 2
    if compareSquares(squares,6,7,8,1): return 1
    if compareSquares(squares,6,7,8,2): return 2
    if compareSquares(squares,0,3,6,1): return 1
    if compareSquares(squares,0,3,6,2): return 2
    if compareSquares(squares,1,4,7,1): return 1
    if compareSquares(squares,1,4,7,2): return 2
    if compareSquares(squares,2,5,8,1): return 1
    if compareSquares(squares,2,5,8,2): return 2
    if compareSquares(squares,0,4,8,1): return 1
    if compareSquares(squares,0,4,8,2): return 2
    if compareSquares(squares,2,4,6,1): return 1
    if compareSquares(squares,2,4,6,2): return 2
    return 0

def isBoardFull(squares):
    for i in range(9):
        if squares[i]==0:
            return False
    return True

def getBigBoard(squares,bigSq):
    sq = []
    for i in range(81):
        if squares[i].bigSq == bigSq:
            sq.append(squares[i].value)
    return sq




def get_move(timeout,data):
   
    PLAYER=int(data[0])
    # assign OPPONENT
    if PLAYER == 1:
        OPPONENT = 2
    else:
        OPPONENT = 1
        
        
    nextsquare=int(data[1])
    squares = []
    
    # a = data[17]
    # print(""a)
    
    for i in range(2,83): 
        squares.append(square(i-2,int(data[i])))  #create current board
    
    move = Strategy(nextsquare, squares, OPPONENT, PLAYER, data)
    
    #print(move)
    
    if move < 0 or move > 80:  
        validMoves=findValidMoves(squares,nextsquare)
        return choice(validMoves)
    
    
    if move is None:  
        validMoves=findValidMoves(squares,nextsquare)
        return choice(validMoves)
    
    return move
    
    # #play first move on a new board
    #if playFirst_newboard(nextsquare)==1:
    #     return newBoardMove(nestsquare, squares)
    # 
    # #play first move on a playing board or play second move
    # if not playFirst_newboard(nextsquare):
    #     #play first
    #     if countFilledSquares(nextsquare, squares)%2 == 0: #count is an even number
    #         
        
    
    
    #validMoves=findValidMoves(squares,nextsquare)
    #return choice(validMoves)
    
    #test:
    #square = []




###strategy part

def Strategy(nextsquare, squares, OPPONENT, PLAYER, data):
    corner = [0, 2, 6, 8]
    edge = [1, 3, 5, 7]
    
    #generate a little square
    littleSquare = [];
    for i in range(81):
        if squares[i].bigSq == nextsquare: #when it is the current board we are playing on
            littleSquare.append(square(i,squares[i].value))
            
            
    
    
    ### play on a empty board
    if playFirst_newboard(nextsquare):
        move_ = newBoardMove(nextsquare, squares, corner,OPPONENT, PLAYER, edge, data)
        
        return move_
    
    
    count = countFilledSquares(nextsquare, littleSquare);

    

    
    ### play on a non empty board
    if not playFirst_newboard(nextsquare):
        # # check if you already win or block the opponent
        # if is_opponent_winning(data) != -1:
        #     return convertSquareID_to_BoardID(nextsquare, is_opponent_winning(data))
        # else:
            # other cases
            move_in_littleSquare = determineMove(nextsquare, littleSquare, OPPONENT,PLAYER, corner, edge, squares, data)
            if move_in_littleSquare is None:
                validMoves=findValidMoves(squares,nextsquare)
                return choice(validMoves) 
            move = convertSquareID_to_BoardID(nextsquare,move_in_littleSquare)
            return move
        
def countNum_player(PLAYER,littleSquare):
    countNum_p = 0
    for i in range (8):
        if littleSquare[i].value == PLAYER:
            countNum_p += 1
    return countNum_p

def countNum_opponent(OPPONENT,littleSquare):
    countNum_o = 0
    for i in range (8):
        if littleSquare[i].value == OPPONENT:
            countNum_o += 1
    return countNum_o
                                    
# outputs the id on littleSquare
def determineMove(nextsquare, littleSquare, OPPONENT,PLAYER, corner, edge,squares, data):
        if isWin(littleSquare, PLAYER) != -1:
            return isWin(littleSquare, PLAYER)
        if isWin(littleSquare, OPPONENT) != -1:
            return isWin(littleSquare, OPPONENT)
        
        count = countFilledSquares(nextsquare, littleSquare);
        # print("count:")
        # print(count)
        if count%2 == 0: #count is an even number
            #------------------for the first move
            if(count == 0):
                    
                return 0
        
        
        
          ################### play first
        if countNum_player(PLAYER,littleSquare) - countNum_opponent(OPPONENT,littleSquare) == 1: # check if it's a regular board:
            
          
                    
                #------------------for the second move
                if(count == 2):
                    
                    # print(OPPONENT)
                    # print(littleSquare[4])
                    #check if O is at center or not
                    if(littleSquare[4].value == OPPONENT): #O is at centre
                        #current board: 100 020 000
                        #two strategies: diagonal or edge
                        #here uses diagonal: place at 8
                        if littleSquare[8].value == 0: #when it's empty
                            return 8
                        
                    else: #O is not at center
                        #place at any corner that has one space between the first X
                        
                        
                        for i in range(4):
                            
                            if littleSquare[corner[i]].value == OPPONENT: #if O is on the corner
        
                                for l in range(4):
                                    #when it's empty append it
                                    if littleSquare[corner[l]].value == 0:
                                        return corner[l]
                            else: #if O is on the edge
                                if littleSquare[edge[i]].value == OPPONENT:
                                    
                                    n = edge[i]
                                        
                                    #print(n)
                                    if n == 1 or n == 5:
                                        if littleSquare[6].value == 0:
                                            return 6
                                    if n == 3 or n == 7:
                                        if littleSquare[2].value == 0:
                                            return 2
                
                #------------------for the third move and above
                if(count > 2):  
                    if(count == 4):
                        if(littleSquare[4].value == OPPONENT): #1: O is at centre
                            
                            for i in range (4):
                                if littleSquare[corner[i]].value == OPPONENT:#2: O on the corner
                                    for l in range(4):
                                        if littleSquare[corner[l]].value == 0:
                                            return corner[l]
                                else:
                                    #ROS
                                    return convertBoardID_to_SquareID(choose(squares, nextsquare))
                                
                    else:
                    #ROS
                        return convertBoardID_to_SquareID(choose(squares, nextsquare))
                    
                else:
                    #ROS
                    return convertBoardID_to_SquareID(choose(squares, nextsquare))
                
         
        
            
        
        ####################### play second
        elif countNum_opponent(OPPONENT,littleSquare) - countNum_player(PLAYER,littleSquare) == 1:
            
            #count is an odd number
            #------------------for the first move
            if(count == 1):
                for i in range (4):
                    if littleSquare[edge[i]].value == OPPONENT: #when opponent plays at the edge node
                        #print("lala")
                        n = edge[i]
                        if n == 1 or n == 3:
                            #if littleSquare[0].value == 0:
                                return 0
                        if n == 1 or n == 5:
                            #if littleSquare[2].value == 0:
                                return 2
                        if n == 3 or n == 7:
                            #if littleSquare[6].value == 0:
                                return 6
                        if n == 5 or n == 7:
                            #if littleSquare[8].value == 0:
                                return 8
                        
                    elif littleSquare[corner[i]].value == OPPONENT: #when opponent plays at corner
                        return 4;
                    elif littleSquare[4].value == OPPONENT: #when opponent plays at center
                        return 0; #returns one of the corner nodes
                    else:
                        #ROS
                        return convertBoardID_to_SquareID(choose(squares, nextsquare))
                        
                
            #------------------for the second move
            elif(count == 3):
                for i in range (4):
                    if littleSquare[edge[i]].value == OPPONENT: #when opponent plays at the edge node
                        if littleSquare[4].value == 0: # when opponent does not play at center
                            return 4;
                        else:
                            #ROS
                            return convertBoardID_to_SquareID(choose(squares, nextsquare))
                            
                    elif littleSquare[corner[i]].value == OPPONENT: #when opponent plays at corner
                        # we should play at the edge
                        for l in range(4):
                            if littleSquare[edge[l]].value == 0:
                                #print("lala")
                                return edge[l]
                            else:
                                #ROS
                                return convertBoardID_to_SquareID(choose(squares, nextsquare))
                    else:
                        #ROS
                        return convertBoardID_to_SquareID(choose(squares, nextsquare))
            
            #------------------for the third move and above
            else:
                #ROS
                return convertBoardID_to_SquareID(choose(squares, nextsquare))
                
    
                    
        else: ### when it is not regular board
            #ROS!!
            return convertBoardID_to_SquareID(choose(squares, nextsquare))
      
    

#check if you are playing first or second
def playFirst_newboard(nextsquare):
    if nextsquare == 9:
        return True
        
def newBoardMove(nextsquare, squares, corner,OPPONENT, PLAYER, edge,data):
        #pick an empty board
        #generate the little board using boardwon output
        
        #check for initial case:
        begin = 1
        for i in range(81):
            if squares[i].value != 0:
                begin = 0
        
        if begin:
            return 0
            
            
        littleSquare_ = []
        for i in range(9):
            sq = getBigBoard(squares,i)
            winner = isBoardWon(sq)
            if winner == 0:
                winner = -1
            littleSquare_.append(square(i, winner))
            # determineMove gives which littleSquare to play
        #move = determineMove(0, littleSquare_, OPPONENT,corner, move)*9 #the first square in the littleSquare 
        move = determineMove(0, littleSquare_, OPPONENT,PLAYER, corner, edge,squares, data) + nextsquare*9
    
        return move
        
            
            
        
    
def countFilledSquares(nextsquare, littleSquare):
    count = 0
    for i in range(9):
        if littleSquare[i].value != 0: 
                count += 1
    return count


def convertSquareID_to_BoardID(nextsquare, squareID):
    #print(squareID)
    ID = squareID+9*nextsquare
    # print(ID)
    return ID
    
def convertBoardID_to_SquareID(BoardID):
    #print(squareID)
    Square_ID = BoardID%9
    # print(ID)
    return Square_ID
    
    
    
# check if you already win

        
# block the opponent
        
# other cases
    
  

########## isWinning

#check if our robot needs to start a game on a new board

def choose_new_board(game_status):

    #second_num = str(game_status)

    if game_status[1] == '9' :

        return True

    else:

        return False

    

# """this function ONLY checks the small board that we are currently playing on
# it returns False if it does not see two opponent's marks that would lead to the opponent's victory
# in the next round anywhere
# if our team is about to win = return 2
# if the opponent is about to win = return 1
# if nothign = return 0 """


#check if our robot needs to start a game on a new board

def choose_new_board(game_status):

    #second_num = str(game_status)

    if game_status[1] == '9' :

        return True

    else:

        return False

    

"""this function ONLY checks the small board that we are currently playing on

it returns False if it does not see two opponent's marks that would lead to the opponent's victory

in the next round anywhere

if our team is about to win = return 2
if the opponent is about to win = return 1
if nothign = return 0 """

def is_opponent_winning(game_status):

    board_array = []
    output_val = 0
 
    if game_status[0] == '1':
        my_mark = '1'
        opponent_mark = '2'
    else:
        my_mark = '2'
        opponent_mark = '1'

    if choose_new_board(game_status) == True:

        output_val = 0

    else: 
        board_using = int (game_status[1])

  #This if statement is to accomodate Roz's function
    if (len(game_status) <= 11):
        board_array = game_status [2:11]
    else:
        board_array = game_status [board_using * 9 + 2: (board_using + 1) * 9 + 2] 

        #check diagonally
        if (board_array[4] == '0'):

            if (board_array[0] == my_mark and board_array[8] == my_mark): # " \ " direction
                return 2
            elif (board_array[0] == opponent_mark and board_array[8] == opponent_mark):
                output_val = 1
            if (board_array[2] == my_mark and board_array[6] == my_mark):# " / " direction
                return 2
            elif (board_array[2] == opponent_mark and board_array[6] == opponent_mark): 
                output_val = 1
             

        elif (board_array[4] == opponent_mark):
            if (board_array[2] == opponent_mark or board_array[6] == opponent_mark or board_array[0] == opponent_mark or board_array[8] == opponent_mark): 

                output_val = 1

        elif (board_array[4] == my_mark):
            if (board_array[2] == my_mark or board_array[6] == my_mark or board_array[0] == my_mark or board_array[8] == my_mark):
        
                return 2

        for row in range (3):

            opp_sum_v = 0
            opp_sum_h = 0
            my_sum_v = 0
            my_sum_h = 0

            for clm in range (3): 

                if board_array[row * 3 + clm] == opponent_mark:#check each row to see if there are two opp's marks
                    opp_sum_h = opp_sum_h + 1
                elif board_array[row * 3 + clm] == my_mark:
                        my_sum_h = my_sum_h + 1
     
                if board_array [clm * 3 + row] == opponent_mark:
                    opp_sum_v = opp_sum_v + 1
                    
                elif board_array [clm * 3 + row] == my_mark:
                    my_sum_v = my_sum_v + 1
            
            if (my_sum_v == 2 or my_sum_h == 2):
                return 2
            
            if (opp_sum_h== 2 or opp_sum_v == 2):
                output_val = 1

        return output_val

        

         

            



########### minmax



		
def choose(current_state, data): #function that determines what move the computer should generate using minimax. Takes a string squares and a board number data
  
  moves=[]
  nochoice=-5
  losechoice=0
  moves=findValidMoves(current_state, data) #generate possible moves
  nummoves=len(moves)
  
  for i in range(0, nummoves):
   temp_board=copy.deepcopy(current_state)
   #print(moves[i])
   
   new_state=change_state(temp_board, moves[i], 1)
   if data!=9:
    if moves[i]==4 or moves[i]==13 or moves[i]==22 or moves[i]==31 or moves[i]==49 or moves[i]==58 or moves[i]==67 or moves[i]==76:
     data=4
   score=YourMove(new_state, data) #Evaluate oponent's possible moves if computer generates this move
   if (score==10): return moves[i] #if computer's move generates a possible win, play this move
   elif (score==0): nochoice=moves[i] #if no win is possible, play a 0 move (generate a tie)
   else: losechoice=moves[i] #losing move better than no move
   
  if nochoice==-5:
   return losechoice
  else:
   return nochoice

def change_state(current_state, move, player): #updates the board based on a move
	current_state[move].value=player
	return current_state

	
def MyMove(current_state, data): #minimax function 1. Takes a game setting based and figures out possible results
	
	if isBoardFull(getBigBoard(current_state,data)) or (isBoardWon(getBigBoard(current_state,data)) != 0): #if the game is in a end state...
		if isBoardWon(getBigBoard(current_state, data))==1:
			return 10										#return max score (10) if the computer wins in this state
		elif isBoardWon(getBigBoard(current_state, data))==2:
			return -10										#return min score (-10) if opponent wins
		else: 
			return 0				#tie
	
	moves=[]	
	temp_board=current_state
	moves=findValidMoves(temp_board, data)				
	nummoves=len(moves)
	best=-1000
	
	for i in range(0, nummoves):
		new_state=change_state(temp_board, moves[i], 1) #evaluate the result if this possible move is played
		boardeval=YourMove(new_state, data)
		
		if boardeval>best: #choose highest level result
			best=boardeval
	
	return best
	
def YourMove(current_state, data): #predicting the opponent's move based on game state. Minimax function 2
	
	if isBoardFull(getBigBoard(current_state,data)) or (isBoardWon(getBigBoard(current_state,data)) != 0):
		if isBoardWon(getBigBoard(current_state, data))==1:
			return 10
		elif isBoardWon(getBigBoard(current_state, data))==2:
			return -10
		else: 
			return 0

	moves=[]
	temp_board=current_state
	moves=findValidMoves(temp_board, data)
	nummoves=len(moves)
	best=1000
	
	for i in range(0, nummoves):
		new_state=change_state(temp_board, moves[i], 2)
		boardeval=MyMove(new_state, data)
		
		if boardeval<best:
			best=boardeval
	
	return best


# returns the move
def isWin(littleSquare, person):
    #for i in range (8):
        if littleSquare[0].value == littleSquare[1].value == person:
            if  littleSquare[2].value == 0:
                return 2
        if littleSquare[0].value == littleSquare[3].value == person:
            if  littleSquare[6].value == 0:
                return 6
        if littleSquare[1].value == littleSquare[2].value == person:
            if  littleSquare[0].value == 0:
                return 0
        if littleSquare[1].value == littleSquare[4].value == person:
            if  littleSquare[7].value == 0:
                return 7
        if littleSquare[2].value == littleSquare[5].value == person:
            if  littleSquare[8].value == 0:
                return 8
        if littleSquare[3].value == littleSquare[4].value == person:
            if  littleSquare[5].value == 0:
                return 5
        if littleSquare[3].value == littleSquare[6].value == person:
            if  littleSquare[0].value == 0:
                return 0
        if littleSquare[4].value == littleSquare[5].value == person:
            if  littleSquare[3].value == 0:
                return 3
        if littleSquare[4].value == littleSquare[7].value == person:
            if  littleSquare[1].value == 0:
                return 1
        if littleSquare[5].value == littleSquare[8].value == person:
            if  littleSquare[2].value == 0:
                return 2
        if littleSquare[6].value == littleSquare[7].value == person:
            if  littleSquare[8].value == 0:
                return 8
        if littleSquare[7].value == littleSquare[8].value == person:
            if  littleSquare[6].value == 0:
                return 6
        if littleSquare[0].value == littleSquare[2].value == person:
            if  littleSquare[1].value == 0:
                return 1
        if littleSquare[0].value == littleSquare[6].value == person:
            if  littleSquare[3].value == 0:
                return 3
        if littleSquare[2].value == littleSquare[8].value == person:
            if  littleSquare[5].value == 0:
                return 5
        if littleSquare[6].value == littleSquare[8].value == person:
            if  littleSquare[7].value == 0:
                return 7
        if littleSquare[0].value == littleSquare[8].value == person:
            if  littleSquare[4].value == 0:
                return 4
        if littleSquare[2].value == littleSquare[6].value == person:
            if  littleSquare[4].value == 0:
                return 4
        
        return -1
        
   
def get9(current_state):
 sum=0
 best=-10000
     
    
 for i in range(9):
  if isBoardFull(getBigBoard(current_state, i))!= False or isBoardWon(getBigBoard(current_state, i))!=0:
   ++i
  moves=[]
 
  moves=findValidMoves(current_state, i) #generate possible moves for this board
  nummoves=len(moves)
  
  for i in range(nummoves):
   temp_board=copy.deepcopy(current_state)
   #print(moves[i])
 
   new_state=change_state(temp_board, moves[i], 1)
   data=i
   if moves[i]==4 or moves[i]==13 or moves[i]==22 or moves[i]==31 or moves[i]==49 or moves[i]==58 or moves[i]==67 or moves[i]==76:
    if not isBoardFull(getBigBoard(current_state, 4)) and isBoardWon(getBigBoard(current_state, 4))==0:
     data=4   
     
   score=YourMove(new_state, data) #Evaluate oponent's possible moves if computer generates this move
   sum+=score
   
   if sum>best:
    sum=best
    bestboard=i

 return bestboard
 
 
def get9(squares):

 current_state = []
 big_grid=[]
 big_grid_list=[]
 PLAYER=int(squares[0])
 nextsquare=int(squares[1])
 for i in range(2,83): 
  current_state.append(square(i-2,int(data[i])))
 for i in range(9):
  if isBoardFull(getBigBoard(current_state, i))!= False:
    big-grid.append(-1)
  elif isBoardWon(getBigBoard(current_state, i))==1:
    big_grid.append(1)
  elif isBoardWon(getBigBoard(current_state, i))==2:
   big_grid.append(2)
  else:
   big_grid.append(0) 
  
 nextmove=choose_new_board(big-grid) #takes a string
 if nextmove!=-1:
  return nextmove
 
 for i in range(2,11): 
  big_grid_list.append(square(i-2,int(big-grid[i])))
  
    

 return choose(big_grid_list, 9)


#check if our robot needs to start a game on a new board

def choose_new_board(game_status):

    #second_num = str(game_status)

    if game_status[1] == '9' :

        return True

    else:

        return False

    






#testing function
def test():
    data_ = input("data is: ")
    
    data = str(data_).replace(" ","")
    
    # player = "1"
    # board = "0"
    # board0 = input("board0 is: ")
    # # # board1 = input("board1 is: ")
    # # # board2 = input("board2 is: ")
    # # # board3 = input("board3 is: ")
    # # # board4 = input("board4 is: ")
    # # # board5 = input("board5 is: ")
    # # # board6 = input("board6 is: ")
    # # # board7 = input("board7 is: ")
    # # # board8 = input("board8 is: ")
    # # 
    # # #board0 = "000000000"
    # board1 = "000000000"
    # board2 = "000000000"
    # board3 = "000000000"
    # board4 = "000000000"
    # board5 = "000000000"
    # board6 = "000000000"
    # board7 = "000000000"
    # board8 = "000000000"

    #data = player + board + str(board0) + str(board1) + str(board2) + str(board3) + str(board4) + str(board5) + str(board6) + str(board7) + str(board8)
    # # print(data)
    #print(len(data))
    
    
    print("move sould be:")
    return get_move(10, data)
    

   