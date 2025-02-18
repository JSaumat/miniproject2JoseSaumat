### INF601 - Advanced Programming in Python
### Jose Saumat
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Creates the charts folder to hold the charts created by the program
os.makedirs("charts", exist_ok=True)



df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

df.to_excel("team.xlsx", sheet_name="passengers", index=False)

