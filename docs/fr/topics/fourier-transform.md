# Transformées de Fourier et FFT

```{raw} html
<p class="language-switch"><a href="../../en/topics/fourier-transform.html">English</a></p>
```

La transformée de Fourier discrète représente un signal échantillonné par des
composantes fréquentielles complexes. NumPy la calcule efficacement avec la
transformée de Fourier rapide (FFT).

## `numpy.fft.fft`

```{py:function} numpy.fft.fft(a, n=None, axis=-1, norm=None)

Calcule la transformée de Fourier discrète unidimensionnelle suivant un axe du
tableau.
```

## `numpy.fft.fftfreq`

```{py:function} numpy.fft.fftfreq(n, d=1.0)

Renvoie la fréquence associée à chaque coefficient de la FFT. `d` est le pas
d'échantillonnage, par exemple le pas de temps en secondes.
```

## `numpy.fft.ifft`

```{py:function} numpy.fft.ifft(a, n=None, axis=-1, norm=None)

Calcule la transformée de Fourier discrète inverse.
```

## Exemple : identifier une fréquence

```python
import numpy as np
import matplotlib.pyplot as plt

frequence_echantillonnage = 100.0
duree = 2.0
t = np.arange(0, duree, 1 / frequence_echantillonnage)
signal = np.sin(2 * np.pi * 7 * t)

spectre = np.fft.fft(signal)
frequences = np.fft.fftfreq(len(signal), d=1 / frequence_echantillonnage)

positives = frequences >= 0
plt.plot(frequences[positives], np.abs(spectre[positives]))
plt.xlabel("fréquence (Hz)")
plt.ylabel("amplitude")
plt.show()
```

Pour un signal réel, les coefficients de fréquence négative reflètent la partie
positive. L'amplitude dépend de la normalisation et du nombre d'échantillons. On
retrouve le signal initial, aux erreurs d'arrondi près, avec :

```python
reconstruit = np.fft.ifft(spectre).real
np.allclose(reconstruit, signal)
```

Voir la [référence FFT officielle de NumPy](https://numpy.org/doc/stable/reference/routines.fft.html).

