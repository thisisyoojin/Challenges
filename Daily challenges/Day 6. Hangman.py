class Hangman:
    """
    Class hangman creates the template for answer/input.
    """

    def __init__(self, answer, lives):       
        # the actual asnwer
        self.answer = answer.lower()
        # the temperory list for guess word
        self.guess = ['*']*len(self.answer)
        # number of tries
        self.lives = lives
        # the letters a player tried
        self.tried_letter=[]
        # game round number
        self.round_num = 1
        # print out the number of answer
        print(f'\nYou have 3 lives to guess the word. The number of letters is {len(self.answer)}.\n')
        

    
    def play(self):

        while self.lives > 0 :
            # Get the letter from a player
            print(f"----------Round {self.round_num}----------")
            letter = input("Please enter a letter: ").lower()


            # Check if the input is valid
            if len(letter) > 2 or not letter.isalpha():
                print(f'\n!!The input should be one English letter!!')
                continue

            # Check if the input is already tried
            elif letter in self.tried_letter:
                print(f'\n!!You already tried "{letter}". Please enter another letter!!')
                continue

            # Otherwise, add the letter in tried letter list
            else:
                self.tried_letter.append(letter)
            
            
            # if the letter is in answer
            if letter in self.answer:
                print('\nGood work! You got the right letter :D')
                # replacing the guess word with the letter
                for i in range(len(self.answer)):
                    if self.answer[i] == letter:
                        self.guess[i] = letter
                    else:
                        continue
                
                
                
                # when the guess word is the answer
                if ''.join(self.guess) == self.answer:
                    print('You won!')
                    break
            
            # if the letter is not in answer
            else:
                # reduce the lives
                self.lives -= 1
                # print the remaing chances
                print(f'\nOops! You got the wrong letter :(\nNow you have {self.lives} chances.')
            
            
            # print out the tried letters and guess so far
            print(f'\nYou tried so far: {self.tried_letter}\nGuess word: {"".join(self.guess)}\n')
            # add the round number
            self.round_num += 1
            
        
        # when the remaing changes are none, print out 'hang'
        print('You lost!')
        return
            

            


first_game = Hangman('joy', 5)
first_game.play()