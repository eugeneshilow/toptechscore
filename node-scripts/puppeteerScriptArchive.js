const puppeteer = require('puppeteer');
const fs = require('fs');

console.log('Script started.');

try {
    (async () => {
        const websiteUrl = process.argv[2];  // Get the website URL from command line arguments
        if (!websiteUrl) {
            console.error('Please provide a website URL as a command line argument');
            process.exit(1);
        }

        console.log(`Website URL: ${websiteUrl}`);

        const cookies = JSON.parse(fs.readFileSync('perplexity_cookies.json', 'utf8'));
        const browser = await puppeteer.launch({headless: false});
        const page = await browser.newPage();

        // Set cookies in the Puppeteer browser
        await page.setCookie(...cookies);
    
        await page.goto('https://www.perplexity.ai', {waitUntil: 'networkidle2'});
        console.log('Navigated to Perplexity website');

        await page.waitForSelector('textarea');
        await page.focus('textarea');
        await page.keyboard.type(`Give description in 10 words or less of the website ${websiteUrl}. (if not able to access the website, use information from the web search). Focus on the problem user can achieve using this website in form - 'solve this issue by doing x'. Do not ask any follow-up questions and answer right away. If no information is available, write None. Do not mention the name of the website in your output.`);
        await page.keyboard.press('Enter');
        console.log('Entered description request');

        await page.waitForTimeout(10000);

        const response = await page.evaluate(() => {
            const element = document.querySelector('.pb-md:last-child .prose');
            return element ? element.innerText : null;
        });
        console.log('Got response');

        // If response is empty, take a screenshot
        if (!response) {
            await page.screenshot({ path: 'error.png' });
        }

        console.log(response);
    
        await browser.close();
    })();
} catch (error) {
    console.error(`Error: ${error.message}`);
}

console.log('Script finished.');
