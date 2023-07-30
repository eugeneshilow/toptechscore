import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { HeartEmptyIconBlack2 } from '../assets/SvgComponents';
import '../styles/Table.css';

// Helper function to create a URL-friendly slug from a string
function createSlug(name) {
  return name.toLowerCase().replace(/\s+/g, '-');
}

function AppTable({ filteredTools }) {
  const [isMobile, setIsMobile] = useState(window.innerWidth <= 768);

  // Add a resize listener
  useEffect(() => {
    const handleResize = () => setIsMobile(window.innerWidth <= 768);
    window.addEventListener('resize', handleResize);

    // Cleanup function to remove the listener when the component unmounts
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return (
    <table className="table">
      <thead>
        <tr>
          {!isMobile && <th className="column-icon"></th>} {/* Empty heading for the new column */}
          <th className="column-number">#</th>
          <th className="column-name">Name {isMobile && "and Description"}</th>
          <th className="column-es-score">ES Score</th>
          {!isMobile && <th className="column-popularity hide-on-mobile">Popularity</th>}
          {!isMobile && <th className="column-engagement hide-on-mobile">Engagement</th>}
          {!isMobile && <th className="column-category hide-on-mobile">Category</th>}
          {!isMobile && <th className="column-sub-category hide-on-mobile">Sub-category</th>}
          {!isMobile && <th className="column-description">Description</th>}
        </tr>
      </thead>
      <tbody>
        {filteredTools.map((tool, index) => (
          <tr key={tool.id}>
            {!isMobile && (
              <td className="column-icon">
                <button className="button-favorite">
                  <HeartEmptyIconBlack2 />
                </button>
              </td>
            )}
            <td data-label="#" className={`tool_id column-number ${isMobile ? 'mobile-number' : ''}`}>{index + 1}</td>
            <td data-label="Name" className="tool_name column-name">
              <Link to={`/aitools/${createSlug(tool.name)}`} className="tool-name-container">
                <img src={tool.favicon_url} alt="tool favicon" className="tool-favicon" />
                <em><span>{tool.name}</span></em>
              </Link>
              {isMobile && <p>{tool.brief_description}</p>}
              {isMobile && <p className="sub-category-mobile">{tool.sub_category}</p>}
            </td>
            <td data-label="ES Score" className="es-score column-es-score">
              {isMobile && (
                <button className="button-favorite">
                  <HeartEmptyIconBlack2 />
                </button>
              )}
              <span className="highlight">{parseFloat(tool.tts).toFixed(1)}</span>
            </td>
            {!isMobile && <td data-label="Popularity" className="column-popularity hide-on-mobile">{parseFloat(tool.popularity).toFixed(1)}</td>}
            {!isMobile && <td data-label="Engagement" className="column-engagement hide-on-mobile">{parseFloat(tool.engagement).toFixed(1)}</td>}
            {!isMobile && <td data-label="Category" className="column-category hide-on-mobile">{tool.category}</td>}
            {!isMobile && <td data-label="Sub-category" className="column-sub-category hide-on-mobile">{tool.sub_category}</td>}
            {!isMobile && <td data-label="Description" className="column-description">{tool.brief_description}</td>}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default AppTable;
