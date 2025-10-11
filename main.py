from tkinter import *
def register():
    username=entry_username.get()
    password=entry_password.get()
    if username=="" or password=="":
        label_message.config(text="Please fill in all the fields", fg="red")
    else:
        label_message.config(text="log in Successful", fg="green")
        entry_username.delete(0, END)
        entry_password.delete(0, END)
        show_welcome_frame()
def show_welcome_frame():
    frame_register.pack_forget()
    frame_welcome=Frame(root)
    frame_welcome.pack(pady=50)
    Label(frame_welcome, text="Welcome to your app", font=("Arial", 24,"bold"),fg="green").pack(pady=20)
    Button(frame_welcome, text="exit", command=root.destroy,
    font=("Arial", 14), bg="red", fg="white",width=10).pack(pady=10)
root=Tk()
root.title("login ")
root.geometry("400x400")
frame_register=Frame(root)
frame_register.pack(pady=30)
Label(frame_register, text="username:").pack()
entry_username=Entry(frame_register)
entry_username.pack()
Label(frame_register, text="password:").pack()
entry_password=Entry(frame_register, show="*")
entry_password.pack()
Button(frame_register, text="login", command=register,bg="blue",fg="white").pack(pady=10)
label_message=Label(frame_register, text="")
label_message.pack()
root.mainloop()

