from bot import InternetSpeedTwitterBot

itbot = InternetSpeedTwitterBot()

itbot.get_internet_speed()
print(itbot.down, itbot.up)
itbot.tweet_at_provider()