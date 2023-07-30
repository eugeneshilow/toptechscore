// AppFooter.js

import React from 'react';

const AppFooter = ({ style }) => {
  const menuItems = ['Categories', 'Learn', 'Advertise', 'About'];
  const legalItems = ['Privacy Policy', 'Terms & Conditions'];

  return (
    <footer className="footer" style={style}>
      <div className="footer-menu">
        {menuItems.map((item, index) => (
          <React.Fragment key={item}>
            <a href="#">{item}</a>
            {index < menuItems.length - 1 && <span> • </span>}
          </React.Fragment>
        ))}
      </div>
      <div className="footer-legal">
        {legalItems.map((item, index) => (
          <React.Fragment key={item}>
            <a href="#">{item}</a>
            {index < legalItems.length - 1 && <span> • </span>}
          </React.Fragment>
        ))}
      </div>
      <div className="footer-copyright">
        © 2023 Findex — Find Your AI
      </div>
    </footer>
  );
};

export default AppFooter;
