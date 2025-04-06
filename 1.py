import sqlite3

def setup_database():
    conn = sqlite3.connect("airline_booking.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_number TEXT,
            seat_number TEXT UNIQUE,
            passenger_id TEXT,
            passenger_name TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def book_seat(flight_number, seat_number, passenger_id, passenger_name):
    conn = sqlite3.connect("airline_booking.db")
    cursor = conn.cursor()

    # Check if the seat is already booked
    cursor.execute("SELECT * FROM bookings WHERE seat_number = ? AND status = 'R'", (seat_number,))
    if cursor.fetchone():
        print(f"Seat {seat_number} is already reserved.")
        conn.close()
        return

    try:
        cursor.execute("""
            INSERT INTO bookings (flight_number, seat_number, passenger_id, passenger_name, status)
            VALUES (?, ?, ?, ?, 'R')
        """, (flight_number, seat_number, passenger_id, passenger_name))
        conn.commit()
        print(f"Seat {seat_number} has been booked successfully!")
    except sqlite3.IntegrityError:
        print(f"Seat {seat_number} already exists in the database.")
    conn.close()

def cancel_seat(seat_number):
    conn = sqlite3.connect("airline_booking.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE bookings SET status = 'F' WHERE seat_number = ? AND status = 'R'", (seat_number,))
    if cursor.rowcount == 0:
        print(f"Seat {seat_number} is not currently reserved.")
    else:
        print(f"Seat {seat_number} reservation cancelled.")
    conn.commit()
    conn.close()

def view_all_bookings():
    conn = sqlite3.connect("airline_booking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    print("\nAll Booking Records:")
    for row in rows:
        print(row)
    conn.close()

def main():
    setup_database()

    while True:
        print("\n=== Apache Airlines - DB Booking System ===")
        print("1. Book a seat")
        print("2. Cancel a seat")
        print("3. View all bookings")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            flight = input("Enter flight number: ")
            seat = input("Enter seat number (e.g., 12B): ").upper()
            pid = input("Enter passenger ID: ")
            name = input("Enter passenger name: ")
            book_seat(flight, seat, pid, name)
        elif choice == '2':
            seat = input("Enter seat number to cancel: ").upper()
            cancel_seat(seat)
        elif choice == '3':
            view_all_bookings()
        elif choice == '4':
            print("Exiting system. Bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
