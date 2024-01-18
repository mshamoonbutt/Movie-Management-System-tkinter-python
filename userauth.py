from tkinter import *
from tkinter import messagebox
from moviesearchanddata import start_movie_finder  # Import the function from moviesearchanddata.py

#Login Page GUI
root = Tk()
root.title("Login Page")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(False, False)

import re

# Check for the strength of the password
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[_@$]", password):
        return False
    return True

#Sigin Screen
def signin():
    username = user.get()
    password = code.get()

    #Error Hnadling
    try:
        #Getting user credentials from file and reading it
        with open("user_credentials.txt", "r") as file:
            user_role = None
            for line in file:
                parts = line.strip().split(',')
                #it checks that there are 3 entries in file line if not that line is skipped
                if len(parts) >= 3:
                    stored_username, stored_password, stored_role = parts
                    #it check if the entered data match the file data
                    if username == stored_username and password == stored_password:
                        messagebox.showinfo("Login Successful", f"Welcome to the App, {username}!")
                        user_role = stored_role
                        break        
            if user_role:
                root.destroy()
                start_movie_finder(user_role)
                return
        messagebox.showerror("Invalid", "Invalid Username or Password")
    except FileNotFoundError:
        messagebox.showerror("Error", "User credentials file not found.")
 
#Signup Window    
def signup_command():
    window=Toplevel(root)       
    window.title("Signup Page")     
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)

    def signup():
        username = user_var.get()
        password = code_var.get()
        confirm_password = confirm_code_var.get()
        
        if not is_strong_password(password):
            messagebox.showerror("Weak Password", "Password must be at least 8 characters long and include uppercase, lowercase, numbers, and special characters (_@$).")
            return
        
        if password == confirm_password:
            try:
                # Include the role "user" when writing to the file
                with open("user_credentials.txt", "a") as file:
                    file.write(f"{username},{password},user\n")
                messagebox.showinfo("Signup", "Successfully Signed Up")
                window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error during signup: {e}")
        else:
            messagebox.showerror("Invalid", "Both Passwords Should Match")

    def toggle_signup_password():
        if confirm_code.cget('show') == '*':
            code.config(show='')
            confirm_code.config(show='')
        else:
            code.config(show='*')
            confirm_code.config(show='*')

    def signin():
        window.destroy()

                
    img = PhotoImage(file='signup1.png')
    Label(window, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg="#fff")
    frame.place(x=480, y=50)

    heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        name = user_var.get()
        if name == "":
            user_var.set("Username")

    user_var = StringVar()
    user = Entry(frame, width=25, textvariable=user_var, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user_var.set("Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    def on_enter(e):
        code.delete(0, "end")

    def on_leave(e):
        name = code_var.get()
        if name == "":
            code_var.set("Password")

    code_var = StringVar()
    code = Entry(frame, width=25, textvariable=code_var, show="*", fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    code.place(x=30, y=150)
    code_var.set("Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    def on_enter(e):
        confirm_code.delete(0, "end")

    def on_leave(e):
        name = confirm_code_var.get()
        if name == "":
            confirm_code_var.set("Confirm Password")

    confirm_code_var = StringVar()
    confirm_code = Entry(frame, width=25, textvariable=confirm_code_var, show="*", fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    confirm_code.place(x=30, y=220)
    confirm_code_var.set("Confirm Password")
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)
    
    view_password_button = Button(frame, text="View", bg="#57a1f8", fg="white", border=0, command=toggle_signup_password)
    view_password_button.place(x=300, y=220)  # Adjust the position as needed

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

    Button(frame, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=signup).place(x=35, y=280)
    label = Label(frame, text="I have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label.place(x=90, y=340)

    sign_in = Button(frame, width=6, text="Sign In", border=0, bg="white", cursor="hand2", fg="#57a1f8",command=signin)
    sign_in.place(x=200, y=340)

    window.mainloop()

def open_app_window():
    screen = Toplevel(root)
    screen.title("App")
    screen.geometry("925x500+300+200")
    screen.config(bg="white")

    Label(screen, text="Hello World", bg="#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)
    screen.mainloop()

img = PhotoImage(file='login1.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign In", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "Username")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)    
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    name = code.get()
    if name == "":
        code.insert(0, "Password")

code = Entry(frame, width=25, show="*", fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

def toggle_password():
    if code.cget('show') == '*':
        code.config(show='')
    else:
        code.config(show='*')
        
def reset_password():
    messagebox.showinfo("Reset Password", "Password reset functionality is not implemented yet.")        

show_hide_button = Button(frame, text="View", bg="#57a1f8", fg="white", border=0, command=toggle_password)
show_hide_button.place(x=300, y=150)  # Adjust the position as needed


Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, pady=7, text="Sign In", bg="#57a1f8", fg="white", border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

forgot_password_button = Button(frame, text="Reset Now", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=reset_password)
forgot_password_button.place(x=190, y=250)  # Adjust the position as needed
label = Label(frame, text="Forgot Password?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=85, y=250)


sign_up = Button(frame, width=6, text="Sign Up", border=0, bg="white", cursor="hand2", fg="#57a1f8",command=signup_command)
sign_up.place(x=215, y=270)


# root.mainloop()

if __name__ == "__main__":
    root.mainloop()