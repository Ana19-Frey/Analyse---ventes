import pandas as pd
import matplotlib.pyplot as plt

# --- Création de données ---
data = {
    "Produit": ["Pomme", "Banane", "Orange", "Mangue", "Fraise"],
    "Quantité": [120, 90, 50, 80, 30],
    "Prix_unitaire": [100, 50, 25, 50, 500],
}

# --- Création du DataFrame ---
df = pd.DataFrame(data)

# --- Analyse ---
df["Total"] = df["Quantité"] * df["Prix_unitaire"]

print("Aperçu des  données ")
print(df)

print("\n Chiffre d'affaires total :", df["Total"].sum(), "€")
print("Produit le plus vendu :", df.loc[df["Quantité"].idxmax(), "Produit"])


# --- visualisation ---
plt.bar(df["Produit"], df["Quantité"])
plt.title("Vente par produit")
plt.xlabel("Produit")
plt.ylabel("Quantité vendue")
plt.savefig("graphique_ventes.png")
plt.show()