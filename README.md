Dépôt accompagnant le cours 420-611-BT
======================================

Démarrage
---------

1.  Clonez ce dépôt sur votre poste en utilisant Git.

1.  Ouvrez-votre éditeur sur ce dépôt (PyCharm est recommandé)

1.  Assurez-vous d'avoir [`uv`](https://docs.astral.sh/uv/getting-started/installation/)

1.  Ouvrez un terminal dans le répertoire du dépôt

1.  Installer les dépendances

    ```
    uv sync
    ```

1.  Exécuter l'ensemble des scripts d'assurance qualité

    ```
    uv run nox
    ```

Aide-mémoire
------------

1.  Ajouter des dépendancesW

    ```
    uv add --dev pytest
    ```

1.  Exécuter le programme

    ```
    uv run intropy
    ```

Crédits, licenses et attributions
---------------------------------

Le contenu de ce dépôt est distribué sous différentes licences:

*   Le code source (Python) est distribué sous licence
    _BSD-2-Clause Plus Patent License_ (`BSD-2-Clause-Patent`).

*  La documentation, notes de cours, diapos, et autres contenus didactiques
    sont distribués sous licence
    _Attribution-NonCommercial-ShareAlike 4.0 International_ (`CC-BY-NC-SA-4.0`).

Copyright (c) 2026 Charles Bouchard-Légaré

### Attribution du cours

Ce contenu est inspiré du cours 
**CS50’s Introduction to Artificial Intelligence with Python** 
de l'Université Harvard.

*   **Auteurs :** Brian Yu ([brian@cs.harvard.edu](mailto:brian@cs.harvard.edu)) 
    et David J. Malan ([malan@harvard.edu](mailto:malan@harvard.edu))

*   **Source originale :** [https://cs50.harvard.edu/ai/](https://cs50.harvard.edu/ai/)

*   **Licence :** 
    [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
