// NewsletterConfirmation.js

import React, { useState } from 'react';
import Modal from 'react-modal';
import Main from './Main';
import '../styles/NewsletterConfirmation.css';

const NewsletterConfirmation = ({ handleTagClick, selectedCategory, uniqueCategories, filteredTools }) => {
  const [modalIsOpen, setModalIsOpen] = useState(true);

  const closeModal = () => {
    setModalIsOpen(false);
  };

  return (
    <>
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        contentLabel="Newsletter Confirmation Modal"
        className="newsletterConfirmationModal"
        overlayClassName="newsletterConfirmationOverlay"
      >
        <h1 className="font-white">Email Confirmed!</h1>
        <p style={{ textAlign: "Center" }}>Thank you for confirming your email. Click OK to continue exploring AI tools on Findex.</p>
        <button className="button5 button-ok" onClick={closeModal}>OK</button>
      </Modal>

      <Main 
        handleTagClick={handleTagClick} 
        selectedCategory={selectedCategory} 
        uniqueCategories={uniqueCategories} 
        filteredTools={filteredTools} 
      />
    </>
  );
};

export default NewsletterConfirmation;
