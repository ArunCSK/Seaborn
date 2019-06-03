import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def barplot():
    fig, ax = plt.subplots()
    titanic_df = pd.read_csv("titanic.csv")
    titanic = sns.barplot(titanic_df["sex"], titanic_df["survived"], data=titanic_df)
    plt.show()


def pointplot():
    fig, ax = plt.subplots()
    titanic_df = pd.read_csv("titanic.csv")
    titanic = sns.pointplot(titanic_df["sex"], titanic_df["survived"], data=titanic_df)
    plt.show()

def scatterplot():
    fig, ax = plt.subplots()
    titanic_df = pd.read_csv("tips.csv")
    titanic = sns.scatterplot(titanic_df["day"], titanic_df["total_bill"], data=titanic_df)
    plt.show()

def violin2():
    fig, ax = plt.subplots()
    titanic_df = pd.read_csv("iris.csv")
    titanic = sns.violinplot(titanic_df["species"], titanic_df["sepal_length"], data=titanic_df)
    plt.show()

def violin1():
    fig, ax = plt.subplots()
    titanic_df = pd.read_csv("tips.csv")
    titanic = sns.violinplot(titanic_df["sex"], titanic_df["total_bill"], data=titanic_df)
    plt.show()

def boxplot1():
    fig, ax = plt.subplots()
    titanic_df = pd.read_csv("gapminder-FiveYearData.csv")
    titanic = sns.boxplot(titanic_df["lifeExp"], titanic_df["continent"], data=titanic_df)
    plt.show()

def boxplot2():
    fig, ax = plt.subplots()
    titanic_df = pd.read_csv("tips.csv")
    titanic = sns.boxplot(titanic_df["day"], titanic_df["tip"], data=titanic_df)
    plt.show()

def swarmplot1():
    fig, ax = plt.subplots()
    titanic_df = pd.read_csv("gapminder-FiveYearData.csv")
    titanic = sns.swarmplot(titanic_df["lifeExp"], titanic_df["continent"], data=titanic_df)
    plt.show()

def swarmplot2():
    fig, ax = plt.subplots()
    titanic_df = pd.read_csv("tips.csv")
    titanic = sns.swarmplot(titanic_df["day"], titanic_df["tip"], data=titanic_df)
    plt.show()


io = input("Enter Options: 1.barplot: 2.pointplot: 3.scatterplot: 4.violin1: 5.violin2: 6.boxplot1: 7.boxplot2: 8.swarmplot1: 9.swarmplot2:")

if io == "barplot":
    barplot()
elif io == "pointplot":
    pointplot()
elif io == "scatterplot":
    scatterplot()
elif io == "violin2":
    violin2()
elif io == "violin1":
    violin1()
elif io == "boxplot1":
    boxplot1()
elif io == "boxplot2":
    boxplot2()
elif io == "swarmplot1":
    swarmplot1()
elif io == "swarmplot2":
    swarmplot2()
else:
    print()