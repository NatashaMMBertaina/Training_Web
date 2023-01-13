import React from "react";

const Home = (props) => {
    return(
        <main>
            <section class="titulo">
                <div>
                    <h1>Bienvenidos</h1>
                </div>
            </section>
            <section class="about__us">
                <p>La presente página nació como trabajo final de grado, el cuál se desprendió de un proyecto aún mas grande: SonoUno. </p>
                <p>SonoUno es un programa de sonorización de datos multiplataforma que cuenta con una versión de escritorio y una versión web, el cual fue desarrollado por la doc. Johanna Casado como parte de su doctorado.</p>
                <p>A lo largo de su desarrollo surgió la necesidad de entrenar a los usuarios en la utilización de la sonorización de datos, pues se debe aprender a entender lo que se escucha. Por ello se hizo un trabajo en paralelo en el cuál se desarrollaran pequeños programas de entrenamientos con, primero, datos básicos matemáticos, para luego ir aumentando la dificultad de los mismo a datos más específicos.
                </p>
                <p>Como sonoUno surgió como un proyecto nucleado en datos astrofísicos es que los entrenamientos tambien fueron elaborados utilizando los mismo tipos de datos, pero los mismos pueden ser usados pará más tipos de datos y para todo tipo de niveles de educación, no siendo uso exclusivo de niveles superiores, como la investigación.
                </p>
            </section>
            <section class="multi">
                <h2>¿Qué es un entrenamiento multisensorial?
                </h2>
                <p>Es uno en el cual se busca aumentar la percepción de la persona para así mejorar el aprendizaje de la misma, estimulando más de un sentido a la vez. Para el caso de los entrenamientos que desarrollamos, usamos tanto estimulación visual como auditiva con el fin de lograr mejores resultados.
                </p>
                <p>Lo que buscamos con el desarrollo de los mismos es introducir a la sonorización de datos como complemento en el análisis de estos. </p>
                <p>Pero, tal como dice el nombre, no solo nos quedaremos con dos estímulos, sino que la idea es ampliar a más tipos de estímulos a la vez, logrando así la utilización de más sentidos a la hora del análisis de datos de distintos tipos y entrenamientos multisensoriales al fin.
                </p>
            </section>
        </main>
    );
}

export default Home;