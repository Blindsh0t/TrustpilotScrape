# TrustpilotScrape
Scrape Trustpilot for required info and save information locally

## Project scope
1. Get Categoric companies available after search
2. Navigate to each companies individual page
3. Extract `Name, website, email, phone, address`
4. Save locally

## Issues
- Cant use a headless browsing option (no output data)
- target page details sometimes not scrapable when request coming from whole program, if tried to scrape individually it returned the result [EG:](https://uk.trustpilot.com/review/comparethediamond.com)
- Dosent load the content after 10 ~ 15 pages scraped `We have received an unusually large amount of requests from your IP so you have been rate limited`
