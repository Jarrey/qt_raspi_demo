#!/usr/bin/python3

import io
import time
import picamera
from PIL import Image
import zbar
import numpy

# create a reader
scanner = zbar.Scanner()

try:
  while True:
    # Create the in-memory stream
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
      camera.rotation = 180
      camera.start_preview()
      time.sleep(2)
      camera.capture(stream, format='jpeg')

    stream.seek(0)
    pil = Image.open(stream)
    pil = pil.convert('L')

    # wrap image data
    image = numpy.array(pil)

    # scan the image for barcodes
    symbols = scanner.scan(image)

    for symbol in symbols:
      print(f'Result: {symbol.data.decode("UTF-8")}')

except KeyboardInterrupt:
  pass
