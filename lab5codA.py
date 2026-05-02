import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


ARCHIVO = r"C:\Users\PAOLA\Downloads\laboratorio5.txt"
fs = 100        # Hz — frecuencia de muestreo del BITalino


datos = np.loadtxt(ARCHIVO, comments="#")
ecg   = datos[:, -1].astype(float)
t     = np.arange(len(ecg)) / fs


f_low  = 0.5   # Hz  frecuencia de corte baja
f_high = 40.0  # Hz  frecuencia de corte alta
orden  = 4     # orden del filtro (4 es estándar para ECG)

# Frecuencias normalizadas (0 a 1, donde 1 = fs/2 = 50 Hz)
Wn = [f_low / (fs/2), f_high / (fs/2)]

# Obtener coeficientes del filtro Butterworth band-pass
b, a = signal.butter(orden, Wn, btype='bandpass')


print("=" * 60)
print("  DISEÑO DEL FILTRO IIR — Butterworth Band-pass")
print("=" * 60)
print(f"  Tipo       : Butterworth pasa-banda")
print(f"  Orden      : {orden}")
print(f"  Fc baja    : {f_low} Hz")
print(f"  Fc alta    : {f_high} Hz")
print(f"  Fs         : {fs} Hz")
print()
print("  Coeficientes b (numerador):")
for i, bi in enumerate(b):
    print(f"    b[{i}] = {bi:.6f}")
print()
print("  Coeficientes a (denominador):")
for i, ai in enumerate(a):
    print(f"    a[{i}] = {ai:.6f}")
print()
print("  Ecuación en diferencias:")
terms_b = " + ".join([f"b[{i}]*x[n-{i}]" for i in range(len(b))])
terms_a = " - ".join([f"a[{i}]*y[n-{i}]" for i in range(1, len(a))])
print(f"  y[n] = {terms_b}")
print(f"       - {terms_a}")
print("=" * 60)


ecg_filtrada = signal.lfilter(b, a, ecg)

fig, axes = plt.subplots(2, 1, figsize=(14, 6), sharex=True)
seg = slice(0, 10 * fs)   # primeros 10 segundos

axes[0].plot(t[seg], ecg[seg], color="#58a6ff", linewidth=0.8, label="Original")
axes[0].set_title("Señal ECG original")
axes[0].set_ylabel("Amplitud (u.a.)")
axes[0].legend(loc="upper right")
axes[0].grid(True, alpha=0.2)

axes[1].plot(t[seg], ecg_filtrada[seg], color="#3fb950", linewidth=0.8, label="Filtrada")
axes[1].set_title("Señal ECG filtrada — Butterworth band-pass (0.5–40 Hz, orden 4)")
axes[1].set_xlabel("Tiempo (s)")
axes[1].set_ylabel("Amplitud (u.a.)")
axes[1].legend(loc="upper right")
axes[1].grid(True, alpha=0.2)

plt.suptitle("Comparación: antes y después del filtro IIR", fontsize=13)
plt.tight_layout()
plt.show()


muestras_2min = 2 * 60 * fs   # = 12 000 muestras

seg1 = ecg_filtrada[:muestras_2min]    # 0–120 s   → REPOSO
seg2 = ecg_filtrada[muestras_2min:2*muestras_2min]  # 120–240 s → LECTURA

t1 = t[:muestras_2min]
t2 = t[muestras_2min:2*muestras_2min]

print(f"\n  Segmento 1 (reposo)  : {len(seg1)/fs:.1f} s  ({len(seg1)} muestras)")
print(f"  Segmento 2 (lectura) : {len(seg2)/fs:.1f} s  ({len(seg2)} muestras)")


def detectar_picos_R(segmento, fs):
    altura_min = 0.5 * np.max(segmento)
    distancia  = int(0.4 * fs)           # al menos 0.4 s entre picos
    picos, _   = signal.find_peaks(segmento,
                                   height=altura_min,
                                   distance=distancia)
    return picos

picos1 = detectar_picos_R(seg1, fs)
picos2 = detectar_picos_R(seg2, fs)


rr1 = np.diff(picos1) / fs * 1000   # ms
rr2 = np.diff(picos2) / fs * 1000   # ms

print(f"\n  Picos R detectados seg. 1: {len(picos1)}")
print(f"  Picos R detectados seg. 2: {len(picos2)}")
print(f"\n  Media R-R seg. 1 (reposo) : {np.mean(rr1):.1f} ms")
print(f"  Media R-R seg. 2 (lectura): {np.mean(rr2):.1f} ms")
print(f"  SDNN       seg. 1 (reposo) : {np.std(rr1):.1f} ms")
print(f"  SDNN       seg. 2 (lectura): {np.std(rr2):.1f} ms")


fig, axes = plt.subplots(2, 1, figsize=(14, 7), sharey=False)

# Segmento 1
axes[0].plot(t1, seg1, color="#58a6ff", linewidth=0.7, label="ECG filtrada")
axes[0].plot(t1[picos1], seg1[picos1], "v", color="#f0c24b",
             markersize=8, label=f"Picos R ({len(picos1)})")
axes[0].set_title("Segmento 1 — Reposo (0–120 s)")
axes[0].set_ylabel("Amplitud (u.a.)")
axes[0].legend(loc="upper right")
axes[0].grid(True, alpha=0.2)

# Segmento 2
axes[1].plot(t2, seg2, color="#79c0ff", linewidth=0.7, label="ECG filtrada")
axes[1].plot(t2[picos2], seg2[picos2], "v", color="#ff7b72",
             markersize=8, label=f"Picos R ({len(picos2)})")
axes[1].set_title("Segmento 2 — Lectura en voz alta (120–240 s)")
axes[1].set_xlabel("Tiempo (s)")
axes[1].set_ylabel("Amplitud (u.a.)")
axes[1].legend(loc="upper right")
axes[1].grid(True, alpha=0.2)

plt.suptitle("Detección de picos R en cada segmento", fontsize=13)
plt.tight_layout()
plt.show()


fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharey=False)

axes[0].plot(rr1, "o-", color="#f0c24b", linewidth=1.2,
             markersize=4, label="RR reposo")
axes[0].axhline(np.mean(rr1), color="white", linewidth=0.8,
                linestyle="--", label=f"Media = {np.mean(rr1):.1f} ms")
axes[0].set_title("Serie R-R — Segmento 1 (reposo)")
axes[0].set_ylabel("Intervalo R-R (ms)")
axes[0].legend()
axes[0].grid(True, alpha=0.2)

axes[1].plot(rr2, "o-", color="#ff7b72", linewidth=1.2,
             markersize=4, label="RR lectura")
axes[1].axhline(np.mean(rr2), color="white", linewidth=0.8,
                linestyle="--", label=f"Media = {np.mean(rr2):.1f} ms")
axes[1].set_title("Serie R-R — Segmento 2 (lectura en voz alta)")
axes[1].set_xlabel("Número de latido")
axes[1].set_ylabel("Intervalo R-R (ms)")
axes[1].legend()
axes[1].grid(True, alpha=0.2)

plt.suptitle("Señal de intervalos R-R por segmento", fontsize=13)
plt.tight_layout()
plt.show()
