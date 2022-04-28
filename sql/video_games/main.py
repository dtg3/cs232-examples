"""
Main application for running queries against the video game database
"""
# Third-party imports
from dotenv import load_dotenv

# Custom application imports
from vg_db import VideoGameDatabase
import init_db as InitDB

load_dotenv()


def main():
    """
    Main function to run the application
    """

    # Optional second parameter can be set to True to force initialization
    #   whether the database exists or not. Essentially rebuilds the database
    #   from scratch.
    InitDB.initialize_database('vgsales.csv')

    vg_database = VideoGameDatabase()

    vg_database.top_k_sales(10)
    vg_database.count_games_in_genre()
    vg_database.count_games_in_genre("Racing")
    vg_database.total_global_sales_per_platform()
    vg_database.total_global_sales_per_platform(year=2016)
    vg_database.total_global_sales_per_platform("NES")
    vg_database.total_global_sales_per_platform("N64", 1998)
    vg_database.number_of_games_per_year_by_publisher("Nintendo")
    vg_database.number_of_games_per_year_by_publisher("THQ")

    vg_database.close()


if __name__ == "__main__":
    main()
