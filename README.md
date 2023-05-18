# Auto-Choice
This code is a random choice generator that allows users to make a random selection from various datasets. The program utilizes CSV files containing different categories of choices such as movies, anime, cryptocurrency, dog breeds, books, songs, electric vehicles, food recipes, games, habits, Instagram profiles, programming languages, K-pop idols, and quotes.

## Dependencies
The following modules are imported in the code:

random.choice: used to randomly select an element from a list
csv: used to read data from CSV files

## Usage
Make sure to have the necessary CSV files in the same directory as the code file.
Run the code and follow the prompts to select a category and make a random choice.

## Categories
The available categories for random selection are:

Movies
Anime series
Cryptocurrencies
Dog breeds
Books
Songs
Electric vehicles
Food recipes
Games
Habits
Instagram profiles
Programming languages
K-pop idols
Quotes

## Adding Choices
To add additional choices to a category, simply add the corresponding data to the respective CSV file in the appropriate format. The code will automatically read the data from the CSV files and include them in the list of choices for each category.

Note: The CSV files should follow the specific format expected by the code. Please refer to the existing CSV files for reference.

Example
Here is an example usage of the code:
```
# Importing necessary modules
from random import choice
import csv

# Take input to append the list of choices
List_of_Choices = []

# Definition of Functions
# ...

# Choose any of the given choices
def my_choices():
    user_in = int(input("How many choices do you have? \n"))

    for i in range(user_in):
        choice = input("Enter the choice: ")
        List_of_Choices.append(choice)

# Choose a movie from the given choices
def choose_movie():
    final_choice = choice(List_of_Choices)
    # Storing the items of the list to respective variables
    # ...

# ...

# Main program
category = input("Choose a category:\n"
                 "1. Movies\n"
                 "2. Anime\n"
                 "3. Cryptocurrency\n"
                 "...")

if category == "1":
    movie()
elif category == "2":
    anime()
elif category == "3":
    crypto()
```

In this example, the user is prompted to choose a category (e.g., "Movies"). Based on the selection, the corresponding function is called to generate a random choice from the available options in that category.

## Prerequisites
Before running the code, ensure that you have the following:

- Python installed on your system (version 3.x)
- CSV files for each category of choices in the same directory as the code file.
## How to Use
Clone or download the repository to your local machine.
Make sure that the required CSV files are present in the same directory as the code file.
Open the code file (random_choice_generator.py) in a text editor or integrated development environment (IDE).
Run the code in a Python environment.

## Functionality
The code consists of several functions, each corresponding to a specific category of choices. Here's a brief description of each function:

- movie(): Opens the movie dataset and appends the choices to the list. Calls the choose_movie() function to select a random movie choice.
- anime(): Opens the anime dataset and appends the choices to the list. Calls the choose_anime() function to select a random anime series choice.
- crypto(): Opens the cryptocurrency dataset and appends the choices to the list. Calls the choose_crypto() function to select a random cryptocurrency choice.
- dog(): Opens the dog breeds dataset and appends the choices to the list. Calls the choose_dog() function to select a random dog breed choice.
- books(): Opens the book dataset and appends the choices to the list. Calls the choose_book() function to select a random book choice.
- songs(): Opens the song dataset and appends the choices to the list. Calls the choose_song() function to select a random song choice.
- ev(): Opens the electric vehicle dataset and appends the choices to the list. Calls the choose_ev() function to select a random electric vehicle choice.
- food_recipes(): Opens the food recipes dataset and appends the choices to the list. Calls the choose_food() function to select a random food recipe choice.
- game(): Opens the games dataset and appends the choices to the list. Calls the choose_game() function to select a random game choice.
- habit(): Opens the skills dataset and appends the choices to the list. Calls the choose_habit() function to select a random habit choice.
- instagram_profile(): Opens the Instagram profiles dataset and appends the choices to the list. Calls the choose_profile() function to select a random profile choice.
`programming

## Welcome Contributors!
We are excited to invite you to contribute to our GitHub project. Your contribution will help us enhance the functionality and improve the overall quality of our project. Whether you are an experienced developer or just starting your journey in coding, we welcome your ideas, suggestions, and code contributions.

### How to Contribute
To get started, follow these simple steps:

- <b>Fork the Repository:</b> Start by forking our project repository to your own GitHub account. This will create a copy of the project that you can freely modify and experiment with.
- <b>Clone the Repository:</b> Once you have forked the repository, clone it to your local machine using the following command:
```
git clone https://github.com/sayampradhan/repository.git
```
- <b>Create a New Branch:</b> Before making any changes, create a new branch to work on. This helps in isolating your changes from the main codebase. Use the following command to create a new branch:
```
git checkout -b my-feature
```
- <b>Make your Changes:</b> Now you can make the desired changes to the codebase. Feel free to add new features, fix bugs, improve documentation, or optimize existing code.

- <b>Commit your Changes:</b> Once you have made your changes, commit them with a descriptive commit message. This helps in tracking the changes and understanding the purpose of each commit. Use the following commands to commit your changes:
```
git add .
git commit -m "Add a brief description of your changes"
```
- <b>Push your Changes:</b> After committing your changes, push them to your forked repository on GitHub. This will make your changes available for review and inclusion in the project. Use the following command to push your changes:
```
git push origin my-feature
```
- <b>Submit a Pull Request:</b> Finally, navigate to the original repository on GitHub and submit a pull request. Provide a clear and concise description of your changes, along with any relevant information that may assist in the review process. Our team will review your contribution and provide feedback or merge it into the main codebase.

### Guidelines and Recommendations
- Make sure to follow coding standards and best practices.
- Keep your changes focused and specific to the purpose of your contribution.
- Write clear and concise commit messages.
- Test your changes thoroughly before submitting a pull request.
- Be open to feedback and willing to collaborate with the project maintainers.
______
Thank you for considering contributing to our project! Your participation is valuable to us, and we look forward to your contributions. If you have any questions or need assistance, feel free to reach out to us. Happy coding!
