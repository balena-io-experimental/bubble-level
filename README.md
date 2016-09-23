# bubble-level
Show a "bubble" based on angle on a Raspberry Pi Sense HAT, with a configurable error threshold

This simply uses the orientation data from a Raspberry Pi Sense HAT to show an indication of angle, much as a [bubble level or spirit level](https://www.wikiwand.com/en/Spirit_level) does.

When the angle of the Raspberry Pi exceeds the limit specified by the "range" variable, it is considered to be out of bounds and a notice will be printed on the console and the LEDs will flash red.
