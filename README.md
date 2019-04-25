# RS-Alcher
A simple script that will log you into RuneScape(you don't need this, but it helps with 6 hour logout timer)

It will alch with what ever is in your inventory, has smooth mouse movement with different movement speeds to make it look more human

It will also make it look like you're afk alching whilst doing something else on your computer

THIS IS NOT A BOT, it is a simple script that controls your mouse and jagex will still ban you for it if you over use it, so use at risk. 

# Requirements
 - You **must** use `RuneLite` client 
 - You must disabled `Stretched Mode` and `Interface Styles` if you have this enabled
 - You must put your game into `Fixed Mode`
 - You must put your game into the highest brightness
 - In `RuneLite Settings` disable `Show display name in title`. The script will not be able to run without this.
 
# Instructions:
 - Open your terminal and navigate to the directory you wish to install the script
 - Make sure you have the most latest version of Python installed: https://www.python.org/downloads/
 - Run these commands:
 ```
 git clone https://github.com/ScooterSam/RS-Alcher.git
 cd RS-Alcher/

 pip install pyatuogui win32gui pywin32 keyboard pyclick

 py alcher.py
 ```

Once you have done this, the script will ask for your password. This feels kinda suspicious as a RuneScape player... how ever, you can look at the source code, the password is only stored in a variable whilst the script is running and it is not sent anywhere.

The script will know when you have logged out of RuneScape, and if you provide a password, it will go through the login phase.

If you are worried about providing your password, I understand. You can enable two factor authentication on your RuneScape account, which makes the use of your password useless without two factor. Just ensure you login to the account once on your device before running the script, it will not be able to handle two factor authentication.

# Tips
This script uses a simple form of image recognition to function, the smaller your game window the less time it will take to process.

# Thanks
Thanks for using my script, be safe and don't go too crazy. I could have sold this script, but I decided to release it for free, if you wanna hit me with donation of any amount, it will be much appreciated.

[Donate here](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UTDXVTC3GY67J&source=url)
Leave your discord username if you like and I'll let you know when its updated or I make something new :)
