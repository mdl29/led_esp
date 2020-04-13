# Simulateur Neopixel 

## Environnement virtuel Python
    
### Mise en oeuvre d'environnement virtuel en Python

Installation d'un module Python de gestion d'environnement virtuel:

```console
$ sudo apt install python3-venv
```

Installation d'un outil de gestion des paquets de Python, pip:

```console
$ sudo apt install python3-pip
```

Test de la version de Python dans l'environnement actuel:

```console
$ python --version
```

Création de l'environnement virtuel de travail pour l'atelier:

```console
$ mkdir atelierNeoPixel
$ cd atelierNeoPixel
$ python3 -m venv .pythonNeoPixel
```

la commande suivante change le PATH pour prendre les commandes par défaut qui se trouvent dans le répertoire .pythonNeoPixel/bin

```console
$ source .pythonNeoPixel/bin/activate
(atelierNeoPixel)$ python --version # 3.5 maintenant
```

Pour quitter l'environnment virtuel:

```console
(atelierNeoPixel)$ deactivate
$ 
```

## Installation de la bibliothèque virtuel neopixel

### Références

* https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel

* https://github.com/Hackable-magazine/vrtneopixel/blob/master/vrtneopixel/vrtneopixel.py


### mise à jour de pip (si besoin)

```console
(atelierNeoPixel)$ pip -V # pour la version pip 8 ou 9 pour python 3.x
(atelierNeoPixel)$ pip install --upgrade pip
```

### Installation

```console
(atelierNeoPixel)$ pip install vrtneopixel     
```

### Test de l'installation

```console
(atelierNeoPixel)$ python     
>>> from vrtneopixel import *
    pygame 1.9.6
    Hello from the pygame community. https://www.pygame.org/contribute.html

>>> quit()
(atelierNeoPixel)$
```

### Démarrer le test du simulateur

```console
(atelierNeoPixel)$ python neo_simulateur.py
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html

# appuyer sur Crtl+C pour arrêter
(atelierNeoPixel)$
```

## Installation des bibliothèques pour le serveur

### Références

* https://flask-restful.readthedocs.io/en/latest/


### Installation

```console
(atelierNeoPixel)$ pip install flask-restful     
```

### Démarrer le serveur du simulateur

Dans une console, démarrer le serveur:

```console
(atelierNeoPixel)$ python server_pixel.py 
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
 * Serving Flask app "server_pixel" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Dans un autre terminal, tester le serveur avec une requête **curl**:

```console
$ curl -X POST -H 'content-type: application/json' -d '{ "red": 200, "blue": 200, "green": 200}' http://localhost:5000/pixel/2
"Ok"
```
