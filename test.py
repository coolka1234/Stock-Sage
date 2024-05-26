from fetch_and_store import fetch_and_store_articles, get_articles_by_date
from database_create import create_news_database, create_stock_database, delete_news_database, delete_stock_database
from utility_functions import date_to_ISO_8601
from fetch_and_store_stocks import store_stock_data, get_stock_data_by_date, print_stock_data
#from non_api_fetch_and_store_news import fetch_and_store_articles_from_sites, get_articles_by_date
#from non_api_create_news_database import create_news_database
from non_api_create_stocks_database import create_stock_database, delete_stock_database
from non_api_fetch_and_store_stocks import fetch_and_store_stock_data, get_stock_data_by_date, print_stock_data
from update_api_scrape import update_all_news, find_all
from newsapi import NewsApiClient, const
def main():
    # # delete_news_database()
    # # create_news_database()
    # delete_stock_database()
    # for i in range(1, 18):
    #     if(i<10):
    #         day=str('0'+str(i))
    #     else:
    #         day=str(i)
    #     fetch_and_store_articles(keyword='Microsoft', from_date='2024-05-01', to_date=''.join(['2024-05-',day]))
    # fetch_and_store_articles(keyword='Apple', from_date='2024-04-24', to_date='2024-05-19')
    # create_stock_database()
    # fetch_and_store_stock_data('AAPL', 'Apple Inc.')
    # fetch_and_store_stock_data('GOOGL', 'Google Inc.')
    # update_all_news()
    # fetch_and_store_articles(keyword='Apple', from_date='2024-04-26T19:56:00', to_date='2024-05-25T00:00:00', language='en', sort_by='publishedAt')
#     2024-04-26T19:56:00
# 2024-05-25T00:00:00
# Apple
# en
# publishedAt
    print("")
if __name__ == "__main__":
    main()
