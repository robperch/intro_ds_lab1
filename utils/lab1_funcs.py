# (shebang incomplete) -> bin/???

## FILE TO STORE FUNCTIONS USED IN LAB_1





"------------------------------------------------------------------------------------"
#############
## Imports ##
#############

import sys

import pandas as pd

import re

import unicodedata





"------------------------------------------------------------------------------------"
###############
## Functions ##
###############



## Counting number of variables in data (¿Cuántas variables tenemos?)
def count_vars(data):
    """
    Counting number of variables in data
        args:
            data (dataframe): data that is being analyzed
        returns:
            -
    """

    res = data.shape[1]
    print("Número de variables en los datos --> {}".format(res))

    return



## Counting number of observations in data (¿Cuántas observaciones tenemos?)
def count_obs(data):
    """
    Counting number of observations in data
        args:
            data (dataframe): data that is being analyzed
        returns:
            -
    """

    res = data.shape[0]

    print("Número de observaciones en los datos --> {}".format(res))

    return



## Counting number of numeric variables
def count_num_vars(vars_num):
    """
    Counting number of numeric variables
        args:
            vars_num (list): selection of columns that comply with the data type
        returns:
            -
    """

    print("Número de variables numéricas --> {}".format(len(vars_num)))
    print("Las variables numéricas son: \n{}".format(vars_num))

    return



def geo_transformation(data, variable):
    """
    Get the Latitude and Longitude columns from a specific column,
    then transform both columns to floats and finally remove the original column
        args:
            data (geodataframe): Original data with Geo Point column
            variable (string): Name of column with longitude and latitude data
        returns:
            Geodataframe with columns longitude and latitude
    """

    data[['Latitud','Longitud']] = data.loc[:,variable].str.split(",", expand = True)
    data[['Latitud','Longitud']] = data[['Latitud','Longitud']].astype('float')
    data = data.drop(columns = [variable, "Geo Shape"])

    return data



## Transform columns' names to standard format
def clean_col_names(dataframe):
    """
    Transform columns' names to standard format (lowercase, no spaces, no points)
        args:
            dataframe (dataframe): df whose columns will be formatted.
        returns:
            dataframe (dataframe): df with columns cleaned.
    """

    ## Definition of cleaning funcitons that will be applied to the columns' names
    fun1 = lambda x: x.lower() ## convert to lowercase
    fun2 = lambda x: re.sub("( |¡|!|¿|\?|\.|,|;|:)", "_", x) ## eliminate spaces and punctuation signs for underscore
    fun3 = lambda x: unicodedata.normalize("NFD", x).encode("ascii", "ignore").decode("utf-8") ## substitute accents for normal letters
    funcs = [fun1, fun2, fun3]

    ## Applying the defined functions to the columns' names
    for fun in funcs:
        dataframe.columns = [fun(col) for col in dataframe.columns]

    return dataframe
