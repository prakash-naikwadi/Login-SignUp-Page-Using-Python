import os
from tkinter import*


def main_window():
    main = Tk()
    main.title("Welcome...!")

    main.geometry("500x500")

    #-------------------------------------------------------------------------------------------------------------------------------------

    def confirmPassword(password,confirm_password):
        if password == confirm_password:
            return True
        else:
            return False

    def validUsername(username):
        file_name = username + ".txt"

        is_file_exist = os.path.exists(file_name)

        if is_file_exist == True:

            return False
    #-------------------------------------------------------------------------------------------------------------------------------------

    def Login_Window():


        def Login():

            username = get_username.get()
            password_new = get_password.get()


            file_name = username + ".txt"

            is_file_exist = os.path.exists(file_name)


            if is_file_exist == True:
                fh = open(file_name,"rt")

                temp = fh.readlines()[1]

                password_validation = temp.strip()

                if password_validation == password_new:
                    print("\nWelcome\n")
                    fh.seek(0)
                    #print(fh.tell())
                    print(fh.readlines()[2])
                    fh.seek(0)
                    print(fh.readlines()[3])
                    fh.seek(0)
                    print(fh.readlines()[4])

                    fh.close() 

                else:
                    print("Wrong Password..!")

            else:
                print("Wrong Username..!")


        main.destroy()
        log = Tk()
        log.geometry("500x500+0+0")
        log.title("Login Page")



        # Set text variables
        get_username = StringVar()
        get_password = StringVar()

        #Username Label
        username_label = Label(log, font = ("Arial", 20, "bold"), text = "Username", fg = "Blue")
        username_label.grid(row = 0, column = 0)

        #Password Label

        password_label = Label(log, font = ("Arial", 20, "bold"), text = "Password", fg = "Blue")
        password_label.grid(row = 1, column = 0)

        #Username Entry

        username_entry = Entry(log, font = ("Helvetica", 20, "bold"), textvariable = get_username, bd = 2, bg = "yellow")

        username_entry.grid(row = 0, column = 1)

        #Password Entry

        password_entry = Entry(log, font = ("Helvetica", 20, "bold"), textvariable = get_password, bd = 2, bg = "yellow")
        password_entry.grid(row = 1, column = 1)


        #Login Button

        login_button = Button(log, padx = 10, pady = 10, fg = "yellow", font = ("Helvetica", 20, "bold"), width = 5, text = "Login", bg = "red", command = Login)
        login_button.grid(row = 2, column = 1)

        def Destroy():            
            
            log.destroy()
            main_window()
        
        back_button = Button(log,padx = 10, pady = 10, text = "Back", command = Destroy)
        back_button.grid(row = 3, column = 1)
        

        log.mainloop() 

    #------------------------------------------------------------------------------------------------------------------    

    def SignUp_Window():
        #SignUp Window


        def sign():
            while(1):
                username = a_get_username.get()


                if validUsername(username) == False:
                    print("Username Already Exist")
                    break

                password = a_get_password.get()
                confirm_password = confirm_get_password.get()

                if confirmPassword(password,confirm_password) == False:
                    print("Password Not Match")
                    break

                name = get_name.get()
                address = get_mobile.get()
                mobile_number = get_address.get()

                file_name = username + ".txt"


                fh = open(file_name,"w")

                fh.write(username)
                fh.write("\n")
                fh.write(password)
                fh.write("\n")
                fh.write(name)
                fh.write("\n")
                fh.write(address)
                fh.write("\n")
                fh.write(mobile_number)
                fh.close()
                print("Account Created")
                break

        main.destroy()
        roo = Tk()
        roo.geometry("700x400+0+0")
        roo.title("SignUp Page")

        # Set text variables
        confirm_get_password = StringVar()
        a_get_username = StringVar()
        a_get_password = StringVar()
        get_mobile = StringVar()
        get_address = StringVar()
        get_name = StringVar()

        #Username Label
        username_label = Label(roo, font = ("Arial", 20, "bold"), text = "Username", fg = "Blue")
        username_label.grid(row = 0, column = 0)

        #Password Label

        password_label = Label(roo, font = ("Arial", 20, "bold"), text = "Password", fg = "Blue")
        password_label.grid(row = 1, column = 0)


        #Confirm Password Label

        password_label = Label(roo, font = ("Arial", 20, "bold"), text = "Confirm Password", fg = "Blue")
        password_label.grid(row = 2, column = 0)

        #Name Label

        password_label = Label(roo, font = ("Arial", 20, "bold"), text = "Name", fg = "Blue")
        password_label.grid(row = 3, column = 0)

        #Mobile Number Label
        username_label = Label(roo, font = ("Arial", 20, "bold"), text = "Mobile No", fg = "Blue")
        username_label.grid(row = 4, column = 0)

        #Address Label
        username_label = Label(roo, font = ("Arial", 20, "bold"), text = "Address", fg = "Blue")
        username_label.grid(row = 5, column = 0)


        #Username Entry

        username_entry = Entry(roo, font = ("Helvetica", 20, "bold"), textvariable = a_get_username, bd = 2, bg = "yellow")

        username_entry.grid(row = 0, column = 1)

        #Password Entry

        password_entry = Entry(roo, font = ("Helvetica", 20, "bold"), textvariable = a_get_password, bd = 2, bg = "yellow")
        password_entry.grid(row = 1, column = 1)



        #Confirm Password Entry

        password_entry = Entry(roo, font = ("Helvetica", 20, "bold"), textvariable = confirm_get_password, bd = 2, bg = "yellow")
        password_entry.grid(row = 2, column = 1)

        #Name Entry

        username_entry = Entry(roo, font = ("Helvetica", 20, "bold"), textvariable = get_name, bd = 2, bg = "yellow")

        username_entry.grid(row = 3, column = 1)

        #Mobile Number Entry

        username_entry = Entry(roo, font = ("Helvetica", 20, "bold"), textvariable = get_mobile, bd = 2, bg = "yellow")

        username_entry.grid(row = 4, column = 1)

         #Address Entry

        username_entry = Entry(roo, font = ("Helvetica", 20, "bold"), textvariable = get_address, bd = 2, bg = "yellow")

        username_entry.grid(row = 5, column = 1)

        #SignUp Button

        login_button = Button(roo, padx = 10, pady = 10, fg = "yellow", font = ("Helvetica", 20, "bold"), width = 5, text = "signup", bg = "red", command = sign)
        login_button.grid(row = 6, column = 1)
        
        def Destroy():            
            
            roo.destroy()
            main_window()
        
        back_button = Button(roo,padx = 10, pady = 10, text = "Back", command = Destroy)
        back_button.grid(row = 7, column = 1)

        roo.mainloop()



    #------------------------------------------------------------------------------------------------------------------            

    #Login Button
    login_button = Button(main, padx = 10, pady = 10, fg = "yellow", font = ("Helvetica", 20, "bold"), width = 5, text = "Login", bg = "red", command = Login_Window)
    login_button.grid(row = 0, column = 0)

    #SignUp Button
    login_button = Button(main, padx = 10, pady = 10, fg = "yellow", font = ("Helvetica", 20, "bold"), width = 5, text = "signup", bg = "red", command = SignUp_Window)
    login_button.grid(row = 0, column = 2)

    main.mainloop()
    
main_window()


