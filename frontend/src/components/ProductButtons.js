import React from 'react';
import { IconCaretUp, IconLink } from '../assets/SvgComponents';
import '../styles/ProductPage.css';

function ProductButtons({ product }) {
  return (
    <div className="button-2-container">
      <button className="button-2 button-2-visit">
        Visit
      </button>
      <button className="button-2 button-2-upvote">
        <IconCaretUp /> Upvote {product.vote_count}
      </button>
    </div>
  );
}

export default ProductButtons;




{/* <button className="button">Favorite</button>
<button className="button">Share</button> */}