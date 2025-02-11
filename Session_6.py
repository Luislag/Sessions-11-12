punctuation_remove = (" , . ! ?")
punctuation_space = (" ' ")

def find_3_letter_words (filename) :
    with open(filename) as f:
        #go line by line
        for line in f:
            for p in punctuation_remove:
                line = line.replace(p, "")
            for p in punctuation_space:
                line = line.replace(p, "")
            words = line.split()


find_3_letter_words("input.txt")