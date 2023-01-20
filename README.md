# Presidential Debate Sentimental Anaysis

This was the final project from the Programming for Data Analysis Graduate course with Jose H Unpingco at UCSD, written in collaboration with Jaeyoung Kang, Anye Shi, and Jasmine Chiang in the Winter of 2020

This project aims to analyze people's sentiment on Twitter as a result of the election debates.

## Datasets

1. Transcript of the two 2020 presidential debates:

- September 29, 2020
- October 22, 2020

2. Twitter dataset 

First, we define search "queries" to find relevant tweets from Twitter posted before Nov. 3rd. For instance, some of the keywords we are considering include "Trump, Biden, Wallace, Debate, Election, Harris, Tax, Pence, National Security, Race in America, Climate Change, US Economy, Supreme Court".


## Requirements

* Python 3.8
* snscrape (with master branch)
* nltk
* pandas
* numpy
* vadersentiment
* tqdm
* google-cloud-language
* textblob
* matplotlib
* wordcloud
* scikit-learn
* bs4

## Quick Start Guide (with Installation)
```bash
$ git clone https://github.com/tycheyoung/p_debate_sentimental_analysis
$ cd p_debate_sentimental_analysis
$ pip3 install requirements.txt
```

## Usage
1. Tweet scraper
```bash
$ python3 scraper.py --queries "QUERY1, QUERY2" --filename "FILENAME" --start-date YYYY-MM-DD --end-date YYYY-MM-DD --max MAX_TWEETS

```
2. Transcript parser
```bash
$ python3 transcript_parser.py --filepath "FOLDERNAME/" --filename "FILENAME"
```


For example, 

1. `python3 scraper.py --queries "National Security" --filename "search_res_1" --start-date 2020-09-30 --end-date 2020-10-01 --max 20`

2. `python3 transcript_parser.py --filepath "dataset/" --filename "transcript_2"`



## Project Structure
```
.
|-- README.md
|-- dataset
|   |-- README.md
|   |-- debate_1
|   |   |-- search_results_Biden.csv
|   |   `-- ....
|   |-- debate_2
|   |   |-- search_results_Biden.csv
|   |   `-- .... 
|   |-- extended_debate_1
|   |   |-- 1_search_results_Debate.csv
|   |   `-- 1_search_results_Election.csv
|   |-- extended_debate_2
|   |   |-- 2_search_results_Debate.csv
|   |   `-- 2_search_results_Election.csv
|   |-- parsed_transcript_1_p1.csv
|   |-- parsed_transcript_1_p2.csv
|   |-- parsed_transcript_2.csv
|   |-- transcript_1_p1.txt
|   |-- transcript_1_p2.txt
|   `-- transcript_2.txt
|-- transcript_analysis
|   |-- transcript_analysis_debate1.ipynb
|   `-- transcript_analysis_debate2.ipynb
|-- tweet_debate_1_analysis
|   |-- Sample-Clean-Sentiment.ipynb
|   |-- D1Biden.ipynb
|   `-- ....
|-- tweet_debate_2_analysis
|   |-- D2Biden.ipynb
|   `-- ....
|-- ECE 143 Group 10 Final Presentation.pdf
|-- Final_Data_Visualization.ipynb
|-- requirements.txt
|-- sample_search_results.json
|-- scraper.py
`-- transcript_parser.py


```

1. datasets/

This folder contains the transcript and the crawled tweets on the day/day before the debate. 
- `debate_1` folder contains the tweets related to the first debate
- `debate_2` folder contains the second debate related tweets. 
- `extended_*` folder contains the whole tweets. However, due to the limitation of the capacity, we saved crawled data on the google drive separately.

2. transcript_analysis/

This folder contains jupyter notebooks with the sentimental analysis of participants during the debate.

3. tweet_debate_*_analysis/

These folders contains the jupyter notebook which handled the analysis (including sentiment) of the tweets within the debate day denoted by the *. In tweet_debate_1_analysis, there is also the Sample-Clean-Sentiment.ipynb, which is an example shows how we can cleanup the crawled data which is what the rest of the notebooks in these folders are built off of. 

4. ECE 143 Group 10 Final Presentation.pdf

This is the final presentation as given on our presentation date (12/4/2020).

5. Final_Data_Visualization.ipynb

This shows a compilation of the code used to visualize the plots as shown in the final presentation. It is comprised of content to visualize sentiment over time as well as content from notebooks in tweet_debate_*_analysis/ as well as transcript_analysis/.


6. sample_search_results.json

This file shows what kind of data we can get from Twitter, as the response of the request.


7. scraper.py

This script is based on the `snscrape` library. Given a query, start date, end date, this code block crawls the tweets and refine it to the CSV file. Short tweets and non-en tweets are filtered out.

8. transcript_parser.py

This script parses the transcript txt file and refines it to CSV format.





