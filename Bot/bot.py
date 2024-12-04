#-*- coding:utf-8 -*-
import pyautogui
from time import sleep

with open('name.txt', 'r', encoding="UTF-8") as file:
    for line in file:
        name = line.split(',')[0]
        middleName = line.split(',')[1]
        lastName = line.split(',')[2]
        identification = line.split(',')[3]
        pswd = 12345678

        pyautogui.click(2298,289,duration=2)
        pyautogui.click(2541,284,duration=2)
        #sleep(2)

        sleep(5) #Writes down the name
        pyautogui.click(2541,284,duration=5)
        pyautogui.typewrite(name)
        
        #Writes Middle and Last name
        pyautogui.click(2933,284,duration=3) 
        pyautogui.typewrite(f"{middleName} {lastName}")
        
        #Formats the e-mail
        pyautogui.click(2432,351,duration=3) 
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('backspace')
        pyautogui.write(f"{name.lower()}{lastName.lower()}")
        pyautogui.write(f".e{identification}")
        
        #Select the position
        pyautogui.click(2569,529,duration=2)
        pyautogui.click(2851,537,duration=2)
        pyautogui.click(2722,618,duration=2)
        pyautogui.click(2819,641,duration=2)
        pyautogui.click(3061,963,duration=2)

        #Defines a temporary password
        pyautogui.click(2398,814,duration=2)
        pyautogui.click(2482,866,duration=2)
        pyautogui.write(f"{pswd}")
        pyautogui.click(2670,865,duration=2)

        #Finishes
        pyautogui.click(3224,1012,duration=1)

        sleep(5)

        #Selects the e-mail
        pyautogui.click(2801,341,duration=2)
        
        pyautogui.doubleClick(2801,341,duration=2)
        pyautogui.hotkey('shift', 'end')
        sleep(2)

        #Copy and paste
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.click(109,342,duration=1) 
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'v')

        #Jumps to the next line and repeats
        pyautogui.click(3192,719,duration=1)
        pyautogui.click(2049,121,duration=1)
        sleep(4)