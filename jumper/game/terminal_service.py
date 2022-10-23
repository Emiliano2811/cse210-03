class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            float: The user's input as a number.
        """
        return float(input(prompt))
        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)

    
    def welcome_text(self):
        """Displays the welcome text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            
        """
        print()
        print("=================================================================================================\n")
        print("Welcome to Jumper! A word guessing game where you try to guess all the letters of the given word!\n")
        print("=================================================================================================\n")

    def print_solved(self, word):
        """Prints the solved portion of our word. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            
        """
        for i in word:
            print(f"{i} ", end = "")

    def you_win(self):
        """Tells the user they won. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            
        """
        print("\n\nCongratulations! You win!")

    def you_lose(self):
        """Tells the user they lost. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            
        """
        print("\n\nSorry! You lose!")

    def invalid_entry(self):
        """Tells the user their entry is invalid.

        Args: 
            self (TerminalService): An instance of TerminalService.
            
        """
        print("Invalid entry!")