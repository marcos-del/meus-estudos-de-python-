import pyautogui as pa
import time

pa.press('win')
pa.write("chrome")
time.sleep(2)
pa.press('ENTER')
time.sleep(2)
pa.write("youtube.com")
pa.press('ENTER')