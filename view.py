import model
import seaborn as sns
import matplotlib.pyplot as plt


def display_menu():
    """
    Displays then user menu
    :return: None
    """
    print("\n\nMENU")
    print("-"*60)
    print("\n1)	Airline Summary and Chart",
"\n2)	Sentiment Summary and Chart",
"\n3)	Sentiment Per Airline Summary and Chart"
"\n4)	Overall Sentiment and Airline Summary and Chart",
"\n5)	Day and Sentiment Summary and Chart",
"\n6)	Exit\n\n")


def display_exit_message():
    """
    Displays the exit menu for program
    :return: None
    """
    sure = input("Are you sure you want to quit? (y or n):  \n")
    if sure.lower() == "y":
        print("\n\nExiting program")
    else:
        return 0


def display_data(pivot_table, headers):
    """
    displays data in tabular format
    :param pivot_table: data to display
    :param headers: list of header names
    :return: None
    """

    pivot_to_display = pivot_table.copy()
    pivot_to_display.columns = headers

    # format left aligned first column
    col_formats = []
    for i in range(len(headers)):

        # first column left aligned
        if i == 0:
            col_formats.append('{:<20}')

        # right align the rest of the columns
        else:
            col_formats.append('{:>25}')

    header_line = ''.join(col_formats[i].format(headers[i]) for i in range(len(headers)))
    print("\n" + header_line)
    print("-" * len(header_line))


    for _, row in pivot_to_display.iterrows():
        row_items = []
        for i, col in enumerate(pivot_to_display.columns):
            value = row[col]
            if 'percent' in col.lower() and isinstance(value,
                                                       (float, int)):
                value = f"{value:.2f}%"
            row_items.append(col_formats[i].format(value))
        print(''.join(row_items))





def plot_data(
        pivot_table,
        title,
        filename,
        xlabel=None,
        ylabel=None,
        is_grouped=False,
        percent_table=None):
    """
        displays information from the tweet dataFrame as a graph. Saves
    the plot as a png file.
    :param pivot_table: the specific information to plot from a
    :param title: str: title for the plot
    :param filename: str: name to save the file as
    :param xlabel: str: name for x axis
    :param ylabel: str: name for y axis
    :return: None
    """

    plt.figure(figsize=(10,6))

    # Plot for flat summary
    if not is_grouped:
        ax = sns.barplot(data=pivot_table, x=pivot_table.columns[0],
                         y=pivot_table.columns[1])

     # Add labels (value and percentage) on bars
        for bar, (_, row) in zip(ax.patches, pivot_table.iterrows()):
            value = bar.get_height()
            percent = row[pivot_table.columns[2]]
            label = f"{int(value)} ({percent:.2f}%)"
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                label,
                ha='center',
                va='bottom',
                fontsize=10
            )

    # Plot for matrix table
    else:
        if is_grouped:
            pivot_table.set_index(pivot_table.columns[0], inplace=True)
            colors = {
                'positive': '#2ca02c',
                'neutral': '#1f77b4',
                'negative': '#d62728'
            }
            bar_colors = [colors.get(col, '#333333') for col in
                          pivot_table.columns]
            ax = pivot_table.plot(kind='bar', figsize=(12, 10),
                                  width=0.9, color=bar_colors)

            # Add labels
            for bars_index, bar in enumerate(ax.patches):
                n_cols = len(pivot_table.columns)
                row_idx = bars_index // n_cols
                col_idx = bars_index % n_cols
                count = pivot_table.iloc[row_idx, col_idx]
                if percent_table is not None:
                    raw_count = int(
                        percent_table.iloc[row_idx, col_idx])
                    percent = float(pivot_table.iloc[row_idx, col_idx])
                    label = f"{percent:.1f}%\n ({raw_count})"
                else:
                    label = str(pivot_table.iloc[row_idx, col_idx])
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height(),
                    label,
                    ha='center',
                    va='bottom',
                    fontsize=8,
                )

    plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    plt.close()

def display_file_save_message(filename):
    """
    displays the file name for file created
    :param filename: str file name
    :return: None
    """

    print(f"\nPlot saved as {filename}")
