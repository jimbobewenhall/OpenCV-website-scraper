import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
from datetime import timedelta
from datetime import datetime



class match:
    def get_match(self, main_image, template_image):
        img_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

        template = cv2.imread(template_image, 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        rect_list = []

        for pt in zip(*loc[::-1]):
            cv2.rectangle(main_image, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            x = np.array(pt)
            y = np.array([pt[0] + w, pt[1] + h])
            rect_list.append([x,y])


        return main_image, rect_list

    def wait_for_match(self, template_image, y_screen, x_screen, move_to=False, click_on=False, movement_type='mid', timeout=10):
        wait_until = datetime.now() + timedelta(seconds=timeout)
        run = True

        while run is True:
            if wait_until < datetime.now():
                run = False
            screen = np.array(ImageGrab.grab(bbox=(0, 0, y_screen, x_screen)))
            img_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

            template = cv2.imread(template_image, 0)
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.95
            loc = np.where(res >= threshold)

            rect_list = []

            for pt in zip(*loc[::-1]):
                cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
                x = np.array(pt)
                y = np.array([pt[0] + w, pt[1] + h])
                rect_list.append([x,y])

            if rect_list:
                mid_array = (rect_list[0][0] + rect_list[0][1]) / 2
                mid_list = mid_array.tolist()
                if move_to is True:
                    if movement_type == 'mid':
                        pyautogui.moveTo(mid_list[0], mid_list[1])
                    if movement_type == 'left':
                        pyautogui.moveTo(pt[0]+(0.2*w), pt[1]+(h/2))
                    if movement_type == 'right':
                        pyautogui.moveTo(pt[0]+w-(0.2*w), pt[1]+(h/2))
                    if click_on is True:
                        pyautogui.click()
                return

    def get_bounding_box(self, top_template, bottom_template, right_template, y_screen, x_screen, timeout=10):
        wait_until = datetime.now() + timedelta(seconds=timeout)
        run = True

        while run is True:
            if wait_until < datetime.now():
                run = False
            screen = np.array(ImageGrab.grab(bbox=(0, 0, y_screen, x_screen)))
            img_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

            template = cv2.imread(top_template, 0)
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.95
            loc = np.where(res >= threshold)

            rect_list = []

            for pt in zip(*loc[::-1]):
                cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
                rect_list.append(pt)

            template = cv2.imread(bottom_template, 0)
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.95
            loc = np.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
                rect_list.append([pt[0], pt[1]-h])

            template = cv2.imread(right_template, 0)
            w, h = template.shape[::-1]

            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.95
            loc = np.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
                x = np.array(pt)
                y = np.array([pt[0] + w, pt[1] + h])
                mid = (x+y)/2
                rect_list.append(mid)

            if len(rect_list) == 3:
                return rect_list