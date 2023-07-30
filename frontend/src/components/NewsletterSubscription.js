import React, { useState } from 'react';
import '../styles/NewsletterSubscription.css';


const NewsletterSubscription = () => {
  const [email, setEmail] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // Add your API request to subscribe the user to the newsletter here
    console.log(`Submitting Email: ${email}`);
  };

  return (
    <div className="newsletter-container">
      <div className="newsletter-content">
        <h2 className="newsletter-title">Be the first to know about</h2>
        <h3 className="newsletter-subtitle">crypto news every day</h3>
        <p className="newsletter-description">Get crypto analysis, news and updates right to your inbox! Sign up here so you don't miss a single newsletter.</p>
        <form className="newsletter-form" onSubmit={handleSubmit}>
          <input
            className="newsletter-input"
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={e => setEmail(e.target.value)}
            required
          />
          <button className="newsletter-button" type="submit">Subscribe now</button>
        </form>
      </div>
    </div>
  );
};

export default NewsletterSubscription;
