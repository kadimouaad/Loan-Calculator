import math



def loan_interest_calculator(x):
    i = x / (12 * 100)
    return i


def converting_years(x):
    o = x / 12
    years = math.trunc(o)
    return years


def converting_months(x):
    o = x / 12
    o = o - int(o)
    m = math.ceil(o * 12)
    return m
