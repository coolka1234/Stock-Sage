from logging import config
from newspaper import Config
config = Config()
config.fetch_images = False
#config.MAX_AUTHORS = 1
#config.MIN_WORD_COUNT = 100
#config.MIN_SENT_COUNT = 1
config.memoize_articles = True
#config.request_timeout = 15
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config.browser_user_agent = user_agent