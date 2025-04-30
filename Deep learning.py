
# Traitement et création du modèle IA pour prédiction de la puissance de transmission (RSSI)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Chargement des données
df = pd.read_excel('datasetB.xlsx')

# Séparation des variables
X = df.drop('RSSI(dBm)', axis=1)
y = df['RSSI(dBm)']

# Séparation des jeux d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)

# Mise à l'échelle des données
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Création du modèle de réseau de neurones
model = Sequential()
model.add(Dense(11, activation='relu'))
model.add(Dense(11, activation='relu'))
model.add(Dense(11, activation='relu'))
model.add(Dense(11, activation='relu'))
model.add(Dense(11, activation='relu'))
model.add(Dense(11, activation='relu'))
model.add(Dense(1))  # couche de sortie

# Compilation du modèle
model.compile(optimizer='adam', loss='mse')

# Entraînement du modèle
model.fit(x=X_train, y=y_train.values,
          validation_data=(X_test, y_test.values),
          batch_size=64, epochs=500)

# Évaluation du modèle
predictions = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, predictions))
print("RMSE:", np.sqrt(mean_squared_error(y_test, predictions)))
print("Explained Variance:", explained_variance_score(y_test, predictions))

# Visualisation des prédictions
plt.scatter(y_test, predictions)
plt.plot(y_test, y_test, 'r')
plt.xlabel("Valeurs réelles RSSI")
plt.ylabel("Prédictions RSSI")
plt.title("Prédiction de la puissance de transmission (RSSI)")
plt.show()

# Affichage de l'erreur absolue
err_histogramme = np.abs(y_test - predictions)
plt.hist(err_histogramme, bins=50)
plt.title("Distribution des erreurs absolues")
plt.show()
