# Python et Data Engineering
## 1. Data Pipeline
### Explication
Le code développé prend en compte quatre phases. Deux de ces quatre phases embarquent les deux autres. On se retrouve donc avec une première phase d’ingestion / normalisation, qui va récupérer la donné. Pour récupérer cette donnée, il va lire le fichier `config/config.yml` et intégré data par data un nombre de fichier défini dans le fichier de configuration en fonction des données disponible. Une fois qu’il a intégré tous les fichiers, il va pouvoir passer a la phase de normalisation, ou il va colonne par colonne faire les actions définit pour normaliser ces données. Une fois que ces deux phases sont faites, les données vont être sauvegardée en tant que fichiers pour être réutilisée dans les phase suivante. La phase de computing va suivre, en fonction de la donnée on va effectuer des calculs qui vont nous permettre de récupérer a la fin le dataset qui nous conviens. On terminera avec la quatrième phase qui elle va tout simplement ecrire la donnée en fonction des options mi dans le fichier de configuration.

### Lancement
1. Créer son environement virtuel
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

2. Installer les module nécessaires
    ```bash
    pip install -r requirements.txt
    ```

3. Lancer l'application
    ```bash
    python3 app.py
    ```
   
4. Le fichier de sortie sera disponible dans le fichier configuré dans le fichier de configuration, par defaut : `data/final/final_output.json`

## 2. Traitement ad-hoc

 ```bash
 python3 adhoc.py
 ```

## 3. Pour aller plus loin 
Dans un premier temps, le choix de l'infrastructure global devra être reconsidéré. Une simple exécution sur une machine virtuelle ne pourra pas assumer le lancement de ce code sur une grosse volumétrie de donnée.
Il faudra plutôt opter pour un cluster Hadoop en faisant le choix de stocker la donnée différemment. Le stockage devra etre différent car il faut changer le format de donnée (CSV, JSON) pour le format parquet, qui est un format typé, et stocker cette donnée sous HDFS (Hadoop Distribued File System).
Avec ces modifications, nous aurons toute la scalibilité et la flexibilité nécessaire pour traiter des grosses volumétries de données qui pourraient même augmenter dans le futur.
Une fois cette architecture mise en place, il faudra aussi mettre à jour la façon dont sont calculées nos données pour utiliser Hadoop Mapreduce, afin d'utiliser de la manière la plus optimisée l'architecture décrite auparavant.

# SQL

## 1. Donnée
**TRANSACTION**(date, order_id, client_id, prod_id, prod_price, prod_qty)  
**PRODUCT_NOMENCLATURE**(product_id, product_type, product_name)

## 2. Premiere partie du test
```sql
SELECT T.date AS date, SUM(T.prod_price*T.prod_qty) AS ventes
FROM transaction T
WHERE T.date BETWEEN '01/01/2019' AND '31/12/2019'
GROUP BY T.date
```

## 3. Seconde partie du test
```sql
SELECT T.client_id, 
       SUM(CASE WHEN PN.product_type = "DECO" THEN T.prod_price*T.prod_qty END) AS ventes_deco, 
       SUM(CASE WHEN PN.product_type = "MEUBLE" THEN T.prod_price*T.prod_qty END) AS ventes_meuble
FROM product_nomenclature PN, transaction T
WHERE PN.product_id = T.prod_id 
AND date BETWEEN '01/01/2019' AND '31/12/2019'
GROUP BY T.client_id
```



