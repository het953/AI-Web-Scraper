#!/usr/bin/env python3
from os import environ
from selenium.webdriver import Remote, ChromeOptions as Options
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection as Connection
from bs4 import BeautifulSoup


AUTH = "brd-customer-hl_9014200b-zone-ai_scraper:z48ph9ld3cld"
TARGET_URL = environ.get('TARGET_URL', default='https://example.com')


def scrape_website(website=TARGET_URL):
    print("Launching chrome browser...")

    server_addr = f'https://{AUTH}@brd.superproxy.io:9515'
    connection = Connection(server_addr, 'goog', 'chrome')
    driver = Remote(connection, options=Options())
    try:
        print(f'Connected! Navigating to {website}...')
        driver.get(website)
        print('Navigated! Waiting captcha to detect and solve...')
        result = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10 * 1000},
        })
        status = result['value']['status']
        print(f'Captcha status: {status}')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]