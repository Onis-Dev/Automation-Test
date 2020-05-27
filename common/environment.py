import json

""" The content of this file is to read the constants file"""
CONSTANTS = {}
with open('./common/constants.json', 'r') as f:
    CONSTANTS = json.load(f)

PAGE_ELEMENTS = {}
with open('./common/aws_page_elements.json', 'r') as f:
    PAGE_ELEMENTS = json.load(f)