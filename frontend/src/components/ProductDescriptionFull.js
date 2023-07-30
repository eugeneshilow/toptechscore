import React, { useState } from 'react';
import parse from 'html-react-parser';
import { IconChevronDownPrimary } from '../assets/SvgComponents';
import '../styles/ProductPage.css';

const ProductDescriptionFull = ({ product }) => {
    const [isExpanded, setIsExpanded] = useState(false);

    return (
        <div>
            {/* <h2>Description</h2> */}
            <div 
            className={`container-features ${isExpanded ? 'expanded' : 'collapsed'}`}
            >
            {product.key_features && parse(product.key_features)}
            {!isExpanded && <div className="fade-out"></div>}
            </div>
            {!isExpanded && 
            <p className="text-showmore" onClick={() => setIsExpanded(true)}>
            Show more
            <IconChevronDownPrimary /> {/* Add the SVG component here */}
            </p>
            }
        </div>
    );
};

export default ProductDescriptionFull;
