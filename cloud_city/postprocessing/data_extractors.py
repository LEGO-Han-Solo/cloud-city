import re

SET_NUM_REGEX_PRIMARY = r"\d{5}"
SET_NUM_REGEX_SECONDARY = r"\d{4}"


def extract_star_wars_set_num(string):
    match = re.findall(SET_NUM_REGEX_PRIMARY, string)
    if not match:
        match = re.findall(SET_NUM_REGEX_SECONDARY, string)
    if not match:
        raise ValueError(f'Unable to detect set number in string: {string}')
    return int(match[0])
