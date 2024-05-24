from fetch_and_store import fetch_and_store_articles, get_articles_by_date
from database_create import create_news_database, create_stock_database, delete_news_database, delete_stock_database
from utility_functions import date_to_ISO_8601
from fetch_and_store_stocks import store_stock_data, get_stock_data_by_date, print_stock_data
#from non_api_fetch_and_store_news import fetch_and_store_articles_from_sites, get_articles_by_date
#from non_api_create_news_database import create_news_database
from non_api_create_stocks_database import create_stock_database
from non_api_fetch_and_store_stocks import fetch_and_store_stock_data, get_stock_data_by_date, print_stock_data
from update_api_scrape import update_all_news
def main():
    # delete_news_database()
    # create_news_database()

    # fetch_and_store_articles(keyword='Apple', from_date='2024-04-24', to_date='2024-05-23')
    # create_stock_database()
    # fetch_and_store_articles_from_sites(sites)
    # create_stock_database()
    # fetch_and_store_stock_data('AAPL', 'Apple Inc.')
    # fetch_and_store_stock_data('MSFT', 'Microsoft Corporation')
    #update_all_news()
    print("")

if __name__ == "__main__":
    main()
