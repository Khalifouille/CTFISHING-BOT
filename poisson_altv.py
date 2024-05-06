import cv2
import numpy as np
import pytesseract
import pyautogui
import time
import os
from PIL import Image
import psutil
import keyboard

pyautogui.FAILSAFE = False

game_name = 'altv-webengine.exe'
game_running = False

for proc in psutil.process_iter():
    try:
        process_info = proc.as_dict(attrs=['pid', 'name'])
        if process_info['name'] == game_name:
            game_running = True
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

if game_running:
    print("Le jeu est lancé. Wala mon akhi")
    test_folder = os.path.join(os.path.expanduser("~"), "Desktop", "test")

    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    word_count = 0

    while True:

        time.sleep(7)
        keyboard.press("e")
        time.sleep(7)
        keyboard.release("e")

        time.sleep(60)

        left = 550
        top = 420
        width = 300
        height = 100

        screenshot = pyautogui.screenshot(region=(left, top, width, height))

        filename = os.path.join(test_folder, "screenshot.png")

        screenshot.save(filename)

        image = cv2.imread(filename)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpened = cv2.filter2D(threshold, -1, kernel)

        processed_filename = os.path.join(test_folder, "processed.png")
        cv2.imwrite(processed_filename, sharpened)

        texte = pytesseract.image_to_string(Image.open(processed_filename), config="--psm 11")
        texte = texte.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
        word_count += 1

        for lettre in texte:
            print(lettre, end="", flush=True)
            if lettre in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                pyautogui.press(lettre)
            elif lettre == " ":
                pyautogui.press("space")
            elif lettre == "\n":
                pyautogui.press("enter")
            elif lettre == "\t":
                pyautogui.press("tab")

        keyboard.press_and_release('i')
        time.sleep(5)
        pyautogui.moveTo(1353, 743)
        time.sleep(5)
        pyautogui.click(clicks=6)
        time.sleep(5)
        keyboard.press_and_release('esc')

        print("\nNombre de mots écrits : {}".format(word_count))

        time.sleep(5)

else:
    print("Le jeu n'est pas lancé. Zbi.")
