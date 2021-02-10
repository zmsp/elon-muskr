# update this file with right parameters
# consumer key and secret is from twitter dev console https://developer.twitter.com/en/portal/dashboard
consumer_key = "REPLACEME"
consumer_secret = "REPLACEME"
# slack configuration.
slack_username = 'elon-bot'
slack_icon_emoji = ':melon:'
slack_channel = '#REPLACEME'  # @username or #channel-name
slack_webhook_url = 'https://hooks.slack.com/services/#TODO '  # TODO
# For csv url, make your google spreadsheet public and update the url.
# Format: https://docs.google.com/spreadsheets/u/1/d/{!!!DOCUMENT ID!!!}/export?format=csv
csv_url = 'https://docs.google.com/spreadsheets/u/1/d/1ghxQzjuZ6LpkgsnS4gpvEkhSY0KYAWt0C72tHZ0rFew/export?format=csv'
# change it to false to post it to slack
debug = True
# If you want to use a proxy server, update it
# example: { "http"  : "http://0.0.0.0:4334/",  "https" : "http://0.0.0.0:4334/", "ftp"   : "http://0.0.0.0:4334/" }
proxyDict = None
