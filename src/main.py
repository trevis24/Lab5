
from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control

lcd = LCD.lcd()

# Called whenever a keypad button is pressed
def key_pressed(key):

    # REQ-02: Press 1 to blink LED
    if key == 1:
        led_control.delay = 1

        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("Blink LED", 2)

    # REQ-03: Press 0 to stop LED
    elif key == 0:
        led_control.delay = 0
        led_control.led.set_output(20, 0)

        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("OFF LED", 2)


def main():

    # REQ-01: Display starting menu
    lcd.lcd_clear()
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string("0:Off 1:Blink", 2)

    # Initialise keypad
    keypad.init(key_pressed)

    # Start keypad thread
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    # Initialise LED control
    led_control.led_control_init()


if __name__ == "__main__":
    main()
