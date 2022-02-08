from terra_sdk.client.lcd import LCDClient, wallet
from terra_sdk.key.mnemonic import MnemonicKey
import difflib
import itertools

####### EXACTLY ONE ERROR #######


# For each word in your seed phrase it looks for n closer words and test them
def soft_force(seed, words, pub_key, n = 10):
    seed_list = seed.split()
    for word in seed_list:
        matches = difflib.get_close_matches(word, words, n)
        for match in matches:
            possible_seed = seed.replace(word, match)
            if check_key(possible_seed, pub_key):
                return True            
    return False

# This try all combination with all the list words
def brute_force(seed, words, pub_key):
    seed_list = seed.split()
    for possible_word in words:
        for seed_word in seed_list:
            possible_seed = seed.replace(seed_word, possible_word)
            if check_key(possible_seed, pub_key):
                return True

    return False

####### MORE THEN ONE ERROR #######

# For each word in your seed phrase it looks for n closer words, then test all the combination with 1 element from each closer words list
# With n > 2 that will take forever, at least on my computer
def almost_brute_force(seed, words, pub_key, n = 2):
    seed_list = seed.split()
    matches = []
    # Getting close words
    for word in seed_list:
        match = difflib.get_close_matches(word, words, n)
        matches.append(match)

    # Generating all combinations
    combinations = [p for p in itertools.product(*matches)]

    # Checking all possible seeds
    for combination in combinations:
        possible_seed = " ".join(combination)
        if check_key(possible_seed, pub_key):
            return True
        
    return False


def check_key(seed, pub_key):
    terra = LCDClient("https://bombay-lcd.terra.dev/", "bombay-12")  # testnet
    key = MnemonicKey(seed)
    wallet = terra.wallet(key)
    possible_pub_key = wallet.key.acc_address
    if possible_pub_key == pub_key:
        print("[*] Seed recovered:\n" + seed)
        return True
    else:
        return False

if __name__ == "__main__":

    with open('en.txt') as f:
        words = f.read().splitlines()

    with open ('seed.txt') as s:
        seed = s.read()

    with open ('pub_key.txt') as p:
        pub_key = p.read()
    
    print("[+] Starting with soft-forcing")
    seed_phrase = soft_force(seed, words, pub_key)
    
    if seed_phrase:
        exit()

    seed_phrase = almost_brute_force(seed, words, pub_key)

    if seed_phrase:
        exit()

    print("[-] No seed found, \n[+] Starting with brute-forcing")

    seed_phrase = brute_force(seed, words, pub_key)

    if seed_phrase:
        exit()
    else:
        print("[-] Sorry, can't recover the phrase check for spaces or newlines in seed.txt/pub_key.txt")

