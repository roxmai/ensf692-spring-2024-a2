# input_processing.py
# Roxanne Mai, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = 'green'
        self.pedestrain = 'no'
        self.vehicle = 'no'

    # Function to update the status of the sensor
    # The option selected by the user and changes_made is the new status value to update
    def update_status(self, option, changes_made): # You may decide how to implement the arguments for this function
        if option == '1':
            if changes_made in ["green", "yellow", "red"]:
                self.light = changes_made
            else:
                raise ValueError("Invalid vision change.")
        elif option == '2':
            if changes_made in ["yes", "no"]:
                self.pedestrain = changes_made
            else:
                raise ValueError("Invalid vision change.")
        elif option == '3':
            if changes_made in ["yes", "no"]:
                self.vehicle = changes_made
            else:
                raise ValueError("Invalid vision change.")
        else:
            raise ValueError("You must select either 1, 2, 3 or 0.")



# The sensor object should be passed to this function to print the action message and current status
# Function to print the action message and current status
# the sensor object with the current status
def print_message(sensor):
    if sensor.light == "red" or sensor.pedestrain == "yes" or sensor.vehicle == "yes":
        action = "STOP"
    elif sensor.light == "green" and sensor.pedestrain == "no" and sensor.vehicle == "no":
        action = "Proceed"
    elif sensor.light == "yellow" and sensor.pedestrain == "no" and sensor.vehicle == "no":
        action = "Caution"
    else:
        action = "STOP" # Default action for any other unforeseen combination
    
    print(f"\n{action}\n")
    print(f"Light = {sensor.light} , Pedestrian = {sensor.pedestrain} , Vehicle = {sensor.vehicle} .\n")


# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    sensor = Sensor()
    changes_detected = None
    
   
    while changes_detected != '0':
        print("Are changes are detected in the vision input?")
        try:
            changes_detected = input("Select 1 for light, 2 for pedestrain, 3 for vehicle, or 0 to end the program: ").strip()

            if changes_detected == '0':
                break
            
            if changes_detected not in ['1', '2', '3']:
                print("You must select either 1, 2, 3 or 0.\n")
                continue

            changes_made = input("What change has been identified?: ").strip()

            # Validate and update the sensor status
            sensor.update_status(changes_detected, changes_made)

            # Print the action message and current sensor status
            print_message(sensor)
    
        except ValueError as e:
            print("Invalid vision change.")
            print_message(sensor)
            continue


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

