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
