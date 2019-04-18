import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from keyboard_input import PressKey, W, A, S, D


def draw_lines(img,lines):
    try: 
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)
    except:
        pass


def interest(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500],
                         ], np.int32)
    processed_img = cv2.GaussianBlur(processed_img,(5,5),0)
    processed_img = interest(processed_img, [vertices])
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 150)
    draw_lines(processed_img,lines)

    return processed_img


def main():
    
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while True:
        # PressKey(W)
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        print('Doing {} fps'.format(1/(time.time()-last_time)))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('feedback', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(33) == ord('a'):
            cv2.destroyAllWindows()
            break


main()