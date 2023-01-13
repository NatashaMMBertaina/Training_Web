import './App.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages/Home';
import Manual from './pages/Manual';
import Training from './pages/Training';

import Header from './components/layout/Header';
import Nav from './components/layout/Nav';
import Footer from './components/layout/Footer';



function App() {
  return (
    <div className='App'>
      <Router>
        <Container fluid>
          <Row>
            <Col>
              <Header/>
            </Col>
            <Col>
              <Nav/>
              <Switch>
                <Route path='/' exact component= {Home} />
                <Route path='/manual' exact component={Manual} />
                <Route path='/training' exact component={Training} />
              </Switch>
            </Col>
          </Row>
        </Container>
        <Footer/>
      </Router>
    </div>
  );
}

export default App;
