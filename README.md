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
4. Create a python virtual environment.
5. In project folder change update_articles.sh file with your venv path and update_articles.py file path.
6. run crontab -e
7. Enter */10 * * * * /path/to/update_articles.sh (Every 10 secs job will be activated and it will update with new articles.)
8. Save the file
9. Run, sudo systemctl restart cron





