# Random Movie Generator

A simple program for generating a random movie or TV show of a specific genre. Enter either movie or TV and then specify the genre, and the program will automatically generate a recommendation. 

## How it Works

The program uses an HTML web-scraper named Beautiful Soup to get the top movies or TV shows of the specified genre from IMDB. It then picks at random from this list.

The script initially only looks for hits with 10,000 IMDB votes or more. If the specified movie / TV show genre does not have any hits with this number of votes, the search is re-run with the number of necessary votes halved. 

If the user is not satisifed with the movie / TV show recommendation, they are prompted if they want to be supplied with another one. Responding "yes" or "y" re-runs the scrape, whereas responding "no" or "n" terminates the program.

## How to run the program

Download and run the executable (.exe) file, or if you have Jupyter Notebooks installed, you can run the ipynb file in your preferred development environment.

## Author

Thomas Lingard