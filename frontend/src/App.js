// App.js

import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ProductPage from './components/ProductPage';
import Main from './components/Main';
import Settings from './components/Settings';
import NewsletterConfirmation from './components/NewsletterConfirmation';
import { ThemeProvider } from './components/ThemeContext';


function App() {
  const [tools, setTools] = useState([]);
  const [filteredTools, setFilteredTools] = useState([]);
  
  // Set 'Top 250' as the default selected category
  const [selectedCategory, setSelectedCategory] = useState('Top 250');

  useEffect(() => {
    let isMounted = true;  
    fetch(`${process.env.REACT_APP_BACKEND_URL}/api/tools/`)
      .then(response => response.json())
      .then(data => {
        if (isMounted) {
          const sortedTools = data.sort((a, b) => b.tts - a.tts);
          setTools(sortedTools);
          if (selectedCategory === 'Top 250') {
            setFilteredTools(sortedTools.slice(0, 250));
          } else {
            setFilteredTools(sortedTools.filter(tool => tool.category === selectedCategory));
          }
        }
      })
      .catch(error => console.error(error));
  
    return () => {
      isMounted = false;
    };
  }, [selectedCategory]);  

  const uniqueCategories = ['Top 250', ...new Set(tools.map(tool => tool.category))];

  const handleTagClick = (category) => {
    setSelectedCategory(category);
    if (category === 'Top 250') {
      const top250Tools = [...tools].sort((a, b) => b.tts - a.tts).slice(0, 250);
      setFilteredTools(top250Tools);
    } else {
      setFilteredTools(tools.filter(tool => tool.category === category));
    }
  };

  return (
    <ThemeProvider>
      <Router>
          <div>
              <Routes>
                  <Route path="/" element={
                      <Main 
                          handleTagClick={handleTagClick} 
                          selectedCategory={selectedCategory} 
                          uniqueCategories={uniqueCategories} 
                          filteredTools={filteredTools} 
                      />
                  } />
                  <Route path="/aitools/:toolName" element={
                      <>
                          <ProductPage tools={tools} />
                      </>
                  } />
                  <Route path="/settings" element={<Settings />} />
                  <Route path="/newsletter-confirmation" element={
                    <NewsletterConfirmation 
                      handleTagClick={handleTagClick} 
                      selectedCategory={selectedCategory} 
                      uniqueCategories={uniqueCategories} 
                      filteredTools={filteredTools} 
                    />
                  } />
              </Routes>
          </div>
      </Router>
    </ThemeProvider>
  );
}

export default App;
