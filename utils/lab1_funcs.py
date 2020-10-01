# (shebang incomplete) -> bin/???

## FILE TO STORE FUNCTIONS USED IN LAB_1

##imports
import pandas as pd 


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
        returns:
        number of unique observations for all variables
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
            xxx
        returns:
            p (int): number of rows in data
    """

    p = len(vars_sel)

    print("Número de variables tipo {} --> {}".format(type_var,p))
    print("Las variables de tipo {} son: \n{}".format(type_var, vars_sel))

    return p


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
            -
        Retruns:
            -
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
    """
    for x in vars_lower:
        data[x]=data[x].str.lower()
    return data

 
 
def proporcion(listaVar,n):
    """
    Create the data profiling of categorical variables.
        args:
            listaVar (Serie): Serie with unique values of categorical variables
                               to get use value_counts() into a Serie 
            n (int): value of total observation of data set.
        returns:
           newList(list): List with name, count and proportion of each category.
    """
    newList = []
    for lis in listaVar.iteritems():
        newList.append([lis[0],lis[1],"{}%".format(round(100*(lis[1]/n),1))])
    return newList

   
 
 
def data_profiling_categ(data, cat_vars):
    """
    Create the data profiling of categorical variables.
        args:
            data (Data Frame): data set into Dataframe.
            cat_vars (list): list with categorical variables names.
        returns:
           display(): display the Dataframes with info.
    """
    
    for val in cat_vars:
        print("*********************************")
        print("Variable Categorica {}".format(val))
        print("*********************************")
        
        catego  = data[val].value_counts()
        totalOb = len(data[val])
        can_Cat = len(catego)
        moda    = data[val].mode().values[0]
        valFal  = data[val].isnull().sum()
        top1    = [catego[0:1].index[0],catego[0:1].values[0]] if can_Cat >= 1 else 0
        top2    = [catego[1:2].index[0],catego[1:2].values[0]] if can_Cat >= 2 else 0
        top3    = [catego[2:3].index[0],catego[2:3].values[0]] if can_Cat >= 3 else 0
        
        elemVarCat = { 
            "Info":val,
            "Num_Registros":[totalOb],
            "Num_de_categorias":[can_Cat],
            "Moda":[moda],
            "Valores_faltantes":[valFal],
            "Top1":[top1], 
            "Top2":[top2], 
            "Top3":[top3]
            }
        
        #primerdataframe
        df_catVar = pd.DataFrame(elemVarCat).set_index("Info").T
        
        #mostrar primer data frame
        print(display(df_catVar))
        
        print("Valores de las categorias y sus proporciones")
        #segundodataframe donde se muestra los valores de las categorias su cantidad y su proporción.
        pro = proporcion(catego,totalOb)
        dfProp = pd.DataFrame(pro,columns=['Categoría', 'Observaciones', 'proporción']).set_index("Categoría")
        #mostrar primer data frame
        print(display(dfProp))
        print("\n\n".format())
    return