# (shebang incomplete) -> bin/???

## FILE TO STORE FUNCTIONS USED IN LAB_1


## Counting number of variables in data (¿Cuántas variables tenemos?)
def count_vars(data):
    """
    Counting number of variables in data
        args:
            data (dataframe): data that is being analyzed
        returns:
            res (int): number of columns in data
    """

    res = data.shape[1]

    return res



## Counting number of observations in data (¿Cuántas observaciones tenemos?)
def count_obs(data):
    """
    Counting number of observations in data
        args:
            data (dataframe): data that is being analyzed
        returns:
            res (int): number of rows in data
    """

    res = df.shape[0]

    return res
