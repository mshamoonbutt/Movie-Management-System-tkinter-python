import tkinter as tk
from tkinter import ttk

class MovieFinderPreview:
    def __init__(self, user_role='user'):
        self.surface = tk.Tk()
        self.surface.geometry('1200x750+20+10')
        self.surface.title("Search And View Movie Details")
        self.surface.resizable(False, False)
        
        if user_role == 'admin':
            self.admin_access_button = tk.Button(self.surface, text='Admin Access', command=self.admin_access, bg='#57a1f8', fg='black')
            self.admin_access_button.place(x=1000, y=20)  # Place to the left of logout button        

        # Movies Results Frame
        movie_results = ttk.LabelFrame(self.surface, text="Movies", width=1140, height=700)
        movie_results.place(x=30, y=120)

        # Unified Search Bar inside Movies Results Frame
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(movie_results, textvariable=self.search_var, width=160)
        self.search_entry.place(x=10, y=10)  # Adjusted position inside movie_results

        # Dropdown for Filter Criteria inside Movies Results Frame
        self.criteria_var = tk.StringVar()
        self.criteria_options = ['Title', 'Year', 'Genre', 'Director', 'Actor']
        self.criteria_dropdown = ttk.Combobox(movie_results, textvariable=self.criteria_var, values=self.criteria_options, width=10)
        self.criteria_dropdown.current(0)  # Default to first option
        self.criteria_dropdown.place(x=980, y=10)  # Adjusted position inside movie_results

        # Search Button inside Movies Results Frame
        tk.Button(movie_results, text='Search', command=self.search_movies, bg='#57a1f8', fg='black').place(x=1080, y=8)  # Adjusted position


        

        # Movie List
        self.movie_results_list = ttk.LabelFrame(movie_results, text="Movie list")
        self.movie_results_list.place(x=0, y=70, height=530, width=475)

        # TreeView for Movies
        self.tree = ttk.Treeview(self.movie_results_list, columns=('Rank', 'Title'), show='headings', height=23)
        self.tree.heading('Rank', text="Rank")
        self.tree.column('Rank', anchor=tk.CENTER, width=50)
        self.tree.heading('Title', text="Movie title")
        self.tree.column('Title', anchor=tk.CENTER, width=400)

        # Bind the method with TreeViewSelect event.
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        # Scrollbar for TreeView
        scrollbar_for_list = ttk.Scrollbar(self.movie_results_list, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar_for_list.set)

        # Place components on the grid
        self.tree.grid(row=0, column=0, sticky='NSEW')
        scrollbar_for_list.grid(row=0, column=1, sticky='NS')

        # Movie Information Frame
        self.movie_info_frame = ttk.LabelFrame(movie_results, text="Movie Information & Ratings and Reviews")
        self.movie_info_frame.place(x=480, y=70, height=500, width=630)  # Adjusted width and placed next to the movie list

        # Text widget for movie information
        self.text_info = tk.Text(self.movie_info_frame, height=30, width=75)
        self.text_info.pack(side=tk.LEFT)

        # Scrollbar for movie information
        scroll_info = ttk.Scrollbar(self.movie_info_frame, command=self.text_info.yview)
        self.text_info.configure(yscrollcommand=scroll_info.set)
        scroll_info.pack(side=tk.RIGHT, fill=tk.Y)

        # Bind the method with the Text widget click event.
        self.text_info.bind("<Button-1>", self.text_info_clicked)

        # Load data from file on initialization
        self.load_data()

        # Add a Logout Button
        self.logout_button = tk.Button(self.surface, text='Logout', command=self.logout, bg='#57a1f8', fg='black')
        self.logout_button.place(x=1100, y=20)  # Adjust the position to top right
        
        # Add a "Rate and Review Movie" Button
        self.rate_review_button = tk.Button(self.surface, text='Review Movie', command=self.rate_review_movie, bg='#57a1f8', fg='black')
        self.rate_review_button.place(x=40, y=20)  # Adjust the position to top right
        
        self.recommendation_button = tk.Button(self.surface, text='Get Recommendation', command=self.get_recommendation, bg='#57a1f8', fg='black')
        self.recommendation_button.place(x=180, y=20)  # Adjust the position
        
                # Dropdown for Filter Options
        self.filter_var = tk.StringVar()
        self.filter_options = ['Title', 'Genre', 'Year', 'Actor', 'Director']
        self.filter_dropdown = ttk.Combobox(self.surface, textvariable=self.filter_var, values=self.filter_options, width=10)
        self.filter_dropdown.current(0)  # Default to first option
        self.filter_dropdown.place(x=320, y=20)  # Adjust the position
        
        # Initialize the watchlist as an empty list
        self.watchlist = []

        # Load watchlist data if it exists
        self.load_watchlist()

        # Add a button to add movies to the watchlist
        self.add_to_watchlist_button = tk.Button(self.surface, text='Add to Watchlist', command=self.add_to_watchlist, bg='#57a1f8', fg='black')
        self.add_to_watchlist_button.place(x=430, y=20)  # Adjust the position

        # Add a button to view the watchlist
        self.view_watchlist_button = tk.Button(self.surface, text='View Watchlist', command=self.view_watchlist, bg='#57a1f8', fg='black')
        self.view_watchlist_button.place(x=530, y=20)  # Adjust the position


        
        self.surface.mainloop()
    
    def add_to_watchlist(self):
        selected_item = self.tree.selection()
        if selected_item:
            title = self.tree.item(selected_item)['values'][1] 
            if title in self.watchlist:
                tk.messagebox.showinfo("Info", "This movie is already in your watchlist.")
            else:
                self.watchlist.append(title)
                tk.messagebox.showinfo("Info", "Movie added to watchlist.")
                self.save_watchlist()

    def save_watchlist(self):
        with open('watchlist.txt', 'w') as file:
            for movie in self.watchlist:
                file.write(movie + '\n')

    def load_watchlist(self):
        try:
            with open('watchlist.txt', 'r') as file:
                self.watchlist = [line.strip() for line in file]
        except FileNotFoundError:
            self.watchlist = []

    def view_watchlist(self):
        watchlist_window = tk.Toplevel(self.surface)
        watchlist_window.title("Watchlist")
        watchlist_window.geometry("400x300+500+250")
        watchlist_window.config(bg="#fff")
        watchlist_window.resizable(False, False)

        if not self.watchlist:
            tk.Label(watchlist_window, text="Your watchlist is empty.", bg="white").pack(padx=10, pady=10)
        else:
            tk.Label(watchlist_window, text="Your Watchlist:", bg="white").pack(padx=10, pady=10)
            watchlist_text = "\n".join(self.watchlist)
            tk.Label(watchlist_window, text=watchlist_text, bg="white").pack(padx=10, pady=10)
        
    def get_recommendation(self):
        # Get the selected filter option
        selected_filter = self.filter_var.get()

        # Read the movie database and recommend movies based on the selected filter
        recommended_movies = self.recommend_movies(selected_filter)

        # Display the recommended movies in the TreeView
        self.display_recommended_movies(recommended_movies)    
    
    def recommend_movies(self, selected_filter):
        from tkinter import messagebox 
        try:
            with open('movie_database.txt', 'r') as file:
                movies = [line.strip().split(',') for line in file]

                # Sort movies by the selected filter (e.g., title, genre, year, actor, director)
                if selected_filter == 'Title':
                    movies.sort(key=lambda x: x[0].lower())
                elif selected_filter == 'Genre':
                    movies.sort(key=lambda x: x[2].lower())
                elif selected_filter == 'Year':
                    movies.sort(key=lambda x: int(x[1]))
                elif selected_filter == 'Actor':
                    movies.sort(key=lambda x: x[4].lower())
                elif selected_filter == 'Director':
                    movies.sort(key=lambda x: x[3].lower())

                # Return the top-rated movie(s) for the selected filter
                top_rated_movies = []
                highest_rating = -1
                for movie in movies:
                    if float(movie[5]) > highest_rating:
                        top_rated_movies = [movie]
                        highest_rating = float(movie[5])
                    elif float(movie[5]) == highest_rating:
                        top_rated_movies.append(movie)

                return top_rated_movies

        except FileNotFoundError:
            print("Error: 'movie_database.txt' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return []

    def display_recommended_movies(self, recommended_movies):
        # Clear the TreeView
        self.tree.delete(*self.tree.get_children())

        # Display recommended movies in the TreeView
        for idx, movie in enumerate(recommended_movies, start=1):
            self.tree.insert('', tk.END, values=(idx, movie[0], movie[5]))

        
    def logout(self):
        self.surface.destroy()  # Close the current window
        
    def rate_review_movie(self):
        from tkinter import messagebox 
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a movie to review.")
            return
        title = self.tree.item(selected_item)['values'][1]

        review_window = tk.Toplevel(self.surface)
        review_window.title(f"Review - {title}")
        review_window.geometry("400x300+500+250")
        review_window.config(bg="#fff")
        review_window.resizable(False, False)
        
        # Add widgets for review input
        tk.Label(review_window, text="Review:", bg="white").grid(row=0, column=0, sticky='nw', padx=10, pady=10)
        review_var = tk.Text(review_window, height=10, width=35)
        review_var.grid(row=0, column=1, padx=10, pady=10)
        
        # Add a button to submit the review
        tk.Button(review_window, text="Submit Review", command=lambda: self.submit_review(title, review_var.get("1.0", tk.END))).grid(row=1, columnspan=2, pady=10)

    def submit_review(self, title, review):
        from tkinter import messagebox 
        # Check if the review is not empty
        if not review.strip():
            messagebox.showerror("Error", "Review cannot be empty.")
            return

        # Now, read the existing data, update the movie's record, and write everything back
        updated_lines = []
        with open("movie_database.txt", "r") as file:
            for line in file:
                data = line.strip().split(',')
                # If the title matches, append the new review
                if data[0].lower() == title.lower():
                    data.append(review.strip())
                updated_lines.append(','.join(data))

        # Write the updated data back to the file
        with open("movie_database.txt", "w") as file:
            for line in updated_lines:
                file.write(line + "\n")

        messagebox.showinfo("Success", "Review submitted successfully.")
    
        
    def admin_access(self):
        from tkinter import messagebox 
        if hasattr(self, 'admin_access_button'):
            self.open_add_movie_window()
        else:
            messagebox.showerror("Access Denied", "You do not have admin privileges.")

        
    def open_add_movie_window(self): 
        from tkinter import messagebox

        def save_movie():
            title = self.title_var.get()
            year = self.year_var.get()
            genre = self.genre_var.get()
            director = self.director_var.get()
            actor = self.actor_var.get()
            rating = self.rating_entry.get()
            review = self.review_entry.get()            

            # Validate that all fields are filled
            if not title or not year or not genre or not director or not actor or not rating or not review:
                messagebox.showerror("Error", "Please fill in all fields.")
                return
            
            try:
                rating = float(rating)
                if not 0 <= rating <= 5:
                    raise ValueError("Rating must be between 0 and 5.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return
            

            # Create a string with the movie information in CSV format
            movie_info = f"{title},{year},{genre},{director},{actor},{rating},{review}\n"

            # Append the movie information to the file
            with open("movie_database.txt", "a") as file:
                file.write(movie_info)

            # Show a success message
            messagebox.showinfo("Success", "Movie information saved successfully.")
             

        
        # GUI setup
        self.window = tk.Toplevel(self.surface)
        self.window.title("Add New Movie")
        self.window.geometry("400x350+500+250")
        self.window.config(bg="#fff")
        self.window.resizable(False, False)

        self.title_label = tk.Label(self.window, text="Title:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.title_label.place(x=30, y=30)
            
        self.title_var = tk.StringVar()
        self.title_entry = tk.Entry(self.window, width=25, textvariable=self.title_var, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.title_entry.place(x=120, y=30)

        self.year_label = tk.Label(self.window, text="Year:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.year_label.place(x=30, y=70)

        self.year_var = tk.StringVar()
        self.year_entry = tk.Entry(self.window, width=25, textvariable=self.year_var, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.year_entry.place(x=120, y=70)

        self.genre_label = tk.Label(self.window, text="Genre:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.genre_label.place(x=30, y=110)

        self.genre_var = tk.StringVar()
        self.genre_entry = tk.Entry(self.window, width=25, textvariable=self.genre_var, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.genre_entry.place(x=120, y=110)

        self.director_label = tk.Label(self.window, text="Director:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.director_label.place(x=30, y=150)

        self.director_var = tk.StringVar()
        self.director_entry = tk.Entry(self.window, width=25, textvariable=self.director_var, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.director_entry.place(x=120, y=150)

        self.actor_label = tk.Label(self.window, text="Actor:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.actor_label.place(x=30, y=190)

        self.actor_var = tk.StringVar()
        self.actor_entry = tk.Entry(self.window, width=25, textvariable=self.actor_var, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.actor_entry.place(x=120, y=190)
        
        self.rating_entry = tk.Label(self.window, text="Rating:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.rating_entry.place(x=30, y=230)
        
        self.rating_entry = tk.StringVar()
        self.rating_entry = tk.Entry(self.window, width=25, textvariable=self.rating_entry, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.rating_entry.place(x=120, y=230)
        
        self.review_entry = tk.Label(self.window, text="Review:", fg="black", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.review_entry.place(x=30, y=270)
        
        self.review_entry = tk.StringVar()
        self.review_entry = tk.Entry(self.window, width=25, textvariable=self.review_entry, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.review_entry.place(x=120, y=270)
        
        self.save_button = tk.Button(self.window, width=15, pady=5, text="Save", bg="#57a1f8", fg="white", border=0, command=save_movie)
        self.save_button.place(x=160, y=310)
        
        
        self.window.mainloop()


    def load_data(self):
        try:
            with open('movie_database.txt', 'r') as file:
                # Read lines, split data, and calculate rank based on ratings
                lines = [line.strip().split(',') for line in file]
                lines.sort(key=lambda x: float(x[5]), reverse=True)  # Sort by ratings in descending order

                for idx, data in enumerate(lines, start=1):
                    self.tree.insert('', tk.END, values=(idx, data[0], data[5]))
        except FileNotFoundError:
            print("Error: 'movie_database.txt' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def search_movies(self):
        query = self.search_var.get().lower()
        criteria = self.criteria_var.get().lower()
        
        criteria_to_index = {
        'title': 0,
        'year': 1,
        'genre': 2,
        'director': 3,
        'actor': 4
        }

        # Clear the movie information box and TreeView
        self.text_info.config(state=tk.NORMAL)
        self.text_info.delete(1.0, tk.END)
        self.tree.delete(*self.tree.get_children())

        try:
            with open('movie_database.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    # Use the criteria_to_index to check the right field in the data array
                    if query in data[criteria_to_index[criteria]].lower():
                        self.tree.insert('', 'end', values=(0, data[0]))  # Adjust as needed
                        details = "Title: {}\nYear: {}\nGenre: {}\nDirector: {}\nActor: {}\nRating: {}\nReview: {}\n\n".format(*data)
                        self.text_info.insert(tk.END, details)
        except FileNotFoundError:
            print("Error: 'movie_database.txt' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
            self.text_info.config(state=tk.DISABLED)

    def item_selected(self, event):
        # Clear existing content in both the movie information and ratings and reviews boxes
        self.text_info.config(state=tk.NORMAL)  # Set state to normal to enable editing temporarily
        self.text_info.delete(1.0, tk.END)
        self.text_info.config(state=tk.NORMAL)  # Set state back to disabled after clearing

        # Get the selected item
        selected_item = self.tree.selection()
        if selected_item:
            # Get the title from the selected row
            title = self.tree.item(selected_item)['values'][1]

            # Fetch details of the selected movie from the file and display in the movie information box
            with open('movie_database.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if data[0] == title:
                        details = f"Title: {data[0]}\nYear Of Release: {data[1]}\nGenre: {data[2]}\nDirector: {data[3]}\nActor: {data[4]}\nRatings: {data[5]}\nReviews: {data[6::]}"
                        self.text_info.insert(tk.END, details)
                        break

    def text_info_clicked(self, event):
        # Enable editing when the text widget is clicked
        self.text_info.config(state=tk.NORMAL)


def start_movie_finder(user_role):
    movie_finder_preview = MovieFinderPreview(user_role)
    movie_finder_preview.surface.mainloop()

