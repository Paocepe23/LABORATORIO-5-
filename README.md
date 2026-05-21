<h1 align="center">Laboratorio 5</h1>
<h1 align="center">Parte A.(BITalino)</h1>
  
### Actividad simpática y parasimpática del sistema nervioso autónomo.

<p align="center"> <img width="650" height="500" alt="sistema nervioso" src="https://github.com/user-attachments/assets/d8d2fb75-4ee7-4021-8ff9-6aa02254f850" />

  Figura 1. El sistema nervioso autónomo y sus divisiones. Adaptado de El sistema nervioso autónomo, por Saluteca, s.f., (https://www.saluteca.com/el-sistema-nervioso-autonomo/).
La parte simpática prepara al cuerpo para situaciones de estrés o actividad (pelea o huida), mientras que la parte parasimpática promueve el descanso y la recuperación (reposa y digiere).

### Efecto de la actividad simpática y parasimpática en la frecuencia cardíaca.

<p align="center"> <img width="682" height="616" alt="image" src="https://github.com/user-attachments/assets/1b200544-c569-4c67-9d7f-ce7975b77491" />

Figura 2. Esquema del Sistema Nervioso Autónomo (SNA) y efectos cardíacos. > Nota. Imagen generada por inteligencia artificial [Gemini 3 Flash] a partir de la información de Saluteca (s.f.).

El simpático  hace que a través de las fibras que liberan noradrenalina, acelerando la despolarización; el parasimpático actúa vía el nervio vago liberando acetilcolina, desacelerándola. En condiciones normales de reposo, el tono vagal (parasimpático) domina.

### Variabilidad de la frecuencia cardíaca (HRV) obtenida a partir de la señal electrocardiográfica (ECG)

<p align="center"> <img width="764" height="392" alt="Gemini_Generated_Image_yns3vryns3vryns3" src="https://github.com/user-attachments/assets/7fbb670f-d6cb-4ea8-bce4-49ed6f9119b9" />
  
Figura 3.  Imagen generada por inteligencia artificial [Gemini 3 Flash] a partir de la información de Saluteca (s.f.).
  
El ECG registra la actividad eléctrica del corazón. De cada latido se extrae el pico R, y la distancia entre picos R consecutivos se llama intervalo R-R (en ms). La HRV es simplemente la variación de esos intervalos a lo largo del tiempo.

### Diagrama de Poincaré como herramienta de análisis de la serie R-R. 
<p align="center"> <img width="517" height="458" alt="image" src="https://github.com/user-attachments/assets/b7e9c148-e68c-4a23-9513-a5e020afb1fe" />
  
Figura 4.  Imagen generada por inteligencia artificial [Gemini 3 Flash] a partir de la información de Saluteca (s.f.).
  
<img width="279" height="360" alt="image" src="https://github.com/user-attachments/assets/4b3e91f4-5430-47de-9daa-c52249f4a4a8" />

Figura 5.  Imagen generada por inteligencia artificial [Gemini 3 Flash] a partir de la información de Saluteca (s.f.).

T = longitud del eje transversal (perpendicular a la identidad). Refleja la variación latido a latido. Se ve afectado tanto por el simpático como por el parasimpático.

L = longitud del eje longitudinal (paralelo a la identidad). Refleja la amplitud general de la fluctuación. Se ve afectado principalmente por el parasimpático.
  
CVI = log₁₀(L × T) → sensible exclusivamente a la actividad vagal (parasimpática). Cuando el vago domina, la elipse crece en área.

CSI = L / T → sensible a la actividad simpática. Cuando el simpático domina, la elipse se vuelve más larga y delgada.
  
### Lo que se espera obtener en reposo.
<p align="center"><img width="380" height="412" alt="image" src="https://github.com/user-attachments/assets/ff330e56-60ea-4e24-892d-84bc74bfe164" />

  
Figura 6.  Imagen generada por inteligencia artificial [Gemini 3 Flash] a partir de la información de Saluteca (s.f.).
  
### Lo que se espera obtener en la lectura.
<p align="center"><img width="383" height="422" alt="image" src="https://github.com/user-attachments/assets/098cdaee-c173-4d98-a0ec-093f6a820f3a" />


# Plan de acción Diagrama de flujo.
<img width="900" height="1954" alt="diagrama_flujo_parte a" src="https://github.com/user-attachments/assets/a75dd685-7529-4ed1-8cbe-8f8ebaf5c51a" />

<p align="center"><img width="820" height="778" alt="diagrama_parteA" src="https://github.com/user-attachments/assets/f3924fc1-bc3a-4417-b671-22a2acab5c98" />


<h1 align="center">Parte B.(BITalino)</h1>
  
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
<p align="center"> <img width="1001" height="498" alt="estesieselcorregidoprimeraparte" src="https://github.com/user-attachments/assets/7808c2aa-bbc3-49c0-b0d4-418d1f7fc2ec" />


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
<p align="center"> <img width="820" height="1082" alt="diagrama_parteB" src="https://github.com/user-attachments/assets/09c40f5e-ea30-47fd-acb3-a071a7be6761" />

<h1 align="center">Parte C.(BITalino)</h1>

<p align="center"> <img width="927" height="427" alt="partec1" src="https://github.com/user-attachments/assets/0d2f1958-1be9-495b-8c91-3153d13f62d6" />

## Diagrama de Poincaré

El diagrama de Poincaré es una herramienta de análisis no lineal de la variabilidad de la frecuencia cardíaca que consiste en graficar cada intervalo R-R contra el intervalo R-R siguiente, es decir, RRₙ en el eje X y RRₙ₊₁ en el eje Y. La nube de puntos resultante adopta típicamente una forma elipsoide cuya geometría permite caracterizar el balance autonómico del sujeto.

Para cuantificar la forma de la elipse se calcularon dos parámetros estadísticos:

- **SD1:** desviación estándar de los puntos proyectados sobre el eje perpendicular a la línea de identidad. Refleja la variabilidad latido a latido y está asociada principalmente a la actividad parasimpática (vagal).
- **SD2:** desviación estándar de los puntos proyectados sobre el eje paralelo a la línea de identidad. Refleja la variabilidad a largo plazo y está asociada tanto a la actividad simpática como parasimpática.

A partir de SD1 y SD2 se calcularon los ejes de la elipse y los índices autonómicos propuestos por Toichi et al. (1997):

> **L = 4 × SD2** (eje longitudinal, paralelo a la línea identidad)

> **T = 4 × SD1** (eje transversal, perpendicular a la línea identidad)

> **CVI = log₁₀(L × T)** → Índice de actividad vagal (parasimpática)

> **CSI = L / T** → Índice de actividad simpática

## 4.7 Resultados del diagrama de Poincaré

Los resultados obtenidos para cada segmento se presentan en la siguiente tabla:

| Parámetro | Segmento 1 — Reposo | Segmento 2 — Lectura |
|---|---|---|
| SD1 (ms) | 134.7 | 56.3 |
| SD2 (ms) | 193.4 | 97.2 |
| L = 4×SD2 (ms) | 773.6 | 388.8 |
| T = 4×SD1 (ms) | 538.8 | 225.2 |
| **CVI = log₁₀(L×T)** | **5.6198** | **4.9427** |
| **CSI = L/T** | **1.4363** | **1.7263** |

## Análisis de los diagramas

Al comparar los diagramas de Poincaré de ambos segmentos se observan diferencias claras tanto en la forma como en la dispersión de la nube de puntos.

En el segmento 1 (reposo) la nube de puntos presenta una mayor dispersión general, con puntos distribuidos en un rango amplio de valores de R-R entre aproximadamente 400 ms y 1200 ms. Esto indica que durante el reposo el corazón presenta mayor variabilidad entre latidos consecutivos, lo cual es característico de un predominio del tono parasimpático. El valor de CVI obtenido (5.6198) es el más alto de los dos segmentos, confirmando una mayor actividad vagal, mientras que el CSI (1.4363) es el más bajo, lo que indica menor actividad simpática.

En el segmento 2 (lectura en voz alta) la nube de puntos es más compacta y adopta una forma más alargada y estrecha a lo largo de la línea de identidad, con los puntos concentrados en un rango más reducido de valores entre aproximadamente 550 ms y 950 ms. Esto refleja una menor variabilidad latido a latido, característica de un predominio del tono simpático. El valor de CVI (4.9427) disminuyó con respecto al reposo, indicando menor actividad vagal, mientras que el CSI (1.7263) aumentó, confirmando una mayor actividad simpática durante la verbalización.

Estos resultados son consistentes con lo reportado por Toichi et al. (1997), quienes demostraron que el CVI es un índice sensible exclusivamente a la actividad parasimpática y el CSI refleja el predominio simpático. La lectura en voz alta genera una demanda cognitiva y motora que activa el sistema nervioso simpático, reduciendo el tono vagal y disminuyendo la variabilidad de la frecuencia cardíaca, tal como se evidencia en los valores obtenidos.

<p align="center"> <img width="820" height="1032" alt="diagrama_parteC" src="https://github.com/user-attachments/assets/b8b3c64f-675e-4314-8db6-eea96ff8823b" />


## Conclusiones

Se logró identificar y cuantificar los cambios en el balance autonómico del sistema nervioso mediante el análisis temporal y no lineal de la variabilidad de la frecuencia cardíaca (HRV), cumpliendo con el objetivo propuesto.

El análisis en el dominio del tiempo mostró que durante el reposo el intervalo R-R medio fue de 754.2 ms con una desviación estándar (SDNN) de 166.2 ms, mientras que durante la lectura en voz alta el intervalo R-R medio disminuyó a 689.3 ms con un SDNN de 79.2 ms. Esto representa un aumento de la frecuencia cardíaca de aproximadamente 80 a 87 latidos por minuto y una reducción considerable de la variabilidad, lo cual es consistente con una activación del sistema nervioso simpático durante la verbalización.

El análisis mediante el diagrama de Poincaré complementó y confirmó estos hallazgos. Durante el reposo se obtuvo una nube de puntos más dispersa con un CVI de 5.6198 y un CSI de 1.4363, indicando predominio del tono parasimpático. Durante la lectura en voz alta la nube se volvió más compacta y alargada, con un CVI de 4.9427 y un CSI de 1.7263, reflejando un mayor tono simpático y una menor actividad vagal. Estos resultados son coherentes con lo reportado por Toichi et al. (1997), quienes demostraron que el CVI y el CSI son índices confiables y sensibles para evaluar de manera independiente la actividad parasimpática y simpática respectivamente.

En conclusión la parte donde se habla produce cambios medibles y cuantificables en el balance autonómico cardíaco. El sistema nervioso simpático se activa durante actividades que implican esfuerzo cognitivo y motor como la lectura en voz alta, reduciendo la variabilidad de la frecuencia cardíaca y aumentando la frecuencia cardíaca promedio. Estos cambios pueden ser detectados de manera no invasiva a través del análisis de la HRV utilizando herramientas como los parámetros temporales y el diagrama de Poincaré, lo que demuestra la utilidad clínica y experimental de estas técnicas en el estudio del sistema nervioso autónomo.
<h1 align="center">PARTE A. (AD8232)</h1>
<img width="820" height="992" alt="diagrama_parteA_v2" src="https://github.com/user-attachments/assets/33de3178-6e56-4567-a91f-8b5714a82b58" />
La señal ECG fue adquirida en tiempo real mediante el sensor AD8232 conectado a un Arduino Uno, transmitiendo los datos por comunicación serial a 115200 baudios hacia el computador, donde fueron procesados en Python usando el entorno Spyder. La frecuencia de muestreo utilizada fue de 100 Hz, apropiada para la captura de señales ECG. Se grabaron 4 minutos continuos de señal, correspondientes a 23.866 muestras.
Para eliminar el ruido presente en la señal cruda se diseñó e implementó un filtro digital IIR de tipo Butterworth pasa-banda de orden 4, con frecuencias de corte de 0.5 Hz y 40 Hz. Se eligió el filtro Butterworth porque presenta una respuesta en frecuencia maximalmente plana dentro de la banda de paso, lo que garantiza que la forma de onda del ECG no sea distorsionada durante el filtrado. El límite inferior de 0.5 Hz elimina la deriva de línea base producida por la respiración y el movimiento del cuerpo. El límite superior de 40 Hz elimina el ruido de alta frecuencia proveniente de la actividad muscular involuntaria y de interferencias eléctricas del entorno.
<img width="1001" height="427" alt="parte1Aseñalenvivofiltrada" src="https://github.com/user-attachments/assets/8ce1606b-9690-44a6-ad11-5d5d44514e0d" />

<h1 align="center">PARTE B.(AD8232)</h1>
<img width="820" height="992" alt="diagrama_parteA_v2" src="https://github.com/user-attachments/assets/e362368f-c70e-4b1c-8987-4b8c45fb1310" />
La implementación del filtro se realizó mediante la ecuación en diferencias correspondiente a un filtro IIR, asumiendo condiciones iniciales iguales a cero, es decir, y[−1] = y[−2] = ... = 0 y x[−1] = x[−2] = ... = 0. La forma general de la ecuación es:

y[n] = b₀·x[n] + b₁·x[n−1] + b₂·x[n−2] + ... + b₈·x[n−8] − a₁·y[n−1] − a₂·y[n−2] − ... − a₈·y[n−8]

Para el procesamiento en tiempo real, el filtro se aplicó muestra a muestra usando la función lfilter de SciPy, actualizando el estado interno del filtro en cada nueva muestra recibida del Arduino, lo que garantiza la causalidad y la correcta implementación de las condiciones iniciales en cero.
<img width="1001" height="498" alt="parte2Aseñalenvivofiltrada" src="https://github.com/user-attachments/assets/be17a2fd-2e44-444e-bf63-7d90b11a5679" />
<img width="857" height="427" alt="parte3Aseñalenvivofiltrada" src="https://github.com/user-attachments/assets/798a20e4-f143-4062-89e4-7a03772352c7" />
| Parámetro | Segmento 1 — Reposo | Segmento 2 — Lectura |
|---|---|---|
| Picos R detectados | 148 | 158 |
| Intervalos R-R válidos | 147 | 157 |
| Media R-R | 812.8 ms | 753.3 ms |
| FC promedio | ≈ 74 lpm | ≈ 80 lpm |
| SDNN | 111.3 ms | 98.3 ms |
La señal filtrada fue dividida en dos segmentos de exactamente 120 segundos cada uno, correspondientes a las dos condiciones experimentales registradas:

Segmento 1 (0–120 s): el sujeto permaneció en reposo completo, inmóvil y en silencio total.
Segmento 2 (120–240 s): el sujeto realizó lectura en voz alta de un texto seleccionado.

Cada segmento corresponde a 12.000 muestras a una frecuencia de muestreo de 100 Hz.
ParámetroSegmento 1 — ReposoSegmento 2 — LecturaPicos R detectados148158Intervalos R-R válidos147157Media R-R812.8 ms753.3 msFC promedio≈ 74 lpm≈ 80 lpmSDNN111.3 ms98.3 ms



<h1 align="center">PARTE C. (AD8232)</h1>
<img width="820" height="1110" alt="diagrama_parteC_v2" src="https://github.com/user-attachments/assets/9a9d1758-59db-4c2f-9b1b-3d0de9ab2746" />

<img width="929" height="427" alt="parte1Cseñalenvivofiltrada" src="https://github.com/user-attachments/assets/48d3254a-2cec-495b-b0ae-57412590a64f" />
| Parámetro | Segmento 1 — Reposo | Segmento 2 — Lectura |
|---|---|---|
| SD1 (ms) | 80.6 | 80.2 |
| SD2 (ms) | 135.7 | 111.1 |
| L = 4×SD2 (ms) | 542.8 | 444.4 |
| T = 4×SD1 (ms) | 322.4 | 320.8 |
| **CVI = log₁₀(L×T)** | **5.2432** | **5.1541** |
| **CSI = L/T** | **1.6829** | **1.3845** |

En el segmento de reposo la nube de puntos presenta mayor dispersión general, con un CVI de 5.2432 que es el más alto de los dos segmentos, confirmando mayor actividad vagal. El CSI de 1.6829 indica un nivel moderado de actividad simpática en reposo.
En el segmento de lectura en voz alta el SD2 disminuyó de 135.7 ms a 111.1 ms, indicando menor variabilidad a largo plazo, y el CVI disminuyó a 5.1541, reflejando menor actividad vagal durante la verbalización. El CSI disminuyó a 1.3845, lo cual sugiere que aunque la frecuencia cardíaca aumentó, la relación entre los ejes de la elipse cambió de manera consistente con el esfuerzo cognitivo y motor de la lectura.
Estos resultados son coherentes con lo reportado por Toichi et al. (1997) y confirman que la verbalización produce cambios medibles en el balance autonómico cardíaco detectables mediante el análisis del diagrama de Poincaré.


# Declaración de uso de herramientas de IA
Durante la elaboración de este laboratorio se utilizaron herramientas de inteligencia artificial basadas en modelos de lenguaje como apoyo en tareas de consulta, revisión de redacción y organización del código.

Estas herramientas se emplearon únicamente como asistencia técnica para estructuración del documento, aclaración de conceptos y verificación de implementaciones en Python.











