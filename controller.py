import model
import view
import pandas as pd


def get_menu_option():
    """
    gets the menu option from the user and validates it
    :param length: length of the menu to use for validation
    :return: menu_option: number assigned to menu option
    """

    menu_option = 0
    while menu_option < 1 or menu_option > 6:
        menu_option = int(input("\nmenu option:  "))
        if 0 < menu_option < 7:
            return menu_option
        else:
            print("please select a number 1 through 6")


def option_1(dataframe):
    """
    handles calling functions that correspond to menu option 1
    :param dataframe: pandas dataframe for the airline tweets
    :return: None
    """

    headers = ["Airline", "Number Of Reviews", "Percentage"]
    pivot = model.create_pivot(dataframe, 'AIRLINE NAME',
                       include_percent=True)
    new_header_pivot = model.add_header(pivot, headers)
    view.display_data(new_header_pivot, headers)
    view.plot_data(
        pivot_table=pivot,
        title="Airline Review Share",
        filename="airline_analysis.png",
        xlabel="Airline",
        ylabel="Number of Reviews"
    )

    view.display_file_save_message("airline_analysis.png")


def option_2(dataframe):
    """
    handles calling functions that correspond to menu option 2
    :param dataframe: pandas dataframe for the airline tweets
    :return: None
    """

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

def option_3(dataframe):
    """
    handles calling functions that correspond to menu option 3
    :param dataframe: pandas dataframe for the airline tweets
    :return: None
    """

    headers = ["Airline", "Positive", "Neutral", "Negative"]
    pivot = model.create_pivot(
        dataframe,
        ['AIRLINE NAME','sentiment'],
        include_percent=False,
        normalize='Index')

    # calculate percentages for plotting labels
    percentages = pivot.select_dtypes(include='number')
    percentages = percentages.div(percentages.sum(axis=1), axis=0) * 100

    # combine counts and percentages for display
    percent_display = percentages.map(lambda x: f"{x:.2f}%")
    display_table = pivot.select_dtypes(include='number').astype(
        int).astype(str) + " (" + percent_display + ")"

    # Add airline name back to table display
    display_table.insert(0, 'Airline', pivot[pivot.columns[0]].values)
    view.display_data(display_table, headers)
    view.plot_data(pivot_table=pivot,
                   title="Sentiment Analysis",
                   filename="airline_senti.png",
                   xlabel="Airline",
                   ylabel="Percentage",
                   is_grouped=True,
                   percent_table=percentages)
    view.display_file_save_message("airline_senti.png")


def option_4(dataframe):
    """
    handles calling functions that correspond to menu option 4
    :param dataframe: pandas dataframe for the airline tweets
    :return: None
    """

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
    view.plot_data(
        pivot_table=percent_transposed,
        title="Percentage of Sentiments by Airline",
        filename="senti_air_per.png",
        xlabel="Airline",
        ylabel="Percentage",
        is_grouped=True,
        percent_table=raw_transposed.iloc[:, 1:]
    )
    view.display_file_save_message("senti_air_per.png")

def option_5(dataframe):
    """
    handles calling functions that correspond to menu option 1
    :param dataframe: pandas dataframe for the airline tweets
    :return: None
    """





