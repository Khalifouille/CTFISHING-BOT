# FISHING BOT [ALTV] POUR LES FLEMMARDS

Ce script Python automatise la saisie de texte dans le mod de jeu Grand Theft Auto V (GTA V), spécifiquement en ciblant le serveur AltV en utilisant l'exécutable altv-webengine.

## Fonctionnement

Le script utilise diverses bibliothèques et techniques pour automatiser ses actions :

1. **Vérification des Processus** : Il vérifie si le processus du jeu AltV (`altv-webengine.exe`) est en cours d'exécution en utilisant la bibliothèque `psutil`.
2. **Capture d'Écran** : Lorsqu'il détecte que le jeu est en cours d'exécution, il capture une capture d'écran d'une région désignée où le texte apparaît en utilisant `pyautogui`.
3. **Extraction de Texte** : La capture d'écran est traitée en utilisant OpenCV (`cv2`) pour extraire le texte. Il applique des techniques de conversion en niveaux de gris, de seuillage et de netteté pour améliorer la lisibilité du texte.
4. **Reconnaissance Optique de Caractères (OCR)** : L'image traitée est ensuite alimentée dans le moteur OCR Tesseract en utilisant `pytesseract` pour extraire le contenu textuel.
5. **Saisie de Texte** : Enfin, le texte extrait est itéré, et chaque caractère est tapé dans le jeu en utilisant `pyautogui`. Une gestion spéciale est appliquée pour les espaces, les sauts de ligne et les tabulations.
6. **Interactions avec le Jeu** : Le script simule également des interactions avec le jeu, telles que l'appui sur la touche 'i' pour ouvrir le chat, le déplacement du curseur à un emplacement spécifique, le clic multiple et l'appui sur 'esc' pour fermer le chat.

## RENDEMENT

Ce script t'assure un rendement supérieur de 50% à la façon normale, tourne le jour et la nuit sans soucis.

## PROBLEMES CONNU

Il peut se tromper sur certains mots, d'aprés mes test ça ne dépasse pas le 1 mot sur 20.

## Avertissement

Ce script est destiné à des fins éducatives et expérimentales uniquement. Son utilisation dans des jeux en ligne ou tout autre logiciel peut violer les conditions de service ou les directives de la communauté. Utilisez toujours l'automatisation de manière responsable et respectez les règles des plateformes avec lesquelles vous interagissez. ⚠️
