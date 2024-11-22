from tkinter import *
from tkinter import messagebox
from db_utils import db
import re

def init_password_change_frame(root, user_id, show_launch_frame):
    change_frame = Frame(root, width=800, height=600)
    change_frame.pack_propagate(False)
    
    # Centered container frame to hold all inner elements
    container = Frame(change_frame, width=800, height=600, padx=20, pady=20)
    container.place(relx=0.5, rely=0.5, anchor=CENTER)
    container.pack_propagate(False)
    
    # Variables for password change
    current_password = StringVar()
    new_password = StringVar()
    confirm_password = StringVar()
    
    def validate_password(password):
        """Validate password meets security requirements."""
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain uppercase letter"
        if not re.search(r"[a-z]", password):
            return False, "Password must contain lowercase letter"
        if not re.search(r"\d", password):
            return False, "Password must contain number"
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Password must contain special character"
        return True, "Password valid"
    
    def change_password():
        """Handle password change request."""
        # Verify new passwords match
        if new_password.get() != confirm_password.get():
            messagebox.showerror("Error", "New passwords do not match")
            return
            
        # Validate new password strength
        valid, msg = validate_password(new_password.get())
        if not valid:
            messagebox.showerror("Error", msg)
            return
            
        # Attempt password change
        success, message = db.change_password(
            user_id.get(), 
            current_password.get(), 
            new_password.get()
        )
        
        if success:
            messagebox.showinfo("Success", "Password changed successfully")
            # Clear the fields
            current_password.set("")
            new_password.set("")
            confirm_password.set("")
            # Return to launch frame
            change_frame.pack_forget()
            show_launch_frame()
        else:
            messagebox.showerror("Error", message)

    def handle_back():
        """Handle back button click."""
        change_frame.pack_forget()
        show_launch_frame()
    
    # GUI Layout
    Label(container, text="Change Password", font=("Helvetica", 16, "bold")).pack(pady=10)
    
    # Current password section
    Label(container, text="Current Password:", font=("Helvetica", 12)).pack()
    Entry(container, textvariable=current_password, show="*", font=("Helvetica", 12)).pack(pady=5)
    
    # New password section
    Label(container, text="New Password:", font=("Helvetica", 12)).pack()
    Entry(container, textvariable=new_password, show="*", font=("Helvetica", 12)).pack(pady=5)
    
    # Confirm password section
    Label(container, text="Confirm New Password:", font=("Helvetica", 12)).pack()
    Entry(container, textvariable=confirm_password, show="*", font=("Helvetica", 12)).pack(pady=5)
    
    # Password requirements info
    requirements_text = """
    Password Requirements:
    • Minimum 8 characters
    • At least one uppercase letter
    • At least one lowercase letter
    • At least one number
    • At least one special character (!@#$%^&*(),.?":{}|<>)
    """
    Label(container, text=requirements_text, font=("Helvetica", 10), justify=LEFT).pack(pady=10)
    
    # Buttons
    Button(container, text="Change Password", 
           command=change_password, 
           font=("Helvetica", 12)).pack(pady=10)
    
    Button(container, text="Back to Menu", 
           command=handle_back, 
           font=("Helvetica", 12)).pack(pady=5)
    
    return change_frame
