from os import linesep
from tkinter import *
from tkinter.font import BOLD
from main import BBManagementSystem
# Positions
user_label_x = 1
user_label_y = 0

global root
root = Tk()
root.title('Blood Bank')
root.geometry('576x360')
root.config(bg="RED")
login_frame = Frame(root, width=576, height=360)
login_frame.pack()
login_frame.config(bg="RED")

register_frame = Frame(root, width=576, height=360)
welcome_frame = Frame(root, width=576, height=360)

#Log In Frame
outfield_label = Label(login_frame, text='Blood Bank Management System', font=('Times New Roman',24,BOLD))
outfield_label.pack(fill='both', expand=1)
outfield_label.config(bg="RED",fg="WHITE")
space_label = Label(login_frame)
space_label.config(bg="RED")
space_label.pack()

username_label = Label(login_frame, text='Username',font=('Times New Roman',15,BOLD))
username_label.config(bg="RED",fg="WHITE")
username_label.pack()

username_entry = Entry(login_frame, width=30,font=('Times New Roman',13))
username_entry.config(fg="RED")
username_entry.pack()

password_label = Label(login_frame, text='Password',font=('Times New Roman',15,BOLD))
password_label.config(bg="RED",fg="WHITE")
password_label.pack()

password_entry = Entry(login_frame, width=30, show= '*',font=('Times New Roman',13))
password_entry.config(fg="RED")
password_entry.pack()


def clearAllEntries():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    new_user_entry.delete(0, END)
    new_pass_entry.delete(0, END)
    confirm_pass_entry.delete(0, END)


login_error_label = Label(login_frame, text='')
login_error_label.config(bg="RED")
login_error_label.pack()

def logMeIn():
    read_txt = open('admin.txt', 'r')
    users = read_txt.read()
    users = users.split()
    if username_entry.get() in users:
        user_index = users.index(username_entry.get())
        print(user_index)
        if password_entry.get() == users[user_index+1]:
            print(users.index(password_entry.get()))
            print('You are logged in!')
            clearAllEntries()
            space_labe2 = Label(welcome_frame(BBManagementSystem(root)))
            space_labe2.pack()
            login_frame.pack_forget()

        else:
            print('Password is incorrect.')
            login_error_label.config(text='Password is incorrect.')
    else:
        print("Username doesn't exist.")
        login_error_label.config(text="Username doesn't exist.")


login_button = Button(login_frame, text=' Log In ', command=logMeIn,bd=4,borderwidth=5)
login_button.config(bg="WHITE",fg="RED")
login_button.pack()


def SignMeUp():
    login_frame.pack_forget()
    register_frame.pack(fill='both')
    register_frame.config(bg="RED")


sign_up_button = Button(login_frame, text='Sign Up', command=SignMeUp,bd=4,borderwidth=5)
sign_up_button.config(bg="WHITE",fg="RED")
sign_up_button.pack()

#Sign up Frame
sign_up_label = Label(register_frame, text='Blood Bank Signup',font=('Times New Roman',24,BOLD),height=2)
sign_up_label.config(bg="RED",fg="WHITE")
sign_up_label.pack(fill='both', expand=1)

new_user_label = Label(register_frame, text='Username',font=('Times New Roman',15,BOLD))
new_user_label.config(bg="RED",fg="WHITE")
new_user_label.pack()

new_user_entry = Entry(register_frame, width=30,font=('Times New Roman',13))
new_user_entry.config(fg="RED")
new_user_entry.pack()

new_pass_label = Label(register_frame, text='Password',font=('Times New Roman',15,BOLD))
new_pass_label.config(bg="RED",fg="WHITE")
new_pass_label.pack()

new_pass_entry = Entry(register_frame, width=30, show= '*',font=('Times New Roman',13))
new_pass_entry.config(fg="RED")
new_pass_entry.pack()

confirm_pass_label = Label(register_frame, text='Confirm Password',font=('Times New Roman',15,BOLD))
confirm_pass_label.config(bg="RED",fg="WHITE")
confirm_pass_label.pack()

confirm_pass_entry = Entry(register_frame, width=30, show= '*',font=('Times New Roman',13))
confirm_pass_entry.config(fg="RED")
confirm_pass_entry.pack()

register_error_label = Label(register_frame, text='')
register_error_label.config(bg="RED")
register_error_label.pack()


def RegisterMe():
    if ' ' not in new_user_entry.get():
        if new_pass_entry.get() == confirm_pass_entry.get():
            check_txt = open('admin.txt', 'r')
            old_users = check_txt.read()
            old_users = old_users.split()
            if new_user_entry.get() in old_users:
                register_error_label.config(text='Username already exists.')
            else:
                print(f'New username: {new_user_entry.get()}')
                print(f'New password: {new_pass_entry.get()}')
                print(f'Confirm Password: {confirm_pass_entry.get()}')
                write_on_txt = open('admin.txt', 'a')
                write_on_txt.writelines(f'{new_user_entry.get()} {new_pass_entry.get()} {confirm_pass_entry.get()}\n')
                write_on_txt.close()
                clearAllEntries()
        else:
            print("Passwords don't match")
            register_error_label.config(text="Passwords don't match.")
    else:
        print('Spaces are not permitted')
        register_error_label.config(text="Spaces are not permitted.")

register_button = Button(register_frame, text='Register', command=RegisterMe,bd=4,borderwidth=5)
register_button.config(bg="WHITE",fg="RED")
register_button.pack()


def returnToLogin():
    register_frame.pack_forget()
    login_frame.pack()


return_to_login_button = Button(register_frame, text=' Return ', command=returnToLogin,bd=4,borderwidth=5)
return_to_login_button.config(bg="WHITE",fg="RED")
return_to_login_button.pack()





root.mainloop()