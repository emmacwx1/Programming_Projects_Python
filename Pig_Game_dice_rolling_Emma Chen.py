"""
Name: Emma Wenxuan Chen
PennID: 58117361
Statement of Work:
-work independently
-read Piazza post and the Pig Game wiki link posted by TA on Piazza
"""
from random import randint


def print_instructions():
    """Print game instructions for players"""
    print("Welcome to Pig--our dice-rolling game! In this game, you and computer will roll a six-sided die. Rules are as following: "
          "1) In this game, you and computer will take turns rolling a die. You can roll as many times as you want, or until you roll a 6. "
          "2) From number 1 to 5, each number you roll will be added to your total score. If you roll a 6, your total score for the turn will be 0, your turn ends and it's computer's turn to roll. "
          "3) The first player to reach or exceed 50 wins. In another turn, you want to roll as many as possible from number 1-5 to reach or exceed total scores of 50 and to avoid rolling a 6."
          "4) Computer always rolls first. Because of first player advantage if the computer reaches or exceeds 50, you get one additional turn to roll. The turns to roll will be equal for both."
          "5) If you and computer BOTH are tied with 50 or more, you will take turn rolling until the tie is broken (you cannot roll as many times as you want in this situation). "
          "Have fun and good luck!")

def computer_move(computer_score, human_score):
    """Generate random number from 1-6 as computer score, displays result of each roll and return result. If computer leads human more than 5 in total score, stop rolling. """
    #computer tried to roll to lead as least more than 5 points than human
    while (computer_score - human_score < 5):
        computer_roll = roll()
        print("Computer rolled {} score(s).".format(str(computer_roll)))
        if computer_roll != 6:
            computer_score += computer_roll
        if computer_roll == 6:
            computer_score = 0
            break
        if computer_score >= 50:
            break
        #force computer to go at least once
        if computer_score - human_score >= 5:
            break
    print("Computer rolled {} score this turn.".format(str(computer_score)))
    return computer_score

def human_move(computer_score, human_score):
    """Return player's rolled scores"""

    human_play = ask_yes_or_no("Do you want to roll the dice for this turn?(Yes/No)")
    while human_play == False:
        #at least roll once per turn
        print("You need to at least roll once per turn.")
        human_play = ask_yes_or_no("Do you want to roll the dice for this turn?(Yes/No)")

    # repeatedly asked if roll again after each roll
    while human_play == True:
        human_roll = roll()
        if human_roll != 6:
            human_score += human_roll
            print("You just rolled {} score(s) and your total score this turn so far is {}.".format(str(human_roll), str(human_score)))
            human_play = ask_yes_or_no("Do you want to roll the dice for this turn?(Yes/No)")
        if human_roll == 6:
            human_score = 0
            break
        if human_score >= 50:
            break
    print("Your score for this turn is {}.".format(str(human_score)))
    return human_score

def is_game_over(computer_score, human_score):
    """determine if the game is over based on computer or player score"""

    if computer_score >= 50 or human_score >= 50 and computer_score != human_score:
        play = True
    else:
        play = False
    return play


def roll():
    """return a number from 1-6 randomly generated, as number that player or computer rolls"""

    return randint(1, 7)


def ask_yes_or_no(prompt):
    """prompts user to answer if ready to play the game, return True if user respond Yes; return False if user responds No"""
    while True:
        user_input = input(prompt)
        if user_input.startswith("Y") == True or user_input.startswith("y") == True:
            play = True
            break
        elif user_input.startswith("N") == True or user_input.startswith("n") == True:
            play = False
            break
        #invalid input, repeat question again
        else:
            print("Please choose again: Do you want to roll? (Yes/No)")
    return play

def show_current_status(computer_score, human_score):
    """return current status"""
    #call BEFORE AND AFTER human's move
    print("Your score is {} and computer's score is {}".format(str(human_score), str(computer_score)))
    score_difference = human_score - computer_score
    if score_difference > 0:
        print("You are {} score ahead of computer's.".format(str(score_difference)))
    if score_difference < 0:
        score_difference = -score_difference
        print("Your are {} score behind computer's.".format(str(score_difference)))
    if score_difference == 0:
        print("Work harder! Your total score is tight with computer's!!")


def show_final_results(computer_score, human_score):
    """Returns final results, how is the winner and win by how much"""
    score_diff = computer_score - human_score
    if computer_score >= 50 and computer_score > human_score:
        print("Computer wins by {} scores.".format(str(score_diff)))
    if human_score >= 50 and human_score > computer_score:
        score_diff = -score_diff
        print("You win computer by {} scores".format(str(score_diff)))


def main():
    """main function to run Pig game"""

    #print the game instructions
    print_instructions()

    #play determines whether the game will be played
    play = False

    #ask if player wants to play the Pig game
    user_ready = ask_yes_or_no("Are you ready to start the game? Computer will start rolling first if you say Yes! (Yes/No)")
    if user_ready == True:
        play = True
    #initial scores for both player and computer are 0
    computer_score = 0
    human_score = 0

    #start main game loop
    while play:
        computer_score += computer_move(computer_score, human_score)
        show_current_status(computer_score, human_score)
        human_score += human_move(computer_score, human_score)
        show_current_status(computer_score, human_score)
        game_over = is_game_over(computer_score, human_score)
        if game_over == False:
            break
    return show_final_results(computer_score, human_score)


#starter code
if __name__ == '__main__':
    main()

