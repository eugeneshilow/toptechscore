import React, { useState } from 'react';
import { GiftBox, HeartEmptyIconWhite } from '../assets/SvgComponents';

function CtaButton2() {
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

  const shareWithFriends = () => {
    // This is where you would implement the share with friends functionality
    console.log("Share with friends");
  };

  return (
    <div className="ctabutton2-container">        
      <button className="ctabutton2 ctabutton-red" onClick={addToFavorites}>
        <span>Favorite</span>
        <HeartEmptyIconWhite />
      </button>
      <button className="ctabutton2 ctabutton-blue" onClick={shareWithFriends}>
        <span>Share</span>
        <GiftBox />
      </button>
    </div>
  );  
}

export default CtaButton2;
