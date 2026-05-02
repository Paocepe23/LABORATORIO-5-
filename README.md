<h1 align="center">Laboratorio 5</h1>
<h1 align="center">Parte A.</h1>
  
### Actividad simpática y parasimpática del sistema nervioso autónomo.

<p align="center"> <img width="576" height="368" alt="simpaticoyparasimpatico" src="https://github.com/user-attachments/assets/b1b6a240-309c-4810-bedc-9e8e9646d4dc" />

La parte simpática prepara al cuerpo para situaciones de estrés o actividad (pelea o huida), mientras que la parte parasimpática promueve el descanso y la recuperación (reposa y digiere).

### Efecto de la actividad simpática y parasimpática en la frecuencia cardíaca.

<p align="center"> <img width="682" height="616" alt="image" src="https://github.com/user-attachments/assets/1b200544-c569-4c67-9d7f-ce7975b77491" />

El simpático  hace que a través de las fibras que liberan noradrenalina, acelerando la despolarización; el parasimpático actúa vía el nervio vago liberando acetilcolina, desacelerándola. En condiciones normales de reposo, el tono vagal (parasimpático) domina.

### Variabilidad de la frecuencia cardíaca (HRV) obtenida a partir de la señal electrocardiográfica (ECG)

<p align="center"> <img width="764" height="392" alt="Gemini_Generated_Image_yns3vryns3vryns3" src="https://github.com/user-attachments/assets/7fbb670f-d6cb-4ea8-bce4-49ed6f9119b9" />
  
El ECG registra la actividad eléctrica del corazón. De cada latido se extrae el pico R, y la distancia entre picos R consecutivos se llama intervalo R-R (en ms). La HRV es simplemente la variación de esos intervalos a lo largo del tiempo.

### Diagrama de Poincaré como herramienta de análisis de la serie R-R. 
<p align="center"> <img width="517" height="458" alt="image" src="https://github.com/user-attachments/assets/b7e9c148-e68c-4a23-9513-a5e020afb1fe" />
  
<img width="279" height="360" alt="image" src="https://github.com/user-attachments/assets/4b3e91f4-5430-47de-9daa-c52249f4a4a8" />
T = longitud del eje transversal (perpendicular a la identidad). Refleja la variación latido a latido. Se ve afectado tanto por el simpático como por el parasimpático.

L = longitud del eje longitudinal (paralelo a la identidad). Refleja la amplitud general de la fluctuación. Se ve afectado principalmente por el parasimpático.
  
CVI = log₁₀(L × T) → sensible exclusivamente a la actividad vagal (parasimpática). Cuando el vago domina, la elipse crece en área.

CSI = L / T → sensible a la actividad simpática. Cuando el simpático domina, la elipse se vuelve más larga y delgada.
  
### Lo que se espera obtener en reposo.
<p align="center"><img width="380" height="412" alt="image" src="https://github.com/user-attachments/assets/ff330e56-60ea-4e24-892d-84bc74bfe164" />
  
### Lo que se espera obtener en la lectura.
<p align="center"><img width="383" height="422" alt="image" src="https://github.com/user-attachments/assets/098cdaee-c173-4d98-a0ec-093f6a820f3a" />


# Plan de acción Diagrama de flujo.
<img width="900" height="1954" alt="diagrama_flujo_parte a" src="https://github.com/user-attachments/assets/a75dd685-7529-4ed1-8cbe-8f8ebaf5c51a" />

<h1 align="center">Parte B.</h1>
  
## Obtencion de la señal con bitalino. 
<p align="center"><img width="713" height="281" alt="grafica primeros 5 segundos" src="https://github.com/user-attachments/assets/9953947c-d60e-47c0-98fc-6897547ba46c" />
Grafica 5 seg

<p align="center"><img width="1001" height="281" alt="grafica completa de los 4 minutos" src="https://github.com/user-attachments/assets/8cf7ac92-604a-48b1-bd02-b1232169e96e" />
Grafica 4 min
  
<h1 align="center">Pre-procesamiento de la señal.</h1>
<p align="center"><img width="1001" height="427" alt="partedosgrafico1" src="https://github.com/user-attachments/assets/c920d936-0a2b-4506-a717-2bbd551cfbbc" />

La señal ECG adquirida con el dispositivo Bitalino fue sometida a un proceso de filtrado digital con el fin de eliminar las componentes de ruido presentes en la señal cruda. Para esto se diseñó un filtro IIR de tipo Butterworth pasa-banda de orden 4 con frecuencias de corte de 0.5 Hz y 40 Hz.

Se eligió el filtro Butterworth porque presenta una respuesta en frecuencia maximalmente plana dentro de la banda de paso, lo que garantiza que la forma de onda del ECG no sea distorsionada durante el filtrado. El límite inferior de 0.5 Hz permite eliminar la deriva de línea base producida por la respiración y el movimiento del cuerpo del sujeto durante la adquisición. El límite superior de 40 Hz elimina el ruido de alta frecuencia proveniente de la actividad muscular involuntaria (EMG) y de posibles interferencias eléctricas del entorno. Estos valores de corte corresponden al rango estándar de la señal ECG clínicamente útil, por lo que no se pierde información relevante del ciclo cardíaco.

## Ecuación en diferencias del filtro

La implementación del filtro se realizó mediante la ecuación en diferencias correspondiente a un filtro IIR, asumiendo condiciones iniciales iguales a cero, es decir, y[−1] = y[−2] = ... = 0 y x[−1] = x[−2] = ... = 0. La forma general de la ecuación es la siguiente:

> **y[n] = b₀·x[n] + b₁·x[n−1] + b₂·x[n−2] + ... + b₈·x[n−8] − a₁·y[n−1] − a₂·y[n−2] − ... − a₈·y[n−8]**

Donde los coeficientes b corresponden al numerador del filtro y los coeficientes a al denominador, obtenidos a partir del diseño Butterworth pasa-banda de orden 4 con frecuencia de muestreo de 100 Hz.

##  Segmentación de la señal
<p align="center"> <img width="1001" height="498" alt="partedosgrafico2" src="https://github.com/user-attachments/assets/c2ee3c13-57d8-4381-9775-597af32ac0ca" />

Una vez filtrada la señal, esta fue dividida en dos segmentos de igual duración, correspondientes a las dos condiciones experimentales registradas:

- **Segmento 1 (0 – 120 s):** corresponde al período en que el sujeto permaneció en reposo completo, inmóvil y en silencio.
- **Segmento 2 (120 – 240 s):** corresponde al período en que el sujeto realizó lectura en voz alta de un texto seleccionado.

Cada segmento tiene una duración exacta de 2 minutos, equivalente a 12.000 muestras a una frecuencia de muestreo de 100 Hz.

##  Detección de picos R y cálculo de intervalos R-R
<p align="center"> <img width="857" height="427" alt="partedosgrafico3" src="https://github.com/user-attachments/assets/b469305c-7ed4-41c7-bb0a-ce16e6f8a987" />


La detección de los picos R en cada segmento se realizó utilizando la función `find_peaks` de la librería SciPy, con un umbral adaptativo basado en el percentil 90 de la señal, lo cual permite evitar que artefactos aislados de gran amplitud distorsionen la detección. Adicionalmente, se estableció una distancia mínima de 0.4 segundos entre picos consecutivos, equivalente a una frecuencia cardíaca máxima de 150 latidos por minuto.

Una vez identificados los picos R, se calcularon los intervalos R-R como la diferencia en tiempo entre picos consecutivos, expresada en milisegundos. Se descartaron aquellos intervalos fisiológicamente imposibles, es decir, menores a 300 ms o mayores a 2000 ms.

Los resultados obtenidos se resumen en la siguiente tabla:

| Parámetro | Segmento 1 — Reposo | Segmento 2 — Lectura |
|---|---|---|
| Picos R detectados | 159 | 174 |
| Intervalos R-R válidos | 158 | 173 |
| Media R-R | 754.2 ms | 689.3 ms |
| FC promedio | ≈ 80 lpm | ≈ 87 lpm |
| SDNN | 166.2 ms | 79.2 ms |

## Resultados

Los resultados muestran que durante la lectura en voz alta la frecuencia cardíaca aumentó de aproximadamente 80 a 87 latidos por minuto, lo que se refleja en una disminución del intervalo R-R medio de 754.2 ms a 689.3 ms. Este comportamiento es consistente con una activación del sistema nervioso simpático durante la verbalización, ya que leer en voz alta implica un mayor esfuerzo cognitivo y motor que reduce el tono parasimpático dominante en reposo.

El valor de SDNN del segmento 1 (166.2 ms) es notablemente mayor al del segmento 2 (79.2 ms), lo que indica que durante el reposo los intervalos R-R presentan mayor variabilidad, señal característica de un mayor tono vagal. En la lectura, la variabilidad se reduce considerablemente, lo que refleja un predominio simpático que regula el corazón de manera más rígida y constante. Estos hallazgos serán confirmados y complementados mediante el análisis del diagrama de Poincaré en la siguiente sección.
<h1 align="center">Parte B.</h1>










