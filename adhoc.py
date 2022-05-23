from app.utils.custom_dataframe import CustomDataFrame
import yaml
import json
import pandas

if __name__ == '__main__':
    with open("config/config.yml") as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)

    with open(conf["export"]["path"] + conf["export"]["name"] + "." + conf["export"]["extension"]) as data_file:
        data = json.load(data_file)

    pubmed = pandas.json_normalize(data, record_path=['pubmed'], meta=["drug"])
    clinical_trials = pandas.json_normalize(data, record_path=['clinical_trials'], meta=["drug"])
    result = pandas.concat([pubmed, clinical_trials])
    result = result[["journal", "drug"]].drop_duplicates().groupby("journal", as_index=False).count()
    result["max_nb_drug"] = int(result.max().get("drug"))
    result = result[(result["drug"] == result["max_nb_drug"])]
    resultat = result["journal"]
    for index, value in resultat.items():
        print(f"'{value}' est un des {len(resultat)} 'journals' qui fait référence au plus de 'drugs'.")
