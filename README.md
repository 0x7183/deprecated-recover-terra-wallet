# Recover-terra-wallet

A simple python script that can be used to brute forcing your seed phrase.

The script works only if you have access to a similar seed phrase e.g. while copying your seed phrase you wrote `big` insted of `bug`.

**Disclaimer:**

This script was made to help people recover their Terra wallet in case they made a mistake in copying words during the creation of their wallet.
The success of the operation is not guaranteed.

Usage:

* Copy the wrong seed phrase in `seed.txt
* Copy your address in `pub_key.txt`

Don't insert space or new line in the files.

From cmd exec the command:
```
python brute.py
```

If you don't have access to this information, this script is not for you.

Good luck!

