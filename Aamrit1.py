import hashlib
import csv

def registration(username, password):
    # hashing password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Writing username and hashed password to a CSV file
    with open('user_credentials.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])
    print("Registration successful")

def logininfo(username, password):
    # Read the CSV file to check if the user exists and verify password
    with open('user_credentials.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                stored_password = row[1]
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if stored_password == hashed_password:
                    print("Login successful!")
                    return
    print("Invalid username or password. Please try again.")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            username = input(" Please enter username: ")
            password = input("Please enter password: ")
            registration(username, password)
        elif choice == '2':
            username = input("Please enter username: ")
            password = input("Please enter password: ")
            logininfo(username, password)
        elif choice == '3':
            print("Exiting...:)")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
