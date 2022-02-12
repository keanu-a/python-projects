# Flashcard Program
This flashcard program is made to learn spanish words.

## Program
The UI is made by using the Tkinter module.
1. The program reads through a CSV file using the pandas module and stores each word into a list.
2. A random word (using the random module) is chosen from the list and the user has 3 seconds to respond.
3. If the user knows the word, then the word is removed from the list.
4. At the end of the program, a list will be generated with words still need to learn.
