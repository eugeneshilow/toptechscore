import React, { useState } from 'react';

function CtaButton1() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);  // Simulated logged in state

  const addToFavorites = () => {
    if(isLoggedIn) {
      // Add tool to the user's favorite tools
      // This is where you would make the API call to add the tool to the user's favorites
      console.log("Tool added to favorites");
    } else {
      // Prompt the user to log in
      console.log("Please log in to add tools to your favorites");
    }
  };

  return (
    <section className="section-white ctabutton-container">
        <div className="container">
            <button className="ctabutton1" onClick={addToFavorites}>Add to favorites</button>
        </div>
    </section>
  );
}

export default CtaButton1;
