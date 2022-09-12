from terra_sdk.client.lcd import LCDClient
from terra_sdk.key.mnemonic import MnemonicKey
import difflib
import itertools

####### UTILS #######

def check_seed(seed, address, blockchain='Terra'):

    if blockchain == 'Terra':
        chain = LCDClient("https://pisco-lcd.terra.dev/", "pisco-1")  # testnet

    key = MnemonicKey(seed)
    wallet = chain.wallet(key)
    possible_address = wallet.key.acc_address
    if possible_address == address:
        return True
    else:
        return False

####### EXACTLY ONE ERROR #######

# For each word in your seed phrase it looks for n closer words and test them
def one_error_close_words(seed, words, address, n = 10):
    seed_list = seed.split()
    for word in seed_list:
        matches = difflib.get_close_matches(word, words, n)
        for match in matches:
            possible_seed = seed.replace(word, match)
            if check_seed(possible_seed, address):
                return possible_seed            
    return False

# This try all combination with all the words
def one_error_all_words(seed, words, address):
    seed_list = seed.split()
    for possible_word in words:
        for seed_word in seed_list:
            possible_seed = seed.replace(seed_word, possible_word)
            if check_seed(possible_seed, address):
              return possible_seed     

    return False

####### UP TO 24 SMALL ERRORS OR WRONG WORDS POSITIONS #######

# For each word in your seed phrase it looks for n closer words, then test for all the combinations of these words
def multiple_errors(seed, words, address, n = 2):
    seed_list = seed.split()
    matches = []
    # Getting close words
    for word in seed_list:
        match = difflib.get_close_matches(word, words, n)
        matches.append(match)

    # Generating all combinations
    combinations = itertools.combinations(matches, 24)

    for possible_seed in combinations:
        if check_seed(possible_seed, address):
          return possible_seed

    # Generating all the products
    products = [p for p in itertools.product(*matches)]

    # Checking all possible seeds
    for product in products:
        possible_seed = " ".join(product)
        if check_seed(possible_seed, address):
          return possible_seed

    return False


def brute_force(seed, words, address):

    seed_phrase = one_error_close_words(seed, words, address)
    if seed_phrase != False:
        return seed_phrase
    
    seed_phrase = one_error_all_words(seed, words, address)

    if seed_phrase != False:
        return seed_phrase

    seed_phrase = multiple_errors(seed, words, address)

    if seed_phrase != False:
        return seed_phrase  
    else:
        return "We are sorry, we can't recover this wallet :("
 

