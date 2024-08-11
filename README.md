# 8bitdo-keyboard
Pi Pico-based solution for running 8Bitdo keyboard extensions directly to USB

## What you need

* A Raspberry Pi Pico board
    * https://www.raspberrypi.com/products/raspberry-pi-pico/
    * You can use the most basic version. Wifi not required.

* A pair of TRS breakout boards
    * like this one: https://core-electronics.com.au/trrs-3-5mm-jack-breakout.html
    * Can be any brand
    * I'm using two, since my chosen 8BD Extension requires two

* Hook up wire
* Some light soldering

## Build

* Schematic coming soon


## Software set up

* Install Circuit python on to your Pico
    * https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython
* Download the Adafruit Circuit python libraries
    * https://circuitpython.org/libraries
* Open your CIRCUITPY drive
* Copy the libraries listed below into your CIRCUITPY/lib/ folder
    * adafruit_hid
    * adafruit_debouncer.mpy
    * adafruit_ticks.mpy
* Copy code.py into the root folder
* Unplug and replug (maybe?)
* Open VS Code and try some buttons

