from tkinter import *
from tkinter import messagebox

def save_movie():
    title = title_var.get()
    year = year_var.get()
    genre = genre_var.get()
    director = director_var.get()
    actor = actor_var.get()

    # Validate that all fields are filled
    if not title or not year or not genre or not director or not actor:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Create a string with the movie information in CSV format
    movie_info = f"{title},{year},{genre},{director},{actor}\n"

    # Append the movie information to the file
    with open("movie_database.txt", "a") as file:
        file.write(movie_info)

    # Show a success message
    messagebox.showinfo("Success", "Movie information saved successfully.")

# GUI setup
window = Tk()
window.title("Add New Movie")
window.geometry("400x300+500+250")
window.config(bg="#fff")
window.resizable(False, False)

title_label = Label(window, text="Title:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
title_label.place(x=30, y=30)
    
title_var = StringVar()
title_entry = Entry(window, width=25, textvariable=title_var, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
title_entry.place(x=120, y=30)

year_label = Label(window, text="Year:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
year_label.place(x=30, y=70)

year_var = StringVar()
year_entry = Entry(window, width=25, textvariable=year_var, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
year_entry.place(x=120, y=70)

genre_label = Label(window, text="Genre:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
genre_label.place(x=30, y=110)

genre_var = StringVar()
genre_entry = Entry(window, width=25, textvariable=genre_var, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
genre_entry.place(x=120, y=110)

director_label = Label(window, text="Director:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
director_label.place(x=30, y=150)

director_var = StringVar()
director_entry = Entry(window, width=25, textvariable=director_var, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
director_entry.place(x=120, y=150)

actor_label = Label(window, text="Actor:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
actor_label.place(x=30, y=190)

actor_var = StringVar()
actor_entry = Entry(window, width=25, textvariable=actor_var, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
actor_entry.place(x=120, y=190)
 
save_button = Button(window, width=15, pady=5, text="Save", bg="#57a1f8", fg="white", border=0, command=save_movie)
save_button.place(x=160, y=240)
    
window.mainloop()
