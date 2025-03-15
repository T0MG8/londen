import pandas as pd
import json
import plotly.express as px
import streamlit as st

# Data over bezoekers metro en soorten metro's
bez_2007 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2007_Entry_Exit.csv", dtype=str, low_memory=False)
bez_2008 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2008_Entry_Exit.csv", dtype=str, low_memory=False)
bez_2009 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2009_Entry_Exit.csv", dtype=str, low_memory=False)
bez_2010 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2010_Entry_Exit.csv", dtype=str, low_memory=False)
bez_2011 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2011_Entry_Exit.csv", dtype=str, low_memory=False)
bez_2012 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2012_Entry_Exit.csv", dtype=str, low_memory=False)
bez_2013 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2013_Entry_Exit.csv", dtype=str, low_memory=False)
bez_2014 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2014_Entry_Exit.csv", dtype=str, low_memory=False)
bez_2015 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2015_Entry_Exit.csv", dtype=str, low_memory=False)
bez_2016 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2016_Entry_Exit.csv", dtype=str, low_memory=False)
bez_2017 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2017_Entry_Exit.csv", dtype=str, low_memory=False)

link_station1 = r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\London stations.JSON"
with open(link_station1, "r", encoding="utf-8") as a:
    data = json.load(a)
features = data["features"]
station1 = pd.json_normalize(features, sep="_")

link_train_lines = r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\London Train Lines.JSON"
with open(link_train_lines, "r", encoding="utf-8") as b:
    data = json.load(b)
features = data["features"]
train_lines = pd.json_normalize(features, sep="_")

link_station2 = r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\stations.JSON"
with open(link_train_lines, "r", encoding="utf-8") as c:
    data = json.load(c)
features = data["features"]
station2 = pd.json_normalize(features, sep="_")


# Data over het weer
weer = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Weer data\weather_london.csv", dtype=str, low_memory=False)


# Data over het gebruik van fietsen
#2021 Q2
fiets_2021_Q2_central = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2021 Q2 spring (Apr-Jun)-Central.csv", dtype=str, low_memory=False)
fiets_2021_Q2_inner = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2021 Q2 spring (Apr-Jun)-Inner.csv", dtype=str, low_memory=False)
fiets_2021_Q2_outer = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2021 Q2 spring (Apr-Jun)-Central.csv", dtype=str, low_memory=False)
#2021 Q3
fiets_2021_Q3_central = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2021 Q3 (Jul-Sep)-Central.csv", dtype=str, low_memory=False)
#2021 Q4
fiets_2021_Q4_central = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2021 Q4 autumn (Oct-Dec)-Central.csv", dtype=str, low_memory=False)
fiets_2021_Q4_cycleways = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2021 Q4 autumn (Oct-Dec)-Cycleways.csv", dtype=str, low_memory=False)
#2022 W1
fiets_2022_w1_central = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2022 w1 spring-Central.csv", dtype=str, low_memory=False)
fiets_2022_w1_cycleways = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2022 w1 spring-Cycleways.csv", dtype=str, low_memory=False)
fiets_2022_w1_inner_1 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2022 w1 spring-Inner-Part1.csv", dtype=str, low_memory=False)
fiets_2022_w1_inner_2 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2022 w1 spring-Inner-Part2.csv", dtype=str, low_memory=False)
fiets_2022_w1_outer = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2022 w1 spring-Outer.csv", dtype=str, low_memory=False)
#2022 W2
fiets_2022_w2_cycleways = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2022 w2 autumn-Cycleways.csv", dtype=str, low_memory=False)
#2023 W1
fiets_2023_w1_central = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2023 w1 spring-Central.csv", dtype=str, low_memory=False)
fiets_2023_w1_cycleways = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2023 w1 spring-Cycleways.csv", dtype=str, low_memory=False)
fiets_2023_w1_inner_1 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2023 w1 spring-Inner-Part1.csv", dtype=str, low_memory=False)
fiets_2023_w1_inner_2 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2023 w1 spring-Inner-Part2.csv", dtype=str, low_memory=False)
fiets_2023_w1_outer = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2023 w1 spring-Outer.csv", dtype=str, low_memory=False)
#2023 W2
fiets_2023_w2_cycleways = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2023 W2 autumn-Cycleways.csv", dtype=str, low_memory=False)
#2024 W1
fiets_2024_w1_central = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2024 w1 spring-Central.csv", dtype=str, low_memory=False)
fiets_2024_w1_cycleways = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2024 w1 spring-Cycleways.csv", dtype=str, low_memory=False)
fiets_2024_w1_inner_1 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2024 w1 spring-Inner-Part1.csv", dtype=str, low_memory=False)
fiets_2024_w1_inner_2 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2024 w1 spring-Inner-Part2.csv", dtype=str, low_memory=False)
fiets_2024_w1_outer = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2024 w1 spring-Outer.csv", dtype=str, low_memory=False)
#2024 W2
fiets_2024_w2_cycleways = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\fiets data\2024 W2 autumn-Cycleways.csv", dtype=str, low_memory=False)