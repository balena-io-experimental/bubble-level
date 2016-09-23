from sense_hat import SenseHat

sense = SenseHat()

BL = [0, 0, 0]
A1 = [166, 125, 0]
A2 = [247, 195, 15]
A3 = [255, 236, 82]

resin_logo = [
BL, BL, BL, A1, A1, BL, BL, BL,
BL, BL, A1, A2, A3, A1, BL, BL,
BL, A1, A2, A1, A1, A3, A1, BL,
A3, A2, A3, A1, A1, A2, A3, A2,
A3, A2, A3, A3, A2, A2, A3, A2,
BL, A3, A1, A3, A2, A1, A2, BL,
BL, BL, A3, A1, A1, A2, BL, BL,
BL, BL, BL, A3, A1, BL, BL, BL
]

sense.set_pixels(resin_logo)
