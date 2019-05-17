# moneybot-scrapper
This application scraps live stock data and news from financial website and Google News and saves to Mongodb.

# Technical Specifications:
1. We are using BeautifulSoup for scrapping current stock prices 
2. Goggle News api to get latest stock news.

# Installation requirements:
1. First generate your own google news api key from here: https://newsapi.org/
## There are two jobs that's running.
### First app:(Collecting latest stock prices)
2. Go to project folder and run, docker build --tag=your_tag .
3. Then, docker run --network="host" --env-file=/path/to/your/env/file image_id
### Second app:(Collecting latest stock news from Google News)
4. Run, pip install -r requirements.txt




