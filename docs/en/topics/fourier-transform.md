# Fourier transforms and the FFT

```{raw} html
<p class="language-switch"><a href="../../fr/topics/fourier-transform.html">Français</a></p>
```

The discrete Fourier transform represents a sampled signal as complex frequency
components. NumPy computes it efficiently with the fast Fourier transform (FFT).

## `numpy.fft.fft`

```{py:function} numpy.fft.fft(a, n=None, axis=-1, norm=None)

Compute the one-dimensional discrete Fourier transform along an array axis.
```

## `numpy.fft.fftfreq`

```{py:function} numpy.fft.fftfreq(n, d=1.0)

Return the frequency associated with every FFT coefficient. Here `d` is the
sample spacing, such as the time step in seconds.
```

## `numpy.fft.ifft`

```{py:function} numpy.fft.ifft(a, n=None, axis=-1, norm=None)

Compute the inverse discrete Fourier transform.
```

## Example: identify a frequency

```python
import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100.0
duration = 2.0
t = np.arange(0, duration, 1 / sampling_rate)
signal = np.sin(2 * np.pi * 7 * t)

spectrum = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), d=1 / sampling_rate)

positive = frequencies >= 0
plt.plot(frequencies[positive], np.abs(spectrum[positive]))
plt.xlabel("frequency (Hz)")
plt.ylabel("magnitude")
plt.show()
```

For a real signal, negative-frequency coefficients mirror the positive side.
The magnitude depends on the transform normalisation and the number of samples.
The original signal is recovered, up to floating-point error, with:

```python
reconstructed = np.fft.ifft(spectrum).real
np.allclose(reconstructed, signal)
```

See the [official NumPy FFT reference](https://numpy.org/doc/stable/reference/routines.fft.html).

