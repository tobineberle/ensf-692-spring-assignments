# input_processing.py
# TOBIN EBERLE, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:
    def __init__(self, light = 'red', pedestrian = 'yes', vehicle = 'yes'):
        self.light = light
        self.pedestrian = pedestrian
        self.vehicle = vehicle
        self.status = 'STOP'

    #From the README specifications:
    # Any scenario where a red light, a pedestrian or a vehicle are detected should display the message "STOP"
    # A green light with no pedestrian or vehicle detected should display the message "Proceed"
    # A yellow light with no pedestrian or vehicle detected should display the message "Caution"
    def update_status(self):

        if self.light in 'red':
            self.status = 'STOP'

        elif self.pedestrian in 'no' and self.vehicle in 'no':
            match self.light:

                case 'green':
                    self.status = 'Proceed'

                case 'yellow':
                    self.status = 'Caution'


#print_message() accepts a sensor obeject and prints the value of the status and the other instance variables
def print_message(sensor):
    print("\nSensor status: Status =  " + sensor.status)
    print("Sensor readings: Light = " + sensor.light + " Pedestrian = " + sensor.pedestrian + " Vehicle = " +sensor.vehicle +"\n")

#Main code
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    #Initialize loop and sensor variables
    sensor = Sensor()
    inputError = ValueError

    #CLI loop
    while(True):
        
        try:
            userInput = int (input("""           
Has there been a change in vision input? Please input an option from below:\n
0. Quit Program\n
1. Light\n
2. Pedestrian\n
3. Vehicle\n          
"""))
            #Matches the user input to a specfied use case, otherwise returns error message
            match userInput:

                #Case 0, exit program
                case 0:
                    print("\nGoodbye.")
                    break

                #Case 1, update light
                case 1:
                    lightInput = input("What change has been identified? (green/yellow/red): \n")

                    if lightInput in ('green', 'yellow', 'red'):
                        sensor.light = lightInput
                        sensor.update_status()
                        print_message(sensor)
                    else:
                        raise inputError
                        
                #Case 2, update pedestrian
                case 2:
                    pedInput = input("What change has been identified? (yes/no): \n")

                    if pedInput in ('yes', 'no'):
                        sensor.pedestrian = pedInput
                        sensor.update_status()
                        print_message(sensor)
                    
                    else:
                        raise inputError
                        
                #Case 3, update vehicle
                case 3:
                    vechicleInput = input("What change has been identified? (yes/no): \n")

                    if vechicleInput in ('yes', 'no'):
                        sensor.vehicle = vechicleInput
                        sensor.update_status()
                        print_message(sensor)
                    else:
                        raise ValueError("Please input an item from the list.\n")
                        
                #Catch all case, return an error for incorrect number
                case _:
                    raise inputError

        except ValueError:
            print("\nError! Please input an item from the list.")
            

if __name__ == '__main__':
    main()

