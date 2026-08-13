
import pandas as pd
dt = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

dt['ca'] = dt['prix'] * dt['qte']


camoy = dt.groupby('produit')['ca'].mean()
camed = dt.groupby('produit')['ca'].median()
volmoy = dt.groupby('produit')['qte'].mean()
volmed = dt.groupby('produit')['qte'].median()
volecat = dt.groupby('produit')['qte'].std()
volevar = dt.groupby('produit')['qte'].var()



print(f"""
6a1 - Moyenne du chiffre d’affaires par produit
     {camoy} 

     Moyenne duvolume des ventes par produit
     {volmoy}


6a2 - Mediannes du chiffre d’affaires par produit
    {camed}

    medianes du volume des ventes par produit :
     {volmed}


6b1 - l’écart-type pour le volume des ventes par produit
     {volecat}

6b2 - la variance pour le volume des ventes par produit
    {volevar}

""")

