"""
GRABADOR DE SEÑAL ECG — AD8232 + Arduino

"""
import serial
import time
import numpy as np

# =============================================================================
# CONFIGURACIÓN
# =============================================================================
PUERTO      = "COM6"
BAUDRATE    = 115200
DURACION    = 4 * 60        
fs          = 100           # Hz
ARCHIVO     = r"C:\Users\PAOLA\Downloads\ecg_ad8232.txt"

# =============================================================================
# ABRIR PUERTO
# =============================================================================
print("=" * 50)
print("  GRABADOR ECG — AD8232")
print("=" * 50)
print(f"\n  Puerto  : {PUERTO}")
print(f"  Duración: {DURACION//60} minutos")
print(f"  Archivo : {ARCHIVO}")

ser = serial.Serial(PUERTO, BAUDRATE, timeout=2)
ser.flushInput()
time.sleep(2)   # esperar que el Arduino se estabilice

print("\n  ✓ Sensor conectado")
print("\n  Prepárate — la grabación empieza en 5 segundos...")
for i in range(5, 0, -1):
    print(f"  {i}...")
    time.sleep(1)

# =============================================================================
# GRABACIÓN
# =============================================================================
print("\n  🔴 GRABANDO —  ")
print("  (en 2 minutos te aviso que empieces a leer)\n")

datos     = []
t_inicio  = time.time()
t_aviso   = False

try:
    while True:
        t_actual = time.time() - t_inicio

        # Aviso a los 2 minutos
        if t_actual >= 120 and not t_aviso:
            print("  📖 YA PASARON 2 MINUTOS — empieza a leer en voz alta!")
            t_aviso = True

        # Terminar a los 4 minutos
        if t_actual >= DURACION:
            break

        # Leer dato del serial
        try:
            linea = ser.readline().decode('utf-8', errors='ignore').strip()
            if linea and linea != "!":
                valor = float(linea)
                datos.append(valor)

                # Mostrar progreso cada 30 segundos
                n = len(datos)
                if n % (30 * fs) == 0:
                    seg = int(t_actual)
                    print(f"  ⏱ {seg//60}:{seg%60:02d} — {n} muestras grabadas")

        except (ValueError, UnicodeDecodeError):
            continue

except KeyboardInterrupt:
    print("\n  Grabación interrumpida por el usuario")

finally:
    ser.close()

# =============================================================================
# GUARDAR ARCHIVO
# =============================================================================
datos = np.array(datos)
np.savetxt(ARCHIVO, datos, fmt='%d')

print(f"\n  ✅ Grabación terminada!")
print(f"  Muestras grabadas : {len(datos)}")
print(f"  Duración real     : {len(datos)/fs:.1f} s")
print(f"  Archivo guardado  : {ARCHIVO}")
print(f"\n  Ahora corre el archivo parte_B_filtro_RR_v2.py")
print(f"  cambiando ARCHIVO por: {ARCHIVO}")
