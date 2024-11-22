from tkinter import *
from tkinter import messagebox
from db_utils import db
import re

def init_signup_frame(root, show_login_frame):
    signup_frame = Frame(root, width=800, height=600)
    signup_frame.pack_propagate(False)
    
    container = Frame(signup_frame)
    container.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    # Input variables
    first_name = StringVar()
    last_name = StringVar()
    username = StringVar()
    password = StringVar()
    confirm_password = StringVar()
    
    def validate_password(password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True
    
    def handle_signup():
        if not all([first_name.get(), last_name.get(), username.get(), password.get()]):
            messagebox.showerror("Error", "All fields are required")
            return
            
        if password.get() != confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match")
            return
            
        if not validate_password(password.get()):
            messagebox.showerror("Error", 
                "Password must be at least 8 characters and contain:\n" +
                "- Uppercase letter\n" +
                "- Lowercase letter\n" +
                "- Number\n" +
                "- Special character")
            return
            
        success, message = db.create_user(
            first_name.get(),
            last_name.get(),
            username.get(),
            password.get()
        )
        
        if success:
            messagebox.showinfo("Success", 
                "Account created! Wait for admin certification before logging in.")
            show_login_frame()
        else:
            messagebox.showerror("Error", message)
    
    # GUI Elements
    Label(container, text="Create Account", font=("Helvetica", 16, "bold")).pack(pady=10)
    
    Label(container, text="First Name:").pack()
    Entry(container, textvariable=first_name).pack(pady=5)
    
    Label(container, text="Last Name:").pack()
    Entry(container, textvariable=last_name).pack(pady=5)
    
    Label(container, text="Username:").pack()
    Entry(container, textvariable=username).pack(pady=5)
    
    Label(container, text="Password:").pack()
    Entry(container, textvariable=password, show="*").pack(pady=5)
    
    Label(container, text="Confirm Password:").pack()
    Entry(container, textvariable=confirm_password, show="*").pack(pady=5)
    
    Button(container, text="Sign Up", command=handle_signup).pack(pady=20)
    Button(container, text="Back to Login", command=show_login_frame).pack()
    
    return signup_frame
