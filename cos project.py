print('COS ASSIGNMENT')
print('SULEIMAN SAMSON BWALA(BHU/24/04/05/0038)')
#PHYSICS FORMULAE.........THIS CODE SHOULD BE ABLE TO HELP THE USER PERFORM SIMPLE CALCULATIONS IN PHYSIVCS WITH INPUTABLE VARIABLES##




def calculate_mechanical_advantage():
    load = float(input("Enter your load (L): "))
    effort = float(input("Enter the effort applied (E): "))
    mechanical_advantage = load / effort
    print("The mechanical advantage (M.A) is:", mechanical_advantage)

def calculate_force():
    mass = float(input("Enter your mass (M): "))
    acceleration = float(input("Enter acceleration (a): "))
    force = mass * acceleration
    print("The force (F) is:", force)

def calculate_pressure():
    force = float(input("Enter the force (F): "))
    area = float(input("Enter the area (A): "))
    pressure = force / area
    print("The pressure (P) is:", pressure)

def calculate_period():
    time_taken = float(input("Enter the time taken (T): "))
    number_of_oscillations = float(input("Enter the number of oscillations made (N): "))
    period = time_taken / number_of_oscillations
    print("The period (T) is:", period)

def calculate_density():
    mass = float(input("Enter the mass (M): "))
    volume = float(input("Enter the volume (V): "))
    density = mass / volume
    print("The density (D) is:", density)

def main():
    while True:
        print('\nWhat do you want to do?')
        print('a. Mechanical advantage')
        print('b. Force')
        print('c. Pressure')
        print('d. Period')
        print('e. Density')
        print('f. Quit')

        choice = input('Enter your choice: ')

        if choice == 'a':
            calculate_mechanical_advantage()
        elif choice == 'b':
            calculate_force()
        elif choice == 'c':
            calculate_pressure()
        elif choice == 'd':
            calculate_period()
        elif choice == 'e':
            calculate_density()
        elif choice == 'f':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    main()
