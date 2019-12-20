# rgbxmastree

A simple python script to drive the Pi Hut's RGB Xmas Tree with various light programs.

## The hardware

You will need a Raspberry Pi and of course the (RGB Xmas Tree)[https://thepihut.com/collections/featured-products/products/3d-rgb-xmas-tree-for-raspberry-pi] 
from The Pi Hut. 

## The required software

You need the following components to run this Python script:

```sudo apt install gpiozero
sudo apt install python3-gpiozero python3-pigpio
```

(I needed to install these, these instructions were missing from the project page)

## This code

You can then just run this code with `python3 xmastree.py`.

There are several modes that will show up in random. Feel free to tweak the main function in order to see more or less of a certain effect.

