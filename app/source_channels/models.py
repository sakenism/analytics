from datetime import datetime

from app import database


class SourceChannels:
    source_channels_query = """
        SELECT 
            count(*),
            source
        FROM (
            SELECT
                CASE
                    WHEN (attrs ->> 'source' in ('Friends', 'Достардан', 'От друзей')) THEN 'Friends'
                    WHEN (attrs ->> 'source' in ('News', 'Новости', 'Жаңалықтар')) THEN 'News'
                    WHEN (attrs ->> 'source' in ('Others', 'Басқа', 'Другое')) THEN 'Others'
                    WHEN (attrs ->> 'source' in ('Google, Yandex, etc.')) THEN 'Search Engines'
                    WHEN (attrs ->> 'source' in ('Instagram, Facebook, VK, etc.')) THEN 'Social Media'
                    ELSE 'Unknown'
                END AS source
            FROM "user" 
            ) AS a
        GROUP BY source
        ORDER BY source;
    """
    def __init__(self):
        pass
    
    def source_channels(self):
        source_channels_data = database.exec_sql(self.source_channels_query)
        return source_channels_data


source_channels_model = SourceChannels()
