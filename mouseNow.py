#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
print('Press Ctrl-C to quit.')
try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # TODO: Get and print the mouse coordinates.
 except KeyboardInterrupt:
    print('\nDone.')

    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)