# Python et Data Engineering
## 1. Data Pipeline
### Explication
Le code développé prend en compte 4 phases différentes. Sur ces 4 phases, deux sont liées et fonctionnent ensemble. Dans un premier temps, on retrouve donc la phase **d'ingestion**, on va pouvoir par ce biais, récupperer les données qui sont détaillées dans le fichier de configuration `config/config.yml` et les intégré dans le system. Une fois que ces données sont intégré, on passe directement a la phase de normalisation. Cette phase va permettre, principalement de renommer certaines colonne (ci besoin), normaliser la donné de certaines autres (comme pour les date). Une fois que ces deux phases sont fini, la donnée est écris dans un espace temporaire. La troisieme phase qui suit est celle du **computing**. Pour se faire on va associé a notre phase les regle définit a l'avance dans le code qui seront appliqué sur les données en entrée. On terminera par la quatrieme phase, qui est la phase d'ecriture, qui va ecrire la donnée calculé en fonctions des information que nous avons précisé dans le fichier de configuration.

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



