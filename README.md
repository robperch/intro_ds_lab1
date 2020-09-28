# Introduction to data science
## Laboratory 1

### Team members
- Edgar Bazo
- Mariana Lugo Ibarra
- Roberto Pérez
- Arturo

### Datos

A fin de comprender el conjunto de datos, se muestra a continuación el significado de cada una de las variables involucrada en el análisis de datos.

| Variable | Categoría | Descripción |
|-|-|-|
| **Tipo de emisión** |  |  |
|  | Consumo medido | Tratándose de tomas de agua donde se encuentre instalado o autorizado el medidor de consumo por parte del Sistema de Aguas. |
|  | Consumo promedio | El consumo promedio se considerará de la siguiente manera:<br><br>1) A falta de aparato medidor, en proceso de instalación o por imposibilidad material para ser instalado, dicho consumo promedio corresponderá a la colonia catastral en el que se encuentra el inmueble en que esté instalada la toma, siempre y cuando dicha colonia catastral el número de tomas con servicio medido sea mayor o igual al 70% del total de las tomas existentes en la colonia. El Sistema de Aguas publicará anualmente en la Gaceta Oficial de la Ciudad de México, la lista de las colonias catastrales que vayan contando con un 70% o más tomas con servicio medido, así como el consumo promedio de cada una de ellas en el ejercicio fiscal inmediato anterior.<br><br>2) Por descompostura del aparato medidor de consumo o cuando exista la imposibilidad de efectuar su lectura, se pagará tomando como base el consumo promedio de los últimos seis bimestres medidos del mismo uso que el actual anteriores al que se factura, sin que exceda de los últimos cinco ejercicios fiscales, quedando fuera de la estadística, el bimestre con facturación más alta. |
| **Uso** |  |  |
|  | Doméstico | Inmuebles de uso Habitacional |
|  | No doméstico | Inmuebles de uso no Habitacional |
|  | Mixto | Inmuebles de uso Doméstico y No Doméstico simultáneamente |
| **Manzana** |  | Es un segmento de la región que regularmente está delimitado por tres o más calles o límites semejantes, representada por los tres siguientes dígitos del mencionado número de cuenta catastral. |
| **Región** |  | Circunscripción convencional del territorio de la Ciudad de México determinada con fines de control catastral de los inmuebles, representada por los tres primeros dígitos del número de cuenta catastral asignado por la autoridad fiscal. |
| **Índice de desarrollo** |  | Construcción estadística mediante variables de tipo socioeconómico derivadas de información oficial, permite diferenciar territorialmente a la población de la Ciudad de México de acuerdo a su nivel de desarrollo económico, agregando la información a nivel manzana. |
|  | Popular | Clasificación que engloba a las manzanas que guardan características socioeconómicas similares y que se tipifican por tener los niveles de desarrollo más bajos de la Ciudad. En esta categoría se agrupa, además, las manzana que se encuentran dentro de la zona rural de la Ciudad de México. |
|  | Bajo | Clasificación que engloba a las manzanas que guardan características socioeconómicas<br>similares y que se tipifican por tener niveles de desarrollo bajo de la Ciudad. |
|  | Medio | Clasificación que engloba a las manzanas que guardan características socioeconómicas similares y que se tipifican por tener niveles de desarrollo medio de la Ciudad. |
|  | Alto | Clasificación que engloba a las manzanas que guardan características socioeconómicas  similares y que se tipifican por tener niveles los más altos niveles de desarrollo de la Ciudad. |
