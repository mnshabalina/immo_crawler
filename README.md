## Immobilien Überwacher App

Crawls wg-gesucht.de for immobilien adds and represents found data in a table.

### To start backend

1. Install required python libraries

`pip install requirements.txt`

2. Start the dev server

`python app.py`


### To start frontend

1. Move to frontend directory

`cd frontend`

2. Install required node modules

`npm install`

3. Start the dev server

`npm start`

### Possible problems

1. Crawler can get outdated and fail due to changes to the website's HTML. 
    In this case you need to update selectors in crawler.py

2. In case of driver not found error, add path to the app folder to Path as it contains the driver.

3. Driver can get outdated due to new releases of Google Chrome. 
    You can download new driver [here](https://chromedriver.chromium.org/downloads).