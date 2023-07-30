import React from 'react';
import parse from 'html-react-parser';
import '../styles/ProductPage.css';

const ProductPricing = ({ pricing }) => (
  <div className="container-pricing">
    <h2 className="subtitle">Pricing</h2>
    {pricing && parse(pricing)}
  </div>
);

export default ProductPricing;
