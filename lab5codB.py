import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# PARÁMETROS GENERALES

ARCHIVO = r"C:\Users\PAOLA\Downloads\laboratorio5.txt"
fs = 100        # Hz


# 1. CARGAR SEÑAL

datos = np.loadtxt(ARCHIVO, comments="#")
ecg   = datos[:, -1].astype(float)
t     = np.arange(len(ecg)) / fs


# 2. DISEÑO DEL FILTRO IIR — Butterworth band-pass

f_low  = 0.5
f_high = 40.0
orden  = 4
Wn     = [f_low / (fs/2), f_high / (fs/2)]
b, a   = signal.butter(orden, Wn, btype='bandpass')

print("=" * 60)
print("  DISEÑO DEL FILTRO IIR — Butterworth Band-pass")
print("=" * 60)
print(f"  Tipo    : Butterworth pasa-banda")
print(f"  Orden   : {orden}")
print(f"  Fc baja : {f_low} Hz")
print(f"  Fc alta : {f_high} Hz")
print(f"  Fs      : {fs} Hz")
print()
print("  Coeficientes b (numerador):")
for i, bi in enumerate(b):
    print(f"    b[{i}] = {bi:.8f}")
print()
print("  Coeficientes a (denominador):")
for i, ai in enumerate(a):
    print(f"    a[{i}] = {ai:.8f}")
print()
print("  Ecuación en diferencias:")
print("  y[n] = b[0]*x[n] + b[1]*x[n-1] + ... + b[8]*x[n-8]")
print("       - a[1]*y[n-1] - a[2]*y[n-2] - ... - a[8]*y[n-8]")
print("=" * 60)

# 3. APLICAR FILTRO (condiciones iniciales = 0)
==
ecg_filtrada = signal.lfilter(b, a, ecg)


# 4. GRAFICAR original vs filtrada

fig, axes = plt.subplots(2, 1, figsize=(14, 6), sharex=True)
seg = slice(0, 10 * fs)

axes[0].plot(t[seg], ecg[seg], color="#58a6ff", linewidth=0.8)
axes[0].set_title("Señal ECG original")
axes[0].set_ylabel("Amplitud (u.a.)")
axes[0].grid(True, alpha=0.2)

axes[1].plot(t[seg], ecg_filtrada[seg], color="#3fb950", linewidth=0.8)
axes[1].set_title("Señal ECG filtrada — Butterworth band-pass (0.5–40 Hz, orden 4)")
axes[1].set_xlabel("Tiempo (s)")
axes[1].set_ylabel("Amplitud (u.a.)")
axes[1].grid(True, alpha=0.2)

plt.suptitle("Comparación: antes y después del filtro IIR", fontsize=13)
plt.tight_layout()
plt.show()


# 5. DIVIDIR EN DOS SEGMENTOS DE 2 MINUTOS

muestras_2min = 2 * 60 * fs   # 12 000 muestras

seg1 = ecg_filtrada[:muestras_2min]
seg2 = ecg_filtrada[muestras_2min : 2*muestras_2min]
t1   = t[:muestras_2min]
t2   = t[muestras_2min : 2*muestras_2min]


# 6. DETECCIÓN DE PICOS R  — CORREGIDA
#    PROBLEMA 1: el artefacto del seg1 inflaba el umbral → usamos percentil
#    PROBLEMA 2: los picos reales pueden ser negativos → buscamos en ambos
=
def detectar_picos_R(segmento, fs):
    distancia = int(0.4 * fs)   # mínimo 0.4 s entre picos (~150 lpm máx)

    # Buscar picos positivos
    umbral_pos = np.percentile(segmento, 90)   # top 10% de la señal
    picos_pos, _ = signal.find_peaks(segmento,
                                     height=umbral_pos,
                                     distance=distancia)

    # Buscar picos negativos (invertimos la señal)
    umbral_neg = np.percentile(-segmento, 90)
    picos_neg, _ = signal.find_peaks(-segmento,
                                     height=umbral_neg,
                                     distance=distancia)

    # Quedarnos con el grupo que tenga más picos (esos son los R reales)
    if len(picos_pos) >= len(picos_neg):
        return picos_pos, "positivos"
    else:
        return picos_neg, "negativos"

picos1, tipo1 = detectar_picos_R(seg1, fs)
picos2, tipo2 = detectar_picos_R(seg2, fs)


# 7. CALCULAR INTERVALOS R-R

rr1 = np.diff(picos1) / fs * 1000   # ms
rr2 = np.diff(picos2) / fs * 1000   # ms

# Filtrar intervalos fisiológicamente imposibles (< 300 ms o > 2000 ms)
rr1 = rr1[(rr1 > 300) & (rr1 < 2000)]
rr2 = rr2[(rr2 > 300) & (rr2 < 2000)]

print(f"\n  Picos R detectados seg. 1 (reposo)  : {len(picos1)}  [{tipo1}]")
print(f"  Picos R detectados seg. 2 (lectura) : {len(picos2)}  [{tipo2}]")
print()
print(f"  Intervalos R-R válidos seg. 1 : {len(rr1)}")
print(f"  Intervalos R-R válidos seg. 2 : {len(rr2)}")
print()
print(f"  Media R-R  seg. 1 (reposo)  : {np.mean(rr1):.1f} ms  →  FC ≈ {60000/np.mean(rr1):.0f} lpm")
print(f"  Media R-R  seg. 2 (lectura) : {np.mean(rr2):.1f} ms  →  FC ≈ {60000/np.mean(rr2):.0f} lpm")
print(f"  SDNN       seg. 1 (reposo)  : {np.std(rr1):.1f} ms")
print(f"  SDNN       seg. 2 (lectura) : {np.std(rr2):.1f} ms")


# 8. GRAFICAR segmentos con picos R marcados

fig, axes = plt.subplots(2, 1, figsize=(14, 7))

axes[0].plot(t1, seg1, color="#58a6ff", linewidth=0.6, label="ECG filtrada")
axes[0].plot(t1[picos1], seg1[picos1], "v", color="#f0c24b",
             markersize=7, label=f"Picos R ({len(picos1)})")
axes[0].set_title("Segmento 1 — Reposo (0–120 s)")
axes[0].set_ylabel("Amplitud (u.a.)")
axes[0].legend(loc="upper right")
axes[0].grid(True, alpha=0.2)

axes[1].plot(t2, seg2, color="#79c0ff", linewidth=0.6, label="ECG filtrada")
axes[1].plot(t2[picos2], seg2[picos2], "v", color="#ff7b72",
             markersize=7, label=f"Picos R ({len(picos2)})")
axes[1].set_title("Segmento 2 — Lectura en voz alta (120–240 s)")
axes[1].set_xlabel("Tiempo (s)")
axes[1].set_ylabel("Amplitud (u.a.)")
axes[1].legend(loc="upper right")
axes[1].grid(True, alpha=0.2)

plt.suptitle("Detección de picos R en cada segmento", fontsize=13)
plt.tight_layout()
plt.show()


# 9. GRAFICAR serie R-R

fig, axes = plt.subplots(2, 1, figsize=(12, 6))

axes[0].plot(rr1, "o-", color="#f0c24b", linewidth=1.2, markersize=4)
axes[0].axhline(np.mean(rr1), color="#ff7b72", linewidth=1,
                linestyle="--", label=f"Media = {np.mean(rr1):.1f} ms")
axes[0].set_title("Serie R-R — Segmento 1 (reposo)")
axes[0].set_ylabel("Intervalo R-R (ms)")
axes[0].set_ylim(0, 1800)
axes[0].legend()
axes[0].grid(True, alpha=0.2)

axes[1].plot(rr2, "o-", color="#ff7b72", linewidth=1.2, markersize=4)
axes[1].axhline(np.mean(rr2), color="#f0c24b", linewidth=1,
                linestyle="--", label=f"Media = {np.mean(rr2):.1f} ms")
axes[1].set_title("Serie R-R — Segmento 2 (lectura en voz alta)")
axes[1].set_xlabel("Número de latido")
axes[1].set_ylabel("Intervalo R-R (ms)")
axes[1].set_ylim(0, 1800)
axes[1].legend()
axes[1].grid(True, alpha=0.2)

plt.suptitle("Señal de intervalos R-R por segmento", fontsize=13)
plt.tight_layout()
plt.show()
