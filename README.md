# csc221-m6pro
airline review

M6Pro Text Analysis and Plotting

1. Open the "Tweets" excel sheet. This file contains randomly selected tweets for a list of airlines, you’ll notice when looking at the date that all tweets were posted in Feb 2015. Go over the content and the variables it contains and see that you understand what each variable/column in the excel sheet references.
Now Prepping the dataset….
This dataset is clean so you will not need to evaluate columns or check for duplicated rows. Not everyone knows all the IATA_CODEs so we will want to add the airline name instead. More on that in Part 1 below  
Part 1 (40 points)
2 . Open the "Tweets" Excel and complete the tasks below
If you go over the Tweet sheet, you will notice that the “IATA_CODE” field contains airline codes. Also notice that there’s another sheet in the Excel that is titled “Airline Code Lookup”, this sheet contains two columns. The first column is the IATA_CODE and the second is the airline name.
 So what we will do the following:
1.	Create a DataFrame that references all the content in “Sheet1” 
2.	The DataFrame is to have Three  additional columns(Variables):
i.	A “sentiment” column. You will have to determine if the review was either positive , negative or neutral, the review is reference under the “text” column. (15 points)
i.	Use either nltk or textblob.
ii.	Only one of three words is to added under the “sentiment” column for each row (Overall analysis for the review).

ii.	AN  “airline_name” column. You might have guessed but this column is referenced the airline name for the “IATA_CODE” referenced in each row.(10 points)

 For instance, row 2 has an IATA_CODE of “VX” therefore the value under the “airline_name” column should be “Virgin America”

iii.	A “day_of_Week” column. This column is to reference the name of the day the review was posted. How? .(10 points)
i.	You will have to extract that information from the value referenced under the “date_created” column.
ii.	Choose an ai platform of your choice and check how to use the “datetime” library to extract the name of the day from a date. 

So for instance for row 2, the date is “2/24/2015”. If properly read , “Tuesday” should be referenced under the “day_of_week” column for row 2.
Important : Instructions on how to add a column to a DataFrame based on a condition , required for the three columns requested above, see the link below
https://www.dataquest.io/blog/tutorial-add-column-pandas-dataframe-based-on-if-else-condition/

Part2 Make the program menu driven(10 pionts)
After creating the DataFrame , the program is to display the following menu
1)	Airline Summary and Chart
2)	Sentiment Summary and Chart
3)	Sentiment Per Airline Summary and Chart
4)	Overall Sentiment and Airline Summary and Chart
5)	Day and Sentiment Summary and Chart
6)	Exit

Part 3 Summarizing (Pivot) and Charts (40 points)
For menu option 1 (Airline Summary and Chart) 
What we want to do here is evaluate the airline_name variable.
You will need to create to summarize the data under this field. Note we did go over summarizing or creating pivots for variables in module 2 (you did it in the titanic project)
When this option is chosen, the program is to display the following :
•	Number of reviews for each airline
•	Percentage ,out of grand total , of review for each airline. 
•	Display information in a tabular format (suggested header row , “Airline_name, Num_of_reveiws, Percentage”)
•	Plot the results , save the plot as “airline_analysis.png”
For menu option 2 (Sentiment Summary and Chart)

Evaluate the sentiment variable. You will summarize again but this time for the sentiment variable.

When this option is chosen, the program is to display the following :
•	Number of reviews for each sentiment (positive, negative, neutral)
•	Percentage ,out of grand total , of review for each sentiment. 
•	Display information in a tabular format (suggested header row , “Sentiment Num_of_reveiws, Percentage”)
•	Plot the results , save the plot as “sentiment_analysis.png”

For menu option 3 (Sentiment Per Airline Summary and Chart)

Percentage of sentiment for each Airline: Here You will summarize again, but this time for two variables (airline_name and sentiment)
When this option is chosen, the program is to display the following :
•	Percentage of each sentiment (positive, neutral and negative )out of total review  for each airline. 
•	Display information in a tabular format (suggested header row , “Airline_name, positive, neutral and negative”)
•	Plot the results , save the plot as “airline_senti.png”

For menu option 4 (Overall Sentiment and Airline Summary and Chart)

Sentiment Percentage out of grand total: The airline_name and sentiment variables again only here, we want to know which airline got the highest percentage of negative, and/or positive sentiments. So the percentage will be out of total of sentiments (whether that’s positive, neutral or negative).
When this option is chosen, the program is to display the following :
•	Percentage of each sentiment (positive, neutral and negative )out of total of similar reviews (for instance percentage of negative reviews out of all negative reviews in dataframe). 
•	Display information in a tabular format (suggested header row , “Airline_name, positive, neutral and negative”)
•	Plot the results , save the plot as “senti_air_per.png”

For menu option 5 (Day and Sentiment Summary and Chart)

Summarize “day_of_week” .and “sentiment”
When this option is chosen, the program is to display the following :
•	Number of each sentiment (positive, neutral and negative ) for each day of the week. 
•	Display information in a tabular format (suggested header row , “day_of_week, positive, neutral and negative”)
•	Plot the results , save the plot as “day_senti.png”


Part 4 (10 points) 
Now it’s time to benefit from what we did and answer some questions. 
Use the analysis you did above to answer the questions below. Answer to the questions should be added in a word document , name the document “M6_analysis_lastFirstname” (replace lastFristname with your actual name)

(1)	Which airline had the highest Number of Tweets? What percent of the total is that? 
(2)	Which airline got the highest number of negative tweets? What percentage was that for the total number of tweets posted for that airline 
(3)	Which airline got the highest number of positive tweets? What percentage was that for the total number of tweets posted for that airline 
(4)	What airline got the highest percentage of negative tweets? What percent of the total number of negative tweets was that?
(5)	What are some interesting finds you got from the analysis you preformed on the Day and airline_sentiment analysis? List two


Submission : After you have completed all the work requested above you should have the following
•	The original tweets excel
•	5 png images
•	A word document listing answers to questions listed in Part 4 of this document



