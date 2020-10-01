# (shebang incomplete) -> bin/???
import pandas as pd
## FILE TO STORE FUNCTIONS USED IN LAB_1





"------------------------------------------------------------------------------"
#############
## Imports ##
#############

## Python libraries
import pandas as pd
pd.set_option('display.max_columns', 100)

import re

import unicodedata





"------------------------------------------------------------------------------"
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
             res (int): number of variables in the data
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
            res (int): number of observations in the data

    """

    res = data.shape[0]

    print("Número de observaciones en los datos --> {}".format(res))

    return


## Counting number of unique observations for all variables
def count_unique_obs(data):
    """
    Counting number of unique observations for all variables
        args:
        data (dataframe): data that is being analyzed
        returns:
        (series): number of unique observations for all variables
    """
    return data.nunique()



def geo_transformation(data, variable_latlong, variable_drop):
    """
    Get the Latitude and Longitude columns from a specific column,
    then transform both columns to floats and finally remove the original column
        args:
            data (geodataframe): Original data with Geo Point column
            variable (string): Name of column with longitude and latitude data
            variable_drop (string): name of columns that will be dropped.
        returns:
            Geodataframe with columns longitude and latitude
    """

    data[['Latitud','Longitud']] = data.loc[:, variable_latlong].str.split(",", expand = True)
    data[['Latitud','Longitud']] = data[['Latitud','Longitud']].astype('float')
    data = data.drop(columns = [variable_latlong, variable_drop])

    return data


def count_type_vars(vars_sel, type_var):
    """
    Counting number of (numerical / categorical / text)  variables
        args:
            vars_sel (list): selection of columns that comply with the data type
            type_var (string): type of variable that is being counted
        returns:
            -
    """

    ## Creating dataframe to print selected variables
    vars_dict = {i:vars_sel[i-1] for i in range(1, len(vars_sel) + 1)}
    df_print_vars = pd.DataFrame.from_dict(vars_dict, orient="index")
    df_print_vars.columns = ["Variable(s)"]

    print("Número de variables de tipo {} --> {}".format(type_var, len(vars_sel)))
    # print("- Las variables de tipo {} son: \n".format(type_var, vars_sel))
    print(display(df_print_vars))


    return



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


## Data profiling for numeric variables
def data_profiling_numeric(data, num_vars):
    """
    Data profiling for numeric variables
        Args:
            data(dataframe): dataframe that will be analyzed.
        num_vars (list): list of variables' names in the dataframe that will be analyzed.
        Retruns:
            Dataframe with the data profiling (type, number of observations, mean, sd, quartiles, max, min, unique observations, top 5 repeated observations, number of null variables)
            of the choosen numeric variables.
    """

    ## Copy of initial dataframe to select only numerical columns
    dfx = data.loc[:, num_vars]


    ## Pipeline to create dataframe with general data description
    print("*********************************")
    print("** General description of data **")
    print("*********************************")

    #### List where the resulting dataframes will be stored for further concatenation
    res_dfs = []

    #### Type of numeric variables
    dfx_dtype = dfx.dtypes.to_frame().T
    dfx_dtype.index = ["dtype"]
    res_dfs.append(dfx_dtype)

    #### Counting unique variables
    dfx_uniqvars = dfx.nunique().to_frame().T
    dfx_uniqvars.index = ["count_unique"]
    res_dfs.append(dfx_uniqvars)

    #### Counting missing values
    dfx_missing = dfx.isnull().sum().to_frame().T
    dfx_missing.index = ["missing_v"]
    res_dfs.append(dfx_missing)

    #### General description of the data and addition of min values
    dfx_desc = dfx.describe()
    dfx_desc.loc["min", :] = dfx.min(axis=0)
    res_dfs.append(dfx_desc)

    #### Concatenating resulting dataframes into one final result
    print(display(pd.concat(res_dfs, axis=0)))
    print("-"*75)
    print("-"*75)
    print("\n\n".format())


    ## Pipeline to obtain top repeated variables per column
    print("****************************")
    print("** Top repeated variables **")
    print("****************************")

    #### Initial variables
    tops = 5 #### Number of tops that will be selected
    i = 0 #### Counter to start joining dataframes

    #### Loop through all variables that will be processed
    for col_sel in dfx:

        #### Creating dataframe with top entries and count
        dfxx = dfx[col_sel].value_counts().iloc[:tops].to_frame()
        dfxx.reset_index(drop=False, inplace=True)
        dfxx["part"] = round(dfxx[col_sel]/dfx[col_sel].count()*100, 2)
        dfxx.columns = pd.MultiIndex.from_tuples([(col_sel, tag) for tag in ["value", "count", "part_notnull"]])

        #### Joining all the variables in one final dataframe
        if i == 0:
            df_tops = dfxx
            i += 1
        else:
            df_tops = df_tops.join(dfxx)

    ## Fill empty spaces of resulting dataframe and renaming index entries
    df_tops.fillna("-", inplace=True)
    df_tops.index = ["top_" + str(i) for i in range(1, df_tops.shape[0] + 1)]
    print(display(df_tops))
    print("-"*75)
    print("-"*75)
    print()
    return


def convert_lower(data, vars_lower):
    """
     Converting observatios for selected columns into lowercase.
        args:
            data (dataframe): data that is being analyzed.
            vars_lower (list): list of the columns' names in the dataframe that will be changed to lowercase.
        returns:
            data(dataframe): dataframe that is being analyzed with the observations (of the selected columns) in lowercase.
    """
    for x in vars_lower:
        data[x]=data[x].str.lower()
    return data
