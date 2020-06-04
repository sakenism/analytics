from datetime import datetime

from app import database


class OnboardingSteps:
    toad_finished_query = """
        select 
            count(*) as count
        from progress
        where
            "objectId"=198 AND attrs->>'status'='succeeded' AND 
            "userId" NOT IN (select "userId" from progress where "objectId"=3293 AND attrs->>'status'='succeeded') AND
            "userId" NOT IN (select "userId" from progress where "objectId"=199 AND 'bestResultId' IS NOT NULL);
    """
    check_in_finished_query = """
        select
            count(*) as count
        from progress
        where 
            "objectId"=3293 AND attrs->>'status'='succeeded' AND 
            "userId" NOT IN (select "userId" from progress where "objectId"=199 AND 'bestResultId' IS NOT NULL) AND
            "userId" NOT IN (select "userId" from progress where "objectId"=26);
    """
    adm_finished_query = """
        select
            count(*) as count
        from progress
        where
            "objectId"=199 AND 'bestResultId' IS NOT NULL AND
	        "userId" NOT IN (select "userId" from progress where "objectId"=26);
    """
    piscine_finished_query = """
        select 
            count(*) as count
        from progress 
        where 
            "objectId"=26;
    """
    def __init__(self):
        pass
    
    def steps(self):
        toad_finished_data = database.exec_sql(self.toad_finished_query)
        check_in_finished_data = database.exec_sql(self.check_in_finished_query)
        adm_finished_data = database.exec_sql(self.adm_finished_query)
        piscine_finished_data = database.exec_sql(self.piscine_finished_query)
        data = [
            dict(step="toad", count=toad_finished_data[0]["count"]),
            dict(step="check-in", count=check_in_finished_data[0]["count"]),
            dict(step="adm", count=adm_finished_data[0]["count"]),
            dict(step="piscine", count=piscine_finished_data[0]["count"])
        ]
        return data


onboarding_steps_model = OnboardingSteps()
