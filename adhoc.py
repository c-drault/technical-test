from app.utils.custom_dataframe import CustomDataFrame
from pandas import Series
import yaml

if __name__ == '__main__':
    with open("config/config.yml") as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)

    dataframe = CustomDataFrame.create_df_from_file(
        conf["export"]["path"] + conf["export"]["name"] + "." + conf["export"]["extension"], "json")

    dataframe = dataframe[["drug", "journal"]].drop_duplicates().groupby("journal").count()
    dataframe["max_drug"] = int(dataframe.max().get("drug"))
    dataframe = dataframe[(dataframe.drug == dataframe.max_drug)]

    print(dataframe.arr)
