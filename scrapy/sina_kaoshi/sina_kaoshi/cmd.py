import scrapy.cmdline
# import as csv
scrapy.cmdline.execute('scrapy crawl spider -t csv -o result.csv -s FEED_EXPORT_ENCODING="utf-8"'.split())