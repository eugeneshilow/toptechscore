// Settings.js

import React, { useContext } from 'react';
import ThemeContext from './ThemeContext';
import '../styles/ToggleSwitch.css';

function Settings() {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <div>
      <h1>Settings</h1>
      <div className="toggle-switch">
        <input 
          type="checkbox" 
          id="theme-toggle" 
          checked={theme === 'dark'} 
          onChange={toggleTheme}
        />
        <label htmlFor="theme-toggle">
          <span className="toggle-track"></span>
          <span className="toggle-thumb"></span>
          {theme === 'dark' ? 'Dark' : 'Light'}
        </label>
      </div>
    </div>
  );
}

export default Settings;
