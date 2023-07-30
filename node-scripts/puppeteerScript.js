const puppeteer = require('puppeteer');
const fs = require('fs');

console.log('Script started.');

(async () => {
    try {
        const websiteUrl = process.argv[2];  // Get the website URL from command line arguments
        if (!websiteUrl) {
            console.error('Please provide a website URL as a command line argument');
            process.exit(1);
        }

        console.log(`Website URL: ${websiteUrl}`);

        const cookies = JSON.parse(fs.readFileSync('/Users/eugeneshilov/Dropbox/1. Business/TopTechScore/toptechscore-root/node-scripts/perplexity_cookies.json', 'utf8'));
        console.log('Cookies loaded.');

        const browser = await puppeteer.launch({headless: true});
        console.log('Browser launched.');

        const page = await browser.newPage();
        console.log('New page opened.');

        // Set cookies in the Puppeteer browser
        await page.setCookie(...cookies);
        console.log('Cookies set in the browser.');

        await page.goto('https://www.perplexity.ai', {waitUntil: 'networkidle2'});
        console.log('Navigated to https://www.perplexity.ai.');

        await page.waitForSelector('textarea');
        console.log('Textarea found.');

        await page.focus('textarea');
        console.log('Textarea focused.');

        await page.keyboard.type(`Give description in 10 words or less of the website ${websiteUrl}. (if not able to access the website, use information from the web search). Focus on the problem user can achieve using this website in form - 'solve this issue by doing x'. Do not ask any follow-up questions and answer right away. If no information is available, write None. Do not mention the name of the website in your output.`);
        console.log('Typed the description request.');

        await page.keyboard.press('Enter');
        console.log('Pressed enter.');

        await page.waitForTimeout(10000);
        console.log('Waited for 10 seconds.');

        const response = await page.evaluate(() => {
            const element = document.querySelector('.pb-md:last-child .prose');
            return element ? element.innerText : null;
        });

        console.log('Response evaluated.');

        // If response is empty, take a screenshot
        if (!response) {
            await page.screenshot({ path: 'error.png' });
            console.log('Screenshot taken.');
        }

        fs.writeFileSync('description_output.txt', response);
        console.log('Response written to file.');

        await browser.close();
        console.log('Browser closed.');
    } catch (error) {
        console.error(`Error: ${error}`);
    }
})();

console.log('Script finished.');
