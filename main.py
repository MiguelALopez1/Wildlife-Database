from tkinter import *
from tkinter import messagebox
from insert import init_insert_frame
from delete import init_delete_frame
from update import init_update_frame
from db_utils import db
from signup import init_signup_frame

class WildlifeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wildlife Call Database - Audio Management")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Variables
        self.username = StringVar()
        self.password = StringVar()
        self.user_id = StringVar()
        self.session_id = None
        self.user_type = None

        # Initialize frames
        self.login_frame = self.create_login_frame()
        self.launch_frame = self.create_launch_frame()
        self.signup_frame = init_signup_frame(root, self.show_login_frame)
        self.insert_frame = None
        self.delete_frame = None
        self.update_frame = None

        # Show login frame
        self.show_login_frame()

    def create_login_frame(self):
        frame = Frame(self.root)
        Label(frame, text="Wildlife Call Database", font=("Helvetica", 20, "bold")).pack(pady=20)
        
        # Username
        Label(frame, text="Username:", font=("Helvetica", 12)).pack()
        Entry(frame, textvariable=self.username, font=("Helvetica", 12)).pack(pady=5)
        
        # Password
        Label(frame, text="Password:", font=("Helvetica", 12)).pack()
        Entry(frame, textvariable=self.password, show="*", font=("Helvetica", 12)).pack(pady=5)
        
        Button(frame, text="Login", command=self.login, font=("Helvetica", 14)).pack(pady=10)
        Button(frame, text="Sign Up", command=self.show_signup_frame, font=("Helvetica", 12)).pack(pady=5)
        return frame

    def create_launch_frame(self):
        frame = Frame(self.root)
        Label(frame, text="Wildlife Call Database", font=("Helvetica", 16)).pack(pady=20)
        
        Button(frame, text="Insert", command=lambda: self.show_frame('insert')).pack(pady=10)
        Button(frame, text="Delete", command=lambda: self.show_frame('delete')).pack(pady=10)
        Button(frame, text="Update", command=lambda: self.show_frame('update')).pack(pady=10)
        Button(frame, text="Logout", command=self.logout, font=("Helvetica", 12)).pack(pady=20)
        
        return frame

    def login(self):
        try:
            username = self.username.get()
            password = self.password.get()
            
            success, message, result = db.verify_user_credentials(username, password)
            
            if success:
                self.user_id.set(str(result[1]))
                self.user_type = result[0]
                self.session_id = db.create_session(result[1], result[0])
                db.log_activity(result[1], "LOGIN")
                self.show_launch_frame()
            else:
                messagebox.showerror("Error", message)
                
        except Exception as e:
            messagebox.showerror("Error", f"Login error occurred: {str(e)}")

    def logout(self):
        if self.session_id:
            cursor = db.get_cursor()
            try:
                cursor.execute("DELETE FROM Sessions WHERE session_id = %s", (self.session_id,))
                db.connect().commit()
                db.log_activity(int(self.user_id.get()), "LOGOUT")
            finally:
                cursor.close()
        
        self.session_id = None
        self.user_id.set("")
        self.show_login_frame()

    def show_login_frame(self):
        for frame in [self.launch_frame, self.insert_frame, self.delete_frame, self.update_frame, self.signup_frame]:
            if frame:
                frame.pack_forget()
        self.login_frame.pack()

    def show_signup_frame(self):
        self.login_frame.pack_forget()
        self.signup_frame.pack()

    def show_launch_frame(self):
        self.login_frame.pack_forget()
        self.launch_frame.pack()

    def show_frame(self, frame_name):
        if not self.verify_session():
            messagebox.showerror("Error", "Session expired. Please login again.")
            self.show_login_frame()
            return

        self.launch_frame.pack_forget()
        
        if frame_name == 'insert':
            if not self.insert_frame:
                self.insert_frame = init_insert_frame(self.root, self.user_id, self.show_launch_frame)
            self.insert_frame.pack()
        elif frame_name == 'delete':
            if not self.delete_frame:
                self.delete_frame = init_delete_frame(self.root, self.user_id, self.show_launch_frame)
            self.delete_frame.pack()
        elif frame_name == 'update':
            if not self.update_frame:
                self.update_frame = init_update_frame(self.root, self.user_id, self.show_launch_frame)
            self.update_frame.pack()

    def verify_session(self):
        if not self.session_id:
            return False
        user_id, user_type = db.verify_session(self.session_id)
        return user_id is not None

if __name__ == "__main__":
    root = Tk()
    app = WildlifeApp(root)
    root.mainloop()
