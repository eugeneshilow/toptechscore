import React from 'react';
import '../styles/Table.css';


function AppTableHeader({ handleTagClick, selectedCategory, uniqueCategories }) {
    return (
        <div className="tag-section">
            {uniqueCategories.map((category, index) => (
                <div
                    key={index}
                    className={selectedCategory === category ? 'tag-selected' : 'tag'}
                    onClick={() => handleTagClick(category)}
                >
                    {category}
                </div>
            ))}
        </div>
    );
}

export default AppTableHeader;
