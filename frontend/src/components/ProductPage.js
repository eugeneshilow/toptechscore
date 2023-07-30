// ProductPage.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import MediaCarousel from './MediaCarousel';
import ProductPageHeader from './ProductPageHeader';
import BreadCrumbs from './BreadCrumbs';
import ProsConsContainer from './ProsConsContainer';
import ProductDescriptionFull from './ProductDescriptionFull';
import ProductDescription from './ProductDescription';
import ProductPricing from './ProductPricing';
import ProductButtons from './ProductButtons';
import CtaButton2 from './CtaButton2';
import AppFooter from './Footer';
import SocialMediaLinks from './SocialMediaLinks';

import '../styles/ProductPage.css';

function createSlug(name) {
  return name.toLowerCase().replace(/\s+/g, '-');
}

function getWindowDimensions() {
  const { innerWidth: width, innerHeight: height } = window;
  return {
    width,
    height
  };
}

function useWindowDimensions() {
  const [windowDimensions, setWindowDimensions] = useState(getWindowDimensions());

  useEffect(() => {
    function handleResize() {
      setWindowDimensions(getWindowDimensions());
    }

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return windowDimensions;
}

function ProductPage({ tools }) {
  const { toolName } = useParams();
  const [product, setProduct] = useState(null);
  const [currentIndex, setCurrentIndex] = useState(0);
  const { width } = useWindowDimensions();
  const [playing, setPlaying] = useState(false);
  const [isFavourite, setIsFavourite] = useState(false);

  useEffect(() => {
    const tool = tools.find(tool => createSlug(tool.name) === toolName);
    setProduct(tool);
  }, [toolName, tools]);

  const handleScroll = (e) => {
    const element = e.target;
    const { scrollWidth, clientWidth, scrollLeft } = element;
    const childWidth = scrollWidth / (1 + product.explanation_photos.length);
    setPlaying(false);
    setCurrentIndex(Math.round(scrollLeft / childWidth));
  }

  const handleFavourite = () => {
    setIsFavourite(!isFavourite);
  };

  if (!product) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <section className="section-lightgrey">      
          
        <div className="section-white">  
          <ProductPageHeader isFavourite={isFavourite} handleFavourite={handleFavourite} />
        </div>

        <div className="container-zeromargins">
          <BreadCrumbs type={product.type} category={product.category} sub_category={product.sub_category} />
        </div>
        
        <div className="container container-bottom section-white">
          <ProductDescription product={product} />
        </div>
        
        <div className="container container-toptobottom section-white">
          <ProductButtons product={product} />
        </div>

        <div className="section-white">
          <MediaCarousel product={product} currentIndex={currentIndex} handleScroll={handleScroll} width={width} playing={playing} setPlaying={setPlaying} />
        </div>



        <div className="container container-top section-white">
          <ProductDescriptionFull product={product} />
        </div>
        
        <div className="container section-white">
          <ProsConsContainer product={product} />
        </div>
        
        <div className="container section-white">
          <ProductPricing pricing={product.pricing} />
        </div>

        <div className="section-white">
          <CtaButton2 />
        </div>

        <SocialMediaLinks />
        
        <AppFooter style={{ marginBottom: '52px' }} />
      
      </section>
    </div>
  );
}

export default ProductPage;
