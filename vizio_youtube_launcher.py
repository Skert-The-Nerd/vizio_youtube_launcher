import time
from pyvizio import Vizio

# Configuration for Vizio TV connection
IP = "192.168.1.185"
DEVICE_ID = "PythonVizio"
DEVICE_TYPE = "tv"
DEVICE_NAME = "My Vizio TV"
AUTH_TOKEN = "Z9u6okz2qw"

# Initialize Vizio instance using the correct parameter for auth token
vizio = Vizio(device_id=DEVICE_ID, ip=IP, name=DEVICE_NAME, auth_token=AUTH_TOKEN, device_type=DEVICE_TYPE)

def main():
    # Step 1: Turn the TV ON
    print("Turning TV ON...")
    vizio.pow_on()
    time.sleep(10)  # Wait for 30 seconds to ensure the TV is fully on

    # Step 2: Launch YouTube App
    print("Launching YouTube App...")
    vizio.launch_app("YouTube")
    time.sleep(5)  # Wait for the app to launch

    # Step 3: Navigate YouTube Interface
    #print("Navigating YouTube Interface...")
    #vizio.remote("DOWN")  # Simulate a down arrow key press on the remote
    #time.sleep(1)
    #vizio.remote("OK")    # Simulate the OK/Enter key press to select
    #time.sleep(5)         # Wait for the interface to update

    # Step 4: Perform key sequence for "Like Im Gonna Lose You"
    print("Performing sequence: Up, OK, then typing out 'Like Im Gonna Lose You'")
    vizio.remote("UP")    # Simulate up arrow key press
    time.sleep(1)
    vizio.remote("OK")    # Simulate the OK key press
    time.sleep(1)
    
    # Type out "Like Im Gonna Lose You"
    for char in "Like Im Gonna Lose You":
        vizio.remote(char.upper())  # Send each character as uppercase for simplicity
        time.sleep(0.2)
    
    vizio.remote("OK")    # Press OK to submit the typed input
    time.sleep(5)         # Wait for the action to complete

if __name__ == "__main__":
    main()
