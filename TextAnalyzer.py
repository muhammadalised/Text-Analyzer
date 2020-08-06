class TextAnalyzer:
    # Class objects
    # list of alphabets used by calculate_character_percentage 
    alphabet_list = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]
    # symbols used in clean_text function
    symbols_list = ['-','.',',','\n','[', ']', '(', ')', '@','^', '*','~']
    
    # for storing text after reading it from file
    text = ''

    # for storing number of lines in a text document
    num_of_lines = ''
    
    def __init__(self):
        
        # welcome message
        print('\n=======================================================================')
        print('=====================| WELCOME TO TEXT ANALYZER |======================')
        print('=======================================================================\n')
    
    '''
        This method gets a filename from user opens that file and read data from it
        then return that text and number of lines of text.
    '''
    def open_file(self):

        while True:
            try:
                # Get filename with extension from user e.g. abc.txt
                filename = str(input('Please enter file name along with file extension: '))
                fh = open(filename)
                self.text = fh.read()
                # for counting the number of lines
                self.num_of_lines = len(open(filename).readlines())

                return self.text, self.num_of_lines
            except:
                print('\nError! Please check the following: \n- The file is a text file\n- The file is present in current directory\n- The filename is correct')
            finally:
                fh.close()
    '''
        This method counts the number of characters (char) in the text and returns the count.
        It is used by calculate_char_percentage method
    '''
    def count_char(self, text, char):
        
        count = 0
        for c in text:
            if c == char:
                count += 1
        return count
    
    '''
        This method counts percentage of characters present in the text. Takes text as an
        argument and returns a dictionary of character percentage (char_perc) with character as key and
        percentage as value
    '''
    def calculate_char_percentage(self, text):
        
        char_perc = {}
        print('CHARACTER PERCENTAGE IN %:\n'.center(60))
        print('\n=======================================================================')
        for char in self.alphabet_list:
            perc = 100 * self.count_char(text, char)/len(text)
            char_perc[char] = round(perc,2)
            print(f'{char} - {round(perc,2)}%'.center(60))

        return char_perc

    '''
        This method counts the number of words in the text document and returns the count
    '''
    def count_words(self, text):
        
        word_list = text.split()
        word_count = 'WORD COUNT: ' + str(len(word_list))
        # str.center methods centers the text in console
        print(word_count.center(60))
        # returns length of word_list which is total no of words in text
        return len(word_list)
    
    '''
        This method counts the number of time each word occurs in the text document stores
        frequency of each word corresponding to the word in tuples nested in a list.
        returns a list of tuples containing words corresponding to frequency
    '''
    def frequent_words(self, text):
        
        # Clean the text of symbols etc.
        word_list = self.clean_text(text)
        # Initializing Dictionary
        d = {}
        # Count number of times each word comes up in list of words (in dictionary)
        for word in word_list:
            if word not in d:
                d[word] = 0
            d[word] += 1
        
        # Next, reverse the key and values so they can be sorted using tuples.
        word_freq = []
        for key, value in d.items():
            word_freq.append((value, key))
        word_freq.sort(reverse=True)
        
        # str.center() method just adds space by default to center the text in console screen
        print('FREQUENT WORDS: \n'.center(60))
        print('\n=======================================================================')
        print('WORDS --- NO OF TIMES IT OCCURED'.center(75))
        # print the top ten frequent words
        for wf in word_freq[1:11]:
            print(f'{wf[1]} --- {wf[0]}'.center(60)) # wf[0] is frequency, wf[1] is the word
        
        # returns words and their frequency in form of tuples nested in a list
        return word_freq

    '''
        Removes the symbols using symbols_list from text and then converts the text
        to lowercase to make it consistent. Returns a list of words (word_list)
    '''
    def clean_text(self, text):
        
        for char in self.symbols_list:
            text=text.replace(char,' ')
            text = text.lower()
        
        word_list = text.split()
        return word_list
    '''
        This methods finds the unique words in the text
        1. Cleans the text
        2. Convert the list of words to set so that only unique words are there since set has
           unique elements.
        3. Counts the unique words in the set
        Returns unique word count and list of unique words
    '''
    def unique_words(self, text):

        text = self.clean_text(text)
        unique_words = set(text)
        unique_word_count = len(unique_words)

        uw_count = 'UNIQUE WORDS COUNT: '+str(unique_word_count)

        print(uw_count.center(60))
        print('\n=======================================================================')
        print('UNIQUE WORDS'.center(60))
        for uw in list(unique_words):
            print(str(uw).center(60))

        return unique_words, unique_word_count
        
    '''
        This method generates a report of text analyzer operations in a formatted way.
        It also writes that report to a file
    '''
    def generate_report(self):
        # word_count = 'Word Count: ' + str(self.count_words(self.text))
        line_count = 'LINE COUNT: ' + str(self.num_of_lines) + '\n'
        
        print('\n=======================================================================')
        print('=====================| WELCOME TO TEXT ANALYZER |======================')
        print('=======================================================================\n')

        print(line_count.center(60))
        word_count = self.count_words(self.text) # word count
        print('\n=======================================================================')
        uw, uwc = self.unique_words(self.text) # unique words and their count  
        print('\n=======================================================================')
        fw = self.frequent_words(self.text) # fw = frequent words
        print('\n=======================================================================')
        cp = self.calculate_char_percentage(self.text) # character percentage


        print('\n=======================================================================')
        print('=======================================================================\n')


        with open('report.txt', mode='w') as f:
            f.write('\nTHIS REPORT WAS CREATED BY TEXT ANALYZER\n')
            f.write(line_count)
            f.write('WORDS COUNT: '+ str(word_count))
            f.write('\nUNIQUE WORDS COUNT: '+ str(uwc))
            f.write('\n----------------------------------------------------')
            f.write('\nUNIQUE WORDS\n')
            
            # Writing unique words to file
            for w in list(uw):
                f.write('\n'+ w)
            
            # Writing frequent words to file
            f.write('\n----------------------------------------------------')
            f.write('\nFREQUENT WORDS\n')
            f.write('\nWORDS ----- NO OF TIMES IT OCCUR')
            for w in fw[1:11]:
                f.write('\n'+ str(w[1]) + ' ----- ' + str(w[0]))
            
            f.write('\n----------------------------------------------------')
            f.write('\nCHARACTER PERCENTAGES\n')
            # Loop through the dictionary
            for alp, perc in cp.items(): # alp = alphabets and perc = percentage
                f.write('\n'+ str(alp) + ' ----- ' + str(perc)+ '%')


        
        

