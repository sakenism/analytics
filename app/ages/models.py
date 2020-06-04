from datetime import datetime

from app import database


class Ages:
    ages_query = """
        SELECT
            date_of_birth,
            gender,
            count (*)
        FROM (
            SELECT 
                substring(attrs->>'dateOfBirth', 1, 4)::INTEGER AS date_of_birth,
                CASE
                    WHEN (attrs ->> 'gender' in ('Male', 'Мужчина', 'Ер адам')) THEN 'Male'
                    WHEN (attrs ->> 'gender' in ('Female', 'Женщина', 'Әйел адам')) THEN 'Female'
                    ELSE 'Unknown'
                END AS gender
            FROM "user"
            WHERE 
                attrs->>'dateOfBirth' IS NOT NULL
            ) AS years
        WHERE
            years.date_of_birth > 1900 
        GROUP BY 
            date_of_birth, gender
        ORDER BY 
            date_of_birth;
    """
    def __init__(self):
        pass
    
    def ages(self):
        ages_data = database.exec_sql(self.ages_query)
        return ages_data


ages_model = Ages()
