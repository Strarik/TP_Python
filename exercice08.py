def get_word_count(sentence):
       words = 0
       splitted_sentence = sentence.split()
       for i in range(len(splitted_sentence)) :
              letters = sum(j.isalpha() for j in splitted_sentence[i])
              if letters != 0 :
                     words += 1
       return words

def run():
   assert get_word_count("Bonjour") == 1
   assert get_word_count("Bonjour toi") == 2
   assert get_word_count("Bonjour ca va ?") == 3
   assert get_word_count("Bonjour ca va toi ?!") == 4
   assert get_word_count("") == 0
