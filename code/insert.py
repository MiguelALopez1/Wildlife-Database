from tkinter import *
from tkinter import filedialog, messagebox
from mutagen.mp3 import MP3
import os
import datetime
from db_utils import db

# Set up database cursor
cursor = db.get_cursor()

def init_insert_frame(root, user_id, init_launch_frame):
    # Variables for insert form
    file_name = StringVar()
    duration = StringVar()
    rating = IntVar()
    domain = StringVar()
    kingdom = StringVar()
    phylum = StringVar()
    class_field = StringVar()
    order = StringVar()
    family = StringVar()
    genus = StringVar()
    species = StringVar()
    audio_file_path = StringVar()

    # Create main frame with fixed size and prevent resizing
    insert_frame = Frame(root, width=800, height=600)
    insert_frame.pack_propagate(False)

    # Function to upload audio and get file duration
    def upload_audio():
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            file_name.set(os.path.basename(file_path))
            audio_file_path.set(file_path)
            try:
                if os.path.getsize(file_path) == 0:
                    duration.set("00:00:00")
                else:
                    #add debug statement of the file_path
                    print(file_path)
                    audio = MP3(file_path)
                    duration_seconds = int(audio.info.length)
                    duration.set(f"{duration_seconds // 3600:02}:{(duration_seconds % 3600) // 60:02}:{duration_seconds % 60:02}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not read file: {e}")
                duration.set("00:00:00")

    # Function to submit insert data
    def submit_insert():
        # Get the current date for upload_date
        current_date = datetime.date.today()

        # Step 1: Insert into Audiofiles table first without taxonomy_id
        cursor.execute(
            "INSERT INTO Audiofiles (user_id, file_name, duration, rating, upload_date, is_certified) VALUES (%s, %s, %s, %s, %s, 1)",
            (user_id.get(), file_name.get(), duration.get(), rating.get(), current_date)
        )
        audio_id = cursor.lastrowid  # Get the auto-incremented ID from Audiofiles table

        # Step 2: Insert taxonomy data into Taxonomy table
        cursor.execute(
            "INSERT INTO Taxonomy (audiofile_id, domain, kingdom, phylum, class, `order`, family, genus, species) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (audio_id, domain.get(), kingdom.get(), phylum.get(), class_field.get(), order.get(), family.get(), genus.get(), species.get())
        )
        taxonomy_id = cursor.lastrowid  # Get the auto-incremented taxonomy_id

        # Step 3: Update the Audiofiles table with the taxonomy_id
        cursor.execute(
            "UPDATE Audiofiles SET taxonomy_id = %s WHERE audiofiles_id = %s",
            (taxonomy_id, audio_id)
        )

        # Commit the transaction
        db.connect().commit()
        messagebox.showinfo("Success", "Audio file and taxonomy data uploaded successfully!")

    # Create a canvas for scroll functionality
    canvas = Canvas(insert_frame)
    scrollbar = Scrollbar(insert_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # GUI layout for scrollable_frame
    Label(scrollable_frame, text="Insert Audio Information", font=("Helvetica", 16, "bold")).pack(pady=10)

    # File selection
    Button(scrollable_frame, text="Choose File", command=upload_audio, font=("Helvetica", 14)).pack(pady=5)
    Label(scrollable_frame, text="File Name:", font=("Helvetica", 12)).pack()
    Label(scrollable_frame, textvariable=file_name, font=("Helvetica", 12), relief=SUNKEN, width=40).pack(pady=5)

    # Duration display
    Label(scrollable_frame, text="Duration (hh:mm:ss):", font=("Helvetica", 12)).pack()
    Label(scrollable_frame, textvariable=duration, font=("Helvetica", 12), relief=SUNKEN, width=20).pack(pady=5)

    # Rating input
    Label(scrollable_frame, text="Rating (1-5)", font=("Helvetica", 12)).pack()
    Entry(scrollable_frame, textvariable=rating, font=("Helvetica", 12), width=5).pack(pady=5)

    # Taxonomy Information Section
    Label(scrollable_frame, text="Taxonomy Information", font=("Helvetica", 16, "bold")).pack(pady=10)
    Label(scrollable_frame, text="Domain", font=("Helvetica", 12)).pack()
    Entry(scrollable_frame, textvariable=domain, font=("Helvetica", 12)).pack(pady=5)
    Label(scrollable_frame, text="Kingdom", font=("Helvetica", 12)).pack()
    Entry(scrollable_frame, textvariable=kingdom, font=("Helvetica", 12)).pack(pady=5)
    Label(scrollable_frame, text="Phylum", font=("Helvetica", 12)).pack()
    Entry(scrollable_frame, textvariable=phylum, font=("Helvetica", 12)).pack(pady=5)
    Label(scrollable_frame, text="Class", font=("Helvetica", 12)).pack()
    Entry(scrollable_frame, textvariable=class_field, font=("Helvetica", 12)).pack(pady=5)
    Label(scrollable_frame, text="Order", font=("Helvetica", 12)).pack()
    Entry(scrollable_frame, textvariable=order, font=("Helvetica", 12)).pack(pady=5)
    Label(scrollable_frame, text="Family", font=("Helvetica", 12)).pack()
    Entry(scrollable_frame, textvariable=family, font=("Helvetica", 12)).pack(pady=5)
    Label(scrollable_frame, text="Genus", font=("Helvetica", 12)).pack()
    Entry(scrollable_frame, textvariable=genus, font=("Helvetica", 12)).pack(pady=5)
    Label(scrollable_frame, text="Species", font=("Helvetica", 12)).pack()
    Entry(scrollable_frame, textvariable=species, font=("Helvetica", 12)).pack(pady=5)

    # Submit button
    Button(scrollable_frame, text="Submit Insert", command=submit_insert, font=("Helvetica", 14, "bold"), width=15).pack(pady=10)

    # Back to Launch button
    Button(scrollable_frame, text="Back to Launch", command=lambda: (insert_frame.pack_forget(), init_launch_frame()), font=("Helvetica", 14)).pack(pady=10)

    return insert_frame

