import random

my_guesses = []
best_guesses = []
#Added a new variable called best_guesses

def main():

  global minimum, maximum, guess_count, computer_number, tries
  
  computer_number = random.randint(1,100)
  minimum = 0
  maximum = 100
  guess_count = 0
  #print(computer_number)
  get_guesses()

def get_guesses():

  global guess_count

  user_guess = int(input("Guess a number between " + str(minimum) +" and " + str(maximum) + ":  "))
  my_guesses.append(user_guess)
  best_guesses.append((maximum + minimum) / 2)#
  guess_count = guess_count + 1
  give_feedback(user_guess)

def give_feedback(user_guess):

  global minimum, maximum, guess_count

  if user_guess == computer_number:
    print("\nCorrect, it took you " + str(guess_count) + " tries.")
    binary_search_feedback()

  elif user_guess > computer_number:
    print('too high')
    maximum = user_guess - 1
    get_guesses()
  else:
    print('too low')
    minimum = user_guess + 1
    get_guesses()
#New function to provide feedback
def binary_search_feedback():

  difference_total = 0
#This part of the code is used to analyze the average away from perfect guess and suggest whtehr understanding of binary search from user is good or not. 
  for i in range (len(my_guesses)):
    difference_total += abs(my_guesses[i]-best_guesses[i])

  average_difference = difference_total/len(my_guesses)

  print("\nYour guesses were off by an average of " + str(average_difference) + " from the perfect guess.")

  if average_difference > 5:
    print("\nYou don't understand how binary search works!")

  elif average_difference > 1:
    print("\nYour understanding of binary search is not perfect.")

  else:
    print("\nYou understand binary search really well!")

  play_again = input("\nWould you like to play again?\n ")
  
  if play_again[0].lower() =='y':
    main()

main()

  
