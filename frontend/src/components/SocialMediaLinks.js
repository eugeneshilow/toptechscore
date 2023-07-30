// SocialMediaLinks.js

import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTwitter, faTiktok, faLinkedin, faInstagram, faYoutube } from '@fortawesome/free-brands-svg-icons';

const SocialMediaLinks = () => (
    <div className="socialmedialinks-container">
        <a href="https://twitter.com/eugeneshilow" target="_blank" rel="noreferrer">
            <FontAwesomeIcon icon={faTwitter} className="socialmedialinks-icon" />
        </a>
        <a href="https://www.tiktok.com/@eugeneshilow" target="_blank" rel="noreferrer">
            <FontAwesomeIcon icon={faTiktok} className="socialmedialinks-icon" />
        </a>
        {/* <a href="https://www.threads.net/@eugeneshilow" target="_blank" rel="noreferrer">
            <FontAwesomeIcon icon={faThreads} className="socialmedialinks-icon" />
        </a> */}
        <a href="https://www.instagram.com/eugeneshilow" target="_blank" rel="noreferrer">
            <FontAwesomeIcon icon={faInstagram} className="socialmedialinks-icon" />
        </a>
        <a href="https://www.linkedin.com/in/eugeneshilow" target="_blank" rel="noreferrer">
            <FontAwesomeIcon icon={faLinkedin} className="socialmedialinks-icon" />
        </a>
        <a href="https://www.youtube.com/@eugeneshilow" target="_blank" rel="noreferrer">
            <FontAwesomeIcon icon={faYoutube} className="socialmedialinks-icon" />
        </a>
    </div>
);

export default SocialMediaLinks;
