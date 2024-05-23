from fetch_and_store import fetch_and_store_articles, get_articles_by_date
from database_create import create_database
from utility_functions import date_to_ISO_8601
def main():
    #create_database()

    #fetch_and_store_articles(keyword='Apple', from_date='2024-04-23', to_date='2024-05-23')

    articles = get_articles_by_date(date_to_ISO_8601('2024-05-01'), date_to_ISO_8601('2024-05-23'))
    for article in articles:
        print(article)

if __name__ == "__main__":
    main()
