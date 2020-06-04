from datetime import datetime

from app import database


class Registrations:
    per_month_query = """
        SELECT 
            count(a.id) as count,
            month,
            gender
        FROM (
            SELECT 
                id,
                to_char("createdAt" at time zone 'Asia/Almaty', 'YYYY-MM') AS month,
                CASE
                    WHEN (attrs ->> 'gender' in ('Male', 'Мужчина', 'Ер адам')) THEN 'Male'
                    WHEN (attrs ->> 'gender' in ('Female', 'Женщина', 'Әйел адам')) THEN 'Female'
                    ELSE 'Unknown'
                END AS gender
            FROM "user" 
            ) AS a
        GROUP BY month, gender ORDER BY month;
    """
    per_day_query = """
        SELECT 
            count(a.id) as count,
            day,
            gender
        FROM (
            SELECT 
                id,
                to_char("createdAt" at time zone 'Asia/Almaty', 'YYYY-MM-DD') AS day,
                CASE
                    WHEN (attrs ->> 'gender' in ('Male', 'Мужчина', 'Ер адам')) THEN 'Male'
                    WHEN (attrs ->> 'gender' in ('Female', 'Женщина', 'Әйел адам')) THEN 'Female'
                    ELSE 'Unknown'
                END AS gender
            FROM "user" 
            WHERE 
                "createdAt" >= '%s' AND 
                "createdAt" <= '%s'
            ) AS a
        GROUP BY day, gender ORDER BY day;
    """
    def __init__(self):
        pass
    
    def monthly(self):
        per_week_data = database.exec_sql(self.per_month_query)
        return per_week_data
    
    def daily(self, start: str, end: str):
        return database.exec_sql(self.per_day_query % (start, end))

registration_model = Registrations()
