import os
import sqlite3

from tkinter import *

main = Tk()
main.title("Welcome...!")

main.geometry("300x150")


# -------------------------------------------------------------------------------------------------------------------------------------

def confirmPassword(password, confirm_password):
    if password == confirm_password:
        return True
    else:
        return False


# -------------------------------------------------------------------------------------------------------------------------------------

def Login_Window():
    # -------------------------------------------------------------------------------------------------------------------------------------

    def Login():
        conn = sqlite3.connect('test5.db')
        c = conn.cursor()

        c.execute(
            "CREATE TABLE IF NOT EXISTS DETAILS(username text PRIMARY KEY ,password text, name text, address text, mobile text)")

        username = get_username.get()
        password_new = get_password.get()

        # ----------------------------------------------------------------
        def validUsername(username):
            c.execute("SELECT username from DETAILS WHERE username = ? ", (username,))
            data = c.fetchall()
            if len(data) == 0:
                return True

            else:
                return False

        # ----------------------------------------------------------------
        if validUsername(username) == True:
            print("Username Not Exist")

        else:
            c.execute("SELECT username from DETAILS WHERE username = ?", (username,))
            data = c.fetchall()
            temp_username = data[0][0]

            c.execute("SELECT password from DETAILS WHERE username = ?", (username,))
            data1 = c.fetchall()
            temp_password = data1[0][0]

            if username == temp_username:

                if password_new == temp_password:
                    c.execute("SELECT name, address, mobile from DETAILS WHERE username = ? ", (username,))
                    data2 = c.fetchall()

                    l1 = data2[0][0]
                    l2 = data2[0][1]
                    l3 = data2[0][2]

                    print("WELCOME....!")
                    print("name:", l1)
                    print("Address:", l2)
                    print("Mobile Number:", l3)

                    conn.commit()
                    c.close()
                    conn.close()

                else:
                    print("Wrong Password")


            else:
                print("Wrong Username")

    # -------------------------------------------------------------------------------------------------------------------------------------

    main.destroy()
    log = Tk()
    log.geometry("500x500+0+0")
    log.title("Login Page")

    # Set text variables
    get_username = StringVar()
    get_password = StringVar()

    # Username Label
    username_label = Label(log, font=("Arial", 20, "bold"), text="Username", fg="Blue")
    username_label.grid(row=0, column=0)

    # Password Label

    password_label = Label(log, font=("Arial", 20, "bold"), text="Password", fg="Blue")
    password_label.grid(row=1, column=0)

    # Username Entry

    username_entry = Entry(log, font=("Helvetica", 20, "bold"), textvariable=get_username, bd=2, bg="yellow")

    username_entry.grid(row=0, column=1)

    # Password Entry

    password_entry = Entry(log, font=("Helvetica", 20, "bold"), textvariable=get_password, bd=2, bg="yellow")
    password_entry.grid(row=1, column=1)

    # Login Button

    login_button = Button(log, padx=10, pady=10, fg="yellow", font=("Helvetica", 20, "bold"), width=5, text="Login",
                          bg="red", command=Login)
    login_button.grid(row=2, column=1)

    log.mainloop()


# ------------------------------------------------------------------------------------------------------------------

def SignUp_Window():
    # SignUp Window
    # -------------------------------------------------------------------------------------------------------------------------------------

    def sign():
        while (1):

            conn = sqlite3.connect('test5.db')
            c = conn.cursor()
            c.execute(
                "CREATE TABLE IF NOT EXISTS DETAILS(username text PRIMARY KEY ,password text, name text, address text, mobile text)")

            username = a_get_username.get()

            # ----------------------------------------------------------------
            def validUsername(username):
                c.execute("SELECT username from DETAILS WHERE username = ? ", (username,))
                data = c.fetchall()
                if len(data) == 0:
                    return True

                else:
                    return False

            # ----------------------------------------------------------------
            if validUsername(username) == False:
                print("Username Already Exist")
                break

            password = a_get_password.get()
            confirm_password = confirm_get_password.get()

            if confirmPassword(password, confirm_password) == False:
                print("Password Not Match")
                break

            name = get_name.get()
            address = get_mobile.get()
            mobile_number = get_address.get()

            c.execute("INSERT INTO DETAILS (username, password, name, address, mobile) Values(?,?,?,?,?)",
                      (username, password, name, address, mobile_number))
            print("Registration Successful")
            conn.commit()
            c.close()
            conn.close()
            break

    # -------------------------------------------------------------------------------------------------------------------------------------

    main.destroy()
    roo = Tk()
    roo.geometry("700x300+0+0")
    roo.title("SignUp Page")

    # Set text variables

    a_get_username = StringVar()
    a_get_password = StringVar()
    confirm_get_password = StringVar()
    get_mobile = StringVar()
    get_address = StringVar()
    get_name = StringVar()

    # Username Label
    username_label = Label(roo, font=("Arial", 20, "bold"), text="Username", fg="Blue")
    username_label.grid(row=0, column=0)

    # Password Label

    password_label = Label(roo, font=("Arial", 20, "bold"), text="Password", fg="Blue")
    password_label.grid(row=1, column=0)

    # Confirm Password Label

    password_label = Label(roo, font=("Arial", 20, "bold"), text="Confirm Password", fg="Blue")
    password_label.grid(row=2, column=0)

    # Name Label

    password_label = Label(roo, font=("Arial", 20, "bold"), text="Name", fg="Blue")
    password_label.grid(row=3, column=0)

    # Mobile Number Label
    username_label = Label(roo, font=("Arial", 20, "bold"), text="Mobile No", fg="Blue")
    username_label.grid(row=4, column=0)

    # Address Label
    username_label = Label(roo, font=("Arial", 20, "bold"), text="Address", fg="Blue")
    username_label.grid(row=5, column=0)

    # Username Entry

    username_entry = Entry(roo, font=("Helvetica", 20, "bold"), textvariable=a_get_username, bd=2, bg="yellow")

    username_entry.grid(row=0, column=1)

    # Password Entry

    password_entry = Entry(roo, font=("Helvetica", 20, "bold"), textvariable=a_get_password, bd=2, bg="yellow")
    password_entry.grid(row=1, column=1)

    # Confirm Password Entry

    password_entry = Entry(roo, font=("Helvetica", 20, "bold"), textvariable=confirm_get_password, bd=2, bg="yellow")
    password_entry.grid(row=2, column=1)

    # Name Entry

    username_entry = Entry(roo, font=("Helvetica", 20, "bold"), textvariable=get_name, bd=2, bg="yellow")

    username_entry.grid(row=3, column=1)

    # Mobile Number Entry

    username_entry = Entry(roo, font=("Helvetica", 20, "bold"), textvariable=get_mobile, bd=2, bg="yellow")

    username_entry.grid(row=4, column=1)

    # Address Entry

    username_entry = Entry(roo, font=("Helvetica", 20, "bold"), textvariable=get_address, bd=2, bg="yellow")

    username_entry.grid(row=5, column=1)

    # SignUp Button

    login_button = Button(roo, padx=10, pady=10, fg="yellow", font=("Helvetica", 20, "bold"), width=5, text="signup",
                          bg="red", command=sign)
    login_button.grid(row=6, column=1)

    roo.mainloop()


# ------------------------------------------------------------------------------------------------------------------

# Login Button
login_button = Button(main, padx=10, pady=10, fg="yellow", font=("Helvetica", 20, "bold"), width=5, text="Login",
                      bg="red", command=Login_Window)
login_button.grid(row=0, ipadx=4, column=0)

# SignUp Button
login_button = Button(main, padx=10, pady=10, fg="yellow", font=("Helvetica", 20, "bold"), width=5, text="signup",
                      bg="red", command=SignUp_Window)
login_button.grid(row=0, ipadx=4, column=1)

main.mainloop()
