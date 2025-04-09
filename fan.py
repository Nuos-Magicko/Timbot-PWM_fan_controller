import pigpio

FAN_MAX_SPEED = 100
FAN_DEFAULT_SPEED = 50
FAN_MIN_SPEED = 0

class fan_ctrl:
    def __init__(self, pwm_pin):
        self.pwm_pin = pwm_pin

        self.pwm = pigpio.pi()
        self.pwm.set_mode(self.pwm_pin, pigpio.OUTPUT)
        # pwm.set_PWM_frequency(self.pwm_pin, 5)

    def set_speed(self, speed = 50):
        '''
        Set-up the fan speed in percentage.
        '''
        speed = speed * 2.55
        self.pwm.set_PWM_dutycycle(int(speed))