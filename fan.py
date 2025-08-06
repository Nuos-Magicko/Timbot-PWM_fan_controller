import RPi.GPIO as GPIO

FAN_MAX_SPEED = 100
FAN_DEFAULT_SPEED = 50
FAN_MIN_SPEED = 0

class fan_ctrl:
    def __init__(self, pwm_pin):
        self.pwm_pin = pwm_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.PWM = GPIO.PWM(self.pwm_pin, 1000)
        self.PWM.start(0)

    def set_speed(self, speed = 50):
        '''
        Set-up the fan speed in percentage.
        '''
        self.PWM.ChangeDutyCycle(speed)

if __name__ == "__main__":
    fan = fan_ctrl(12)  # Example GPIO pin
    fan.set_speed(FAN_DEFAULT_SPEED)
    print("Fan speed set to default:", FAN_DEFAULT_SPEED)
    
    # Clean up GPIO on exit
    try:
        while True:
            pass
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIO cleaned up and program exited.")