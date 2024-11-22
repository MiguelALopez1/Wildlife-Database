from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db_utils import db
import re

def init_admin_panel(root, user_id, show_launch_frame):
    admin_frame = Frame(root, width=800, height=600)
    admin_frame.pack_propagate(False)
    
    # Create main canvas for scrolling
    main_canvas = Canvas(admin_frame)
    scrollbar = Scrollbar(admin_frame, orient="vertical", command=main_canvas.yview)
    scrollable_frame = Frame(main_canvas)
    
    # Configure the canvas
    scrollable_frame.bind(
        "<Configure>",
        lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
    )
    
    main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    main_canvas.configure(yscrollcommand=scrollbar.set)
    
    # Enable mouse wheel scrolling
    def _on_mousewheel(event):
        main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    main_canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Variables
    first_name = StringVar()
    last_name = StringVar()
    username = StringVar()
    password = StringVar()
    is_certified = BooleanVar()
    user_id_var = StringVar()

    def create_new_user():
        """Handle new user creation by admin."""
        if not all([first_name.get(), last_name.get(), username.get(), password.get()]):
            messagebox.showerror("Error", "All fields are required")
            return

        success, message = db.create_user_by_admin(
            first_name.get(),
            last_name.get(),
            username.get(),
            password.get(),
            is_certified.get()
        )

        if success:
            messagebox.showinfo("Success", "User created successfully")
            # Clear fields
            first_name.set("")
            last_name.set("")
            username.set("")
            password.set("")
            is_certified.set(False)
            # Refresh user list
            update_user_list()
        else:
            messagebox.showerror("Error", message)

    def toggle_certification():
        """Toggle user certification status."""
        selected_id = user_id_var.get()
        if not selected_id:
            messagebox.showerror("Error", "Please enter a user ID")
            return
        
        success, message = db.toggle_user_certification(selected_id)
        if success:
            messagebox.showinfo("Success", message)
            update_user_list()
            user_id_var.set("")
        else:
            messagebox.showerror("Error", message)

    def handle_back():
        """Return to launch frame."""
        admin_frame.pack_forget()
        main_canvas.unbind_all("<MouseWheel>")  # Unbind mousewheel event
        show_launch_frame()

    def update_user_list(event=None):
        """Update the user list with formatting."""
        users = db.get_all_users()
        users_text.delete(1.0, END)
        users_text.insert(END, "User List:\n", 'header')
        users_text.insert(END, "-" * 40 + "\n\n")
        
        for user in users:
            users_text.insert(END, f"ID: {user[0]}\n", 'bold')
            users_text.insert(END, f"Name: {user[1]} {user[2]}\n")
            users_text.insert(END, f"Username: {user[3]}\n")
            cert_status = "✓ Certified" if user[5] else "✗ Not Certified"
            users_text.insert(END, f"Status: {cert_status}\n")
            users_text.insert(END, "-" * 40 + "\n\n")

    # Content
    content_frame = Frame(scrollable_frame, padx=20, pady=20)
    content_frame.pack(fill=BOTH, expand=True)

    # Header
    Label(content_frame, text="Admin Panel", font=("Helvetica", 16, "bold")).pack(pady=10)
    Label(content_frame, text="Create New User", font=("Helvetica", 14)).pack(pady=5)
    Frame(content_frame, height=2, bd=1, relief=SUNKEN).pack(fill=X, pady=5)

    # User Creation Form
    entries_frame = Frame(content_frame)
    entries_frame.pack(pady=10)

    Label(entries_frame, text="First Name:").pack()
    Entry(entries_frame, textvariable=first_name).pack(pady=2)
    Label(entries_frame, text="Last Name:").pack()
    Entry(entries_frame, textvariable=last_name).pack(pady=2)
    Label(entries_frame, text="Username:").pack()
    Entry(entries_frame, textvariable=username).pack(pady=2)
    Label(entries_frame, text="Password:").pack()
    Entry(entries_frame, textvariable=password, show="*").pack(pady=2)
    Checkbutton(entries_frame, text="Certified User", variable=is_certified).pack(pady=5)
    Button(entries_frame, text="Create User", command=create_new_user).pack(pady=10)

    # User Management Section
    Frame(content_frame, height=2, bd=1, relief=SUNKEN).pack(fill=X, pady=5)
    Label(content_frame, text="User Management", font=("Helvetica", 14)).pack(pady=5)

    # Certification Management Section
    cert_frame = LabelFrame(content_frame, text="User Certification Control", padx=10, pady=5)
    cert_frame.pack(fill=X, pady=10)
    
    cert_input_frame = Frame(cert_frame)
    cert_input_frame.pack(pady=5)
    
    Label(cert_input_frame, text="Enter User ID:").pack(side=LEFT, padx=5)
    Entry(cert_input_frame, textvariable=user_id_var, width=10).pack(side=LEFT, padx=5)
    Button(cert_input_frame, text="Toggle Certification", 
           command=toggle_certification,
           bg='lightblue').pack(side=LEFT, padx=5)

    # User List Section
    list_frame = Frame(content_frame)
    list_frame.pack(fill=BOTH, expand=True, pady=10)
    
    list_scrollbar = Scrollbar(list_frame)
    list_scrollbar.pack(side=RIGHT, fill=Y)
    
    users_text = Text(list_frame, wrap=WORD, width=50, height=10, 
                     yscrollcommand=list_scrollbar.set)
    users_text.pack(side=LEFT, fill=BOTH, expand=True)
    list_scrollbar.config(command=users_text.yview)

    # Configure text tags for formatting
    users_text.tag_configure('header', font=('Helvetica', 12, 'bold'))
    users_text.tag_configure('bold', font=('Helvetica', 10, 'bold'))

    # Buttons at bottom
    button_frame = Frame(content_frame)
    button_frame.pack(fill=X, pady=10)
    
    Button(button_frame, text="Refresh List", 
           command=update_user_list,
           font=("Helvetica", 10)).pack(side=LEFT, padx=5)
           
    Button(button_frame, text="Back to Menu", 
           command=handle_back,
           font=("Helvetica", 10)).pack(side=RIGHT, padx=5)

    # Initial load of users
    update_user_list()

    # Pack the canvas and scrollbar
    main_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return admin_frame
