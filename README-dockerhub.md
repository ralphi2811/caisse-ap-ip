# Caisse AP IP - Simulateur de Terminal de Paiement

Simulateur de terminal de paiement implémentant le protocole Caisse AP over IP, avec interface web de contrôle.

## Fonctionnalités

- Simulation d'un terminal de paiement
- Interface web pour le contrôle du serveur
- Support des paiements CB (contact/sans contact)
- Simulation de différents scénarios (succès, échec, timeout)

## Démarrage Rapide

1. Créez un fichier `docker-compose.yml` :
```yaml
version: '3.8'

services:
  web:
    image: ralphi2811/caisse-ap-ip:latest
    ports:
      - "5000:5000"  # Interface web
      - "8888:8888"  # Serveur de paiement
```

2. Lancez l'application :
```bash
docker-compose up
```

L'application sera accessible sur :
- Interface web : http://localhost:5000
- Serveur de paiement : port 8888

## Configuration

Via l'interface web, vous pouvez configurer :
- Le type de paiement (CB contact/sans contact)
- Les scénarios d'échec
- La durée de la transaction
- Le port du serveur

## Licence

Ce projet est sous licence [GPL](https://www.gnu.org/licenses/gpl-3.0.html).

## Auteurs

- Rémi de Lattre - *Développement initial*
- Raphaël Auberlet - *Dockerisation et interface web*

## Plus d'informations

Pour plus de détails sur le projet, visitez le [dépôt GitHub](https://github.com/ralphi2811/caisse-ap-ip)
