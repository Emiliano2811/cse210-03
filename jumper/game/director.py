from game.terminal_service import TerminalService
from game.word import Word
from game.parachute import Parachute

"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/encapsulation/materials/jumper-specification.html
"""

class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        win (boolean): Have we lost or won the game?
        terminal_service: For getting and displaying information on the terminal
        parachute: An instance of Parachute Class
        word: An instance of the Word Class
        solved: the solved portion of the word
        hidden: the hidden portion of the word
        guess: The current guessed letter
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._win = True
        self._terminal_service = TerminalService()
        self._parachute = Parachute()
        self._guess = ""
        self._word = Word()
        self._hidden = ""
        self._solved = ""

        self._opening_moves()
        
    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        self._terminal_service.print_solved(self._solved) 

        if self._win == True:
            self._terminal_service.you_win()
        else:
            self._terminal_service.you_lose()
        self._word.reveal_answer()


    def _get_inputs(self):
        """Receives the new guessed letter from the user

        Args:
            self (Director): An instance of Director.
        """

        # Print hidden word
        #print(self._word._hidden) #comment this out

        self._terminal_service.print_solved(self._solved)  

        #get input from user
        #input validation [only letters a-z]

        self._guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        while not (self._guess.isalpha()) or (len(self._guess) != 1):
            #print("Invalid entry!")
            self._terminal_service.invalid_entry # print an error message
            self._guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        pass


    def _do_updates(self):
        """Check the guessed letter, update the word, update the parachute

        Args:
            self (Director): An instance of Director.
        """

        #check the letter against the characters in the word.

        #if letter in word:
            #add letter to the solved portion of the word
            #remove letter from the array of the hidden word
        #else:
            #remove a line from the parachute
            #adds to the lose counter

        
        if self._guess in self._hidden:
            self._word.process_guess(self._guess)
            self._solved = self._word.get_solved()
        else:
            self._parachute.bad_answer()
        pass

    def _do_outputs(self):
        """Prints the current state of the parachute, and checks to see if we've won or lost the game

        Args:
            self (Director): An instance of Director.
        """

        #Check to see if we lost or won the game

            #check to see if the word is solved by checking word.hidden for letters
        self._hidden = self._word.get_hidden()
        self._is_playing = False
        for i in self._hidden:
            if i != "":
                self._is_playing = True

            #check to see if we ran out of parachute
        if self._is_playing == True:
            self._is_playing, self._win = self._parachute.losing_check()

        #print out the current state of the parachute
        self._parachute.print_parachute()

        pass


    def _opening_moves(self):
        """Prints opening speil and gets difficulty

        Args:
            self (Director): An instance of Director.
        """

        self._terminal_service.welcome_text() # print the welcome text using the terminal_service class

        #create the word to be guessed
        self._word.generate_word()
        self._hidden = self._word.get_hidden()
        self._solved = self._word.get_solved()