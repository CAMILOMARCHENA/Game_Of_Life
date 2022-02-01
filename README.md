# Introducción Juego de la vida
Game of Life (o simplemente "Life") no es realmente un juego. No se puede ganar, perder o destruir a tu oponente mental y espiritualmente. La vida es un "autómata celular", un sistema de células que viven en una cuadrícula, donde viven, mueren y evolucionan de acuerdo con las reglas que gobiernan su mundo.

Las reglas simples y elegantes de la vida dan lugar a un comportamiento emergente asombrosamente complejo. Se juega en una cuadrícula 2-D. Cada cuadrado de la cuadrícula contiene una celda, y cada celda comienza el juego como "viva" o "muerta". El juego procede en rondas. Durante cada ronda, cada celda mira a sus 8 vecinos inmediatos y cuenta el número de ellos que están vivos actualmente.

## Reglas
- Cualquier celda viva con 0 o 1 vecinos vivos se vuelve muerta debido a la falta de población
- Cualquier celda viva con 2 o 3 vecinos vivos se mantiene viva, porque su vecindario es perfecto
- Cualquier celda viva con más de 3 vecinos vivos se vuelve muerta debido a la superpoblación
- Cualquier celda muerta con exactamente 3 vecinos vivos se vuelve viva, por reproducción


## Resultado final

![Image text](https://github.com/CAMILOMARCHENA/Game_Of_Life/blob/master/gol-intro-2.gif)




