import React, {useEffect} from 'react';
import { Route, Switch } from "react-router-dom";
import NavBar from "./NavBar/component/NavBar";
import Footer from "./Footer/component/Footer";
import LandingPage from "./LandingPage/component/LangdingPage";
import SearchPage from "./SearchPage/component/SearchPage";
import './App.css';

function App() {

    return (
      <>
      <NavBar />
      <Switch>
        <Route exact path="/" component={LandingPage} /> 
        <Route exact path="/search" component={SearchPage} /> 
      </Switch>
      <Footer />
      </>
    );
  }

export default App;