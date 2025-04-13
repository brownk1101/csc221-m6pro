import model
import view
import pandas as pd

def get_menu_option():
    """
    gets the menu option from the user and validates it
    :param length: length of the menu to use for validation
    :return: menu_option: number assigned to menu option
    """

    try:
        menu_option = 0
        while menu_option < 1 or menu_option > 6:
            menu_option = int(input("\nmenu option:  "))
            if 0 < menu_option < 7:
                return menu_option
            else:
                print("please select a number 1 through 6")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        exit(0)


def option_1(dataframe):
    """
    handles calling functions that correspond to menu option 1
    :param dataframe: pandas dataframe for the airline tweets
    :return: None
    """

    try:
        headers = ["Airline", "Number Of Reviews", "Percentage"]
        pivot = model.create_pivot(dataframe, 'AIRLINE NAME',
                           include_percent=True)
        new_header_pivot = model.add_header(pivot, headers)
        view.display_data(new_header_pivot, headers)
        view.plot_data(
            pivot_table=pivot,
            title="Total Airline Reviews",
            filename="airline_analysis.png",
            xlabel="Airline",
            ylabel="Number of Reviews"
        )

        view.display_file_save_message("airline_analysis.png")
    except (KeyError, ValueError, TypeError) as e:
        print(f" Error in Option 1: {type(e).__name__} - {e}")


def option_2(dataframe):
    """
    handles calling functions that correspond to menu option 2
    :param dataframe: pandas dataframe for the airline tweets
    :return: None
    """

    try:
        headers = ["Sentiment", "Number of Reviews", "Percentage"]
        pivot = model.create_pivot(dataframe, 'sentiment')
        new_header_pivot = model.add_header(pivot, headers)
        view.display_data(new_header_pivot, headers)
        view.plot_data(pivot_table=pivot,
                       title="Sentiment Analysis",
                       filename="sentiment_analysis.png",
                       xlabel="Sentiment",
                       ylabel="Number of Reviews")
        view.display_file_save_message("sentiment_analysis.png")
    except (KeyError, ValueError, TypeError) as e:
        print(f" Error in Option 2: {type(e).__name__} - {e}")


def option_3(dataframe):
    """
    handles calling functions that correspond to menu option 3
    :param dataframe: pandas dataframe for the airline tweets
    :return: None
    """

    try:
        headers = ["Airline", "Positive", "Neutral", "Negative"]
        pivot = model.create_pivot(
            dataframe,
            ['AIRLINE NAME','sentiment'],
            include_percent=False,
            normalize='index')
        percent_display = model.format_percent_display(pivot,
                                                       first_col_label="Airline")
        percent_display = model.add_header(percent_display, headers)
        view.display_data(percent_display, percent_display.columns.tolist())
        pie_data = pivot.set_index('AIRLINE NAME')
        view.plot_sentiment_pies(pie_data,
                                 "airline_senti.png",
                                 color_map={'positive': '#2ca02c',
                                            'negative': '#d62728',
                                            'neutral': '#7f7f7f'},
                                 legend_title="Sentiment",
                                 title="Percentage of Sentiment for Each"
                                       "Airline")
        view.display_file_save_message("airline_senti.png")
    except (KeyError, ValueError, TypeError) as e:
        print(f" Error in Option 3: {type(e).__name__} - {e}")


def option_4(dataframe):
    """
    handles calling functions that correspond to menu option 4
    :param dataframe: pandas dataframe for the airline tweets
    :return: None
    """

    try:
        percent_pivot = model.create_pivot(
            dataframe,
            ['sentiment', 'AIRLINE NAME'],
            include_percent=False,
            normalize='index'
        )
        raw_counts = model.create_pivot(
            dataframe,
            ['sentiment', 'AIRLINE NAME'],
            include_percent=False,
            normalize=None
        )
        # Format for display
        percent_display = model.format_percent_display(percent_pivot,
                                                     first_col_label="Sentiment")

        view.display_data(percent_display, percent_display.columns.tolist())

        # Transpose so airlines are on x-axis
        percent_transposed = percent_pivot.set_index(
            'sentiment').T.reset_index()
        percent_transposed.rename(columns={'index': 'Airline'},
                                  inplace=True)
        raw_transposed = raw_counts.set_index('sentiment').T.reset_index()
        raw_transposed.rename(columns={'index': 'Airline'}, inplace=True)

        # Plot
        pie_data = percent_pivot.set_index('sentiment')
        view.plot_sentiment_pies(pie_data,
                                 "senti_air_per.png",
                                 color_map={
                                     'american': '#1f77b4',
                                     'delta': '#ff7f0e',
                                     'southwest': '#2ca02c',
                                     'united': '#d62728',
                                     'us airways': '#9467bd',
                                     'virgin america': '#8c564b'
                                 },
                                 legend_title="Airline",
                                 title="Sentiments Per "
                                       "Airline Compared to Total "
                                       "Sentiments"
                                 )
        view.display_file_save_message("senti_air_per.png")
    except (KeyError, ValueError, TypeError) as e:
        print(f" Error in Option 4: {type(e).__name__} - {e}")

def option_5(dataframe):
    """
    handles calling functions that correspond to menu option 1
    :param dataframe: pandas dataframe for the airline tweets
    :return: None
    """
    try:
        # Create raw count pivot table
        pivot = model.create_pivot(
            dataframe,
            ['day_of_week', 'sentiment'],
            include_percent=False,
            normalize=None
        )
        ordered_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                        'Thursday', 'Friday', 'Saturday']
        pivot['day_of_week'] = pd.Categorical(pivot['day_of_week'],
                                              categories=ordered_days,
                                              ordered=True)
        pivot = pivot.sort_values('day_of_week')

        # Format and display the table
        headers = ["Day of Week", "Positive", "Neutral", "Negative"]
        pivot_display = model.add_header(pivot.copy(), headers)
        view.display_data(pivot_display, headers)

        # Plot grouped bar chart
        view.plot_grouped_bar_chart(
            pivot.set_index('day_of_week'),
            title="Number of Tweets by Sentiment and Day",
            filename="day_senti.png",
            xlabel="Day of Week",
            ylabel="Number of Tweets"
        )
        view.display_file_save_message("day_senti.png")
    except (KeyError, ValueError, TypeError) as e:
        print(f"Error in Option 5: {type(e).__name__} - {e}")





