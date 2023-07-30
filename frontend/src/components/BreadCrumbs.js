import React from 'react';
import '../styles/BreadCrumbs.css';


function generateBreadcrumbs(type, category, sub_category) {
  let breadcrumbs = [
    <span key="home" className="breadcrumbs-text">
      <span className="breadcrumbs-logo"></span>
    </span>
  ];

  if (type) {
    breadcrumbs.push(<span key="arrow1" className="breadcrumbs-arrow"> → </span>);
    breadcrumbs.push(<span key={type} className="breadcrumbs-text">{type}</span>);
  }

  if (category) {
    breadcrumbs.push(<span key="arrow2" className="breadcrumbs-arrow"> → </span>);
    breadcrumbs.push(<span key={category} className="breadcrumbs-text">{category}</span>);
  }

  if (sub_category) {
    breadcrumbs.push(<span key="arrow3" className="breadcrumbs-arrow"> → </span>);
    breadcrumbs.push(<span key={sub_category} className="breadcrumbs-text">{sub_category}</span>);
  }

  return breadcrumbs;
}

function BreadCrumbs({ type, category, sub_category }) {
  const breadcrumbs = generateBreadcrumbs(type, category, sub_category);

  return <p className="breadcrumbs-container">{breadcrumbs}</p>;
}

export default BreadCrumbs;
