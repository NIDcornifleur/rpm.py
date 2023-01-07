import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pulse_count = 0

start_time = time.time()

while True:
  if GPIO.input(19) == 0:
    pulse_count += 1

  elapsed_time = time.time() - start_time

  if elapsed_time > 1:
    rpm = pulse_count / elapsed_time

    pulse_count = 0
    start_time = time.time()

    print("RPM:", rpm)



