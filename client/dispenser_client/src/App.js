import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom';

// Pages
import Home from "./components/home";
import RegisterDispenser from "./components/register_dispenser";
import SearchDispenser from "./components/search_dispenser";

// // AWS
// import Amplify from 'aws-amplify';
// import aws_exports from './aws-exports';
// import { withAuthenticator } from 'aws-amplify-react';

// Amplify.configure(aws_exports);

class App extends Component {

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/register_dispenser" component={RegisterDispenser} />
          <Route exact path="/search_dispenser" component={SearchDispenser} />
          <Route component={Error} />
        </Switch>
      </Router>
    )
  }
}
// export default withAuthenticator(App);
export default App;
