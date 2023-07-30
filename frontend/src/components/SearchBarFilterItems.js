import React from 'react';
import logoChatGPT from '../assets/logo-chatgpt.png';
import logoChrome from '../assets/logo-chrome.png';
import logoTensorFlow from '../assets/logo-tensorflow.png';

// FilterItem component
function FilterItem({ text, onFilterChange, isActive, icon, isDisabled }) {
  return (
    <div 
      className={`filter-item ${isActive ? 'active' : ''} ${isDisabled ? 'disabled' : ''}`}
      onClick={() => !isDisabled && onFilterChange(text)}
    >
      <img src={icon} alt={text} className="filter-icon" />
      <span className="filter-text">{text}</span>
    </div>
  );
}

function SearchBarFilterItems({ handleFilterChange, activeFilter }) {
  return (
    <div className="filter-items">
        <FilterItem text="Tools" icon={logoChatGPT} onFilterChange={handleFilterChange} isActive={activeFilter === 'Tools'} />
        <FilterItem text="Extensions" icon={logoChrome} onFilterChange={handleFilterChange} isActive={activeFilter === 'Extensions'} isDisabled={true} />
        <FilterItem text="Models" icon={logoTensorFlow} onFilterChange={handleFilterChange} isActive={activeFilter === 'Models'} isDisabled={true} />
    </div>
  );
}

export default SearchBarFilterItems;
