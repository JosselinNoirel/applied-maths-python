# Bonnes pratiques de programmation

```{raw} html
<p class="language-switch"><a href="../../en/topics/good-practice.html">English</a></p>
```

Un bon code scientifique doit être facile à comprendre, à tester, à réutiliser
et à modifier. Ces qualités comptent même dans un court notebook, car les
exercices du cours deviennent souvent des calculs plus importants.

## Conception modulaire

Adoptez une {concept}`conception modulaire` : divisez un calcul en petites
fonctions ayant chacune une responsabilité claire. Séparez autant que possible
la préparation des données, le calcul numérique et la visualisation. Une
fonction doit recevoir les informations nécessaires par ses paramètres et
renvoyer explicitement son résultat.

```python
import numpy as np

def damped_signal(time, frequency, decay_rate):
    """Return a sinusoidal signal with exponential damping."""
    oscillation = np.sin(2 * np.pi * frequency * time)
    return np.exp(-decay_rate * time) * oscillation

time = np.linspace(0.0, 5.0, 500)
signal = damped_signal(time, frequency=2.0, decay_rate=0.4)
```

Cette structure permet de tester le calcul sans devoir également créer un
graphique.

## Lisibilité et noms

Préférez la {concept}`lisibilité` aux astuces. Employez des noms descriptifs
comme `decay_rate` et `sampling_frequency`, une indentation cohérente, des
espaces autour des opérateurs et des lignes raisonnablement courtes. Évitez les
noms d'une lettre inexpliqués, sauf lorsqu'une notation mathématique
conventionnelle améliore réellement la clarté.

Utilisez l'anglais pour les identifiants, les commentaires et les docstrings.
Le code reste ainsi cohérent avec les mots-clés Python et les interfaces des
bibliothèques, et devient plus facile à partager. Un commentaire doit expliquer
un choix ou une hypothèse, et non répéter l'instruction sur la même ligne ;
mettez-le à jour lorsque le code change.

## Docstrings des fonctions

Une {concept}`docstring` est la chaîne placée immédiatement sous la définition
d'une fonction. Donnez à chaque fonction réutilisable une courte docstring qui
indique son rôle. Pour une fonction plus substantielle, documentez aussi ses
paramètres, sa valeur de retour, ses hypothèses importantes et les erreurs
possibles.

```python
def relative_error(approximation, reference):
    """Return the absolute relative error.

    Parameters
    ----------
    approximation : float
        Value being assessed.
    reference : float
        Non-zero reference value.

    Returns
    -------
    float
        Absolute relative error.
    """
    if reference == 0:
        raise ValueError("reference must be non-zero")
    return abs((approximation - reference) / reference)
```

## Références de style Python

La [PEP 8 — guide de style du code Python](https://peps.python.org/pep-0008/)
traite de la mise en page, des noms et des commentaires, et recommande
explicitement les commentaires en anglais pour le code susceptible d'être
partagé. La [PEP 257 — conventions pour les
docstrings](https://peps.python.org/pep-0257/) explique les docstrings courtes et
multilignes. Considérez ces documents comme des conventions communes, et non
comme des règles qui primeraient sur la clarté propre à un projet.
