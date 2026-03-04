import pandas as pd
import numpy as np

data = {
    "names": ["Lisa", "Katie", "Tom", "Jack", "Samantha", "Amanda"],
    "sex": ["Female", "Female", "Male", "Male", "Female", "Female"],
    "cabin_class": [1, 2, 2, 1, 1, 1],
    "hasSurvived": [False, False, True, True, True, False],
    "destination": ["Arkansas", "Alabama", "Arkansas", 
                    "Alabama", "Arkansas", "Alabama"],
    "payed_price": [72.5, 15.0, 20.3, 80.0, 65.4, 90.0]
}

df = pd.DataFrame(data)

filtered_df = 
df[(df['sex'] == "Female") & 
(df['cabin_class'] == 1) & 
(df['hasSurvived'] == False)]
print(filtered_df['names'])

destination_df = df["destination"]
avg_price = np.mean((df['destination'] == "Alabama"))
