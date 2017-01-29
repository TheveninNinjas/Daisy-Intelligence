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

    small_board_array = [];
    output_val = 0;

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

        small_board_array = game_status [board_using * 9 + 2: (board_using + 1) * 9 + 2] 

        #check diagonally
        if (small_board_array[4] == '0'):

            if (small_board_array[0] == my_mark and small_board_array[8] == my_mark): # " \ " direction
            	return 2
            elif (small_board_array[0] == opponent_mark and small_board_array[8] == opponent_mark):
            	output_val = 1
            if (small_board_array[2] == my_mark and small_board_array[6] == my_mark):# " / " direction
            	return 2
            elif (small_board_array[2] == opponent_mark and small_board_array[6] == opponent_mark): 
				output_val = 1
            	

        elif (small_board_array[4] == opponent_mark):
        	if (small_board_array[2] == opponent_mark or small_board_array[6] == opponent_mark or small_board_array[0] == opponent_mark or small_board_array[8] == opponent_mark): 

				output_val = 1

		elif (small_board_array[4] == my_mark):
			if (small_board_array[2] == my_mark or small_board_array[6] == my_mark or small_board_array[0] == my_mark or small_board_array[8] == my_mark):
				
				return 2

        for row in range (3):

            opp_sum_v = 0
            opp_sum_h = 0
            my_sum_v = 0
            my_sum_h = 0

            

            for clm in range (3): 

                if small_board_array[row * 3 + clm] == opponent_mark:#check each row to see if there are two opp's marks
                    opp_sum_h = opp_sum_h + 1
                elif small_board_array[row * 3 + clm] == my_mark:
					my_sum_h = my_sum_h + 1
					
                if small_board_array [clm * 3 + row] == opponent_mark:
                    opp_sum_v = opp_sum_v + 1
                    
                elif small_board_array [clm * 3 + row] == my_mark:
                	my_sum_v = my_sum_v + 1
            
            if (my_sum_v == 2 or my_sum_h == 2):
            	return 2
            	
            if (opp_sum_h== 2 or opp_sum_v == 2):
            	output_val = 1

        return output_val

        

         

            

#this is a test case

print (is_opponent_winning ('102000200005'))
