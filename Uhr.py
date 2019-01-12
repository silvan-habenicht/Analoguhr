import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


pwm_frequenz = 50

out_stunde  = GPIO.PWM(11, pwm_frequenz)
out_minute  = GPIO.PWM(13, pwm_frequenz)
out_sekunde = GPIO.PWM(15, pwm_frequenz)

out_stunde.start(0)
out_minute.start(0)
out_sekunde.start(0)

try:
    while 1:

        zeit   = time.localtime()
        
        stunde  = zeit.tm_hour
        minute  = zeit.tm_min
        sekunde = zeit.tm_sec

        if stunde > 12:
            stunde = stunde - 12
        
        out_stunde.ChangeDutyCycle( (stunde  * 100) / 12)
        out_minute.ChangeDutyCycle( (minute  * 100) / 60)
        out_sekunde.ChangeDutyCycle((sekunde * 100) / 60)

        time.sleep(1)   

except KeyboardInterrupt:
    pass

out_stunde.stop()
out_minute.stop()
out_sekunde.stop()
GPIO.cleanup()

