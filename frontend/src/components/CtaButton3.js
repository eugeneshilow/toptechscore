// CtaButton3.js

import React, { useContext } from 'react';
import ThemeContext from './ThemeContext';

function CtaButton3() {
  const { theme } = useContext(ThemeContext);  // removed toggleTheme
  const viewDetails = () => {
    // This is where you would implement the view details functionality
    console.log("View details");
  };

  return (
    <div className={`ctabutton3-container ${theme}`}>
      <div className="ctabutton3-image-section"></div>
      <div className="ctabutton3-text-section">
        <p>Learn how I am creating Findex without engineering background.</p>
      </div>
      <div className="ctabutton3-button-section">
        <button className="ctabutton3" onClick={viewDetails}>
          <span>Learn</span>
        </button>
      </div>
    </div>
  );
}

export default CtaButton3;

