# importing necessary modules
from random import choice
import csv

# take input to append the list of choices
List_of_Choices = []


# Definition of Functions

# Function to open the datasets of the movies and
# append them to the list of choices
def movie():
    with open('imdb_top_1000.csv', 'r') as dataset:  # open the dataset
        read_data = csv.reader(dataset)  # read data
        for row in read_data:
            List_of_Choices.append(row)  # append the choice to the list
    choose_movie()  # Calling the function to choose one of the choices


# Function to choose an anime series for the user
def anime():
    with open('anime.csv', 'r') as dataset:
        read_data = csv.reader(dataset)  # read data
        for row in read_data:
            List_of_Choices.append(row)  # append the choice to the list
    choose_anime()  # Calling the function to choose one of the choices


# Function to choose an anime series from the given choices
def choose_anime():
    final_choice = choice(List_of_Choices)
    # Storing item to respective variables
    name = final_choice[2]

    print("Let's watch", name)


# Function to read and append a cryptocurrency dataset to the list of choices
def crypto():
    with open("cryptocurrency.csv", 'r') as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)
        choose_crypto()

# Function t o choose a cryptocurrency from the given list of choices


def choose_crypto():
    final_choice = choice(List_of_Choices)
    # Storing items to respective variables
    coin_name = final_choice[9]
    coin_shortname = final_choice[5]

    print("Let's invest on", coin_name, "(", coin_shortname, ")")


# Function to append dog breeds to the list of choices
def dog():
    with open("dog.csv", 'r') as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)
        choose_dog()

# Function to choose a dog breed from the given dataset


def choose_dog():
    final_choice = choice(List_of_Choices)

    # Storing items to respective variables
    License_type = final_choice[0]
    Breed = final_choice[1]

    # Printing the choice made by the program
    print("You should go for a", Breed)


# Function to choose


# Function to open the datasets of the books and
# append them to the list of choices
def books():
    with open('books.csv', 'r') as dataset:
        read_data = csv.reader(dataset)  # read data from the file
        for row in read_data:
            # append the data to the list of choices
            List_of_Choices.append(row)
    choose_book()  # calling the choose function to


# Function for choosing a song
def songs():
    with open("data.csv", 'r') as dataset:
        read_data = csv.reader(dataset)  # read data from the given dataset
        for row in read_data:
            List_of_Choices.append(row)

        choose_song()

# Function to add Electric Vehicles dataset to the list of choices


def ev():
    with open("ev.csv") as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)

    choose_ev()

# Function to choose an electric vehicle from the given list of choices


def choose_ev():
    final_choice = choice(List_of_Choices)

    # Assigning values to respective variables
    brand = final_choice[0]
    model = final_choice[1]
    pickup = final_choice[2]
    topspeed = final_choice[3]
    range = final_choice[4]
    efficiency = final_choice[5]
    fastcharging = final_choice[6]
    rapidcharging = final_choice[7]
    powertrain = final_choice[8]
    plugtype = final_choice[9]
    bodytype = final_choice[10]
    segment = final_choice[11]
    seats = final_choice[12]
    price = final_choice[13]

    # Print the final choice
    print("Let's go for", brand, "\'s", model)
    print()
    print()

    # Asking user if they want to know more
    user_in = input("Do you want to know more about this model? (y/n) \n")
    print()
    print()

    if user_in == 'y':
        print("Brand: ", brand)
        print()
        print("Model: ", model)
        print()
        print("Pickup: ", pickup)
        print()
        print("Top Speed: ", topspeed)
        print()
        print("Range (in kilometers)", range)
        print()
        print("Efficiency: ", efficiency)
        print()
        print("Fast Charging: ", fastcharging)
        print()
        print("Rapid Charging: ", rapidcharging)
        print()
        print("Power Train: ", powertrain)
        print()
        print("Plug Type: ", plugtype)
        print()
        print("Body Type: ", bodytype)
        print()
        print("Segment", segment)
        print()
        print("Seats", seats)
        print()
        print("Price: ", price)
        print()

# Function to add food datasets to the list of choices


def food_recipes():
    with open("food_recipes.csv", 'r') as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)

    choose_food()


# Function to choose food
def choose_food():
    final_choice = choice(List_of_Choices)
    # Assigning values to respective variables
    name = final_choice[1]
    translatedname = final_choice[2]
    ingredients = final_choice[3]
    translatedingredients = final_choice[4]
    prep_time = final_choice[5]
    cook_time = final_choice[6]
    servings = final_choice[7]
    cuisine = final_choice[8]
    course = final_choice[9]
    diet = final_choice[10]
    instructions = final_choice[11]
    trans_instruction = final_choice[12]
    url = final_choice[13]

    # Printing values
    print("Let's learn to cook the dish named \"", name, "\"")
    print()
    print()
    print()
    print("Translated Name: ", translatedname)
    print()
    print("Ingredients", ingredients)
    print()
    print("Translated Ingredients: ", translatedingredients)
    print()
    print("Preparation Time: ", prep_time)
    print()
    print("Cook Time: ", cook_time)
    print()
    print("Servings: ", servings)
    print()
    print("Cuisine: ", cuisine)
    print()
    print("Course", course)
    print()
    print("Diet: ", diet)
    print()
    print("Instruction: ", instructions)
    print()
    print("Translated Instructions: ", trans_instruction)
    print()
    print("URL: ", url)

# FUnction to append dataset of games to the list of choices


def game():
    with open("games.csv") as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)
        choose_game()

# Function to choose a game from the list of choices


def choose_game():
    final_choice = choice(List_of_Choices)

    # Storing the items to the respective variables
    game_name = final_choice[0]

    # Print the choice made by the computer/program
    print("Let's play", game_name)


# Function to add the items in the dataset to the list of choices
def habit():
    with open("skills.csv", 'r') as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)

    choose_habit()


# Function to choose a distinct habit from the dataset
def choose_habit():
    final_choice = choice(List_of_Choices)

    # Assigning values to the respective variables
    skills = final_choice[0]

    print("Lets work on building", "\"", skills, "\"")


# Function to add the dataset of various instagram profiles to the list of choices
def instagram_profile():
    with open("instagram_profiles.csv", 'r') as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)

        choose_profile()

# Function to choose a profile from the given dataset


def choose_profile():
    final_choice = choice(List_of_Choices)

    # Assigning values to their respective variables
    name = final_choice[0]
    ranking = final_choice[1]
    category = final_choice[2]
    followers = final_choice[3]
    audience = final_choice[4]
    authentic_engagement = final_choice[5]
    engagement = List_of_Choices[6]

    # Print the values
    print("Let's follow", name)
    print()
    print()
    print()
    print(name.upper())
    print()
    print("Ranking (worldwide): ", ranking)
    print()
    print("Category", category)
    print()
    print("Followers: ", followers)
    print()
    print("Audience: ", audience)
    print()
    print("Authentic Engagement: ", authentic_engagement)
    print()
    print("Engagement: ", engagement)
    print()


# Function to add datasets to the list of choices
def programming_language():
    with open("programming_languages.csv", 'r') as datasets:
        read_data = csv.reader(datasets)
        for row in read_data:
            List_of_Choices.append(row)

        choose_prog_lang()


def choose_prog_lang():
    final_choice = choice(List_of_Choices)
    # Assign items to the variables
    language_name = final_choice[1]
    _extension_ = final_choice[2]
    program_sample = final_choice[3]

    # Print the values
    print("Let's learn", language_name)
    print()
    print()
    print("Programming Language Name: ", language_name)
    print()
    print("Extension: ", _extension_)
    print()
    print("Hello world sample code: ", program_sample)
    print()
    print()


# Function to add the datasets to the list of choices
def kpop_idol():
    with open("kpop_idols.csv", 'r') as datasets:
        final_choice = choice(List_of_Choices)

        # Assigning elements to the respective variables
        stage_name = final_choice[0]
        full_name = final_choice[1]
        korean_name = final_choice[2]
        korean__stage_name = final_choice[3]
        dob = final_choice[4]
        group = final_choice[5]
        country = final_choice[6]
        birthplace = final_choice[7]
        other_group = final_choice[8]
        gender = final_choice[9]

        # Print the values
        print("Let's go for", stage_name, "(", group, ")")

        print("FULL DETAILS")
        print()
        print()
        print("Stage name: ", stage_name)
        print()
        print("Full name: ", full_name)
        print()
        print("Korean Stage Name: ", korean__stage_name)
        print()
        print("Korean full name: ", korean_name)
        print()
        print("Date of Birth: ", dob)
        print()
        print("Group: ", group)
        print()
        print("Country", country)
        print()
        print("Birthplace: ", birthplace)
        print()
        print("Other Group: ")
        print()
        print("Gender", gender)
        print()


# Function to add datasets to the list of choices
def quote():
    with open("quotes.csv", 'r') as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)

        choose_quote()


# Function to choose quote from a given list of choices
def choose_quote():
    final_choice = choice(List_of_Choices)
    # Assigning the values to their respective variables
    quote = final_choice[1]
    author = final_choice[2]
    tags = final_choice[3]

# Choose any of the given choices


def my_choices():
    user_in = int(input("How many choices do you have? \n"))

    for i in range(user_in):
        choice = input("Enter the choice: ")
        List_of_Choices.append(choice)


def choose_movie():
    final_choice = choice(List_of_Choices)  # choice one element from the list

    # Storing the items of the list to respective variables
    poster_link = final_choice[0]
    name = final_choice[1]
    release_year = final_choice[2]
    certificate = final_choice[3]
    runtime = final_choice[4]
    genre = final_choice[5]
    imdb_rating = final_choice[6]
    overview = final_choice[7]
    director = final_choice[8]
    star1 = final_choice[9]
    star2 = final_choice[10]
    star3 = final_choice[11]
    votes = final_choice[12]
    gross = final_choice[13]

    # Printing the final choice made by the program
    print("Let's go for", final_choice[1])
    print("")
    print("Name: ", name)
    print("Genre: ", release_year)
    print("Duration: ", runtime)
    print("Starring", star1, ",", star2, ",", star3)

    # User input to ask if they want more details
    user_in = input("Hmmmmm.... Want to know more? (y/n) \n")

    # To show more information about the choosen movie
    # If user opts "yes"
    if user_in.lower() == 'y':
        print("Poster link: ", poster_link)
        print()
        print("Certificate: ", certificate)
        print()
        print("Release Year: ", release_year)
        print()
        print("Duration: ", runtime)
        print()
        print("Genre: ", genre)
        print()
        print("IMDB Rating: ", imdb_rating)
        print()
        print("Overview: ", overview)
        print()
        print("Director: ", director)
        print()
        print("Starring", star1, ",", star2, ",", star3)
        print()
        print("Votes", votes)
        print()
        print("Gross: ", gross)
        print()
        print()

    # If user opts "no"
    elif user_in.lower() == 'n':
        print("Okay!!")

    # In case of wrong input
    else:
        print("Umm.. Invalid Input")


def choose_song():
    final_choice = choice(List_of_Choices)  # Choose only element from the list

    # Storing the items of the list to respective variables
    index = final_choice[0]
    acousticness = final_choice[1]
    danceablity = final_choice[2]
    duration = final_choice[3]
    energy = final_choice[4]
    instrument = final_choice[5]
    key = final_choice[6]
    liveness = final_choice[7]
    loudness = final_choice[8]
    mode = final_choice[9]
    speechness = final_choice[10]
    tempo = final_choice[11]
    valence = final_choice[12]
    target = final_choice[13]
    name = final_choice[15]
    artist = final_choice[16]

    # Printing the element chosen by the program
    print("Let's listen to", "\"", name, "\"", 'by', artist)
    print()
    print()


# Function to choose a book
def choose_book():
    # List of the final choice
    final_choice = choice(List_of_Choices)

    # Assignment of the heading to the elements
    bookid, title, authors, average_rating, isbn, isbn_13, language_code, pages, ratings, text_review, publication, publisher = [
        final_choice[0], final_choice[1], final_choice[2], final_choice[3], final_choice[4], final_choice[5], final_choice[6], final_choice[7], final_choice[8], final_choice[9], final_choice[10], final_choice[11]]

    # Print the choice
    print("I think, you should try", "\"", title, "\"" "by", authors)
    print("Publisher: ", publisher)
    print()
    print()

    # Ask if they want to know more
    user_in = input("Do you want to know more? (y/n) \n")
    print()
    print()

    # If user opts for yes
    if user_in.lower() == 'y':
        print("OKAY... HERE ARE THE MORE INFORMATION ABOUT THIS BOOK!!\n")
        print()
        print()
        print("Title:", title)
        print()
        print("Author(s):", authors)
        print()
        print("Average Rating: ", average_rating)
        print()
        print("ISBN: ", isbn)
        print()
        print("ISBN 13: ", isbn_13)
        print()
        print("Language Code: ", language_code)
        print()
        print("Ratings: ", ratings)
        print()
        print("Text Review: ", text_review)
        print()
        print("Publication: ", publication)
        print()
        print("Publisher:", publisher)
        print()

    elif user_in.lower() == 'n':
        print("Okay.. Have a Nice Day!!")

    else:
        print("Hmmm... Invalid Input")


# Function to the dataset of ted talks to the list of choices
def ted():
    with open('ted.csv', 'r') as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)
        choose_ted()

# Function to choose one of the choices


def choose_ted():
    final_choice = choice(List_of_Choices)

    # ASsign values to the required variables
    title = final_choice[0]
    author = final_choice[1]
    date = final_choice[2]
    views = final_choice[3]
    likes = final_choice[4]
    link = final_choice[5]

    # Printing the values
    print("Let's watch", "\"", title, "\"", "by", author)
    print()
    print()
    print("Title: ", title)
    print()
    print("Author: ", author)
    print()
    print("Date: ", date)
    print()
    print("Views: ", views)
    print()
    print("Likes: ", likes)
    print()
    print("Link: ", link)
    print()


# Function to add the datasets to the list of choices
def youtube():
    with open("youtube.csv", 'r') as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)

    choose_youtuber()

# Function to choose a youtuber from the list of choices


def youtuber():
    final_choice = choice(List_of_Choices)
    # Assign values to their respective variables
    ranking = final_choice[0]
    youtuber = final_choice[1]
    subs = final_choice[2]
    view = final_choice[3]
    videos = final_choice[4]
    category = final_choice[5]
    started = final_choice[6]

    #  Printing the values
    print("Let's subscribe", youtuber)
    print()
    print()
    print("World Ranking: ", ranking)
    print()
    print("Youtuber: ", youtuber)
    print()
    print("Video Views: ", view)
    print()
    print("Video Count: ", videos)
    print()
    print("Category: ", category)
    print()
    print("Started in: ", started)
    print()
    print()


# Function to add the dataset to the list of choices
def articles():
    with open("article.csv", 'r') as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)

        choose_article()


# Function to choose an choice from the list of choices
def choose_article():
    final_choice = choice(List_of_Choices)
    # Assignment of values to respective variables
    title = final_choice[0]
    author = final_choice[1]
    last_updated = final_choice[2]
    link = final_choice[3]
    category = final_choice[4]

    # Printing the values
    print("Let's read", "\'", title, "\" by", author)
    print()
    print()
    print()
    print("Title:", title)
    print()
    print("Author", author)
    print()
    print("Last Update", last_updated)
    print()
    print("Link: ", link)
    print()
    print("Category: ", category)


# Function to add dataset of jokes to the list of choices
def joke():
    with open("shortjokes.csv", 'r') as dataset:
        read_data = csv.reader(dataset)
        for row in read_data:
            List_of_Choices.append(row)

    choose_joke()


def choose_joke():
    final_choice = choice(List_of_Choices)
    # Assign the values to the respective variables
    joke = final_choice[1]

    # print the choice
    print("The Joke is..........", joke)
    print()


# MAIN
# USER CHOICE
user_choice = input("""
What do you want me to choose for you?
(a) an ANIME SERIES to watch
(b) a BOOK to read
(c) a CRYPTO CURRENCY to invest on
(d) a DOG for me
(e) an ELECTRIC VEHICLE to see
(f) a FOOD RECIPE to try
(g) a GAME to play
(h) a HABIT (Skill) to build
(i) an INSTAGRAM ACCOUNT to follow
(j) a JOKE to laugh
(k) a K-POP IDOL to know about
(m) a MOVIE to watch
(p) a PROGRAMMING LANGUAGE to learn
(q) a QUOTE for me
(s) a SONG to listen
(t) a TED TALK to watch
(w) a WEB ARTICLE to visit
(y) a YOUTUBE CHANNEL to watch

(MY) one of my custom choices

(exit) Nothing...
\n""")
print()
print()

# Decision
while True:
    if user_choice.lower() == 'm':
        movie()
        break

    elif user_choice.lower() == 'b':
        books()
        break

    elif user_choice.lower() == 's':
        songs()
        break

    elif user_choice.lower() == 'my':
        my_choices()
        break

    elif user_choice.lower() == 'a':
        anime()
        break

    elif user_choice.lower() == 'c':
        crypto()
        break

    elif user_choice.lower() == 'd':
        dog()
        break

    elif user_choice.lower() == 'e':
        ev()
        break

    elif user_choice.lower() == 'f':
        food_recipes()
        break

    elif user_choice.lower() == 'g':
        game()
        break

    elif user_choice.lower() == 'h':
        habit()
        break

    elif user_choice.lower() == 'i':
        instagram_profile()
        break

    elif user_choice.lower() == 'j':
        joke()
        break

    elif user_choice.lower() == 'k':
        kpop_idol()
        break

    elif user_choice.lower() == 'p':
        programming_language()
        break

    elif user_choice.lower() == 'q':
        quote()
        break

    elif user_choice.lower() == 't':
        ted()
        break

    elif user_choice.lower() == 'y':
        youtube()
        break

    elif user_choice.lower() == 'w':
        articles()
        break

    elif user_choice.lower() == 'exit':
        break

    else:
        print("Ummm... Invalid Input")
        break

print()
print("Thanks for using our application!!")
