# Utiliser une image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . .

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Exposer le port 8888 pour le serveur de paiement
EXPOSE 8888

# Variable d'environnement pour indiquer que nous sommes dans un conteneur
ENV PYTHONUNBUFFERED=1

# Commande pour démarrer l'application
CMD ["python", "app.py"]
