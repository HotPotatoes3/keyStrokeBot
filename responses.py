import time

import pyautogui

sprint = False
pause = False


def handle_response(message) -> str:
    p_message = message.lower()
    global sprint

    if p_message == '!help':
        return "**Bot to play current game on stream: Currently playing Super Mario Bros (Web Version)**\n**Commands:**\n!pause: pauses or unpauses the game\n!right,!left: move right or left\n!sprint: toggle sprint\n!crouch: crouch\n!jump,!rump,!lump: jump straight up, right or left respectively\nping @hotpotatoes for more info"

    if p_message == '!right':
        return "Moving right a bit"

    if p_message == '!left':
        return "Moving left a bit"

    if p_message == '!crouch':
        return "Crouching"

    if p_message == '!jump':
        return "Jumping"

    if p_message == '!sprint':
        return "Toggled Sprint"

    if p_message == '!rump':
        return "Jumping right"

    if p_message == '!lump':
        return "Jumping left"

    if p_message == '!pause':
        return "Pausing/Unpausing the game"


def handle_response2(message):
    p_message = message.lower()
    global sprint
    global pause
    if p_message == '!right':
        pyautogui.keyDown('right')
        time.sleep(0.5)
        pyautogui.keyUp('right')

    if p_message == '!left':
        pyautogui.keyDown('left')
        time.sleep(0.5)
        pyautogui.keyUp('left')

    if p_message == '!crouch':
        pyautogui.keyDown('down')
        time.sleep(0.5)
        pyautogui.keyUp('down')

    if p_message == '!jump':
        pyautogui.keyDown('up')
        time.sleep(0.5)
        pyautogui.keyUp('up')

    if p_message == '!sprint':
        if sprint:
            pyautogui.keyDown('shift')
            sprint = not sprint
        else:
            pyautogui.keyUp('shift')
            sprint = not sprint

    if p_message == '!rump':
        pyautogui.keyDown('up')
        pyautogui.keyDown('right')
        time.sleep(0.5)
        pyautogui.keyUp('up')
        pyautogui.keyUp('right')

    if p_message == '!lump':
        pyautogui.keyDown('up')
        pyautogui.keyDown('left')
        time.sleep(0.5)
        pyautogui.keyUp('up')
        pyautogui.keyUp('left')

    if p_message == '!pause':
        if pause:
            pyautogui.keyUp('p')
            pause = not pause
        else:
            pyautogui.keyDown('p')
            pause = not pause
