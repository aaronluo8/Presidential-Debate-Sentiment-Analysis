import snscrape.modules.twitter as st
import datetime
import json
import os
import argparse
import csv
from tqdm import tqdm
import sys


def collect_search(queries: list, search_filename: str, start_date, end_date, max_tweets):
    """
    Search tweets on Twitter with queries and duration

    :param queries: list of keywords to search
    :param search_filename: filename to save data
    :param start_date: search tweets starting from this date
    :param end_date: search tweets before this date. Needs to be at least +1day from start_date
    :param max_tweets: maximum tweets to search. if none, search all tweets
    :return: None
    """
    if not (start_date and end_date):
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            assert (start < end)
        except ValueError:
            print("Incorrect date format. It should be YYYY-MM-DD")

    for query in queries:
        if not os.path.exists('dataset'):
            os.makedirs('dataset')
        file_loc = "./dataset/" + search_filename + "_" + query + ".csv"
        try:
            os.remove(file_loc)
        except OSError:
            pass

        if start_date and end_date:
            query_with_criterion = query + " since:" + str(start_date) + " until:" + str(end_date)
        else:
            query_with_criterion = query

        print('Searching "{}"'.format(query))
        search_results = st.TwitterSearchScraper(query=query_with_criterion).get_items()

        f = open(file_loc, "w")
        fields = ['user_country', 'source', 'content', 'date']
        csv_writer = csv.DictWriter(f, fieldnames=fields)
        csv_writer.writeheader()

        cnt = 0
        for search_result in tqdm(search_results, total = max_tweets):
            # progress bar can be disappeared if iterations are max_tweets
            j = json.loads(search_result.json())
            if j["lang"] == "en":  # only save when lang=en
                if not len(j["content"]) < 20:  # filter out short tweets
                    user_country = j["user"]["location"]
                    source = j["sourceLabel"]
                    content = j["content"].replace("\n", " ")
                    content = f'{content}'  # wrap with quote; some tweets might include commas
                    date = j["date"]
                    csv_writer.writerow({'user_country': user_country,
                                         'source': source,
                                         'content': content,
                                         'date': date
                                         })
                    if max_tweets is not None:
                        cnt += 1
            if max_tweets is not None:
                if cnt == max_tweets:
                    break
        f.close()
    return


def collect_hashtag(hashtags: list, hashtag_filename: str, start_date: str, end_date: str, max_tweets: int):
    """
    Search tweets on Twitter with hashtags and duration
    searching hashtags in Twitter follows same logic as query search

    :param hashtags: list of hashtags to search
    :param hashtag_filename: filename to save data
    :param start_date: search tweets starting from this date
    :param end_date: search tweets before this date. Needs to be at least +1day from start_date
    :param max_tweets: maximum tweets to search. if none, search all tweets
    :return: None
    """
    for idx, data in enumerate(hashtags):
        hashtags[idx] = "#" + data
    collect_search(hashtags, hashtag_filename, start_date, end_date, max_tweets)
    return


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--queries", help="Keywords 'a,b,c,...'", dest="queries", type=str, required=True)
    parser.add_argument("--filename", help="CSV Filename", dest="filename", type=str, required=True)
    parser.add_argument("--start-date", help="Start date (2019-09-20)", dest="start_date")
    parser.add_argument("--end-date", help="End date (2019-09-21)", dest="end_date")
    parser.add_argument("--max", help="Max Tweets", dest="max_tweets", type=int, default=None)
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    return args


if __name__ == "__main__":
    args = parse_args()

    queries = [str(item) for item in args.queries.split(',')]
    filename = args.filename
    first_start_date = args.start_date
    first_end_date = args.end_date
    max_tweets = args.max_tweets

    # queries = ["Trump", "Biden", "Wallace", "Walker", "Debate", "Election", "Harris",
    #            "Tax", "Pence", "National Security", "Race in America",
    #            "Climate Change", "US Economy", "Supreme Court"]
    # first_start_date = "2020-09-29"
    # first_end_date = "2020-09-30"
    # first_start_date = "2020-10-22"
    # first_end_date = "2020-10-23"
    collect_search(queries, filename, first_start_date, first_end_date, max_tweets)
