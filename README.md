# twitch-scrape
A set of python scripts made to help scrape twitch for available usernames. 

I made this project because I wanted a cool sounding username on twitch that was a normal word. The project uses selenium to validate twitch usernames. It can either test combinations of letters or names from a file. I used it to find my new username [webinar](https://www.twitch.tv/webinar).

In the project I have a couple of files that should be run through command line.

twitch_name_combinations.py [starting point (optional)][number of characters (optional)] 
*tests all random combinations of letters. you can specify a word for it to start out and it will continue interating from there down the alphabet. you can also specify the length of the combinations. the program will only except the first arguement given.*

twitch_name_file.py [file path]
*this file tests all of the words in the file. words should be on seperate lines in the file.*

parse_file [input file] [output file (optional)] [length (optional)]
*parse file allows the user to go through a list of words and filter out all words that aren't a specific length/made up of valid twitch username characters. If the length is not specified, the script will default to 4 characters long.*

Contact me with any questions at nicolaesanderberg@gmail.com
