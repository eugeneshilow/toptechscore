import React from 'react';
import { IconSearch, IconArrowBack, HeartEmptyIconBlack, HeartFilledIconBlack, ShareIcon } from '../assets/SvgComponents';
import '../styles/ProductPage.css';

const ProductPageHeader = ({ isFavourite, handleFavourite }) => {

  const handleShare = () => {
    // handle share logic here
  };

  return (
    <div className="product-page-header">
      <IconArrowBack className="icon-arrowback" /> {/* GoBackArrowIcon without onClick event */}
      <div className="search-container">
        <input className="search-bar" type="text" placeholder="Search AI on Findex" />
        <IconSearch className="icon-search" />
      </div>
      {isFavourite ? 
        <HeartFilledIconBlack onClick={handleFavourite} className="icon-heart" /> : 
        <HeartEmptyIconBlack onClick={handleFavourite} className="icon-heart" />
      }
      <ShareIcon className="icon-share" onClick={handleShare} />
    </div>
  );
};

export default ProductPageHeader;
