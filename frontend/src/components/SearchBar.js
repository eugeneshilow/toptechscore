// SearchBar.js

import React, { useState } from 'react';
import '../styles/SearchBar.css';

function SearchBar() {
  return (
    <div>
      <input type="text" className="field-input search-input" placeholder="Find your AI tool" />
    </div>
  );
}

export default SearchBar;