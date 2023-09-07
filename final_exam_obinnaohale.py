# Obinna Ohale
# Introduction to Programming with Python
# Live Code File for Final Exam
# I particated in the live sessions
# Thank you for this amazing class Professor Garwood

# START main
def main():
    """
    Main Function Description: This is the main driver for this app, and enforces a proper flow of the flight
    cycle (starting with take-off, then in-flight, and finally landing). The two variables described below,
    user_selection and previous_selection are used to enforce the flight cycle. This application uses other
    functions described for data processing and file updates.
    :: No incoming data (empty parameter list)
    :: Print welcome message "Welcome to Python Airways"
    """
    print("\nWelcome to Python Airways")
    print("\n\tYou will be prompted for 1) flight-phase, and 2) plane angle data.")
    # :: Create Variables:
    user_selection = 0
    previous_selection = 0
    # :: Initialize previous_selection at 0
    save_flight_data("Flight Beginning", 0, "Taxi-to-Runway")
    flight_phase, angle = data_prompt()
    while user_selection != 4:  # (4 is exit – see data prompt for actual message)
        # :: A while loop is used to manage the flight cycle
        # :: while user_selection is not equal to 4 (4 is exit – see data prompt for actual message)
        if flight_phase >= previous_selection and flight_phase == 1:
            take_off_calculation(angle)
            previous_selection = flight_phase
        if flight_phase >= previous_selection and flight_phase == 2:
            in_flight_calculation(angle)
            previous_selection = flight_phase
        if flight_phase >= previous_selection and flight_phase == 3:
            landing_calculation(angle)
            previous_selection = flight_phase
        if flight_phase == 4:
            save_flight_data("Flight Successful", 0, "Taxi-to-Terminal")
            break
        # if any other flight_phase value is found:
        #   save_flight_data(flight_phase, angle, "invalid data")
        #   Print a message "Invalid data received, please try again"
        flight_phase, angle = data_prompt()
    print("\nThank you for flying Python Airways")
    return


# :: No incoming data (empty parameter list)
def data_prompt():
    """ Description: This function prompts the user for data, validates the data is received, and returns the data
    to the caller. Use two Try-Except blocks to validate user input.
    * Create Variables:
    flight_status, current_angle
    * First Try Block Collects Flight Status Data (flight_status) """
    # print options for the user:
    print("\n\tFlight Phase: ")
    print("\t\t1) Take-off")
    print("\t\t2) In-flight")
    print("\t\t3) Landing")
    print("\t\t4) Exit")
    # print("\t\tPlease enter flight phase: ")
    # Take user input (save data into flight_status)
    # Use catch block to attempt the cast of the data into an integer
    #   Handle improper character data received:
    try:
        flight_status = int(input("\t\tPlease enter flight status: "))
        if flight_status == 4:
            pass
    except ValueError:
        #   if improper data is received set flight_status to -1
        flight_status = -1
        pass

    if flight_status < 1 or flight_status > 3:
        current_angle = 0  # improper data was received in first try-catch bock
    else:
        try:
            current_angle = float(input("\t\tPlease enter current angle: "))
        except ValueError:
            flight_status = -1
            current_angle = 0
    #   Take user input (save into angle)
    #   Use catch block to attempt the cast of the data into a float
    #   if improper data is received set flight_status to -1
    #       and set angle to 0
    # Return flight_status and angle
    return flight_status, current_angle


# START save_flight_data
# :: Three incoming data members (flight phase, angle, message)
# This is okay as a definition:
# def save_flight_data(data1, inter, data2):
#     pass
# This is how we would call the function
# save_flight_data("Flight Beginning" , 0, "Taxi-to-runaway")

def save_flight_data(flight_phase, angle, message):
    """ Description: This function creates a text-log of all flight data received. Each time a user enters proper
    data, this function is called, and that data is appended into the file. This file also records any error
    messages which are generated for the user. When the application starts, an initial message should be
    recorded, and before the app ends, another final message should be recorded. When the app starts, if
    the text file does not exist, create it, otherwise if the file does exist (a subsequent run of the app) then
    simply append new information into the file which already exists. """
    file_name = "flight_log.txt"
    # :: Establish a file handle and open the file in append mode
    with open(file_name, 'a') as file_handle:
        # :: Write the three data pieces of data received to the file (place all on the same line)
        file_handle.write('\n{} {} {}'.format(flight_phase, angle, message))
    # :: Close the file handle
    # :: Return (void or nothing)
    # END save_flight_data
    return


# take_off_calculation
# One incoming data member (angle)
def take_off_calculation(angle):
    min_pitch = 30.0
    max_pitch = 45.0
    reduce_dup(angle, max_pitch, min_pitch)
    return


def in_flight_calculation(angle):
    min_pitch = 4.1
    max_pitch = 5.2
    reduce_dup(angle, max_pitch, min_pitch)
    return


def landing_calculation(angle):
    """ Developer's Note: There are three calculation functions (take_off_calculation, in_flight_calculation and
    landing_calculation): Each of these functions has the same flow, but contain different static data (min
    and angle ranges) and text messages. Please code these functions alike, but update each with the
    appropriate min and max angle ranges, and update text messages (i.e., 'take-off, 'in-flight, and 'landing')
    for each function. The take_off_calculation is outlined below.
    Description: This function calculates data received from the user in order to create an update message,
    which is both printed to the screen, and saved into the flight_log.
    * Establish a baseline 'take off' message as a variable (basic_message)
    * basic_message = "The acceptable take-off pitch range is 30 – 45-degrees."
    * Create Variables for maximum and minimum take-off pitch range """
    min_pitch = 12
    max_pitch = 25.5
    reduce_dup(angle, max_pitch, min_pitch)
    # # :: Check (angle) received from user against max_pitch and min_pitch
    # if angle > max_pitch:
    #     adjustment = angle - max_pitch
    #     adjust_message = "\t\tNose DOWN by {:.2f} degrees.".format(adjustment)
    #     print(adjust_message)
    # elif angle < min_pitch:
    #     adjustment = min_pitch - angle
    #     adjust_message = "\t\tNose UP by {:.2f} degrees.".format(adjustment)
    #     print(adjust_message)
    # else:
    #     adjust_message = "Maintain your current pitch at {}".format(angle)
    #     print(adjust_message)
    # save_flight_data("take-off", angle, adjust_message)
    return


def reduce_dup(angle, max_pitch, min_pitch):
    if angle > max_pitch:
        adjustment = angle - max_pitch
        adjust_message = "\t\tNose DOWN by {:.2f} degrees.".format(adjustment)
        print(adjust_message)
    elif angle < min_pitch:
        adjustment = min_pitch - angle
        adjust_message = "\t\tNose UP by {:.2f} degrees.".format(adjustment)
        print(adjust_message)
    else:
        adjust_message = "Maintain your current pitch at {}".format(angle)
        print(adjust_message)
    save_flight_data("take-off", angle, adjust_message)
    return


if __name__ == "__main__":
    main()


