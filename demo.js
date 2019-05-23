const puppeteer = require('puppeteer');
const CREDS = require('./creds.js');

const CANVAS_SELECTOR = '#validate-big';
const BLOCK_SELECTOR = '#verify-bar-box > div.validate-main > img.validate-block';
const DRAG_BUTTON_SELECTOR = '#validate-drag-wrapper > div.validate-drag-button > img';

(async () =>{
    const browser =  await puppeteer.launch({
        headless: false
    });
    const page = await browser.newPage();
    await page.goto('https://star.toutiao.com/login?role=ad');
    const USERNAME_SELECTOR = '#user-name';
    const PASSWORD_SELECTOR = '#password';
    const BUTTON_SELECTOR = '#bytedance-SubmitStatic';
    
    await page.click(USERNAME_SELECTOR);
    await page.type(USERNAME_SELECTOR, CREDS.username);

    await page.click(PASSWORD_SELECTOR);
    await page.type(PASSWORD_SELECTOR, CREDS.password);
    
    await page.click(BUTTON_SELECTOR);
    
    await page.waitForNavigation();

    const cookies = await page.cookies();
    let cookie_strArray = []
    cookies.forEach(function(cookie, index){
        cookie_strArray.push(cookie.name +"="+cookie.value);
    });
    console.log(cookie_strArray.join("; "));
    await browser.close()
})();