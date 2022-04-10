# Recover-terra-wallet

A simple python script that can be used to brute forcing your seed phrase.

The script works only if you have access to a similar seed phrase e.g. while copying your seed phrase you wrote `big` insted of `bug`.
For the correct operation of this program you'll need your address and your wrong seed phrase, if you don't have access to this information, this program is not for you.

If you can't run the script feel free to ping me in the Terra Discord.

## Disclaimer:

This script was made to help people recover their Terra wallet in case they make a mistake in copying words during the creation of the wallet.
This script should be used as last chance and the success of the operation is not guarantee.

The code is open source and can be read and used by anyone, for usability reason we compiled some executables with pyinstaller for non developer.
Remember that using executable files or code without understanding them is like closing your eyes and crossing the highway.
The authors do not assume any kind of responsability regarding the possible loss of funds, use this tool at YOUR OWN RISK.

After the recover of your seed phrase is highly recommended to:

* Generate a new address with an hardware wallet 
* Write down your new seed phrase
* Erase the new empty wallet
* Restore it with your new seed phrase
* Move all your funds to this new address

## Usage for non developer:

* Click on the `Code` button in this page
* Click on `Download Zip` and save the file on your PC
* Unzip the downloaded directory
* Navigate in the `dist` directory
* Double click on the file `windows_run.exe` (Windows) `macOS_run` (macOS)
* Insert your seed phrase in the first box
* Insert your address in the second box
* Click the `START` button and wait

On macOS the double click may not work, if this is your case then:

* Open your terminal
* Copy and paste into it `cd Downloads/recover-terra-wallet-main/dist`
* Copy and paste `chmod 755 ./macOS_run`
* Then copy and paste it `./macOS_run`

DO NOTHING ON GITHUB!!

## Usage for developer:

* Navigate to `recover-terra-wallet/src/`
* Run `pip install terra_sdk kivy cdifflib` in your terminal
* Run `python app.py` in your terminal
* Insert your seed phrase in the first box
* Insert your address in the second box
* Click the `START` button and wait

If you have recovered your seed and would like to thank us you can help us paying our bills:

`terra1mjws9dnh99q7f5mfx6u4hlahgp60as2n6ggrtn`

Good luck!

