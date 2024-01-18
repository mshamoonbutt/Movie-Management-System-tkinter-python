from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Movie Data Base")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(False, False)

#Add Movie Button
Button(root, width=39, pady=7, text="Add Movies", bg=
       "#57a1f8", fg="white", border=0).place(x=330, y=450)
add= Label(root, text="Want to add new Movie data?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
add.place(x=380, y=425)

#Search BAR
Button(root, width=7, pady=4, text="Search", bg="#57a1f8", fg="white", border=0).place(x=837, y=38)
search_bar = Entry(root, width=100, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
search_bar.place(x=30, y=40)
search_title = Label(root, text="Search for Movies from Title, Genre, Year, Cast etc", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
search_title.place(x=330, y=16)

#Database Frame
search_bar = Listbox(root, width=150, height=20, selectmode=SINGLE)
search_bar.place(x=10, y=100)

root.mainloop()