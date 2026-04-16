import pyautogui
import keyboard
import time
import threading

running = False
pressed_kill = False
stop_reason = ""
time_interval = 0
double_click = False
hold = False
hold_time = 0
yes_no_dc = ""
yes_no_hold = ""
yes_no_loc = ""
set_no_loc = True
x = 0
y = 0

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
    global double_click
    global time_interval
    global stop_reason
    global set_no_loc
    global x
    global y
    global hold_time
    global hold
    start_time = time.time()

    while running and pressed_kill != True and (time.time() - start_time < 1800):  # 1800 sec = 30 min
        if set_no_loc != True:
            pyautogui.moveTo(x, y)
        if hold != True:
            pyautogui.click()
            if double_click == True:
                pyautogui.click()
            time.sleep(time_interval)
        else:
            pyautogui.mouseDown()
            time.sleep(hold_time)
            pyautogui.mouseUp()
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
        print("Press F6 to start again. Won't start again if kill switch has been activated.")
    else:
        print("❌ Stopped")
        print("Press F6 to start again. Won't start again if kill switch has been activated.")

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
    print("🛑 Kill switch has been activated.")

keyboard.add_hotkey("F6", start)
keyboard.add_hotkey("F7", stop)
keyboard.add_hotkey("Esc", kill)

print("⚠️  Warning, use this under your own risk. Autoclicking may break the ToS. This program may be uncontrollable.\nQuickly move your mouse to any of the corner of the screen in case the Esc key fails.")
time_interval = float(input("Enter the time interval between the click in seconds (Decimals are allowed) (Very fast intervals may break your PC or the app): "))
print("Do you want to do hold the click?")
yes_no_hold = input('Type "yes" to do hold: ').lower()
if yes_no_hold == "yes":
    hold = True
    hold_time = float(input("Enter how long you want to hold the click (Decimals are allowed): "))
else:
    hold = False
    print("Do you want to do double click?")
    yes_no_dc = input('Type "yes" to do double click: ').lower()
    if yes_no_dc == "yes":
        double_click = True
    else:
        double_click = False
print("Do you want to set the click location right here?")
yes_no_loc = input('Type "yes" set in here: ').lower()
if yes_no_loc == "yes":
    set_no_loc = True
else:
    set_no_loc = False
    text = input("Enter the location to autoclick (x, y)): ")
    x, y = map(int, text.split(","))
print("F6 = start, F7 = stop | Esc = kill switch")
keyboard.wait()
