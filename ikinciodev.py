import psycopg2
import snscrape.modules.twitter as sntwitter

cnxn = psycopg2.connect(host="localhost", database="tweets", port=5432, user="postgres", password="12345")
cursor = cnxn.cursor()

maxTweets = 20

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 + since:2021-01-01 until:2021-03-01').get_items()):
    if i > maxTweets:
        break
    print(tweet.content)
    print(tweet.username)
    print(tweet.date)
    print("\n")

    command = 'insert into tablo(content, username, date) values (%s,%s,%s);'
    values = [tweet.content, tweet.username, tweet.date]

    cursor.execute(command, values)
    cnxn.commit()

cursor.close()
