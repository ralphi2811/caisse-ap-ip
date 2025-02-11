# Caisse AP over IP protocol server and client

Ce projet fournit un serveur et un client pour le protocole Caisse AP over IP sous la [licence GPL](https://www.gnu.org/licenses/gpl-3.0.html).

Le [protocole Caisse AP](https://www.associationdupaiement.fr/protocoles/protocole-caisse/) est un protocole indépendant des fournisseurs utilisé en France pour la communication entre un point de vente et un terminal de paiement. Il est implémenté par les terminaux de paiement [Ingenico](https://ingenico.com/fr/produits-et-services/terminaux-de-paiement), [Verifone](https://www.verifone.com/) et d'autres marques. Ce protocole est conçu par une association française appelée [Association du paiement](https://www.associationdupaiement.fr/), abrégée **AP**. Notez que le protocole Caisse-AP est utilisé par les terminaux de paiement Ingenico déployés en France, mais pas par les mêmes modèles déployés dans d'autres pays !

Le protocole Caisse-AP était initialement conçu pour les connexions série et USB. Depuis la version 3.x, il prend également en charge l'IP. Lorsqu'il est utilisé via IP, le client (point de vente) et le serveur (terminal de paiement) échangent des données texte simples encodées en ASCII via une socket TCP brute.

Ce projet fournit deux scripts Python 3 :

- un client `caisse-ap-ip-client.py` qui peut simuler un point de vente,
- un serveur `caisse-ap-ip-server.py` qui peut simuler un terminal de paiement.

# Installation

## Installation Classique

Le client nécessite la bibliothèque Python [iso4217](https://github.com/dahlia/iso4217) (non nécessaire si vous utilisez uniquement `EUR`).

    pip3 install iso4217

Le serveur nécessite la bibliothèque Python [Twisted](https://twisted.org/) :

    pip3 install Twisted

## Installation Docker

L'application est également disponible sous forme d'image Docker. Pour l'utiliser :

1. Téléchargez l'image depuis DockerHub :
```bash
docker pull ralphi2811/caisse-ap-ip:latest
```

2. Lancez l'application avec Docker Compose :
```bash
docker-compose up
```

L'application sera accessible sur :
- Interface web : http://localhost:5000
- Serveur de paiement : port 8888

# Utilisation

Les scripts client et serveur disposent tous deux d'une option `--help` (ou `-h`) qui affiche la liste complète des options disponibles.

Le serveur peut être configuré pour simuler des transactions de paiement réussies, mais aussi des échecs de paiement ou des délais d'attente.

# Tests

Pour développer ce projet, nous avons utilisé un **Ingenico Desk/5000** (avec l'application `CONCERT V3` version `8400740115`) avec l'imprimante de chèques **Ingenico i2200**. Nous avons effectué de vrais paiements par carte et imprimé de vrais chèques.

# Auteurs

- Rémi de Lattre - *Développement initial*
- Raphaël Auberlet - *Dockerisation et interface web*
