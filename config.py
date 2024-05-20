from logging import config
from newspaper import Config, Article, Source
config = Config()
config.fetch_images = False
#config.MAX_AUTHORS = 1
#config.MIN_WORD_COUNT = 100
#config.MIN_SENT_COUNT = 1
config.memoize_articles = True