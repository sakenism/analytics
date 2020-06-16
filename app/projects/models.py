from datetime import datetime

from app import database


class Projects:
    project_query = """
        SELECT
            count (*),
            name
        FROM (
            SELECT
                "userId",
                obj.name AS name,
                obj.id AS obj_id
            FROM progress prog
            JOIN "object" obj ON obj.id = prog."objectId"
            WHERE 
                obj."type" = 'project' AND
                obj.attrs ->> 'exerciseType' = '%s'
        ) AS p
        GROUP BY name, obj_id
        ORDER BY obj_id
    """
    def __init__(self):
        pass
    
    def projects(self, project_type):
        data = database.exec_sql(self.project_query % project_type)
        return data



projects_model = Projects()
