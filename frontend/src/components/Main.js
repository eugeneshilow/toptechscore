// Main.js

import React, { useState } from 'react';
import AppHeader from './Header';
import SearchBar from './SearchBar';
import SearchBarFilterItems from './SearchBarFilterItems'; // Importing the SearchBarFilterItems component
import AppTableHeader from './TableHeader';
import AppTable from './Table';
import NewsletterSubscription from './NewsletterSubscription';
import OneLine from './OneLine';
import CtaButton4 from './CtaButton4';
import AppFooter from './Footer';
import SocialMediaLinks from './SocialMediaLinks';

function Main({ handleTagClick, selectedCategory, uniqueCategories, filteredTools }) {
    const [activeFilter, setActiveFilter] = useState('Tools');

    const handleFilterChange = (filter) => {
        setActiveFilter(filter);
        console.log(`Filter changed to: ${filter}`);
        // Here you can update the search context based on the selected filter
    };

    return (
        <>            
            <div className="section-blue">
                <div className="container-zeromargins">
                    <AppHeader />
                </div>
            </div>

            <div className="section-blue">
                <div className="container-zeromargins">
                    <OneLine />
                </div>
            </div>
            
            <div className="section-blue">
                <div className="container-zeromargins">
                    <SearchBarFilterItems handleFilterChange={handleFilterChange} activeFilter={activeFilter} /> 
                </div>
            </div>

            <div className="section-blue search-section-sticky">
                <div className="container-zeromargins">
                    <SearchBar />
                </div>
            </div>

            <div className="section-lightgrey tag-section-sticky">
                <div className="container-zeromargins padding-buffer">
                    <AppTableHeader 
                        handleTagClick={handleTagClick} 
                        selectedCategory={selectedCategory} 
                        uniqueCategories={uniqueCategories} 
                    />
                </div>
            </div>

            <div className="section-white">
                <div className="container-zeromargins">
                    <AppTable filteredTools={filteredTools} />
                </div>
            </div>
            {/* <NewsletterSubscription /> */}
            
            {/* <div className="section-white ctabutton3-section-sticky">
                <div className="container-zeromargins"> */}
                    <CtaButton4 />
                {/* </div>
            </div>         */}

            <SocialMediaLinks />
        
            <AppFooter />
      
        </>
    );
}

export default Main;