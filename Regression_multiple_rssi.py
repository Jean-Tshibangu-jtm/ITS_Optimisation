
# Régression multiple pour la prédiction de la puissance de transmission (RSSI)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_excel('datasetB.xlsx')

# Séparation des variables
X = df.drop('RSSI(dBm)', axis=1)
y = df['RSSI(dBm)']

# Découpage train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisation des features
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Régression linéaire multiple
reg = LinearRegression()
reg.fit(X_train_scaled, y_train)

# Prédictions
y_pred = reg.predict(X_test_scaled)

# Évaluation
print("Régression multiple :")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R² Score:", r2_score(y_test, y_pred))

# Visualisation
plt.figure(figsize=(6,4))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot(y_test, y_test, 'r')
plt.xlabel("RSSI réel")
plt.ylabel("RSSI prédit")
plt.title("Régression Multiple : Prédiction du RSSI")
plt.grid()
plt.tight_layout()
plt.show()
