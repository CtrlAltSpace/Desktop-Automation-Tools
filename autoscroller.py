import pyautogui
import keyboard
import time
import threading
import re

running = False
pressed_kill = False
stop_reason = ""
time_interval = 0
yes_no = ""
inverse_scroll = False

def start():
    global running
    global pressed_kill
    if not running:
        if pressed_kill != True:
            print("Starting")
            print("Press F7 to stop. \nFor kill switch, use Esc key")
            print("Will start in 5.")
            time.sleep(1)
            print("4")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("0")
            print("⚠️  Started!")
            running = True
            threading.Thread(target=spam_loop).start()

def spam_loop():
    global pressed_kill
    global running
    global time_interval
    global stop_reason
    global inverse_scroll
    start_time = time.time()

    while running and pressed_kill != True and (time.time() - start_time < 1800):  # 1800 sec = 30 min
        if inverse_scroll:
            pyautogui.scroll(200)
            time.sleep(time_interval)
        else:
            pyautogui.scroll(-200)
            time.sleep(time_interval)

    elapsed = time.time() - start_time
    if pressed_kill == True:
        stop_reason = "pressed_kill"
    elif running == False:
        stop_reason = "stop"
    elif elapsed >= 1800:
        stop_reason = "timer"
    else:
        stop_reason = "stop"

    running = False
    if stop_reason == "pressed_kill":
        print("❌ Stopped")
        print("Won't start again as kill switch has been activated.")
    elif stop_reason == "timer":
        print("⏲️  Stopped by safety limit")
        print("Press F6 to start again. Won't start again as kill switch has been activated.")
    else:
        print("❌ Stopped")
        print("Press F6 to start again. Won't start again as kill switch has been activated.")

def stop():
    global running
    global stop_reason
    running = False
    stop_reason = "stop"

def kill():
    global running
    global pressed_kill
    global stop_reason
    running = False
    pressed_kill = True
    stop_reason = "pressed_kill"
    print("⚠️  Kill switch has been activated.")

keyboard.add_hotkey("F6", start)
keyboard.add_hotkey("F7", stop)
keyboard.add_hotkey("Esc", kill)

print("⚠️  Warning, use this under your own risk. This program may be uncontrollable. Quickly move your mouse to any of the corner of the screen in case the Esc key fails.")
time_interval = float(input("Enter the time interval between the scroll in seconds (Very fast intervals may break your PC or the app.): "))
print("Does the app/website have inverse scroll?")
yes_no = input('Type "yes" if it is inverse scroll: ').lower()
if yes_no == "yes":
    inverse_scroll = True
else:
    inverse_scroll = False
print("F6 = start, F7 = stop | Esc = kill switch")
keyboard.wait()
