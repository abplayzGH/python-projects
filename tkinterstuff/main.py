import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")

def buttonFuction() -> None:
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_password2 = tk.Label(frame_auth, text=password, font='Arial')
    lbl_password2.pack()



frame_login = tk.Frame(root)
frame_login.grid(row = 0, column = 0, sticky = 'news', columnspan=3, padx=35, pady=10)

frame_auth = tk.Frame(root)
frame_auth.grid(row = 0, column = 0, sticky = 'news', columnspan=3, padx=35, pady=10)

lbl_username = tk.Label(frame_login, text='Username:', font='Arial')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:', font='Arial')
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)

login_button = tk.Button(frame_login, text='Login', font='Arial', command=buttonFuction)
login_button.pack(pady=5)

frame_login.tkraise()

root.mainloop()