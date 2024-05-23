from fetch_and_store import fetch_and_store_articles, get_articles_by_date
#from database_create import create_news_database, create_stock_database
from utility_functions import date_to_ISO_8601
from fetch_and_store_stocks import store_stock_data, get_stock_data_by_date, print_stock_data
from non_api_fetch_and_store_news import fetch_and_store_articles_from_sites, get_articles_by_date
from non_api_create_news_database import create_news_database
def main():
    #create_database()

    #fetch_and_store_articles(keyword='Apple', from_date='2024-04-23', to_date='2024-05-23')

    # articles = get_articles_by_date(date_to_ISO_8601('2024-05-01'), date_to_ISO_8601('2024-05-23'))
    # for article in articles:
    #     print(article)
    # create_stock_database()

    # store_stock_data('AAPL', 'Apple Inc.')
    # store_stock_data('MSFT', 'Microsoft Corporation')

    # # Query stock data by date
    # stocks = get_stock_data_by_date('2023-05-01', '2023-05-23')
    # print_stock_data(stocks)
    sites = [
    'https://www.onet.pl/',
    'https://www.tvn24.pl/',]
    create_news_database()
    fetch_and_store_articles_from_sites(sites)


if __name__ == "__main__":
    main()
