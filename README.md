# ISI-Project
Implementación del juego de Carcassonne en Python.


1- Componentes del juego.
  1.1. Número de piezas.
    72 piezas de territorio (incluyendo una pieza de inicio, con el reverso de color
  negro), ilustradas con segmentos de aldeas, caminos, prados e iglesias.

  1.2. Fichas.
    40 fichas de seguidores, en 5 colores. Cada seguidor puede ser usado como caballero, ladrón, granjero o monje.
  Una de las fichas de seguidores de cada jugador se utiliza como contador
  de puntuación.

  1.3. Marcador.
    1 marcador, para llevar la cuenta de los puntos que suman los jugadores.


 2- Resumen del juego.
      Los jugadores colocan las piezas de territorio por turnos. A medida que lo van haciendo, los caminos,
aldeas, prados e iglesias van emergiendo y creciendo. En estos territorios, los jugadores pueden desplegar sus
seguidores para ganar puntos. Los jugadores acumulan puntos durante el desarrollo de la partida, y también al
final de la misma. El ganador será el jugador que haya conseguido sumar más puntos tras el recuento final.

 3- Desarrollo del juego.
  3.1 Turno
    Durante su turno, el jugador llevará a cabo las siguientes acciones, en el orden indicado:

    3.1.1 Sacar pieza.
      El jugador debe Sacar una pieza de territorio de uno de los montones, y colocarla en juego.

    3.1.2 Desplegar seguidor (opcional)
      El jugador puede desplegar uno de los seguidores de su provisión sobre la pieza de territorio que acaba de poner
    en juego.

    3.1.3 Sumar puntos.
      Si al colocar la pieza de territorio se completan uno o más claustros, caminos o ciudades, se suman de inmediato
    sus puntos

  4- Colocar las piezas de territorio en juego.
    4.1
      La nueva pieza de territorio debe ser colocada con al menos uno de sus lados tocando directamente a otra pieza
    colocada anteriormente.

    4.2
      La nueva pieza debe ser colocada de modo que todos sus segmentos de prado, aldea y camino se vean continuados por
    segmentos del mismo tipo, en todas las piezas a las que esté tocando (las iglesias son una excepción a esta
    norma, ya que no se encuentran divididos en varios segmentos, si no que siempre están completos en una única pieza).

    4.3
      Si se da la rara circunstancia de que la pieza que se acaba de robar no puede colocarse en juego de manera legal,
    el jugador la descartará y sacará otra pieza nueva.


  5- Desplegar a los seguidores.
    Cuando el jugador coloca una pieza de territorio en juego, puede desplegar sobre ella a uno de sus seguidores, de
    acuerdo con las siguientes normas:

    5.1
      El jugador sólo puede desplegar un seguidor por turno.

    5.2
      El jugador debe coger al seguidor de su provisión (no puede reutilizar un seguidor que ya esté en otra pieza de
    territorio).

    5.3
      El jugador sólo puede desplegar al seguidor en la pieza de territorio que acaba de poner en juego.

    5.4
      El jugador debe elegir en qué parte de la pieza de territorio desplegar al seguidor: en un segmento de
    aldea,camino, prado o iglesia.

    5.5
      No se puede desplegar un seguidor en un segmento de prado, aldea o camino, que esté conectado con otro segmento
    del mismo tipo (a cualquier distancia) en el que ya haya un seguidor (sea del jugador que sea).

    5.6
      Cuando un jugador ha desplegado a todos sus seguidores, sigue colocando una nueva pieza de territorio cada turno.
    Si bien los seguidores que están en juego no pueden ser movidos de sitio, los jugadores los recuperan cuando suman
    puntos por iglesias, caminos y aldeas.


  6- Puntuar por completar iglesias, caminos y aldeas.
    Cuando un claustro, camino o ciudad es completado al colocar una nueva pieza de territorio, se cuenta su puntuación
  inmediatamente.
