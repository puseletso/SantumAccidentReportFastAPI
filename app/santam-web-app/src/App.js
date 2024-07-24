import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import AccidentReportForm from './components/AccidentReportForm';
import AccidentReportList from './components/AccidentReportList';
import Home from './pages/Home';
import NotFound from './pages/NotFound';

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/add-report" component={AccidentReportForm} />
          <Route path="/reports" component={AccidentReportList} />
          <Route component={NotFound} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
