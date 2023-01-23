import sqlite3


def get_title(query: str):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        result = []

        for item in connection.execute(query).fetchall():
                    result.append(dict(item))
        return result


def get_one(query: str):
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(query).fetchone()
        if result is None:
            return None
        else:
            return dict(result)


def get_movie_by_genre(type_movie, release_year, listed_in):
    query = f"""
    SELECT title, description
    FROM netflix
    WHERE "type"='{type_movie}'
    AND release_year = {release_year},
    AND listed_in LIKE '%{listed_in}%'
    """
    result = []

    for item in get_title(query):
        result.append({
                'title': item['title'],
                'description': item['description'],
                })
        return result


def search_by_cast(name1: str = "Jack Black", name2: str = "Dustin Hoffman"):
    query = f"""
            SELECT *
            FROM netflix
            WHERE netflix."cast" LIKE '%Jack Black%'
            AND netflix."cast" LIKE '%Dustin Hoffman%'
            """

    cast = []
    set_cast = set()
    result = get_title(query)

    for item in result:
        for actor in item['cast'].split(','):
                    cast.append(actor)

    for actor in cast:
        if cast.count(actor) > 2:
            set_cast.add(actor)

    return list(set_cast)
