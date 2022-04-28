# Python library imports
import os

# Third-party imports
import mysql.connector


class VideoGameDatabase:
    """
    VideoGameDatabase class to connct and run queries about
    video game data against the database
    """

    def __init__(self):
        """
        Initialization of a VideoGameDatabase class and members
        """
        self.db_connection = mysql.connector.connect(
            host=os.getenv("DBHOST"),
            user=os.getenv("DBUSERNAME"),
            password=os.getenv("DBPASSWORD"),
            database=os.getenv("DATABASE")
        )
        self.mycursor = self.db_connection.cursor(dictionary=True)


    def top_k_sales(self, k):
        """
        Function to display the top k selling games

        :param k: integer representing the top k to display
        """

        print(f"QUERY TOP {k} SALES:")
        query = """
            SELECT g.game_name, s.global_sales
            FROM game_sales s
                INNER JOIN game g
                ON s.game_id = g.game_id
            ORDER BY s.global_sales DESC
            LIMIT %s;
        """
        self.mycursor.execute(query, (k,))
        for item in self.mycursor.fetchall():
            print(item)
        
        print()
    

    def count_games_in_genre(self, genre_name=None):
        """
        Function to display the count of games in a given genre.
        The genre is optional and defaults to displaying the count
        of all game genres.

        :param genre_name: string representation of the genre name
        """

        print(f'COUNT GAMES{" IN THE " + genre_name.upper() + " GENRE" if genre_name else ""}:')
        query = f"""
            SELECT ge.genre_name, COUNT(*) count
            FROM game_sales s
                INNER JOIN game g
                ON s.game_id = g.game_id
                INNER JOIN genre ge
                on g.genre_id = ge.genre_id
            WHERE ge.genre_name {"IS NOT NULL" if not genre_name else "= %s"}
            GROUP BY ge.genre_name
            ORDER BY count DESC;
            """
        if not genre_name:
            self.mycursor.execute(query)
        else:
            self.mycursor.execute(query, (genre_name,))

        for item in self.mycursor.fetchall():
            print(item)
        
        print()


    def total_global_sales_per_platform(self, platform=None, year=None):
        """
        Function to display global sales per game platform

        :param platform: optional platform name
        :param year: optional year 
        """

        # Over engineered code to display a context sensitive string
        #   representing the data being displayed.
        platform_string = f'{" FOR " + platform if platform else "" }'
        year_string = f'{" IN THE YEAR " + str(year) if year else "" }'
        print(f"GLOBAL SALES{platform_string}{year_string}:")
        
        
        # Composing format strings to build a SQL query. Again, overengineered :)
        year_clause = f'g.release_year {"IS NOT NULL" if not year else "= %s"}'
        platform_clause = f'p.platform_name {"IS NOT NULL" if not platform else "= %s"}'
        full_query = f"""
            SELECT p.platform_name, ROUND(SUM(s.global_sales), 2) all_global_sales
            FROM game_sales s
                INNER JOIN game g
                ON s.game_id = g.game_id
                INNER JOIN platform p
                on p.platform_id = g.platform_id
            WHERE {year_clause} AND {platform_clause}
            GROUP BY p.platform_name
            ORDER BY p.platform_name;
        """

        values = []

        if year:
            values.append(year)
        if platform:
            values.append(platform)

        if values:
            self.mycursor.execute(full_query, tuple(values))
        else:
            self.mycursor.execute(full_query)

        for item in self.mycursor.fetchall():
            print(item)

        print()

    def number_of_games_per_year_by_publisher(self, publisher):
        """
        Function to display the number of games per year by a publisher

        :param publisher: publisher name used to find matching games
        """
        print(f"GAMES RELEASED BY {publisher.upper()}")
        query = f"""
            SELECT g.release_year, COUNT(*) game_releases
            FROM game_sales s
                INNER JOIN game g
                ON s.game_id = g.game_id
                INNER JOIN publisher p
                on p.publisher_id = g.publisher_id
            WHERE g.release_year IS NOT NULL and p.publisher_name {"IS NOT NULL" if not publisher else "= %s"}
            GROUP BY g.release_year;
        """

        if publisher:
            self.mycursor.execute(query, (publisher,))
        else:
            self.mycursor.execute(query)

        for item in self.mycursor.fetchall():
            print(item)
        
        print()


    def close(self):
        """
        Function to clean up the database cursor and connection
        """
        
        self.mycursor.close()
        self.db_connection.close()
    