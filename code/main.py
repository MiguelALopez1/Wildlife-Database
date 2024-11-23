from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pygame
from insert import init_insert_frame
from delete import init_delete_frame
from update import init_update_frame
from db_utils import db
from signup import init_signup_frame
from password_change import init_password_change_frame
from admin_panel import init_admin_panel
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class WildlifeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wildlife Call Database - Audio Management")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Initialize pygame mixer for sound
        pygame.mixer.init()

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
        
        # Initialize as None - will be created when needed
        self.insert_frame = None
        self.delete_frame = None
        self.update_frame = None
        self.password_frame = None
        self.admin_frame = None
        self.tables_frame = None
        self.view_options_frame = None
        self.taxonomy_frame = None
        self.audiofiles_frame = None

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
        
        Button(frame, text="View", command=self.show_view_options).pack(pady=10)
        Button(frame, text="Insert", command=lambda: self.show_frame('insert')).pack(pady=10)
        Button(frame, text="Delete", command=lambda: self.show_frame('delete')).pack(pady=10)
        Button(frame, text="Update", command=lambda: self.show_frame('update')).pack(pady=10)
        Button(frame, text="Change Password", command=lambda: self.show_frame('password')).pack(pady=10)
        Button(frame, text="Admin Panel", command=self.show_admin_panel).pack(pady=10)
        Button(frame, text="Logout", command=self.logout, font=("Helvetica", 12)).pack(pady=20)
        
        return frame

    def login(self):
        try:
            username = self.username.get()
            password = self.password.get()
            
            success, message, result = db.verify_user_credentials(username, password)
            
            if success:
                self.user_id.set(str(result[1]))  # id
                self.user_type = result[0]  # type
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
        # Hide all other frames
        frames = [self.launch_frame, self.insert_frame, self.delete_frame, 
                 self.update_frame, self.signup_frame, self.admin_frame, 
                 self.tables_frame, self.view_options_frame, self.taxonomy_frame, 
                 self.audiofiles_frame]
        for frame in frames:
            if frame:
                frame.pack_forget()
        if self.password_frame:
            self.password_frame.pack_forget()
        self.login_frame.pack()

    def show_signup_frame(self):
        self.login_frame.pack_forget()
        self.signup_frame.pack()

    def show_launch_frame(self):
        # Hide all frames except launch
        frames = [self.login_frame, self.insert_frame, self.delete_frame, 
                 self.update_frame, self.signup_frame, self.admin_frame, 
                 self.tables_frame, self.view_options_frame, self.taxonomy_frame, 
                 self.audiofiles_frame]
        for frame in frames:
            if frame:
                frame.pack_forget()
        if self.password_frame:
            self.password_frame.pack_forget()
        self.launch_frame.pack()

    def show_admin_panel(self):
        if not self.verify_session():
            messagebox.showerror("Error", "Session expired. Please login again.")
            self.show_login_frame()
            return

        if not db.is_admin(self.user_id.get()):
            messagebox.showerror("Error", "Access denied. Admin privileges required.")
            return
            
        self.launch_frame.pack_forget()
        if not self.admin_frame:
            self.admin_frame = init_admin_panel(self.root, self.user_id, self.show_launch_frame)
        self.admin_frame.pack()


    def show_view_options(self):
        self.hide_all_frames()
        self.view_options_frame = Frame(self.root)
        self.view_options_frame.pack(fill=BOTH, expand=True)

        Label(self.view_options_frame, text="View Options", font=("Helvetica", 16)).pack(pady=20)
        
        Button(self.view_options_frame, text="View Taxonomy Table", command=self.show_taxonomy_table, font=("Helvetica", 14)).pack(pady=10)
        Button(self.view_options_frame, text="View Audiofiles Table", command=self.show_audiofiles_table, font=("Helvetica", 14)).pack(pady=10)
        Button(self.view_options_frame, text="Back", command=self.show_launch_frame, font=("Helvetica", 12)).pack(pady=10)
    
    
    def show_taxonomy_table(self):
        self.hide_all_frames()
        self.taxonomy_frame = Frame(self.root)
        self.taxonomy_frame.pack(fill=BOTH, expand=True)

        Label(self.taxonomy_frame, text="Taxonomy Table", font=("Helvetica", 16)).pack(pady=20)
        
        column_names, taxonomy_data = db.get_table_data("Taxonomy")
        taxonomy_table = ttk.Treeview(self.taxonomy_frame, columns=column_names, show="headings")
        taxonomy_table.pack(fill=BOTH, expand=True)

        for col in column_names:
            taxonomy_table.heading(col, text=col)
            taxonomy_table.column(col, width=100)

        # Populate taxonomy_table with data from the database
        for row in taxonomy_data:
            taxonomy_table.insert("", "end", values=row)
        
        Button(self.taxonomy_frame, text="Back", command=self.show_view_options, font=("Helvetica", 12)).pack(pady=10)
    

    def show_audiofiles_table(self):
        self.hide_all_frames()
        self.audiofiles_frame = Frame(self.root)
        self.audiofiles_frame.pack(fill=BOTH, expand=True)

        Label(self.audiofiles_frame, text="Audiofiles Table", font=("Helvetica", 16)).pack(pady=20)
        
        column_names, audiofiles_data = db.get_table_data("Audiofiles")
        audiofiles_table = ttk.Treeview(self.audiofiles_frame, columns=column_names, show="headings")
        audiofiles_table.pack(fill=BOTH, expand=True)

        for col in column_names:
            audiofiles_table.heading(col, text=col)
            audiofiles_table.column(col, width=100)

        # Populate audiofiles_table with data from the database
        for row in audiofiles_data:
            audiofiles_table.insert("", "end", values=row)
        
        # Add Play button
        play_button = Button(self.audiofiles_frame, text="Play", command=self.play_selected_audio, font=("Helvetica", 12))
        play_button.pack(pady=10)

        Button(self.audiofiles_frame, text="Back", command=self.show_view_options, font=("Helvetica", 12)).pack(pady=10)

    def play_selected_audio(self):
        if not hasattr(self, 'audiofiles_frame'):
            logger.error("Audiofiles frame is not initialized.")
            return

        # Find the Treeview widget
        audiofiles_table = self.audiofiles_frame.winfo_children()[0]  # Assuming the Treeview is the first child of the frame
        
        # Get the selected item
        selected_item = audiofiles_table.selection_get()
        if selected_item:
            # Get the data for the selected row
            item = audiofiles_table.item(selected_item)
            logger.info(f"Selected audio file: {item}")

            # Assuming the second column contains the file path
            audio_file = item['values'][1]
            if audio_file:
                try:
                    # Play the audio file using pygame
                    pygame.mixer.music.load(audio_file)
                    pygame.mixer.music.play()
                    logger.info(f"Playing audio file: {audio_file}")
                except Exception as e:
                    logger.error(f"Error playing audio file: {str(e)}")
                    messagebox.showerror("Error", f"Could not play audio file: {str(e)}")
            else:
                messagebox.showerror("Error", "No audio file path found in the selected row.")
        else:
            messagebox.showerror("Error", "No row selected. Please select an audio file first.")

            
    def hide_all_frames(self):
        for frame in [self.login_frame, self.launch_frame, self.signup_frame, self.insert_frame, self.delete_frame, self.update_frame, self.password_frame, self.admin_frame, self.tables_frame, self.view_options_frame, self.taxonomy_frame, self.audiofiles_frame]:
            if frame is not None:
                frame.pack_forget()
    
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
        elif frame_name == 'password':
            if not self.password_frame:
                self.password_frame = init_password_change_frame(self.root, self.user_id, self.show_launch_frame)
            self.password_frame.pack()

    def verify_session(self):
        if not self.session_id:
            return False
        user_id, user_type = db.verify_session(self.session_id)
        return user_id is not None

if __name__ == "__main__":
    root = Tk()
    app = WildlifeApp(root)
    root.mainloop()
