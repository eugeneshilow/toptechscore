import React, { useState, useRef } from 'react';
import ReactPlayer from 'react-player/youtube';
import '../styles/MediaCarousel.css';

function MediaCarousel({ product, currentIndex, handleScroll, width, playing, setPlaying }) {
  const videoHeight = width * 9 / 16; // Assuming a 16:9 aspect ratio
  const totalItems = 1 + product.explanation_photos.length; // 1 for video, rest for photos

  const handleCarouselScroll = (event) => {
    handleScroll(event);
    setPlaying(false);
  };

  return (
    <div className="media-carousel-container">
      <div className="media-carousel" onScroll={handleCarouselScroll}>
        <div className="media-item">
          <ReactPlayer
            url={product.review_video}
            width="100%"
            height={videoHeight}
            playing={playing}
            controls={true}
            onPause={() => setPlaying(false)}
            onPlay={() => setPlaying(true)}
          />
          {!playing && <div className="overlay" onClick={() => setPlaying(true)}></div>}
        </div>
        {product.explanation_photos.map((photo, index) => (
          <div className="media-item" style={{ height: videoHeight, overflow: 'hidden' }}>
            <img src={photo.image_url} alt={`${product.name} screenshot ${index + 1}`} key={index} style={{ objectFit: 'contain', width: '100%', height: '100%' }} />
          </div>
        ))}
      </div>

      {/* <div className="dot-container">
        {[...Array(totalItems)].map((_, index) => (
          <span className={`dot ${index === currentIndex ? 'dot-selected' : ''}`}></span>
        ))}
      </div> */}

      <div className="media-tracker">
        <span>{currentIndex + 1}/{totalItems}</span>
      </div>
    </div>
  );
}

export default MediaCarousel;