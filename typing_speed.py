# Typing Speed Test
import random
import time
from random_words import RandomWords

rw = RandomWords()

# List that will be used to create the passage for the typing test
word_list = []
# List that will keep the words of what the player types
player_typing = []

# Main function that will contain all the options the user can do
def main():
    print("Typing Speed Test")
    print("Choose a number option you want to do")
    print("1 - Start test")
    print("2 - Leave")
    try:
        user_choice = input()
        if(int(user_choice) == 1):
            print("How many lines do you want for your test: 1, 2, 3")
            global length
            length = input("")
            if(int(length) == 1):
                test_length(1)
                print(" ")
                typing_test()
            elif(int(length) == 2):
                test_length(2)
                print(" ")
                typing_test()
            elif(int(length) == 3):
                test_length(3)
                print(" ")
                typing_test()
        elif(int(user_choice) == 2):
            print("Thanks for Playing")
            quit()
        else:
            print("Invalid Input\n")
    except ValueError:
        print("Invalid Input\n")
    return main()

# Determines the length of the typing test
# @param length of typing test
def test_length(length):
    i = 0
    word_list.clear()
    if(length == 1):
        for word in range(10):
            word_list.append(rw.random_word())
        for word in word_list:
            print(word, end=" ")
    elif(length == 2):
        for word in range(20):
            word_list.append(rw.random_word())
        for word in word_list:
            if (i < 10):
                print(word, end=" ")
                i += 1
            elif (i == 10):
                print("")
                print(word, end=' ')
                i += 1
            elif(i > 10):
                print(word, end=" ")
    elif(length == 3):
        for word in range(30):
            word_list.append(rw.random_word())
        for word in word_list:
            if (i < 10):
                print(word, end=" ")
                i += 1
            elif (i == 10 or i == 20):
                print("")
                print(word, end=" ")
                i += 1
            elif (i > 10):
                print(word, end=" ")
                i += 1
    return

# countdown(seconds) will create a countdown
# @param seconds for the countdown to start with
def countdown(seconds):
    for i in range(seconds):
        # Prints the parameter "seconds" and decreases by 1 as the loop iterates
        print(seconds - i, end="...")
        time.sleep(1)   # Stops the code for 1 second to create a countdown
        # After the countdown gets to 1, it will say "Go!" to indicate the end of the countdown
        if((seconds - i) == 1):
            print("Go!")
    return

# typing_test function will create the typing test
def typing_test():
    print("Type the following text above as fast as you can:")
    if (int(length) == 1):
        # Starts the typing test and gives a brief countdown of 10 seconds
        countdown(5)
        starting_time = time.time()
        player_text = input("")
        ending_time = time.time()

        # Calculating WPM, time, and accuracy
        player_typing = player_text.split(" ")
        time_spent = round(ending_time - starting_time)
        wpm = round(((len(player_text))/5) / (time_spent/60))
        correct_characters = 0
        for index, character in enumerate(word_list):
            try:
                if(player_typing[index] == character):
                    correct_characters += 1
            except:
                pass
        accuracy = round(correct_characters / len(word_list)*100, 2)

        # Printing results after typing test
        print("WPM: " + str(wpm))
        print("Time spent: " + str(time_spent) + " seconds")
        print("Accuracy: " + str(accuracy) + "%")
        print(" ")

    elif (int(length) == 2):
        # Starts the typing test and gives a brief countdown of 10 seconds
        countdown(5)
        first_start_time = time.time()
        first_text = input("")
        first_end_time = time.time()
        second_start_time = time.time()
        second_text = input("")
        second_end_time = time.time()

        # Calculating WPM, time, and accuracy
        player_typing = first_text.split(" ")
        player_typing += second_text.split(" ")
        first_time_spent = round(first_end_time - first_start_time)
        second_time_spent = round(second_end_time - second_start_time)
        total_time_spent = round(first_time_spent + second_time_spent)
        wpm = round(((len(first_text) + len(second_text)) / 5) / (total_time_spent / 60))
        correct_characters = 0
        for index, character in enumerate(word_list):
            try:
                if (player_typing[index] == character):
                    correct_characters += 1
            except:
                pass
        accuracy = round(correct_characters / len(word_list) * 100, 2)

        # Printing results after typing test
        print("WPM: " + str(wpm))
        print("Time spent: " + str(total_time_spent) + " seconds")
        print("Accuracy: " + str(accuracy) + "%")
        print(" ")

    elif (int(length) == 3):
        # Starts the typing test and gives a brief countdown of 10 seconds
        countdown(5)
        first_start_time = time.time()
        first_text = input("")
        first_end_time = time.time()
        second_start_time = time.time()
        second_text = input("")
        second_end_time = time.time()
        third_start_time = time.time()
        third_text = input("")
        third_end_time = time.time()

        # Calculating WPM, time, and accuracy
        player_typing = first_text.split(" ")
        player_typing += second_text.split(" ")
        player_typing += third_text.split(" ")
        first_time_spent = round(first_end_time - first_start_time)
        second_time_spent = round(second_end_time - second_start_time)
        third_time_spent = round(third_end_time - third_start_time)
        total_time_spent = round(first_time_spent + second_time_spent + third_time_spent)
        wpm = round(((len(first_text) + len(second_text) + len(third_text)) / 5) / (total_time_spent / 60))
        correct_characters = 0
        for index, character in enumerate(word_list):
            try:
                if (player_typing[index] == character):
                    correct_characters += 1
            except:
                pass
        accuracy = round(correct_characters / len(word_list) * 100, 2)

        # Printing results after typing test
        print("WPM: " + str(wpm))
        print("Time spent: " + str(total_time_spent) + " seconds")
        print("Accuracy: " + str(accuracy) + "%")
        print(" ")

    return main()

main()
