import pandas as pd

data = pd.read_csv('../dataset/Survey.csv', na_values='n/a')

data.fillna('no', inplace=True)

noValues = ["no", "No", "N/A", "NA", "NaN", "n/a", "None", "none", "none used for course"]


def clean_f(item):
    if item in noValues:
        return "Did not use"
    return item


def clean_no(item):
    if item in noValues:
        return "No"
    return item


def clean_grade(item):
    if item in "B":
        return 85
    return item


def clean_hrrange(item):
    if item in "10-20 hours":
        return 15
    if item in "25 - 35":
        return 30
    if item in "40-50 hours":
        return 45
    if item in "15-20":
        return 18
    if item in "12+":
        return 12
    return item


data["What kind of AI Model did you use?"] = data["What kind of AI Model did you use?"].apply(clean_f)

data.loc[data["Was AI available when you took OOD?"] == "No", "What kind of AI Model did you use?"] = "Did not use"
data.loc[data["Was AI available when you took OOD?"] == "No", (f"How much have you used / are "
                                                               "you using AI in OOD if at all?\n")] = 0
data.loc[data["Was AI available when you took OOD?"] == "No", (f"If you use/used AI, do you believe that it"
                                                               f" benefits/benefitted your academic performance? ")]\
    = "Did not use"
data.loc[data["Was AI available when you took OOD?"] == "No", ("How do you use AI to assist your work if you use them?"
                                                               " (Select one that you use the most)")] = "Did not use"

data["If you use/used AI, do you believe that it benefits/benefitted your academic performance? "] \
    = (data[f"If you use/used AI, do you believe that it benefits/benefitted your academic performance? "]
       .apply(clean_no))
data[f"What was/is your grade from OOD? (0-100)"] = \
    (data[f"What was/is your grade from OOD? (0-100)"].apply(clean_grade))
data["How many hours did you spend on OOD per week?"] = (data["How many hours did you spend on OOD per week?"]
                                                         .apply(clean_hrrange))

data.to_csv('../dataset/CleanedSurvey.csv', index=False)
