import pandas as pd
import numpy as np



def get_cluster_df(df, index_list): 

    result = df.iloc[index_list]
    return result

