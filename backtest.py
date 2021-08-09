from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed

feed = yahoofeed.Feed()

feed.addBarsFromCSV("spy", "spy.csv")

print(feed)
