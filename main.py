# Import required modules
from TextAnalyzer import TextAnalyzer
from os import system, name
from time import sleep  

# Create the class instance
ta = TextAnalyzer()

text, num_of_lines = ta.open_file()

'''
    This function displays a menu containing a set of options.
    It prompts the user to select an option from available ones
    and then perform operations accordingly
'''
def main_menu():
    clear()
    while True:
        print('\n1. Character percentage in text\n2. Number of lines and words in text\n3. Unique words in text\n4. Most frequent words\n5. Generate text analysis report\n6. Exit')
        try:
            # Get input from user
            option = int(input('\nSelect any option: '))

            if option == 1:
                # clear the screen
                clear()
                # Calculate text percentage in text
                ta.calculate_char_percentage(text)
            elif option == 2:
                clear()
                # Number of lines and words in text
                no_of_lines = 'NUMBER OF LINES: '+str(num_of_lines)
                print(no_of_lines.center(60))
                ta.count_words(text)
            elif option == 3:
                clear()
                # Unique words in text
                ta.unique_words(text)
            elif option == 4:
                clear()
                # Frequent words in text
                ta.frequent_words(text)
            elif option == 5:
                clear()
                # generate report in a file
                ta.generate_report()
            elif option == 6:
                break
        except:
            print('\nPLEASE ENTER A VALID OPTION!')
    
  
# clear function for clearing screen
def clear(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# Call the main menu function
main_menu()
