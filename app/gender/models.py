from datetime import datetime

from app import database


class Gender:
    gender_query = """
        SELECT 
            count(*),
            gender
        FROM (
            SELECT
                CASE
                    WHEN (attrs ->> 'gender' in ('Male', 'Мужчина', 'Ер адам')) THEN 'Male'
                    WHEN (attrs ->> 'gender' in ('Female', 'Женщина', 'Әйел адам')) THEN 'Female'
                    ELSE 'Unknown'
                END AS gender
            FROM "user" 
            ) AS a
        GROUP BY gender
        ORDER BY gender;
    """
    def __init__(self):
        pass
    
    def gender(self):
        gender_data = database.exec_sql(self.gender_query)
        return gender_data


gender_model = Gender()
