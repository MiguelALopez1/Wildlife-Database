from tkinter import *
from tkinter import messagebox
from db_utils import db

# Set up database cursor
cursor = db.get_cursor()

def init_delete_frame(root, user_id, init_launch_frame):
    delete_frame = Frame(root, width=800, height=600)
    delete_frame.pack_propagate(False)  # Keep the frame size fixed

    # Variable for inputting audio file ID to delete
    file_id_to_delete = StringVar()
    file_list_text = StringVar()

    # Function to fetch and display audio files for the given user
    def fetch_audio_files():
        user_id_value = user_id.get()
        if not user_id_value:
            print("User ID is empty.")
            messagebox.showwarning("Warning", "No User ID provided.")
            return

        # Fetch audio files from the database
        try:
            cursor.execute("SELECT audiofiles_id, file_name FROM Audiofiles WHERE user_id = %s", (user_id_value,))
            results = cursor.fetchall()

            # Update file list text based on fetched results
            if results:
                formatted_list = ""
                for audio_id, file_name in results:
                    formatted_list += (
                        f"ID: {audio_id}\n"
                        f"File: {file_name}\n"
                        f"{'-'*40}\n"
                    )
                file_list_text.set(formatted_list)
            else:
                file_list_text.set("No audio files found for the specified User ID.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch audio files: {e}")

    # Function to delete the selected audio file by ID
    def delete_file():
        audio_id = file_id_to_delete.get().strip()

        if audio_id:
            try:
                # Check if the audio ID exists for the current user
                cursor.execute("SELECT file_name FROM Audiofiles WHERE audiofiles_id = %s AND user_id = %s", (audio_id, user_id.get()))
                file_check = cursor.fetchone()
                
                if file_check:
                    # Proceed with deletion
                    cursor.execute("DELETE FROM Audiofiles WHERE audiofiles_id = %s", (audio_id,))
                    conn.commit()
                    messagebox.showinfo("Success", f"Deleted file '{file_check[0]}' successfully.")
                    fetch_audio_files()  # Refresh the list after deletion
                    file_id_to_delete.set("")  # Clear the input field
                else:
                    messagebox.showwarning("Warning", "File ID not found for this user.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete audio file: {e}")
                print("Error deleting audio file:", e)  # Debugging output
        else:
            messagebox.showwarning("Warning", "Please enter a valid file ID to delete.")

    # Create a canvas for scrolling within the delete frame
    canvas = Canvas(delete_frame)
    scrollbar = Scrollbar(delete_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Display list of audio files with scrollable text in the scrollable frame
    Label(scrollable_frame, text="Audio Files List:", font=("Helvetica", 12)).pack(pady=5)
    file_list_label = Message(scrollable_frame, textvariable=file_list_text, font=("Helvetica", 10), justify=LEFT, width=500)
    file_list_label.pack(pady=5)

    # Button to refresh the audio files list
    Button(scrollable_frame, text="Show/Update List", command=fetch_audio_files, font=("Helvetica", 12)).pack(pady=5)

    # Field to enter the ID of the file to delete
    Label(scrollable_frame, text="Enter File ID to Delete:", font=("Helvetica", 12)).pack(pady=5)
    Entry(scrollable_frame, textvariable=file_id_to_delete, font=("Helvetica", 12)).pack(pady=5)

    # Button to delete the selected file
    Button(scrollable_frame, text="Delete Selected File", command=delete_file, font=("Helvetica", 14)).pack(pady=10)

    # Back button to return to launch page
    Button(scrollable_frame, text="Back to Launch", command=lambda: (delete_frame.pack_forget(), init_launch_frame()), font=("Helvetica", 14)).pack(pady=10)

    # Pack the canvas and scrollbar within the delete frame
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Fetch audio files initially
    fetch_audio_files()

    return delete_frame

