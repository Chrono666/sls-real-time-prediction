"""
Created on Tue Feb  1 13:27:24 2022

FLIR Image to JPG
"""

#Für den Import der FLIR Images
import flirimageextractor

temp_min = 162
temp_max = 250


fir = flirimageextractor.FlirImageExtractor()
fir.process_image('1234.jpg')
fir.save_images(minTemp=temp_min, maxTemp=temp_max)


#Kompletten Ordner Interieren

import flirimageextractor
import os

fir = flirimageextractor.FlirImageExtractor()

temp_min = 162
temp_max = 250

path = "D:/_Education/FH Campus/BA2/_Programme/jpegTest/Bilder"
with os.scandir(path) as it:
    for entry in it:
        if entry.name.endswith(".jpg") and entry.is_file():
            print(entry.name)
            fir.process_image(entry.name)
            fir.save_images(minTemp=temp_min, maxTemp=temp_max)



