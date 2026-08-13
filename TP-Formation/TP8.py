#importation des modules
import plotly.express as px
import pandas as pd

#import des données
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

#calcul du ca
données['ca'] = données['prix'] * données['qte']

#création des graphs
figureproduit = px.pie(données, values='qte', names='produit', title='Ventes par produit')
figureca = px.pie(données, values='ca', names='produit', title='CA par produit')

#ajout des valeurs pour affichage
figureca.update_traces(textinfo='label+value+percent')

#génération des pages html
figureproduit.write_html('ventes-par-produit.html')
figureca.write_html('ventes-par-ca.html')

print('ventes-par-produit.html généré avec succès !')
print('ventes-par-ca.html généré avec succès !')