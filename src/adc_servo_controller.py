
from hal import hal_adc as adc
from hal import hal_servo as servo
from time import sleep

def main():

    # Initialise ADC and Servo
    adc.init()
    servo.init()

    while True:

        # Read potentiometer from ADC channel 1
        adc_value = adc.get_adc_value(1)

        # Convert ADC value to servo angle
        angle = 180 - (adc_value * 180 / 1023)

        # Set servo motor angle
        servo.set_servo_position(angle)

        # Display values in terminal
        print("ADC:", adc_value, "Angle:", angle)

        sleep(0.2)


if __name__ == "__main__":
    main()
    