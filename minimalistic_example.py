import random
import kaggle_environments

ROCK = 0
PAPER = 1
SCISSORS = 2


def rock():
    return ROCK


def paper():
    return PAPER


def scissors():
    return SCISSORS


def dumb_agent():
    return random.randint(0, 2)


print(kaggle_environments.evaluate("rps", [dumb_agent, rock], configuration={"episodeSteps": 30}, debug=True))

