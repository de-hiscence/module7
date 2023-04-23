import mysql.connector
from mysql.connector import errorcode

try:
    db = mysql.connector.connect(user= "root",
                                password= "M1krokosmos!2223",
                                host= "localhost",
                                database= "movies",
                                raise_on_warnings= True
                            )
    print("\n Database user {} connected to MySQL on host {} with database {}".format("root","localhost","movies"))

    input("\n\n Press any key to continue...")
   
    # Studio records
    print("-- DISPLAYING Studio RECORDS --")
    cursor = db.cursor()
    cursor.execute ("SELECT studio_id, studio_name FROM studio") 
    studios = cursor.fetchall()
    for studio_id, studio_name in studios:
        print ('\n Studio ID: {}\n Studio Name: {}\n'.format(studio_id, studio_name))
    cursor.close()

    # Genre records
    print("-- DISPLAYING Genre RECORDS --")
    cursor = db.cursor()
    cursor.execute ("SELECT genre_id, genre_name FROM genre") 
    genres = cursor.fetchall()
    for genre_id, genre_name in genres:
        print('\n Genre ID: {}\n Genre Name: {}'.format(genre_id, genre_name))
    cursor.close()

    # Short film records
    print("-- DISPLAYING Short Film RECORDS --")
    cursor = db.cursor()
    cursor.execute ("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120") 
    films = cursor.fetchall()
    for film_name, film_runtime in films:
        print('\n Film Name: {}\n Film Runtime: {}'.format(film_name, film_runtime))
    cursor.close()

    # Director records
    print("-- DISPLAYING Director RECORDS --")
    cursor = db.cursor()
    cursor.execute ("SELECT film_name, film_director FROM film ORDER BY film_director") 
    films = cursor.fetchall()
    for film_name, film_director in films:
        print('\n Film Name: {}\n Film Runtime: {}'.format(film_name, film_director))
    cursor.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

db.close()
