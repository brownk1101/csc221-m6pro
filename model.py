import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer


def read_excel_file(filename):
    """
    reads information from an excel file into a dataframe
    :param filename: str: name of file to read
    :return: dictionary of pandas dataframe
    """

    try:
        df_dict = pd.read_excel(filename, sheet_name=None)
        return df_dict
    except FileNotFoundError:
        print(F"File not found: {filename}")
    except ValueError as ve:
        print(f"ValueError while reading Excel file: {ve}")


def add_airline_name(dataframes, foreign_key='IATA_CODE'):
    """
    merges two dataframes based on a foreign key
    :param dataframes: a dictionary of dataframes to merge the
    airline names
    :param foreign_key: the column name with the IATA_CODE for each
    airline
    :return: merged_dataframe: a new dataframe created from multiple
    dataframes
    """

    try:
        df1 = dataframes['Sheet1']
        df2 = dataframes['Airline Code Lookup']
        merged_dataframe = pd.merge(df1, df2, how="left", on=foreign_key)
        return merged_dataframe
    except KeyError as ke:
        print(f"Missing expected sheet: {ke}")
    except pd.errors.MergeError as me:
        print(f"Merge error: {me}")


def get_day_of_week(dataframe):
    """
    determines day of week based on date given. Adds it to the
    column named "day_of_week"
    :param dataframe: a pandas dataframe to add day of week two
    :return: updated_dataframe: an updated dataframe that now has
    the weekday included
    """

    try:
        # ensure date from dataframe is in usable form
        dataframe["date_created"] = pd.to_datetime(dataframe[
                                                       "date_created"])
        dataframe['day_of_week'] = dataframe["date_created"].dt.day_name()
        return dataframe
    except KeyError:
        print("'date_created' column not found in DataFrame.")
    except Exception as e:
        print(
            f"Error converting date to weekday: {type(e).__name__} - {e}")


def get_sentiment(dataframe):
    """
    Assigns sentiment labels to each row in the DataFrame based on text polarity.
    Adds a 'sentiment' column with values: positive, neutral, or negative.
    :param dataframe: Dataframe containing the review text
    :return: sentiment_df: new pandas dataframe that includes data
    for the sentiment column
    """

    try:
        from tqdm import tqdm
        tqdm.pandas()

        # get compound score for each row, show progress bar
        print("Analyzing text")
        dataframe['compound'] = dataframe['text'].progress_apply(
            compound_score)

        # assign sentiment based on compound score
        dataframe['sentiment'] = dataframe['compound'].apply(lambda score: (
            'positive' if score > 0 else
            'negative' if score < 0 else
            'neutral'
        ))

        # remove the compound column from final dataframe
        dataframe.drop(columns=['compound'], inplace=True)
        return dataframe
    except KeyError:
        print("'text' column not found in DataFrame.")
    except Exception as e:
        print(f"Sentiment analysis failed: {type(e).__name__} - {e}")


def compound_score(text):
    """
        Returns compound polarity score of a text using VADER.
        """
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)['compound']


def create_pivot(dataframe, groupby_cols, normalize=None,
                  include_percent=True):
    """
    creates a pivot table
    :param dataframes: parent dataframe
    :param groupby_cols: stre or list, column(s) to group by
    :param normalize:
        - None = no normalization (just counts)
        - 'index' = row-wise percentage (good for option 3, 5)
        - 'columns' = column-wise percentage (like option 4)
        - True = normalize whole table
    :param include_percent: Bool: if True and normalize is None,
    add percent column
    :return: DataFrame pivot table
    """

    try:
        # test is pivot is a flat summary
        if isinstance(groupby_cols, str):

            # count the number of rows in each group and turn it into a
            # table with a new column "Num_of_reviews"
            pivot = dataframe.groupby(groupby_cols).size().reset_index(
                name='Num_of_reviews')
            if include_percent:

                # calculate the percent and add new column for it
                total = pivot['Num_of_reviews'].sum()
                pivot['Percentage'] = pivot['Num_of_reviews'].apply(
                    lambda x: round((x/total) * 100, 2))
                return pivot

        # test is pivot is a matrix table
        elif isinstance(groupby_cols, list) and len(groupby_cols) == 2:

            # Use normalization if provided
            if normalize:
                pivot = pd.crosstab(
                    dataframe[groupby_cols[0]],
                    dataframe[groupby_cols[1]],
                    normalize=normalize) * 100
            else:
                pivot = pd.crosstab(
                    dataframe[groupby_cols[0]],
                    dataframe[groupby_cols[1]]
                )
            return pivot.reset_index()
        else:
            raise ValueError("groupby_cols must be a string or a list of "
                             "two strings")
    except KeyError as ke:
        print(f"KeyError in create_pivot(): {ke}")
    except ValueError as ve:
        print(f"ValueError in create_pivot(): {ve}")


def add_header(dataframe, headers=None):
    """
    Renames columns in a dataframe to improve user interface
    :param dataframe: dataframe whose columns are to be renames
    :param headers: list: lister of new headers
    :return: updated dataframe with improved headings
    """

    try:
        if len(headers) ++ len(dataframe.columns):
            dataframe.columns = headers
        return dataframe
    except TypeError:
        print("Header input must be a list matching the number of "
              "DataFrame columns.")
    except Exception as e:
        print(f"Error in add_header: {type(e).__name__} - {e}")

def prepare_final_df(df_dict):
    """
    handles preparing final dataframe by adding sentiment, airline
    name, and day of week
    :param df_dict: dictionary of dataframes
    :return: fully processed DataFrame
    """

    try:
        df = add_airline_name(df_dict)
        df = get_sentiment(df)
        df = get_day_of_week(df)
        return df
    except Exception as e:
        print(f"Failed to prepare final DataFrame:"
              f" {type(e).__name__} - {e}")


def format_percent_display(pivot_df, first_col_label="Label"):
    """
    Creates a string-formatted display table from a numeric pivot table.
    Adds % signs and returns a clean DataFrame for display only.

    :param pivot_df: DataFrame with numeric percentages
    :param first_col_label: Optional replacement label for the first
    column (e.g., 'Sentiment')
    :return: DataFrame with string-formatted percentages
    """

    try:
        display_df = pivot_df.copy()

        # Format all columns except the first
        for col in display_df.columns[1:]:
            display_df[col] = display_df[col].map(lambda x: f"{x:.2f}%")

        # Rename first column if needed
        headers = display_df.columns.tolist()
        headers[0] = first_col_label
        display_df.columns = headers

        return display_df
    except Exception as e:
        print(f"Error formatting percent display: {type(e).__name__} "
              f"- {e}")
