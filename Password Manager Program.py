import sqlite3
from hashlib import sha256


ADMIN_PASSWORD = "87UhtftGreq"

connect = input("Enter your password: ")

while connect != ADMIN_PASSWORD:
    connect = input("What is your password?\n")
    if connect == "q":
        break

conn = sqlite3.connect('pass_manager.db')

def create_password(pass_key, service, admin_pass):
    return sha256(admin_pass.encode('utf-8') + service.lower().encode('utf-8') + pass_key.encode('utf-8')).hexdigest()[:15]

def get_hex_key(admin_pass, service):
    return sha256(admin_pass.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()

def get_password(admin_pass, service):
    secret_key = get_hex_key(admin_pass, service)
    cursor = conn.execute("SELECT * from KEYS WHERE PASS_KEY=" + '"' + secret_key + '"')

    file_string = ""
    for row in cursor:
        file_string = row[0]
    return create_password(file_string, service, admin_pass)

def add_password(service, admin_pass):
    secret_key = get_hex_key(admin_pass, service)

    command = 'INSERT INTO KEYS (PASS_KEY) VALUES (%s);' %('"' + secret_key +'"')        
    conn.execute(command)
    conn.commit()
    return create_password(secret_key, service, admin_pass)

if connect == ADMIN_PASSWORD:
    try:
        conn.execute('''CREATE TABLE KEYS
            (PASS_KEY TEXT PRIMARY KEY NOT NULL);''')
        print("Your account has been created! What would you like to do in it today?")
    except:
        print("You have created a safe, what would you like to do today?")
    
    
    while True:
        print("\n"+ "*"*15)
        print("The set of operations you can perform are given below")
        print("If you press 'q' then you quit the program")
        print("If you press 'gp' you can display your password")
        print("If you press 'sp' then you can remember your passowrd")
        print("*"*15)
        input_ = input(":")

        if input_ == "q":
            break
        if input_ == "sp":
            service = input("What is the name of the service?")
            print("\n" + service.capitalize() + " Password has been generated: \n" + add_password(service, ADMIN_PASSWORD))
        if input_ == "gp":
            service = input("What is the name of the service?")
            print("\n" + service.capitalize() + " Password: "+get_password(ADMIN_PASSWORD, service))


