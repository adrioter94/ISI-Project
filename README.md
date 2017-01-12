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


  7- Camino completado.

    7.1
      Un camino se considera completado cuando sus segmentos de camino en ambos extremos están conectados con un cruce,
    un segmento de aldea, o una iglesia. Entre ambos extremos puede haber cualquier número de segmentos de camino.

    7.2
      Un jugador que tiene un ladrón en un camino completado suma un punto por cada segmento que tenga el camino
    (cuenta el número de piezas de territorio).


  8- Ciudad completada.

    8.1
      Una aldea se considera completada cuando está totalmente rodeada por una muralla, en la que no
    queda ningún hueco abierto. Una aldea puede tener cualquier cantidad de segmentos.

    8.2
      El jugador que tenga un caballero en una aldea completada suma dos puntos por cada segmento que tenga
la aldea. Cada escudo que haya en los segmentos de la aldea otorga al jugador dos puntos extra.

    8.3- Si la ciudad o camino completados tienen más de un seguidor:

      8.3.1
        Cuando pase, el jugador con más ladrones (en un camino) o más caballeros (en una aldea) se llevará todos los puntos.

      8.3.2
        Si dos o más jugadores empatan con el mayor número de ladrones o caballeros, todos esos jugadores se llevarán
      los puntos por el camino o ciudad en cuestión.


  9- Iglesia completada.
    Una iglesia se considera completada cuando la pieza de territorio en la que se encuentra está completamente
  rodeada por otras piezas de territorio. En ese caso, el jugador que tenga un monje en esa iglesia sumará 9 puntos.


  10- Recuperar seguidores.
    Cuando se suman puntos por un camino, aldea o iglesia completados (y sólo entonces), todos los seguidores
  implicados son devueltos a sus jugadores, que pueden usarlos de nuevo (como ladrones, granjeros, caballeros o
  monjes) en turnos posteriores. También puede ocurrir que se devuelvan los seguidores en ese mismo turno si al
  colocar la pieza y el seguidor se completa el camino, la aldea o la iglesia.


  11- Las granjas.
    Los segmentos de campo conectados entre sí se llaman “granjas”. las granjas están rodeadas por caminos, aldeas, y
  por los extremos del área donde se juegan las piezas de territorio. Las granjas no suman puntos durante el juego.
  Sólo existen como lugares donde desplegar granjeros. Los granjeros otorgan sus puntos a los jugadores en el recuento
  final. Los granjeros se mantienen toda la partida en el segmento de campo en el que hayan sido desplegados, y nunca
  son recuperados por sus jugadores.


  12- Final del juego.
    Al final del turno del jugador que coloca la última pieza de territorio que queda, la partida finaliza y se lleva
  a cabo el recuento final.


  13- Recuento final. Ladrones, caballeros y monjes.
    Primero se puntúan las aldeas, caminos e iglesias incompletos en los que algún jugador tenga un ladrón o un
  caballero. Dicho jugador se lleva 1 punto por cada segmento que tenga el camino o aldea. Además, cada escudo en la
  ciudad da al jugador 1 punto extra (para determinar quien se lleva los puntos en los caminos y ciudades con más de
  un seguidor, utiliza las mismas reglas que para los caminos y ciudades completos). Por cada iglesia incompleta, el
  jugador que tenga un monje allí se llevará 1 punto por la pieza de iglesia, y otro punto por cada pieza de
  territorio que esté rodeando la iglesia.


  14- Recuento final. Granjeros.
    Tras puntuar las aldeas, caminos e iglesias incompletos, se cuentan los puntos logrados por los granjeros. Los
  granjeros abastecen a las aldeas, y por tanto acumulan puntos de manera acorde, según las siguientes normas:

    14.1
      Sólo las aldeas completas se consideran abastecidas, y por tanto son las únicas que suman puntos por los
    granjeros. Para abastecer a una aldea completa, la granja debe bordearla. La distancia entre el granjero y la
    ciudad es irrelevante. Por cada ciudad que un granjero abastece de esta manera, el jugador que lo ha desplegado
    suma 3 puntos, sin importar el tamaño de la aldea ni de la granja.

    14.2
      Un mismo granjero puede abastecer varias ciudades adyacentes a su granja (y por tanto sumar puntos por todas
    ellas).

    14.3
      Varias granjas pueden abastecer una misma aldea. En este caso, el jugador con más granjeros en las granjas que
    abastecen la aldea se lleva 3 puntos. Si dos o más jugadores están empatados con el mayor número de granjeros,
    cada uno de estos jugadores se lleva 3 puntos.

    14.4
      De este modo, todas las aldeas abastecidas por granjas van sumando puntos una por una. Cuando todas las ciudades
    hayan sido puntuadas, el recuento final se habrá completado. ¡El jugador con más puntos será el ganador del juego!
