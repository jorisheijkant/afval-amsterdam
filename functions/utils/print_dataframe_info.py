def print_dataframe_info(dataframe):
    print("-- Length of dataframe -- ")
    print(f"Dataframe has {len(dataframe)} rows")
    print("-- First rows --")
    print(dataframe.head())
    print("-- Dataframe columns --")
    print(dataframe.columns.tolist())


