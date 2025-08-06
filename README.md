# Timbot-PWM_fan_controller
 This project is aobut to control the rotational speed of fan on Raspberry Pi CM4 Module.

## Run script on startup

* Copy the python file to /bin:
    ```
    sudo cp -i ~/Timbot-PWM_fan_controller/fan.py /bin
    ```
* Add A New Cron Job:
    ```
    sudo crontab -e
    ```

    Scroll to the bottom and add the following line (after all the #'s):
    ```
    @reboot python3 /bin/fan.py &
    ```
    
    The “&” at the end of the line means the command is run in the background and it won’t stop the system booting up.

* Test it:
    ```
    sudo reboot
    ```