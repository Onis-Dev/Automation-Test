import json

CONSTANTS = {}
with open('./common/constants.json', 'r') as f:
    CONSTANTS = json.load(f)
    print(CONSTANTS)