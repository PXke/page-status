# monte image ubuntu
FROM ubuntu:latest

# monte le dossier appelé code
ADD . /code

# défini le répertoire dans lequel travailler
WORKDIR /code

# execute la commande
CMD ["echo", "toto"]
