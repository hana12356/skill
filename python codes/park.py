# Initialize parking slots with False indicating slot is empty
parking_slots = [False] * 20

def park_vehicle():
    while True:
        slot_number = int(input("Enter the parking slot number (1-20): "))
        
        if slot_number < 1 or slot_number > 20:
            print("Invalid slot number. Please enter a number between 1 and 20.")
            continue
        
        if parking_slots[slot_number - 1] == False:
            parking_slots[slot_number - 1] = True
            print(f"Vehicle parked successfully in slot {slot_number}.")
            break
        else:
            print(f"Slot {slot_number} is already occupied. Please select a different slot.")

def exit_vehicle():
    vehicle_number = input("Enter the vehicle number to exit: ")
    found = False
    
    for i in range(len(parking_slots)):
        if parking_slots[i] == True:
            print(f"Vehicle found in slot {i + 1}.")
            if vehicle_number.lower() == 'exit':
                parking_slots[i] = False
                print(f"Vehicle exited from slot {i + 1}.")
                found = True
                break

    if not found:
        print("Vehicle not found in any of the parking slots.")

def main():
    while True:
        action = input("Do you want to park or exit? Type 'park' or 'exit': ").lower()
        
        if action == 'park':
            park_vehicle()
        elif action == 'exit':
            exit_vehicle()
        else:
            print("Invalid input. Please type 'park' to park a vehicle or 'exit' to exit a vehicle.")

        another_action = input("Do you want to perform another action? Type 'yes' or 'no': ").lower()
        if another_action != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
