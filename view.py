
import seaborn as sns
import matplotlib.pyplot as plt
import math
import pandas as pd


def display_menu():
    """
    Displays then user menu
    :return: None
    """
    print("\nMENU")
    print("-"*60)
    print("\n1)	Airline Summary and Chart",
"\n2)	Sentiment Summary and Chart",
"\n3)	Sentiment Per Airline Summary and Chart"
"\n4)	Overall Sentiment and Airline Summary and Chart",
"\n5)	Day and Sentiment Summary and Chart",
"\n6)	Exit\n")


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

    try:
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
    except (ValueError, IndexError, KeyError) as e:
        print(f"Error displaying data: {type(e).__name__} - {e}")


def plot_data(
        pivot_table,
        title,
        filename,
        xlabel=None,
        ylabel=None):
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

    try:
        plt.figure(figsize=(10,6))

        # Plot for flat summary
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
        plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        plt.tight_layout()
        plt.savefig(filename)
        plt.show()
        plt.close()
    except (KeyError, IndexError, TypeError, ValueError) as e:
        print(f"Error creating bar plot: {type(e).__name__} - {e}")

def display_file_save_message(filename):
    """
    displays the file name for file created
    :param filename: str file name
    :return: None
    """

    print(f"\nPlot saved as {filename}")


def plot_sentiment_pies(pivot_table, filename, color_map=None,
                        legend_title="", title=""):
    """
    Creates a single image with pie charts

    :param pivot_table: DataFrame with sentiments as rows, airlines as columns
    :param filename: Output filename for the combined image
    """
    try:
        pivot_table.index = pivot_table.index.astype(str)
        num_pies = len(pivot_table)

        # Arrange pies in a grid instead of a row
        cols = math.ceil(math.sqrt(num_pies))
        rows = math.ceil(num_pies / cols)
        fig, axes = plt.subplots(rows, cols, figsize=(6 * cols, 6 * rows))
        axes = axes.flatten()
        shared_labels = None
        shared_wedges = None
        for i, (label, row) in enumerate(pivot_table.iterrows()):
            values = [float(v) for v in row.values if is_number(v)]
            labels = [k for k, v in zip(row.index, row.values) if
                      is_number(v)]
            colors = [color_map.get(label.lower(), '#cccccc') for label
                      in labels] if color_map else None
            wedges, texts, autotexts = axes[i].pie(
                values,
                labels=None,
                colors=colors,
                autopct='%1.1f%%',
                startangle=140
            )
            axes[i].set_title(str(label), fontsize=14)
            if shared_labels is None:
                shared_labels = labels
                shared_wedges = wedges
        for j in range(i + 1, len(axes)):
            axes[j].axis('off')

        # Show shared legend
        fig.legend(
            shared_wedges,
            shared_labels,
            title=legend_title,
            loc="lower center",
            bbox_to_anchor=(0.5, 0.0),
            ncol=len(shared_labels)
        )
        plt.suptitle(title, fontsize=18)
        plt.tight_layout(
            rect=[0, 0.1, 1, 0.95])
        plt.savefig(filename)
        plt.show()
        plt.close()
    except (KeyError, ValueError, IndexError, TypeError) as e:
        print(
            f"Error in plot_sentiment_pies: {type(e).__name__} - {e}")


def is_number(x):
    """
    Helper to check if value is numeric
    :param x:
    :return:boolean, True is numeric, false if not
    """
    try:
        float(x)
        return True
    except ValueError:
        return False

def plot_grouped_bar_chart(pivot_table,
                           title,
                           filename,
                           xlabel=None,
                           ylabel=None):
    try:
        plt.figure(figsize=(10, 6))
        ax = pivot_table.plot(kind='bar', width=0.75)

        # Add labels above each bar
        for bar in ax.patches:
            height = bar.get_height()
            if pd.notnull(height) and height > 0:
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    height,
                    f"{int(height)}",
                    ha='center',
                    va='bottom',
                    fontsize=9
                )
        ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(filename)
        plt.show()
        plt.close()
    except Exception as e:
        print(f"Error in grouped bar chart: {type(e).__name__} - {e}")