import React from 'react';
import parse from 'html-react-parser';
import '../styles/ProductPage.css';


function ProductDescription({ product }) {
  return (
    <div>
      {product.favicon_url && <img className="logo-product" src={product.favicon_url} alt={`${product.name} logo`} />}
      <div className="product-info">
        <h1>{product.name}</h1>
        <div className="es-score-wrapper">
          <p>ES Score <span className="highlight-productpage">{parseFloat(product.tts).toFixed(1)}</span></p>
        </div>
      </div>
      <div className="section">
        <p>{parse(product.brief_description)}</p>
      </div>
    </div>
  );
}

export default ProductDescription;
