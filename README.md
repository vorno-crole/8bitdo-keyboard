# 8bitdo-keyboard
Pi Pico-based solution for running 8Bitdo keyboard extensions directly to USB

## What you need

* A Raspberry Pi Pico board
    * https://www.raspberrypi.com/products/raspberry-pi-pico/
    * You can use the most basic version. Wifi not required.
* A pair of TRS breakout boards
    * like this one: https://core-electronics.com.au/trrs-3-5mm-jack-breakout.html
    * Can be any brand
    * I'm using two, since my [chosen 8BD Extension](https://shop.8bitdo.com/products/8bitdo-keyboard-extensions?variant=44141790068913) needs two jacks
* Hook up wire
* Some light soldering

## Build

* Schematic coming soon


## Software set up

* Install Circuit Python on to your Pico
    * https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython

* Download the Adafruit Circuit Python libraries
    * https://circuitpython.org/libraries

* Open your CIRCUITPY drive
* Copy the following libraries (listed below) into your CIRCUITPY/lib/ folder
    * adafruit_hid (the whole folder)
    * adafruit_debouncer.mpy
    * adafruit_ticks.mpy
* Copy code.py (from this repository) into the root CIRCUITPY/ folder
* (maybe) You might need to unplug and reconnect the Pico to your computer for changes to be seen
* Open VS Code (or Notepad) and test your buttons

