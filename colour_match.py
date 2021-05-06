import cv2
import numpy as np
from PIL import ImageGrab
import imutils

class match_c:
    def get_green_red(self, left_x, top_y, right_x, bottom_y):
        run = True

        while run is True:
            screen = np.array(ImageGrab.grab(bbox=(left_x, top_y, right_x, bottom_y)))
            green_upper_range = np.array([20, 200, 140])  # Set the Lower range value of color in
            green_lower_range = np.array([0, 170, 100])  # Set the Upper range value of color in
            mask = cv2.inRange(screen, green_lower_range, green_upper_range)  # Create a mask with range

            red_upper = np.array([210, 50, 80])  # Set the Lower range value of color in
            red_lower = np.array([190, 30, 60])  # Set the Upper range value of color in74, 48, 207
            mask2 = cv2.inRange(screen, red_lower, red_upper)  # Create a mask with range

            merge = cv2.bitwise_or(mask, mask2)

            ret, thresh = cv2.threshold(merge, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            # You need to choose 4 or 8 for connectivity type
            connectivity = 4
            # Perform the operation
            output = cv2.connectedComponentsWithStats(thresh, connectivity, cv2.CV_32S)

            return output[3]

