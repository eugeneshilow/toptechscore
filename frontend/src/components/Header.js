import React, { useState, useEffect } from 'react';
import { WorldIcon, HamburgerIcon, IconCrossDark, UserIcon } from '../assets/SvgComponents';
import SocialMediaLinks from './SocialMediaLinks';
import '../styles/Header.css';



function AppHeader() {
  const [showMenu, setShowMenu] = useState(false);  // state for showing/hiding menu
  const [isUserSignedIn, setIsUserSignedIn] = useState(true);  // state for tracking user sign in status

  const toggleMenu = () => {
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    const metaThemeColor = document.querySelector("meta[name='theme-color']");
    const primaryColor = window.getComputedStyle(document.documentElement).getPropertyValue('--primary-color').trim();

    metaThemeColor.setAttribute("content", primaryColor);

    return () => {
      const whiteColor = window.getComputedStyle(document.documentElement).getPropertyValue('--white-color').trim();
      metaThemeColor.setAttribute("content", whiteColor);
    };
  }, []);

  return (
    <header className="header">
      <div className="logo-menu-wrapper">
        <img src="/Findex-white-removebg.png" alt="Logo" className="logo" />
        <nav className={`menu ${showMenu ? 'menu-show' : ''}`}>
          <div className="menu-content">
            <div className={`menu-items ${showMenu ? 'menu-items-open' : ''}`}>            
              <a href="#" className={`menu-item ${showMenu ? 'menu-item-open' : ''}`}>Categories</a>
              <a href="#" className={`menu-item ${showMenu ? 'menu-item-open' : ''}`}>Learn</a>
              <a href="#" className={`menu-item ${showMenu ? 'menu-item-open' : ''}`}>Advertise</a>
              <a href="#" className={`menu-item ${showMenu ? 'menu-item-open' : ''}`}>About</a>
            </div>
            {showMenu && 
            <div className="header-socialmedialinks">
              <div className="social-media-links"><SocialMediaLinks /></div>
            </div>}
          </div>
        </nav>
      </div>
      <div className="header-icons">
        {isUserSignedIn ? (
          <UserIcon />
        ) : (
          <button className="signup-btn">Sign Up</button>
        )}
        <button className="world-icon">
          <WorldIcon />
        </button>
        <button className="hamburger-menu" onClick={toggleMenu}>
          {showMenu ? <IconCrossDark /> : <HamburgerIcon />}
        </button>
      </div>
    </header>
  );
}

export default AppHeader;
