import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("Africa_climate_change.csv")
data = pd.read_csv("Africa_climate_change.csv")

# Exploratory Data Analysis
data.info()
data_head = data.head()
data_tail = data.tail()
data_descriptive_statistic = data.describe()
data_more_desc_statistic = data.describe(include = "all")
data_mode = data.mode()
data_distinct_count = data.nunique()
data_correlation_matrix = data.corr() 
data_null_count = data.isnull().sum()
data_total_null_count = data.isnull().sum().sum()
data_hist = data.hist(figsize = (15, 10), bins = 10)

# Data Cleaning and Transformation
    # - Fix Date Column
data["DATE"] = pd.to_datetime(data["DATE"]).dt.date

# Data Analysis
    # 1) Plot a line chart to show the average temperature fluctuations in Tunisia and Cameroon. Interpret the results.
data_tunisia = data[(data["COUNTRY"] == "Tunisia")]
data_cameroon = data[(data["COUNTRY"] == "Cameroon")]

data_tunisia1 = data_tunisia[["TAVG", "DATE"]].groupby("DATE").mean().reset_index()
data_cameroon1 = data_cameroon[["TAVG", "DATE"]].groupby("DATE").mean().reset_index()

#     # GRAPH
#     # - Line Chart of Tunisia average temperature flunctuations
# plt.figure(figsize = (200, 70))
# plt.plot(data_tunisia1["DATE"], data_tunisia1["TAVG"])
# plt.xlabel("Dates", labelpad = 20)
# plt.ylabel("Average Temperature", labelpad = 20)
# plt.title("Analyzing the average temperature fluctuations in Tunisia")
# plt.show()

#     # - Line Chart of Cameroon average temperatur flunctuations
# plt.figure(figsize = (200, 70))
# plt.plot(data_cameroon1["DATE"], data_cameroon1["TAVG"])
# plt.xlabel("Dates", labelpad = 20)
# plt.ylabel("Average Temperature", labelpad = 20)
# plt.title("Analyzing the average temperature fluctuations in Cameroon")
# plt.show()
