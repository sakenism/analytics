from datetime import datetime

from app import database


class Audits:
    per_week_query = """
        SELECT 
            count(a.id) as count,
            a.week as week,
            a.grade as grade
        FROM (
            SELECT 
                id,
                to_char("updatedAt" at time zone 'Asia/Almaty', 'YYYY-IW') AS week,
                CASE
                    WHEN (grade < 1) THEN 0
                    WHEN (grade >= 1) THEN 1
                END AS grade
            FROM audit 
            WHERE 
                grade IS NOT NULL
            ) AS a
        GROUP BY week, grade ORDER BY week;
    """
    per_day_query = """
        SELECT 
            count(a.id) as count,
            a.day as day,
            a.grade as grade
        FROM (
            SELECT 
                id,
                to_char("updatedAt" at time zone 'Asia/Almaty', 'ID') AS day,
                CASE
                    WHEN (grade < 1) THEN 0
                    WHEN (grade >= 1) THEN 1
                END AS grade
            FROM audit 
            WHERE 
                grade IS NOT NULL AND
                "updatedAt" >= '%s' AND 
                "updatedAt" <= '%s'
            ) AS a
        GROUP BY day, grade ORDER BY day;
    """
    def __init__(self):
        pass
    
    def weekly(self):
        per_week_data = database.exec_sql(self.per_week_query)
        for i in range(len(per_week_data)):
            per_week_data[i]['last_day'] = datetime.strptime(per_week_data[i]['week']+"-7", "%G-%V-%u")
        return per_week_data
    
    def daily(self, start: str, end: str):
        return database.exec_sql(self.per_day_query % (start, end))

audit_model = Audits()
