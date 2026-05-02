import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


ARCHIVO = r"C:\Users\PAOLA\Downloads\laboratorio5.txt"
fs = 100

datos        = np.loadtxt(ARCHIVO, comments="#")
ecg          = datos[:, -1].astype(float)
t            = np.arange(len(ecg)) / fs

b, a = signal.butter(4, [0.5/(fs/2), 40/(fs/2)], btype='bandpass')
ecg_filtrada = signal.lfilter(b, a, ecg)


muestras_2min = 2 * 60 * fs
seg1 = ecg_filtrada[:muestras_2min]
seg2 = ecg_filtrada[muestras_2min : 2*muestras_2min]


def detectar_picos_R(segmento, fs):
    distancia   = int(0.4 * fs)
    umbral_pos  = np.percentile(segmento, 90)
    picos_pos,_ = signal.find_peaks(segmento, height=umbral_pos, distance=distancia)
    umbral_neg  = np.percentile(-segmento, 90)
    picos_neg,_ = signal.find_peaks(-segmento, height=umbral_neg, distance=distancia)
    if len(picos_pos) >= len(picos_neg):
        return picos_pos
    else:
        return picos_neg

picos1 = detectar_picos_R(seg1, fs)
picos2 = detectar_picos_R(seg2, fs)

rr1 = np.diff(picos1) / fs * 1000
rr2 = np.diff(picos2) / fs * 1000


rr1 = rr1[(rr1 > 300) & (rr1 < 2000)]
rr2 = rr2[(rr2 > 300) & (rr2 < 2000)]


def calcular_poincare(rr):
    rr_n  = rr[:-1]   # RRn
    rr_n1 = rr[1:]    # RRn+1


    SD1 = np.std((rr_n1 - rr_n) / np.sqrt(2))
    SD2 = np.std((rr_n1 + rr_n) / np.sqrt(2))

    L   = 4 * SD2
    T   = 4 * SD1

    CVI = np.log10(L * T)
    CSI = L / T

    return rr_n, rr_n1, SD1, SD2, L, T, CVI, CSI

rn1, rn1_1, SD1_1, SD2_1, L1, T1, CVI1, CSI1 = calcular_poincare(rr1)
rn2, rn2_1, SD1_2, SD2_2, L2, T2, CVI2, CSI2 = calcular_poincare(rr2)


print("=" * 60)
print("  DIAGRAMA DE POINCARÉ — Resultados")
print("=" * 60)
print()
print(f"  {'Parámetro':<20} {'Seg. 1 Reposo':>18} {'Seg. 2 Lectura':>18}")
print(f"  {'-'*56}")
print(f"  {'SD1 (ms)':<20} {SD1_1:>18.2f} {SD1_2:>18.2f}")
print(f"  {'SD2 (ms)':<20} {SD2_1:>18.2f} {SD2_2:>18.2f}")
print(f"  {'L = 4*SD2 (ms)':<20} {L1:>18.2f} {L2:>18.2f}")
print(f"  {'T = 4*SD1 (ms)':<20} {T1:>18.2f} {T2:>18.2f}")
print(f"  {'CVI = log10(L*T)':<20} {CVI1:>18.4f} {CVI2:>18.4f}")
print(f"  {'CSI = L/T':<20} {CSI1:>18.4f} {CSI2:>18.4f}")
print("=" * 60)
print()
print("  INTERPRETACIÓN:")
if CVI1 > CVI2:
    print(f"  → CVI mayor en reposo ({CVI1:.4f} > {CVI2:.4f})")
    print(f"    Mayor actividad vagal (parasimpática) en reposo ✓")
if CSI2 > CSI1:
    print(f"  → CSI mayor en lectura ({CSI2:.4f} > {CSI1:.4f})")
    print(f"    Mayor actividad simpática durante la verbalización ✓")
print("=" * 60)


fig, axes = plt.subplots(1, 2, figsize=(13, 6))


ax = axes[0]
ax.scatter(rn1, rn1_1, color="#1D9E75", alpha=0.5, s=18, label="Puntos RR")

# Elipse SD1 y SD2
centro = (np.mean(rn1), np.mean(rn1_1))
angulo = np.linspace(0, 2*np.pi, 300)

e_x =  SD2_1 * np.cos(angulo)
e_y =  SD1_1 * np.sin(angulo)
rot_x = (e_x - e_y) / np.sqrt(2) + centro[0]
rot_y = (e_x + e_y) / np.sqrt(2) + centro[1]
ax.plot(rot_x, rot_y, color="#f0c24b", linewidth=1.5, linestyle="--", label="Elipse SD1/SD2")


lim = [min(rn1.min(), rn1_1.min())-50, max(rn1.max(), rn1_1.max())+50]
ax.plot(lim, lim, color="gray", linewidth=0.8, linestyle=":", alpha=0.6)

ax.set_title("Poincaré — Segmento 1 (Reposo)", fontsize=12)
ax.set_xlabel("RRₙ (ms)")
ax.set_ylabel("RRₙ₊₁ (ms)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.2)
ax.text(0.04, 0.95,
        f"CVI = {CVI1:.4f}\nCSI = {CSI1:.4f}\nSD1 = {SD1_1:.1f} ms\nSD2 = {SD2_1:.1f} ms",
        transform=ax.transAxes, fontsize=9, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='#1a2332', alpha=0.8),
        color="#c9d1d9")


ax = axes[1]
ax.scatter(rn2, rn2_1, color="#D85A30", alpha=0.5, s=18, label="Puntos RR")

centro2 = (np.mean(rn2), np.mean(rn2_1))
e_x2 =  SD2_2 * np.cos(angulo)
e_y2 =  SD1_2 * np.sin(angulo)
rot_x2 = (e_x2 - e_y2) / np.sqrt(2) + centro2[0]
rot_y2 = (e_x2 + e_y2) / np.sqrt(2) + centro2[1]
ax.plot(rot_x2, rot_y2, color="#f0c24b", linewidth=1.5, linestyle="--", label="Elipse SD1/SD2")

lim2 = [min(rn2.min(), rn2_1.min())-50, max(rn2.max(), rn2_1.max())+50]
ax.plot(lim2, lim2, color="gray", linewidth=0.8, linestyle=":", alpha=0.6)

ax.set_title("Poincaré — Segmento 2 (Lectura en voz alta)", fontsize=12)
ax.set_xlabel("RRₙ (ms)")
ax.set_ylabel("RRₙ₊₁ (ms)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.2)
ax.text(0.04, 0.95,
        f"CVI = {CVI2:.4f}\nCSI = {CSI2:.4f}\nSD1 = {SD1_2:.1f} ms\nSD2 = {SD2_2:.1f} ms",
        transform=ax.transAxes, fontsize=9, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='#1a2332', alpha=0.8),
        color="#c9d1d9")

plt.suptitle("Diagrama de Poincaré — Comparación reposo vs lectura", fontsize=13)
plt.tight_layout()
plt.show()
