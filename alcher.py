import pyautogui
import win32gui
import pprint
import sys
import keyboard
import os
import pyautogui
from GameManager import GameManager

# The Game manager(just extracts some logic from here)
gameManager = None

# The rect of the runelite window
runeLiteWindowRect = None

# If we have already checked the login screen or need to check it
hasCheckedLoginScreen = False

# If we are at the login screen
isAtLoginScreen = False

# Whether or not the main loop is running
running = False

# The password we want to use if the user wants to use auto login
password = None

paused = False


# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutSine)

def prepare_everything():
    global runeLiteWindowRect
    global running
    global password
    global gameManager

    password = input('Enter your runescape password: ')
    if password is "":
        password = None

    keyboard.add_hotkey('control+shift+s', stop_script)
    keyboard.add_hotkey('control+shift+p', pause_script)

    hwnd = win32gui.FindWindowEx(None, None, None, 'RuneLite')

    if hwnd == 0:
        print('RuneLite window not found')
        sys.exit()

    rectReturned = win32gui.GetWindowRect(hwnd)
    runeLiteWindowRect = (rectReturned[0], rectReturned[1], rectReturned[2] - rectReturned[0], rectReturned[3] - rectReturned[1])
    gameManager = GameManager(runeLiteWindowRect, hwnd)
    print(runeLiteWindowRect)
    running = True


def stop_script():
    global running
    running = False
    print('exiting')
    os._exit(0)
    pass


def pause_script():
    global paused

    if paused:
        paused = False
    else:
        paused = True
    pass


prepare_everything()

previous_state = None

while running:
    if paused: continue

    state = gameManager.check_state()

    if previous_state is not None:
        if previous_state is not state:
            print('New state is: ', state)

    previous_state = state

    if state == 'login':
        gameManager.handle_login(password)
    if state == 'ingame':
        gameManager.handle()

    # if hasCheckedLoginScreen is False:
    #     check_login_screen()
    # else:
    #     if isAtLoginScreen is True and password is not None:
    #         print('Handle login')
    #     else:
    #         print('Run script')
    #
    #     imageToLookFor = 'img_templates/welcome-to-rs.png'
    #     screenshot = pyautogui.screenshot('RuneLiteSS.png', runeLiteWindowRect)
    #     retVal = pyautogui.locate(imageToLookFor, screenshot)
    #
    #     if retVal is None:
    #         print('Not ingame')
    #         continue
    #
    # print('woop were ingame')
