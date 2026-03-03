import sqlite3

from module24.main import connection, cursor


def create_conection():
    """Create a database connection"""
    connection =  sqlite3.connect("movie.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    """Create tables if they dont exist"""
    connection = create_conection()
    cursor = connection.cursor()
    cursor.execute("""
    Create Table IF DONT EXIST movies(
    id INTEGER PRIMARY KEY AUTOOINCREMENT
    tiitle TEXT NOT NULL,
    director TEXT NOT NULL
    """)
    connection.comit()
    connection.close()


    def create_movies(movie: MovieCreate) ->int:
        """
        ADDS a new movie to the database
        :param movie:
        Args:
        movie(MovieCreate)
        :return:
        int: The id of the new creatde movie
        :return:
        """
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("INSEWRT INTO movies (title , Director) vALUES(??)")
        return movie_id