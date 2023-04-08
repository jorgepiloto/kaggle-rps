from datetime import datetime
from random import choice

def agent_datetime(observation, configuration):
    now = datetime.now()
    datesum = sum([now.year, now.month, now.second])
    return 0 if datesum % 2 == 0 else choice([0, 1])
