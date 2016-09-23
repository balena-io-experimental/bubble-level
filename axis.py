from sense_hat import SenseHat

# Maxium range of distance from zero to detect (in degrees)
range = 45

def distance_from_zero(d):
  if (360 - d) > d:
    return d
  else:
    return d-360

def map_to_axis(d):
  # We have an 8x8 grid, so we have 4 pixels in each direction from the origin
  scale = int(round(d / (range/4)))

  # Normalize for everything being [0,4] by starting positive direction at 3
  if d < 0:
    return 4 + scale
  else:
    return 3 + scale

def out_of_bounds(sense, range, pitch, roll):
  sense.clear(255, 0, 0)
  print("THRESHOLD EXCEEDED!")
  if abs(pitch) > range:
    print("pitch: " + str(pitch) + " (threshold: " + str(range) + ")")
  else:
    print ("roll: " + str(roll) + " (threshold: " + str(range) + ")")
  print("")


sense = SenseHat()

while True:
  # Get data from the sensors
  orientation = sense.get_orientation_degrees()
  # Normalize this to be distance from origin (for display)
  p = distance_from_zero(orientation['pitch'])
  r = distance_from_zero(orientation['roll'])
  # Map p to x axis, r to y axis and find pixel to light up
  x = map_to_axis(p)
  y = map_to_axis(-r)

  sense.clear()
  if (x > 7 or y > 7 or x < 0 or y < 0):
    out_of_bounds(sense, range, p, r)
  else:
    sense.set_pixel(x, y, 0, 255, 0)
