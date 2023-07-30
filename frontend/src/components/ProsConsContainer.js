import React, { useState } from 'react';
import parse, { domToReact } from 'html-react-parser';
import { IconCheckmark, IconCrossmark } from '../assets/SvgComponents';
import '../styles/ProductPage.css';

function ProsConsContainer({ product }) {
  const [show, setShow] = useState('pros');  // 'pros' is displayed by default

  const options = {
    replace: ({ name, children }) => {
      if (name === 'li') {
        return show === 'pros' ? (
          <li className="li-pros">
            <IconCheckmark />
            {domToReact(children, options)}
          </li>
        ) : (
          <li className="li-cons">
            <IconCrossmark />
            {domToReact(children, options)}
          </li>
        );
      }
    },
  };

  return (
    <div>
      <div>
        <button
          className={`button-1 ${show === 'pros' ? 'button-1-active' : ''}`}
          onClick={() => setShow('pros')}
        >
          Pro's
        </button>
        <button
          className={`button-1 ${show === 'cons' ? 'button-1-active' : ''}`}
          onClick={() => setShow('cons')}
        >
          Con's
        </button>
      </div>

      <div className="container-button1-text">
        {product && product.pros && show === 'pros' && (
            <div className="section-pros">
            {parse(product.pros, options)}
            </div>
        )}

        {product && product.cons && show === 'cons' && (
            <div className="section-cons">
            {parse(product.cons, options)}
            </div>
        )}
      </div>
    </div>
  );
}

export default ProsConsContainer;
