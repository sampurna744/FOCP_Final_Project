# login.py
from password_utils import read_passwords, encrypt_password

def login():
    """
    This function handles the login process. It prompts the user for a username and password,
    checks if the username is in the list of usernames, encrypts the password, and then checks
    if the username and encrypted password match any user in the password list. It prints
    "Access granted." if the credentials are correct, and "Access denied." otherwise.
    """

    usernames = [user[0] for user in read_passwords()]
    
    username = input("User: ").lower()
    
    if username not in usernames:
        print("Access denied.")
        return

    password = input("Password: ")
    encrypted_password = encrypt_password(password)

    for user in read_passwords():
        if user[0] == username and user[2] == encrypted_password:
            print("Access granted.")
            return

    print("Access denied.")

if __name__ == "__main__":
    login()
