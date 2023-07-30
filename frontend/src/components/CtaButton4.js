import React, { useState, useContext, useRef, useEffect } from 'react';
import ThemeContext from './ThemeContext';
import validator from 'email-validator';
import GmailIcon from '../assets/logo-gmail.svg';
import '../styles/CtaButton.css';


function CtaButton4() {
  const { theme } = useContext(ThemeContext);
  const [isClicked, setIsClicked] = useState(false);
  const [showSubcontainer12, setShowSubcontainer12] = useState(false);
  
  const [isSendClicked, setIsSendClicked] = useState(false);
  const [isEmailSent, setIsEmailSent] = useState(false);

  const inputRef = useRef();
  const checkboxRef = useRef();

  const [isInputFocused, setIsInputFocused] = useState(false);
  const [isInputEmpty, setIsInputEmpty] = useState(true);

  const hasClickedSend = document.cookie.split(';').some((item) => item.trim().startsWith('hasClickedSend='));

  // don't render if the user has clicked "Send" before
  if (hasClickedSend) {
    return null;
  }

  const viewDetails = () => {
    setIsClicked(true);
    setShowSubcontainer12(true);
  };

  const handleInputChange = (event) => {
    setIsInputEmpty(event.target.value === '');
  };

  useEffect(() => {
    // do nothing
  }, [isClicked]);

  const sendEmail = () => {
    setIsSendClicked(true);
    
    const email = inputRef.current.value;
    if (validator.validate(email)) {
      fetch(`${process.env.REACT_APP_BACKEND_URL}/api/tools/subscribe_newsletter/`, { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
        }),
      })
      .then(response => {
        console.log('HTTP status:', response.status);
        console.log('Response:', response);
        return response.json();
      })
      .then(data => {
        console.log('Success:', data);
        // handle success (e.g. show success message)
        setIsEmailSent(true);
        setShowSubcontainer12(false); // hide the subcontainer12

        // set a cookie here
        document.cookie = "hasClickedSend=true; path=/; max-age=31536000";  // expires in 1 year
      })
      .catch((error) => {
        console.error('Error:', error);
        // handle error (e.g. show error message)
      });
    } else {
      // email is not valid, show an error message...
    }
  };

  return (
    <div className={`ctabutton4-container ${theme}`}>
      <div className="ctabutton4-subcontainer1">
        <div className="ctabutton4-subcontainer11">
          <div className={`ctabutton4-container-imagetext ${isClicked ? 'out-of-screen ' : ''}`}>
            <div className="ctabutton4-image-section"></div>
            <div className="ctabutton4-text-section">
              Learn how I create Findex with no engineering background.
            </div>
          </div>
          
          <div className="ctabutton4-button-section">
            <button 
              className={`ctabutton4 button-learn ${isClicked ? 'button-transition hide-button' : 'initial-position'}`}
              onClick={viewDetails}
            >
              <span>Learn</span>
            </button>
          </div>

          <div className={`ctabutton4-container-emailinput ${isEmailSent ? 'out-of-screen' : 'initial-position'}`}>            
            <input 
              id="email-input"
              type="text"
              ref={inputRef}
              className={`email-input ${isClicked ? 'button-transition' : 'initial-position'} ${isInputFocused ? 'focused' : ''}`}
              onFocus={() => setIsInputFocused(true)}
              onBlur={() => setIsInputFocused(false)}
              onChange={handleInputChange}
            />
            <label htmlFor="email-input" className={`email-label ${isClicked && !isSendClicked ? 'show' : 'hide'}`}>Email</label>
            <label htmlFor="email-input" className={`email-example ${isInputFocused && isInputEmpty ? 'show' : 'hide'}`}>john@domain.com</label>
          </div>
          
          <div className={`ctabutton4-section-sendemail ${isEmailSent ? 'hide' : ''}`}>
            <button 
              className={`ctabutton4 send-email ${isClicked ? 'button-transition' : 'initial-position'}`}
              onClick={sendEmail}
            >
              <span>Send</span>
            </button>
          </div>

          <div className="ctabutton4-container-emailinstructions">
            <div className={`email-instructions ${isEmailSent ? 'show' : ''}`}>
              Check your inbox and spam to verify your account!
            </div>
          </div>

          <div className={`ctabutton4-container-opengmail ${isEmailSent ? 'show' : ''}`}>
            <button 
              className={`ctabutton4 button-checkgmail ${isEmailSent ? 'button-transition' : 'initial-position'}`}
              onClick={sendEmail}
            >
              <span>Open Gmail</span>
              <img src={GmailIcon} alt="Gmail logo" className="gmail-icon" />
            </button>
          </div>


        </div>
        
        <div className={`ctabutton4-subcontainer12 newsletter-agreement ${showSubcontainer12 ? 'show' : 'hide'}`}>
          {/* <input ref={checkboxRef} type="checkbox" id="newsletter-agreement" name="newsletter-agreement" /> */}
          <label htmlFor="newsletter-agreement">I consent to receiving the newsletter upon submission.</label>
        </div>
      </div>
    </div>
  );
}

export default CtaButton4;
