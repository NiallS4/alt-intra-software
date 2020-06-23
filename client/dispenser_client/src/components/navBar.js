import React from 'react';
import { Link } from 'react-router-dom';

import '../css/navBar.css';
import Home from'../images/home_logo.png';
import About from'../images/about.png';
import SignOut from'../images/sign_out.png';
import Help from'../images/help.png';

const NavBar = () => (
    <header className='navbar'>
        <div className='navbar__title navbar__item'>
        <Link to="/">
                <img src={Home} alt="link to homepage"/>
            </Link>
        </div>
        <div className='navbar__item'>
        <Link to="/">
                <img src={About} alt="about"/>
            </Link>
        </div>
        <div className='navbar__item'>
        <Link to="/">
                <img src={Help} alt="help"/>
            </Link>
        </div>
        <div className='navbar__item'>
        <Link to="/">
                <img src={SignOut} alt="sign_out"/>
            </Link>
        </div>
    </header>
);

export default NavBar;
