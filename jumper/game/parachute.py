from game.terminal_service import TerminalService

class Parachute:
    """The parachute that's tracking how close to losing the player is. 
    
    The responsibility of parachute is to keep track of how many incorrect guesses the player has made, and print out the current diagram of the player and their parachute after each guess
    
    Attributes:
        
    """

    def __init__(self):
        """Constructs a new parachute.

        Args:
            self (parachute): An instance of parachute.
        """
        self._drawing = ["  _____", " /_____\\", " \     /", "  \   /", "   \ /", "    0", "   /|\\", "   / \\", "", "^^^^^^^^^^"]
        self._counter = 0
        self._death = 5
        self._terminal_service = TerminalService()

    def bad_answer(self):
        """Deletes first line of parachute and increases counter

        Args:
            self (parachute): An instance of parachute.
        """

        self._drawing.pop(0)
        self._counter += 1

    def losing_check(self):
        """Checks if we lost the game or not

        Args:
            self (parachute): An instance of parachute.
        """
        if self._counter == self._death:
            self._dead_head()
            return False, False
        else:
            return True, True

    def _dead_head(self):
        """Upon losing, turns the head into an 'X'.

        Args:
            self (parachute): An instance of parachute.
        """
        self._drawing[0] = "    X"

    def print_parachute(self):
        """Prints the current state of the parachute

        Args:
            self (parachute): An instance of parachute.
        """
        for i in self._drawing:
            self._terminal_service.write_text(i)
