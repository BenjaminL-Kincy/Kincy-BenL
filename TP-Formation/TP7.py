import csv


ventes_par_produit = {}


with open("ventes.csv", "r") as csvfile:
    datas = csv.DictReader(csvfile, delimiter=",")
    for row in datas:
        produit = row['produit']
        qte = int(row['qte'])
        ventes_par_produit[produit] = ventes_par_produit.get(produit, 0) + qte
        
maxp = max(ventes_par_produit, key=ventes_par_produit.get)
minp = min(ventes_par_produit, key=ventes_par_produit.get)

print(f"""
--> Ventes par produit   
{ventes_par_produit}

--> Produit le plus vendu
{maxp} pour {ventes_par_produit[maxp]} ventes

--> Produit le moins vendu
{minp} pour {ventes_par_produit[minp]} ventes

""")

