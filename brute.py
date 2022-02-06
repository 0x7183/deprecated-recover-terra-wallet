from terra_sdk.client.lcd import LCDClient, wallet
from terra_sdk.key.mnemonic import MnemonicKey
import difflib
def similar_word(seed, words, pub_key, n = 10):
    seed_list = seed.split()
    for word in seed_list:
        matches = difflib.get_close_matches(word, words, n)
        for match in matches:
            possible_seed = seed.replace(word, match)
            if check_key(possible_seed, pub_key):
                return True            
    return False

def brute_force(seed, words, pub_key):
    seed_list = seed.split()
    for possible_word in words:
        for seed_word in seed_list:
            possible_seed = seed.replace(seed_word, possible_word)
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
    
    print("[+] Starting with soft-brute-forcing")
    seed_phrase = similar_word(seed, words, pub_key)
    
    if seed_phrase:
        exit()

    print("[+] No seed found, trying with the pure-brute-forcing")

    seed_phrase = brute_force(seed, words, pub_key)

    if seed_phrase:
        pass
    else:
        print("[-] Sorry, can't recover the phrase, maybe you mismatched more then one word")

