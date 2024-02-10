import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

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
    # 1) Plot a line chart to show the average temperature fluctuations in Tunisia and Cameroon between 1980 till 2023. Interpret the results.
data_tunisia = data[(data["COUNTRY"] == "Tunisia")]
data_cameroon = data[(data["COUNTRY"] == "Cameroon")]

data_tunisia1 = data_tunisia[["TAVG", "DATE"]].groupby("DATE").mean().reset_index()
data_cameroon1 = data_cameroon[["TAVG", "DATE"]].groupby("DATE").mean().reset_index()

    # GRAPH
    # (1)
    # - Line Chart of Tunisia average temperature flunctuations (1980 - 2023)
plt.figure(figsize = (200, 70))
plt.plot(data_tunisia1["DATE"], data_tunisia1["TAVG"])
plt.xlabel("Dates", labelpad = 20, fontsize = 150)
plt.ylabel("Average Temperature", labelpad = 20, fontsize = 150)
plt.title("Analyzing the average temperature fluctuations in Tunisia (1980 - 2023)", fontsize = 150, pad = 20)
plt.show()

    # - Line Chart of Cameroon average temperature flunctuations (1980 - 2023)
plt.figure(figsize = (200, 70))
plt.plot(data_cameroon1["DATE"], data_cameroon1["TAVG"])
plt.xlabel("Dates", labelpad = 20, fontsize = 150)
plt.ylabel("Average Temperature", labelpad = 20, fontsize = 150)
plt.title("Analyzing the average temperature fluctuations in Cameroon (1980 - 2023)", fontsize = 150, pad = 20)
plt.show()



    # 2) Plot a line chart to show the average temperature fluctuations in Tunisia and Cameroon between 1980 till 2005. Interpret the results.
data_tunisia2 = data[(data["COUNTRY"] == "Tunisia") & (pd.to_datetime(data["DATE"]).dt.year <= 2005)]
data_cameroon2 = data[(data["COUNTRY"] == "Cameroon") & (pd.to_datetime(data["DATE"]).dt.year <= 2005)]

data_tunisia3 = data_tunisia2[["TAVG", "DATE"]].groupby("DATE").mean().reset_index()
data_cameroon3 = data_cameroon2[["TAVG", "DATE"]].groupby("DATE").mean().reset_index()

    # GRAPH
    # (1)
    # - Line Chart of Tunisia average temperature flunctuations (1980 - 2005)
plt.figure(figsize = (200, 70))
plt.plot(data_tunisia3["DATE"], data_tunisia3["TAVG"])
plt.xlabel("Dates", labelpad = 20, fontsize = 150)
plt.ylabel("Average Temperature", labelpad = 20, fontsize = 150)
plt.title("Analyzing the average temperature fluctuations in Tunisia (1980 - 2005)", fontsize = 150, pad = 20)
plt.show()

    # - Line Chart of Cameroon average temperature flunctuations (1980 - 2005)
plt.figure(figsize = (200, 70))
plt.plot(data_cameroon3["DATE"], data_cameroon3["TAVG"])
plt.xlabel("Dates", labelpad = 20, fontsize = 150)
plt.ylabel("Average Temperature", labelpad = 20, fontsize = 150)
plt.title("Analyzing the average temperature fluctuations in Cameroon (1980 - 2005)", fontsize = 150, pad = 20)
plt.show()



    # 3) Create Histograms to show temperature distribution in Senegal between [1980,2000] and [2000,2023] (in the same figure). Describe the obtained results.
data_senegal = data[(data["COUNTRY"] == "Senegal") & (pd.to_datetime(data["DATE"]).dt.year <= 2000)]
data_senegal1 = data_senegal[["TAVG", "TMAX", "TMIN", "DATE"]].groupby("DATE").mean().reset_index()

data_senegal2 = data[(data["COUNTRY"] == "Senegal") & (pd.to_datetime(data["DATE"]).dt.year >= 2000)]
data_senegal3 = data_senegal2[["TAVG", "TMAX", "TMIN", "DATE"]].groupby("DATE").mean().reset_index()

descriptive_statistics_senegal_1980to2000 = data_senegal1.describe()
descriptive_statistics_senegal_2000to2023 = data_senegal3.describe()

        # GRAPH
        # - Histogram of distribution of temperature in Senegal between (1980 & 2000) and (2000 & 2023)
plt.figure(figsize = (50, 20))
plt.subplot(231)
plt.title("Histogram of average temperature distribution in Senegal (1980 & 2000)")
plt.hist(x = data_senegal1["TAVG"], bins = 10,)
plt.xlabel("Bins", labelpad = 20)
plt.ylabel("Average Temperature", labelpad = 20)

plt.subplot(232)
plt.title("Histogram of maximum temperature distribution in Senegal (1980 & 2000)")
plt.hist(x = data_senegal1["TMAX"], bins = 10,)
plt.xlabel("Bins", labelpad = 20)
plt.ylabel("Maximum Temperature", labelpad = 20)

plt.subplot(233)
plt.title("Histogram of minimum temperature distribution in Senegal (1980 & 2000)")
plt.hist(x = data_senegal1["TMIN"], bins = 10,)
plt.xlabel("Bins", labelpad = 20)
plt.ylabel("Minimum Temperature", labelpad = 20)

plt.subplot(234)
plt.title("Histogram of average temperature distribution in Senegal (2000 & 2023)")
plt.hist(x = data_senegal3["TAVG"], bins = 10,)
plt.xlabel("Bins", labelpad = 20)
plt.ylabel("Average Temperature", labelpad = 20)

plt.subplot(235)
plt.title("Histogram of maximum temperature distribution in Senegal (2000 & 2023)")
plt.hist(x = data_senegal3["TMAX"], bins = 10,)
plt.xlabel("Bins", labelpad = 20)
plt.ylabel("Maximum Temperature", labelpad = 20)

plt.subplot(236)
plt.title("Histogram of minimum temperature distribution in Senegal (2000 & 2023)")
plt.hist(x = data_senegal3["TMIN"], bins = 10,)
plt.xlabel("Bins", labelpad = 20)
plt.ylabel("Minimum Temperature", labelpad = 20)

plt.tight_layout()
plt.show()

# # ----> YOUR TASK: Describe the results



    # 4) Select the best chart to show the Average temperature per country.
tunisia_data = data[data["COUNTRY"] == "Tunisia"]
senegal_data = data[data["COUNTRY"] == "Senegal"]
cameroon_data = data[data["COUNTRY"] == "Cameroon"]

grouped_tunisia = tunisia_data[["DATE", "TAVG"]].groupby("DATE").mean().reset_index()
grouped_senegal = senegal_data[["DATE", "TAVG"]].groupby("DATE").mean().reset_index()
grouped_cameroon = cameroon_data[["DATE", "TAVG"]].groupby("DATE").mean().reset_index()

        # GRAPH
plt.figure(figsize = (15, 10))
plt.plot(grouped_tunisia["DATE"], grouped_tunisia["TAVG"])
plt.plot(grouped_senegal["DATE"], grouped_senegal["TAVG"])
plt.plot(grouped_cameroon["DATE"], grouped_cameroon["TAVG"])
plt.show()