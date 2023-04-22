import RPi.GPIO as GPIO
import time

# Set BCM pin number for the moisture sensor
MOISTURE_SENSOR_PIN = 18

# Set BCM pin number for the relay (motor)
RELAY_PIN = 23

# Function to check soil moisture
def check_soil_moisture():
    # Set GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set up the moisture sensor pin as an input
    GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)

    # Set up the relay pin as an output
    GPIO.setup(RELAY_PIN, GPIO.OUT)

    # Function to read the moisture level
    def read_moisture_level():
        # Read the moisture sensor value
        moisture_value = GPIO.input(MOISTURE_SENSOR_PIN)
        return moisture_value

    # Read the moisture level
    moisture_level = read_moisture_level()

    # Display the soil status based on the moisture sensor value
    if moisture_level == GPIO.LOW:
		print("Soil is wet")
    else:
        print("Soil is dry")

    # Turn off the relay initially
    GPIO.output(RELAY_PIN, GPIO.LOW)
    motor_status = "off"

    # Control the relay based on the moisture sensor value
    if moisture_level == GPIO.LOW:
        print("Turning off the motor")
        # Turn off the relay
        GPIO.output(RELAY_PIN, GPIO.LOW)
        motor_status = "off"
    else:
        print("Turning on the motor for 5 seconds")
        print("Watering the plants")
        # Turn on the relay for 5 seconds
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        motor_status = "on"
	  time.sleep(5)
        # Turn off the relay
        GPIO.output(RELAY_PIN, GPIO.LOW)
        motor_status = "off"

    # Display the motor status
    print("Motor status: " + motor_status)

    # Clean up GPIO
    GPIO.cleanup()

# Function to call check_soil_moisture() every 30 seconds
def c():
    while True:
        check_soil_moisture()
        time.sleep(30)

# Call the function to check soil moisture every 30 seconds
c()
