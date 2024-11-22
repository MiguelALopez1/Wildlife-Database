from tkinter import *
from tkinter import messagebox
from insert import init_insert_frame
from delete import init_delete_frame
from update import init_update_frame

root = Tk()
root.title("Wildlife Call Database - Audio Management")

# Set fixed window size and disable resizing
root.geometry("800x600")
root.resizable(False, False)  # Disable window resizing

# Define user_id as a
user_id = StringVar()

# Launch page function
def init_launch_frame():
    launch_frame.pack()
    insert_frame.pack_forget()
    delete_frame.pack_forget()
    update_frame.pack_forget()
    print("Returning to launch page")  # Debugging

# Launch frame with User ID prompt and buttons
launch_frame = Frame(root)
Label(launch_frame, text="Wildlife Call Database", font=("Helvetica", 16)).pack(pady=20)
Label(launch_frame, text="Enter User ID:", font=("Helvetica", 12)).pack()
Entry(launch_frame, textvariable=user_id, font=("Helvetica", 12)).pack(pady=5)

# Function to navigate to frames only if user_id is filled
def show_frame(frame):
    if not user_id.get():
        messagebox.showwarning("Warning", "Please enter your User ID.")
    else:
        print("Switching to", frame, "with User ID:", user_id.get())
        launch_frame.pack_forget()
        frame.pack()

Button(launch_frame, text="Insert", command=lambda: show_frame(insert_frame)).pack(pady=10)
Button(launch_frame, text="Delete", command=lambda: show_frame(delete_frame)).pack(pady=10)
Button(launch_frame, text="Update", command=lambda: show_frame(update_frame)).pack(pady=10)

# Initialize frames
insert_frame = init_insert_frame(root, user_id, init_launch_frame)
delete_frame = init_delete_frame(root, user_id, init_launch_frame)
update_frame = init_update_frame(root, user_id, init_launch_frame)

# Start with the launch page
init_launch_frame()
root.mainloop()

