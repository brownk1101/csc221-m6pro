"""
GeneralPseudocode:
Take a dataset containing airlines and tweet reviews of those
airlines and determine if they are positive, negative, or neutral.
Then create a program that has the following menu:
1)	Airline Summary and Chart
2)	Sentiment Summary and Chart
3)	Sentiment Per Airline Summary and Chart
4)	Overall Sentiment and Airline Summary and Chart
5)	Day and Sentiment Summary and Chart
6)	Exit
Option 1 does the following:
Displays in a tabular format the number of reviews for each airline,
percentage(out of grand total) of review for each airline. Then plots
the results.
Option2 does the following:
display, in a tabular format, the number of positive, negative,
neutral reviews, and the percentage of each for entire dataset. Then
plots
the results
Option 3
narrows down to the airline and displays the percentage of
each sentiment for each airline. It then plots the results.
Option 4
Find the airline with highest percentage of negative comments and the
highest percentage of positive comments. Display in a tabular format
the percentage an airline got out of the total amount of negative
reviews, positive reviews, then neutral revies. Plot the results.
Option 5
Summarizes the data by day of the week. The number of each sentiment
for each day of the week. Plot the results
Option 6
Exits the program

Detailed pseudocode

Read data from Tweets.xlsx, sheet 1, into a Pandas DataFrame.
Add three additional columns: sentiment, airline_name, and day_of_week
use nltk package to determine if the data in each row under the "text"
column is positive, negative, or neutral. Assign it with the
corresponding string
Use the foreign key IATA_CODE to match the code with the airline name
Extract the date from the date_created column and use datetime
library to determine the day of the week it corresponds to. Add this
day to the day_of_the week column for the corresponding row

Display the menu
Option 1
create a pivot table that shows the number of reviews for each
airline, percentage (out of all) for number of reviews per airline.
Using seaborn, plot the results.
Options 2, 3, 4, and 5 are to do the same as option 1 except the
data pivoted will change based on the description noted in the general
pseudocode

"""

import view
import controller
import model
import pandas as pd

def main():

    dfs = model.read_excel_file("Tweets(1).xlsx")
    df = model.prepare_final_df(dfs)
    df.to_csv('final_tweets.csv')
    view.display_menu()
    menu_option = 0
    while menu_option != 6:
        menu_option = controller.get_menu_option()
        if menu_option == 1:
            controller.option_1(df)
        elif menu_option == 2:
            controller.option_2(df)
        elif menu_option == 3:
            controller.option_3(df)
        elif menu_option == 4:
            controller.option_4(df)
        elif menu_option == 5:
            controller.option_5(df)
        else:
            if view.display_exit_message() is not None:
                menu_option = 0


if __name__ == "__main__":
    main()