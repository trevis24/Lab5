import time
from hal import hal_lcd as LCD

lcd = LCD.lcd()

def main():
    show_colon=True
    while True:
        local_time = time.localtime() # get struct_time  
        time_string = time.strftime("%H:%M:%S", local_time)
        date_string = time.strftime("%d:%m:%Y", local_time)

        if show_colon == False:
            time_string=time_string.replace(":"," ")

        lcd.lcd_clear()
        lcd.lcd_display_string(time_string, 1)
        lcd.lcd_display_string(date_string, 2)

        show_colon = not show_colon
        time.sleep(1)



if __name__ == "__main__":
    main()
