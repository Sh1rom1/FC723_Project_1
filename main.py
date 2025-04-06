# Apache Airlines - Seat Booking System
# Developed by: You
# Version: Part A
# Functions: Check, Book, Cancel, Show seat status

def generate_seat_map():
    """
    Generate a dictionary to store the seat map.
    Rows: 1 to 80
    Columns: A to F
    'F' = Free, 'R' = Reserved, 'X' = Aisle, 'S' = Storage (not available)
    """
    seat_map = {}
    rows = 80
    columns = ['A', 'B', 'C', 'D', 'E', 'F']
    for row in range(1, rows + 1):
        for col in columns:
            seat_id = f"{row}{col}"
            if col in ['D', 'E', 'F'] and row > 76:
                seat_map[seat_id] = 'S'  # Storage area
            elif col == 'C' and row % 5 == 0:
                seat_map[seat_id] = 'X'  # Aisle
            else:
                seat_map[seat_id] = 'F'  # Free
    return seat_map


def print_seat_status(seat_map):
    """
    Display the current status of all seats.
    """
    print("\nCurrent Seat Status (F=Free, R=Reserved, X=Aisle, S=Storage):")
    for row in range(1, 81):
        status = []
        for col in ['A', 'B', 'C', 'D', 'E', 'F']:
            seat_id = f"{row}{col}"
            status.append(seat_map.get(seat_id, ' '))
        print(f"Row {row}: {status}")


def check_seat(seat_map, seat_id):
    """
    Check if a seat is available.
    """
    if seat_id in seat_map:
        status = seat_map[seat_id]
        if status == 'F':
            print(f"Seat {seat_id} is available.")
        elif status == 'R':
            print(f"Seat {seat_id} is already reserved.")
        elif status == 'X':
            print(f"Seat {seat_id} is an aisle and cannot be booked.")
        elif status == 'S':
            print(f"Seat {seat_id} is a storage area and cannot be booked.")
    else:
        print("Seat number does not exist.")


def book_seat(seat_map, seat_id):
    """
    Book a seat if it is free.
    """
    if seat_map.get(seat_id) == 'F':
        seat_map[seat_id] = 'R'
        print(f"Seat {seat_id} successfully reserved.")
    elif seat_map.get(seat_id) in ['R', 'X', 'S']:
        print(f"Seat {seat_id} cannot be booked. It is already reserved or not available.")
    else:
        print("Invalid seat number.")


def free_seat(seat_map, seat_id):
    """
    Cancel a reserved seat.
    """
    if seat_map.get(seat_id) == 'R':
        seat_map[seat_id] = 'F'
        print(f"Seat {seat_id} has been released.")
    else:
        print(f"Seat {seat_id} is not currently reserved.")


def main():
    """
    Main function to show the menu and handle user input.
    """
    seat_map = generate_seat_map()

    while True:
        print("\n=== Apache Airlines Seat Booking System ===")
        print("1. Check seat availability")
        print("2. Book a seat")
        print("3. Cancel a seat")
        print("4. Show all seat status")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            seat_id = input("Enter seat number (e.g., 12B): ").upper()
            check_seat(seat_map, seat_id)
        elif choice == '2':
            seat_id = input("Enter seat number to book: ").upper()
            book_seat(seat_map, seat_id)
        elif choice == '3':
            seat_id = input("Enter seat number to cancel: ").upper()
            free_seat(seat_map, seat_id)
        elif choice == '4':
            print_seat_status(seat_map)
        elif choice == '5':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
