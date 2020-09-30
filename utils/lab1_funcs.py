# (shebang incomplete) -> bin/???

## FILE TO STORE FUNCTIONS USED IN LAB_1


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
            res (int): number of rows in data
    """

    print("Número de variables numéricas --> {}".format(len(vars_num)))
    print("Las variables numéricas son: \n{}".format(vars_num))

    return

## Counting number of unique observations for all variables
def count_unique_obs(data):
    """
    Counting number of unique observations for all variables
        args:
        data (dataframe): data that is being analyzed
           
    """
    return data.nunique()



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