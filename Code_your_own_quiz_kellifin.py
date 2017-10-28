



#Code your own quiz assignment by Kelli Westmoreland

#Goal: Use python to perform the functions and run the quiz

easy_test = ["There are ___1___ seasons of the year.",
              " The month of March is typically when ___2___ begins. ",
              "Fall is also called ___3___. ",
              "Leap year always occurs during the ___4___ season."] #timeanddate.com

medium_test = ["December Solstice is in the ___1___ season.",
              " We have seasons because the Earth spins around the ___2___ at an angle.",
              " Astronomers and scientists use the dates of equinoxes and ___3___ to mark the beginning and end of seasons.",
              " The four seasons are divided into ___4___ months each."] #timeanddate.com

hard_test = ["Seasons occur because of the ___1___ of the Earth's rotational axis.",
            " People in the Southern Hemisphere consider Sept 1 as the beginning of  ___2___.",
            " In the Northern Hemisphere, the June Solistice marks the start of ___3___.",
            " The Northern and Southern Hemisphere seasons are  ___4___ of each other." ] #timeanddate.com

# answer keys for sentences
easy_answers = ['four', 'spring', 'autumn', 'winter']

medium_answers = ['winter', 'sun', 'solstices', 'three']

hard_answers = ['tilt', 'spring', 'summer', 'opposite']

show_space = [ '___1___', '___2___', '___3___', '___4___']

print "Welcome to the Earth and seasons quiz. You have three tries. Good luck!" 

#choose game level from list 
def launch_levels(quiz_level):
    while True:
        if quiz_level == "easy":
            print "Okay, here's the 'easy' quiz. Good Luck!"
            return easy_test, easy_answers
        elif quiz_level == "medium":
            print "Okay, here's the 'medium' quiz. Good Luck!"
            return medium_test, medium_answers
        elif quiz_level == "hard":
            print "Okay, here's the 'hard' quiz. Good Luck!"
            return hard_test, hard_answers
#returning (output) specific test questions and answer key
def launch_answers(answer, sentence, show_space):
    index, answer_index,blank_index,entire_sentence,tries = 0,0,0,4,0.
    tries = 0
# while loop for asking questions for player responses and updating indexes
    while index < entire_sentence:
        quiz_answer = raw_input('Type your answer for' + show_space[blank_index] + 'here: ')
        if quiz_answer.lower() == answer[answer_index]:
            sentence[index] = sentence[index].replace(show_space[blank_index],answer[index])
            #print sentence[index]
            print ''.join (sentence)
            answer_index += 1
            index += 1
            blank_index += 1Sprin
            print 'Correct! Great job!'
        else:
             print 'Oops! Try again'
             maximum_tries = 2
             tries+=1
             if tries > maximum_tries:
                print "Game Over"
                break#prevents Game Over loop


    print "Blinding me with science O_0"
def launch_game():
    quiz_level = raw_input('Choose easy, medium or hard here: ')
    if quiz_level == 'easy' or quiz_level == 'medium' or quiz_level == 'hard':
        sentence, answers = launch_levels(quiz_level)
        print sentence

        launch_answers(answers, sentence, show_space)
    else:
        print "The choice you entered is not included. Please try again."

#checks accuracy and confirms correct answers and prompts if incorrect
#also tracks tries on each question and ends quiz once limit is reached.
launch_game()#Code your own quiz assignment by Kelli Westmoreland

