# v2.1
from Modules.Commands import execute, os, cursor, conn
import colorama

colorama.init()

print("Welcome")
print("Type help to know the commands")

cursor.execute('CREATE TABLE IF NOT EXISTS contact_info (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name char(25), Phone char(25), Email char(40))')


def main():
    running = True

    while running:
        command_input = input("--> ").strip().split()
        if command_input[0] == "exit":
            verify = input("Are you sure you want to leave (Y|N) :")
            if verify[0].strip().lower() == 'y':
                running = False
                break
        execute(command_input)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
