import React from "react";

import '../../styles/layout/Footer.css';

const Footer = (props) => {
    return (
        <footer>
            <section className="holder">
                <div className="contact">
                    <p className="fs-5 text-decoration-underline">Contacto:</p>
                    <p>instituto.bioingenieria@um.edu.ar</p>
                    <p>750 Paseo Doctor Emilio Descotte, Mendoza M5500 </p>
                    <p>Facultad de Ingenieria, Universidad de Mendoza</p>
                </div>
                <div className="logof">
                    <img src="images/logofooter.png" width={80} alt="Logos Universidad de Mendoza y Reinforce"/>
                </div>
            </section>
        </footer>
    );
}

export default Footer;