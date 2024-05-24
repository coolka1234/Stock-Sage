import sqlite3
import NewsFeature
import csv
def update_single_news_row(name, data, index):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute(f'UPDATE articles SET {name} = ? WHERE url = ?', (data, index))
    conn.commit()
    conn.close()

def companies_of_interest():
    companies = []
    with open('companies_of_interest.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            companies.append(row[0])
    return companies

def contains_any(string, string_list):
    return any(s in string for s in string_list)

def find_all(string, string_list):
    list= [s for s in string_list if s in string]
    print(list)
    return list

def scrape_content(url):
    from bs4 import BeautifulSoup
    import requests
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all('p')
    data = ''
    for i in content:
        data += i.text
    return data

def update_all_news():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    table_name = 'articles'
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]
    companies_of_interest_list = companies_of_interest()
    for i in range(1, row_count+1):
        curr_news= NewsFeature.NewsFeature(i)
        row = curr_news.row
        url = curr_news.url
        if('chars' in curr_news.content):
            data = scrape_content(url)
            update_single_news_row('content', data, url)
        companies = ''.join(find_all(row[7], companies_of_interest_list)) 
        cursor.execute('UPDATE articles SET companies = ? WHERE id = ?', (companies, row[0]))
        conn.commit()
    conn.close()