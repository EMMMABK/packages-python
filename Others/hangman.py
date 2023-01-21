import random
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar 
      coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
      lion lizard llama mole monkey moose mouse mule newt otter owl panda
      parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
      skunk sloth snake spider stork swan tiger toad trout turkey turtle
      weasel whale wolf wombat zebra'''.split()
def get_random_word(word_list):
  word_index = random.randint(0,len(word_list)-1)
  return word_list[word_index]
def display_board(sec_w):
  return len(sec_w)* '_'
def get_guess(secret_word):
  error_counter = 0
  while error_counter < 6:
    get_letter = input('guess letter: ')
    if get_letter in secret_word:
      print('the letter exists in word')
    else:
      error_counter+=1 # error_counter= error_counter + 1
      print('the letter does not exist in letter')

def main():
  secret_word = get_random_word(words)
  print(display_board(secret_word))
  get_guess(secret_word)

if __name__ == '__main__':
  main()