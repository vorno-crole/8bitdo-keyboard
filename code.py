import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_debouncer import Debouncer

# Set your pins here
btn_A_pin = board.GP16
btn_B_pin = board.GP17
btn_X_pin = board.GP19
btn_Y_pin = board.GP18

# Set your keys here
btn_A_key = Keycode.Q
btn_B_key = Keycode.W
btn_X_key = Keycode.E
btn_Y_key = Keycode.R


# Set up HID keyboard
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Set up pins
btn_A = digitalio.DigitalInOut(btn_A_pin)
btn_A.direction = digitalio.Direction.INPUT
btn_A.pull = digitalio.Pull.DOWN
btn_A_switch = Debouncer(btn_A)

btn_B = digitalio.DigitalInOut(btn_B_pin)
btn_B.direction = digitalio.Direction.INPUT
btn_B.pull = digitalio.Pull.DOWN
btn_B_switch = Debouncer(btn_B)

btn_X = digitalio.DigitalInOut(btn_X_pin)
btn_X.direction = digitalio.Direction.INPUT
btn_X.pull = digitalio.Pull.DOWN
btn_X_switch = Debouncer(btn_X)

btn_Y = digitalio.DigitalInOut(btn_Y_pin)
btn_Y.direction = digitalio.Direction.INPUT
btn_Y.pull = digitalio.Pull.DOWN
btn_Y_switch = Debouncer(btn_Y)

# Main loop
while True:
    btn_A_switch.update()
    btn_B_switch.update()
    btn_X_switch.update()
    btn_Y_switch.update()

    # A Button: letter Q
    if btn_A_switch.rose:
        keyboard.press(btn_A_key)
    if btn_A_switch.fell:
        keyboard.release(btn_A_key)

    # # AB Button: letter W
    if btn_B_switch.rose:
        keyboard.press(btn_B_key)
    if btn_B_switch.fell:
        keyboard.release(btn_B_key)

    # # X Button: letter E
    if btn_X_switch.rose:
        keyboard.press(btn_X_key)
    if btn_X_switch.fell:
        keyboard.release(btn_X_key)

    # # A Button: letter R
    if btn_Y_switch.rose:
        keyboard.press(btn_Y_key)
    if btn_Y_switch.fell:
        keyboard.release(btn_Y_key)

