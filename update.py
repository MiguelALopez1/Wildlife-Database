from tkinter import *
from tkinter import messagebox
from db_connection import conn

# Set up database cursor
cursor = conn.cursor()

def init_update_frame(root, user_id, init_launch_frame):
    # Set fixed size for the update frame
    update_frame = Frame(root, width=800, height=600)
    update_frame.pack_propagate(False)  # Keep the frame size fixed

    # Centered container frame to hold all inner elements with the same fixed size
    container = Frame(update_frame, width=800, height=600, padx=20, pady=20)
    container.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center align container within update_frame
    container.pack_propagate(False)  # Prevent resizing within container

    # Variables for inputting audio file ID to update and taxonomy fields
    file_id_to_update = StringVar()
    file_list_text = StringVar()

    # Variables for taxonomy details
    domain = StringVar()
    kingdom = StringVar()
    phylum = StringVar()
    class_field = StringVar()
    order = StringVar()
    family = StringVar()
    genus = StringVar()
    species = StringVar()

    # Function to fetch and display audio files with taxonomy details for the given user
    def fetch_audio_files():
        user_id_value = user_id.get()
        if not user_id_value:
            print("User ID is empty.")
            messagebox.showwarning("Warning", "No User ID provided.")
            return

        # Fetch audio files and taxonomy details from the database
        try:
            query = """
                SELECT a.audiofiles_id, a.file_name, t.domain, t.kingdom, t.phylum, t.class, t.order, 
                       t.family, t.genus, t.species
                FROM Audiofiles a
                LEFT JOIN Taxonomy t ON a.audiofiles_id = t.audiofile_id
                WHERE a.user_id = %s
            """
            cursor.execute(query, (user_id_value,))
            results = cursor.fetchall()

            if results:
                formatted_list = ""
                for (audio_id, file_name, domain, kingdom, phylum, class_, order, family, genus, species) in results:
                    formatted_list += (
                        f"ID: {audio_id}\n"
                        f"File: {file_name}\n"
                        f"Domain: {domain or 'N/A'}\n"
                        f"Kingdom: {kingdom or 'N/A'}\n"
                        f"Phylum: {phylum or 'N/A'}\n"
                        f"Class: {class_ or 'N/A'}\n"
                        f"Order: {order or 'N/A'}\n"
                        f"Family: {family or 'N/A'}\n"
                        f"Genus: {genus or 'N/A'}\n"
                        f"Species: {species or 'N/A'}\n"
                        f"{'-'*40}\n"
                    )
                file_list_text.set(formatted_list)
            else:
                file_list_text.set("No audio files found for the specified User ID.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch audio files: {e}")

    def update_taxonomy():
        audio_id = file_id_to_update.get().strip()
        if audio_id:
            try:
                cursor.execute("SELECT audiofiles_id FROM Audiofiles WHERE audiofiles_id = %s AND user_id = %s", (audio_id, user_id.get()))
                file_check = cursor.fetchone()

                if file_check:
                    cursor.execute("""
                        UPDATE Taxonomy SET domain = %s, kingdom = %s, phylum = %s, class = %s, 
                        `order` = %s, family = %s, genus = %s, species = %s
                        WHERE audiofile_id = %s
                    """, (domain.get(), kingdom.get(), phylum.get(), class_field.get(), order.get(), family.get(), genus.get(), species.get(), audio_id))
                    conn.commit()
                    messagebox.showinfo("Success", "Taxonomy details updated successfully.")
                    fetch_audio_files()  # Refresh the list after updating
                    file_id_to_update.set("")
                else:
                    messagebox.showwarning("Warning", "File ID not found for this user.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update taxonomy details: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter a valid file ID to update.")

    # Create a canvas for scrolling within the centered container
    canvas = Canvas(container)
    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Display list of audio files with taxonomy details
    Label(scrollable_frame, text="Audio Files and Taxonomy Details:", font=("Helvetica", 12)).pack(pady=5)
    file_list_label = Message(scrollable_frame, textvariable=file_list_text, font=("Helvetica", 10), justify=LEFT, width=500)
    file_list_label.pack(pady=5)

    # Button to show/update list
    Button(scrollable_frame, text="Show/Update List", command=fetch_audio_files, font=("Helvetica", 12)).pack(pady=5)

    # Field to enter the ID of the file to update
    Label(scrollable_frame, text="Enter File ID to Update:", font=("Helvetica", 12)).pack(pady=5)
    Entry(scrollable_frame, textvariable=file_id_to_update, font=("Helvetica", 12)).pack(pady=5)

    # Taxonomy Information Section
    Label(scrollable_frame, text="Taxonomy Information", font=("Helvetica", 16, "bold")).pack(pady=10)
    for field_name, variable in zip(
        ["Domain", "Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"],
        [domain, kingdom, phylum, class_field, order, family, genus, species]):
        Label(scrollable_frame, text=field_name, font=("Helvetica", 12)).pack()
        Entry(scrollable_frame, textvariable=variable, font=("Helvetica", 12)).pack(pady=5)

    # Button to update taxonomy details
    Button(scrollable_frame, text="Update Taxonomy", command=update_taxonomy, font=("Helvetica", 14)).pack(pady=10)

    # Back button
    Button(scrollable_frame, text="Back to Launch", command=lambda: (update_frame.pack_forget(), init_launch_frame()), font=("Helvetica", 14)).pack(pady=10)

    # Pack the canvas and scrollbar within the container frame
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return update_frame

