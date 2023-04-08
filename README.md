# kaggle-rps

https://www.kaggle.com/competitions/rock-paper-scissors/

# Jugadas
```python
ROCK = 0
PAPER = 1
SCISSORS = 2
```

# Agent description
Un agente es una función del siguiente estilo:
```python
def agent(observation: dict, configuration: dict) -> int:
    # Your code here
    sign = ROCK
    return sign
```
`observation` es un dict de la siguiente forma: `{'remainingOverageTime': 60, 'step': 0, 'reward': 0, 'lastOpponentAction': 0}`
Donde `step` indica cuántas manos se han jugado y `reward` indica la puntuación hasta el momento (nr. de manos ganadas - nr. de manos perdidas).
`lastOpponentAction` no existe en la primera jugada.

`configuration` es constante: 
```
{'episodeSteps': 30,
 'actTimeout': 1,
 'runTimeout': 1200,
 'signs': 3,
 'tieRewardThreshold': 20,
 'agentTimeout': 60}
```