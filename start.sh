#!/bin/bash

# i2c needed for sense hat
modprobe i2c-dev

python /app/axis.py
