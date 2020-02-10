'''
Name: Emma Chen
Penn ID: 58117361
Statement of work:
    source of help: Google how to get out of one loop to another (before lecture).. later found answer in slide. 
Win: velocity >= 10 m/s
Loss: velocity < 10 m/s 
'''



game_running = True

#a while loop: while condition is met, run code block inside loop
#while game_running is True , run code block inside loop
while (game_running == True):

    altitude = 100.0 
    velocity = 0.0 
    fuel = 100.0 
    second = 0 
    #while loop: while condition is met, run code block inside loop
    while (altitude > 0):    
        while True:
            #get user input on how many fuel to use the next second
            usedfuel = input("Please put in a number for the amount of fuel you want to burn in the next second?")
            #catch input error 
            try:
                usedfuel=int(usedfuel)
                #if fuel input is negative, fuel used is 0
                if usedfuel < 0:
                    usedfuel = 0
                #if fuel input > fuel left, burn ALL fuel left
                if usedfuel > fuel:
                    usedfuel = fuel
                break
            #catch the raised exception if there is an error-i.e. it can't be casted
            except ValueError as e:
                print("Your input is not a number, please choose again.")
                print(e)
            
        altitude -= 1.6 #altitude decreases 1.6 meters per second
        velocity = velocity + 1.6 - (0.15 * usedfuel)
        fuel -= usedfuel #fuel(left) = fuel(before) - usedfuel
        second += 1 #time tracker, increase 1 second after every entry of fuel used   
        if velocity >= 10:
            print("Your landing is unsafe, your landing velocity is {} m/s,it took {} seconds to land, you have {} liter(s) fuel left.".format(str(velocity), str(second), str(fuel)))
            break       

    #users decide if they want to play again or not
    play = input("Do you want to play again (Y/y or N/n)?")
    while (play != 'Y' and play != 'y' and play != 'N' and play != 'n'):
        play = input("Please try again: Do you want to play again (Y/N or y/n)?")
        if (play == 'Y' or play == 'y'):
            game_running = True
        if (play == 'N' or play == 'n'):
            game_running = False
    
            

            
        

