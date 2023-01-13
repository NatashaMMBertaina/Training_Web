import React from 'react';


import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import '../../styles/layout/Header.css';

const Header = (props) => {
    return(
        <header>
            <Container className="contenedor">
                <Row className="logo">
                    <Col>
                    <img src="images/logoheader.png" width={150} alt="Logos Instituto de Bioingeniería e ITeDA"/>
                    </Col>
                </Row>
            </Container>
        </header>
    );
}

export default Header; 