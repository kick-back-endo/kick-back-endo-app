"""
Symptoms to check (mvp):
* bleeding for more than 7 days
* 80% or more medium or heavy
* pain for more than 4 days

"""


def symptom_checker(df):

    long_pain = True if df['Cramps'].mean() > 4 else False

    heavy_periods_ratio = (df['Medium'] + df['Heavy'])/df['Day']

    heavy_period = True if heavy_periods_ratio.mean() > 0.8 else False

    long_period = True if df['Day'].mean() >= 7 else False

    if (long_pain and heavy_period) or long_period:
        return True
    else:
        return False
