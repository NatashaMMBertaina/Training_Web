import React from "react";
import '../../styles/layout/Nav.css';
import { NavLink } from "react-router-dom";

const Nav = (props) => {
    return (
        <nav className="barra">
            <ul>
                <li>
                    <NavLink activeClassName="activo" exact to='/'>INICIO</NavLink>
                </li>
                <li>
                    <NavLink activeClassName="activo" exact to='/manual'>MANUAL</NavLink>
                </li>
                <li>
                    <NavLink activeClassName="activo" exact to='/training'>ENTRENAMIENTOS</NavLink>
                </li>
            </ul>
        </nav>
    );
}

export default Nav;