

#Code your own quiz assignment by Kelli Westmoreland

#Goal: Use python to perform the functions and run the quiz

easy_test = ["There are ___1___  seasons of the year.",
              "From Spring typically starts in the month of  ___2___."
              "Fall is also called ___3___.",
              "Leap year always occurs during the ___4___ season."] #timeanddate.com

intermediate_test = ["Winter is also called the ___1___ Solstice.",
              "We have seasons because the Earth spins around the ___2___ at an angle.",
              "Astronomers and scientists use the dates of equinoxes and ___3___ to mark the beginning and end of seasons.",
              "The four seasons are divided into ___4___ months each."] #timeanddate.com

hard_test = ["Seasons occur because of the ___1__ of the Earth's rotational axis.",
            "People in the Southern Hemisphere consider Sept 1 as the beginning of  ___2___.",
            "In the Northern Hemisphere, the June Solistice marks the start of ___3___ .",
            "The Northern and Southern Hemisphere seasons are  ___4___ of each other." ] #timeanddate.com

# answer keys for sentences
intermediate_answers = ['December', 'sun', 'solstices', 'three']

hard_answers = ['tilt', 'spring', 'summer', 'opposite']
def Greet():
	print "Welcome to the quiz" 

#choose game level from list 
def launch_levels(quiz_level):
    while True:
        if quiz_level == "easy":
            print "You chose 'easy'"
            return easy_test, easy_answers
        elif quiz_level == "intermediate":
            print "You chose 'intermediate'"
            return intermediate_test, intermediate_answers
        elif quiz_level == "hard":
            print "You chose 'hard'"
            return hard_test, hard_answers
#returning (output) specific test questions and answer key
def launch_game():
    quiz_level = raw_input('Choose easy, intermediate or hard here ==> ')
    if quiz_level == 'easy' or quiz_level == 'intermediate' or quiz_level == 'hard':
        sentence, answers = launch_levels(quiz_level)
        print sentence

        launch_answers(answers, sentence, show_blank_space)
    else:
        print "The choice you entered is not included. Please try again."

#checks player accuracy/acknowleges correct answers and prompts if incorrect
#also tracks the user guesses on each question and terminates once limit is reached 
def launch_answers(answer, sentence, blank_space):
    index, answer_index,blank_index,total_sentence,guesses = 0,0,0,4,0.
# while loop for asking questions for player responses and updating indexes
    while index < total_sentence:
        player_answer = raw_input('Type your answer for' + blank_space[blank_index] + 'here ==> ')
        if player_answer.lower() == answer[answer_index]:
            sentence[index] = sentence[index].replace(blank_space[blank_index],answer[index])
            print ''.join (sentence)
            answer_index += 1
            index += 1
            blank_index += 1
            print 'Great job! You answered correctly!'
        else:
             print 'Sorry! Try again'
             maximum_tries = 2
             tries+=1
             if tries > maximum_tries:
                print "Game Over"
                break


    print "Blinding me with science O_0"
