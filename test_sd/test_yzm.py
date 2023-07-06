from PIL import Image
import cv2
import numpy


image = Image.open('')

gray_image = image.convert("L")

threshold = 100

binary_image = gray_image.point(lambda x: 0 if x < threshold else 255, '1')

image_array = cv2.cvtColor(numpy.array(binary_image), cv2.COLOR_RGB2BGR)

contours, hierarchy = cv2.findContours(image_array, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

slider_contour = max(contours, key=cv2.contourArea)

slider_x, slider_y, slider_w, slider_h = cv2.boundingRect(slider_contour)
