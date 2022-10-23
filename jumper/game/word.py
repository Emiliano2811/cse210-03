import random
from game.terminal_service import TerminalService

class Word:
    """The word that's trying to be solved 
    
    The responsibility of Word is to generate the random word, and keep track of what has been solved and left unsolved.
    
    Attributes:
        _terminal_service (Class): Our Terminal Service.
        _easy_list (List[str]): A list of possible easy words to choose from
        _medium_list (List[str]): A list of possible medium words to choose from
        _hard_list (List[str]): A list of possible hard words to choose from
        _choice (str): The randomly selected word from one of the above lists.
        _hidden_word (str): The hidden portion of the word.
        _solved_word (str): The solved portion of the word.
        _difficulty (str): Which list to pick our word from
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self (Word): An instance of Word.
        """

        self._terminal_service = TerminalService()

        self._easy_list = 'worcestershire bandwagon hippopotomonstrosesquippedaliophobia circumlocution xenotransplantation uncopyrightable floccinaucinihilipilification incomprehensibility trichotillomania daddy water baby mango juice road python brave song heart mouth life fish shoe school shop dinner doctor song sing serious moon educated water wind size'.split() # easy list of words
        self._medium_list = 'square death magnificent calculator famous marble petite archetypal aware paddle brave bushes waiting confess overjoyed shocking hushed hilarious female shame stimulating dinner doctor scribble heartbreaking rabid haunt arrive serious confused educated oafish nation sticky helpful reading recognise'.split() # medium list of words
        self._hard_list = 'banjo bayou beekeeper bikini blitz blizzard boggle bookworm heartbreaking boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt cycle disavow dizzying duplex dwarves embezzle equip espionage exodus faking fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx spritz squawk staff strength strengths stretch subway swivel syndrome thriftless thumbscrew topaz transcript transgress transplant twelfth twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz wave wavy waxy wellspring wheezy whiskey whizzing whomever wimpy witchcraft wizard woozy wristwatch wyvern xylophone yachts yippee yoked youthful yummy zigzag zilch zipper zodiac zombie'.split()
        
        self._choice = ""
        self._hidden = []
        self._solved =[]
        self._difficulty = ""
        

    def generate_word(self):
      """Picks a word from the list

      Args:
        self (Word): An instance of Word.
      """

      self._get_difficulty()
      
      #method that generates a random word from the list
      # assign the guess list according to the level of difficulty
      if self._difficulty.lower() == "easy":
        self._choice = random.choice(self._easy_list)
      elif self._difficulty.lower() == "medium":
       self._choice = random.choice(self._medium_list)
      else:
        self._choice = random.choice(self._hard_list)
      

      #sets that as hidden_word
      #sets an empty array the length of hidden_word as solved_word
      self._hidden = list(self._choice)
      
      for _ in range(len(self._hidden)):
        self._solved.append("_")

    def _get_difficulty(self):
      """Sets the difficulty to determine word list.

      Args:
        self (Word): An instance of Word.
      """

      self._difficulty = self._terminal_service.read_text("Choose your difficulty: [easy/medium/hard]")
      while self._difficulty not in ["easy", "medium", "hard"]:
        self._difficulty = self._terminal_service.read_text("Choose your difficulty: [easy/medium/hard]")

    def process_guess(self, guess):
      
      for i in self._hidden:
          if i == guess:
             index = self._hidden.index(i)
             self._solved[index] = i
             self._hidden[index] = ""
            

    def reveal_answer(self):
      """Prints the final answer.

      Args:
        self (Word): An instance of Word.
      """
      self._terminal_service.write_text(f"The word was {self._choice}!")

    def get_hidden(self):
      """Getter for hidden

      Args:
        self (Word): An instance of Word.
      """
      return self._hidden

    def get_solved(self):
      """Getter for solved

      Args:
        self (Word): An instance of Word.
      """
      return self._solved

