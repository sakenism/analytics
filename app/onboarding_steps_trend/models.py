from datetime import datetime

from app import database


class OnboardingStepsTrend:
    toad_query = """
        select 
            count(*) as count
        from progress
        where
            "objectId"=198 AND attrs->>'status'='succeeded';
    """
    check_in_query = """
        select
            count(*) as count
        from progress
        where 
            "objectId"=3293 AND attrs->>'status'='succeeded';
    """
    adm_query = """
        select
            count(*) as count
        from progress
        where
            "objectId"=199 AND 'bestResultId' IS NOT NULL;
    """
    piscine_query = """
        select 
            count(*) as count
        from progress 
        where 
            "objectId"=26;
    """
    step_query = """
        select 
            count(*),
            month
        FROM (
        SELECT 
            to_char("createdAt" at time zone 'Asia/Almaty', 'YYYY-MM') AS month
            FROM 
                progress 
            WHERE "objectId" = %d
        ) AS progress
        GROUP BY 
            month
        ORDER BY 
            month
    """
    def __init__(self):
        pass
    
    def steps(self):
        toad_data = database.exec_sql(self.toad_query)
        check_in_data = database.exec_sql(self.check_in_query)
        adm_data = database.exec_sql(self.adm_query)
        piscine_data = database.exec_sql(self.piscine_query)
        data = [
            dict(step="toad", count=toad_data[0]["count"]),
            dict(step="check-in", count=check_in_data[0]["count"]),
            dict(step="adm", count=adm_data[0]["count"]),
            dict(step="piscine", count=piscine_data[0]["count"])
        ]
        return data
    
    def step(self, step_name):
        step_dict = {
            "toad": 198,
            "check-in": 3293,
            "adm": 199,
            "piscine": 26
        }
        return database.exec_sql(self.step_query % step_dict[step_name])


onboarding_steps_trend_model = OnboardingStepsTrend()
