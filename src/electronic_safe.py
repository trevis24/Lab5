from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_buzzer as buzzer
from hal import hal_lcd as LCD
from time import sleep

lcd = LCD.lcd()
lcd.lcd_clear()
password=[]
display=""
count =0
unlocked=False

def key_pressed(key):
    global password, display, count,unlocked
    if unlocked == True or count >= 3:
            return
    lcd.lcd_clear()
    lcd.lcd_display_string("Pin",1)
    password.append(key)
    display+='*'
    print(display)
    print(password)
    lcd.lcd_display_string(display,2)

    
    
    if len(password)==4:

        if password[0] == 1 and password[1] == 2 and password[2] == 3 and password[3] == 4:
                lcd.lcd_clear() 
                lcd.lcd_display_string("Safe Unlocked",1)
                lcd.lcd_display_string("",2)
                unlocked=True


        else:
                lcd.lcd_display_string(" Wrong Pin",1)
                lcd.lcd_display_string("",2)
                buzzer.turn_on_with_timer(1)
                password=[]
                display=""
                count +=1
                sleep(3)
                lcd.lcd_clear()
                key_start()

    if count >= 3:
            lcd.lcd_clear()
            lcd.lcd_display_string("Safe Disabled", 1)

    


def key_start():
    lcd.lcd_clear()
    lcd.lcd_display_string("Safe Lock",1)
    lcd.lcd_display_string("Enter PIN",2)

def main():
    lcd.lcd_clear()
    key_start()
    buzzer.init()
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()



if __name__ == "__main__":
    main()