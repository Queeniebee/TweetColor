import sys
import argparse
from twython import twython



def search_twitter(query='python'):
  url = 'http://search.twitter.com/search.json?q=' + query
  response = urllib.urlopen(url).read()
  data = json.loads(response)
  return data['results']

def print_tweets(tweets):
  for tweet in tweets:
    print tweet['from_user'] + ': ' + tweet['text'] + '\n'

results = search_twitter()
print_tweets(results)

def main():
	query = sys.argv[1]
	tw = Twython()
	results = tw.searchTwitter(q=query)
	print_tweets(results['results'])

if __name__ == "__main__":
  	query = sys.argv[1]
	print_tweets(results)

# status.text
# status.hashtags

# methods:
# GetText(self)
# GetRelativeCreatedAt(self)
#__init__

# SetStatusesCount(self, count)
# |      Set the status update count for this user.
# |      
# |      Args:
# |        count:
# |          The number of updates for this user.

#GetStatusesCount(self)
# |      Get the number of status updates for this user.
# |      
# |      Returns:
# |        The number of status updates for this user.