import React, { createContext, useState, useEffect } from 'react';

const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('dark');  // Changed from 'light' to 'dark'

  // Change the theme of the application
  const toggleTheme = () => {  // Removed event argument and preventDefault call
    setTheme((prevTheme) => prevTheme === 'dark' ? 'light' : 'dark');  // Fixed ternary operator
  };

  // Use effect to update the data-theme attribute whenever the theme changes
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export default ThemeContext;
