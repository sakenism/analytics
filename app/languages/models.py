from datetime import datetime

from app import database


class Languages:
    languages_query = """
        SELECT 
            count(*),
            language
        FROM (
            SELECT
                attrs ->> 'language' AS language
            FROM "user" 
            ) AS a
        GROUP BY language
        ORDER BY language;
    """
    def __init__(self):
        pass
    
    def languages(self):
        languages_data = database.exec_sql(self.languages_query)
        return languages_data


languages_model = Languages()
