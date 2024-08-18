import numpy as np
import pandas as pd
import requests
import feedparser
from datetime import datetime as dt, timedelta as td

from arXiv_category_dict import *

def parse_entry(entry):
    etime = dt.strptime(entry.published, '%Y-%m-%dT%H:%M:%SZ')
    if 'arxiv_doi' in entry.keys():
        doi = entry.arxiv_doi
    else:
        doi = ''
    if 'arxiv_affiliation' in entry.keys():
        arx_aff = entry.arxiv_affiliation
    else:
        arx_aff = ''
    if 'arxiv_journal_ref' in entry.keys():
        jref = entry.arxiv_journal_ref
    else:
        jref = ''

    return (etime, doi, arx_aff, jref)

def get_start_time():
    if dt.utcnow().hour > 18:
        start_time = dt.utcnow() - td(days=1)
    else:
        start_time = dt.utcnow() - td(days=2)
    return start_time.replace(hour=18, minute=00)

def get_query_params(start_time, end_time, search_query='', categories=None, max_results=100):
    start_str = dt.strftime(start_time, '%Y%m%d%H%M')
    end_str = dt.strftime(end_time, '%Y%m%d%H%M')

    left_par = '%28'
    right_par = '%29'

    if categories:
        categories_query = left_par + '+OR+'.join(['cat:' + cat for cat in categories]) + right_par
        if len(search_query) > 0:
            query = search_query + '+AND+' + categories_query
        else:
            query = categories_query
    
    query += f'+AND+submittedDate:[{start_str}+TO+{end_str}]'

    # Prepare the query parameters
    params = {
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
        'start': 0,
        'max_results': max_results
    }

    return params

def query_arXiv(search_query='', categories=None, start_time=None, end_time=None, max_results=None,
                verbose=False, mode='as_is'):
    """
    Query the arXiv API to retrieve a list of articles based on specified criteria.
    
    Args:
        search_query (str): The search query string.
        categories (list): A list of categories (e.g., ['cs.AI', 'cs.CL']) to filter the search. Default is None.
        start_time (datetime): The start time for the search. Default is 24 hours ago.
        end_time (datetime): The end time for the search. Default is now.
        max_results (int): The maximum number of results to retrieve. Default is None (100 results).
        
    Returns:
        pandas.DataFrame: A DataFrame containing article information including title, published date, authors,
            categories, and summary.
    """
    
    if not max_results:
        max_results = 100
        expand_search = True
    else:
        expand_search = False

    # Set default values if not provided
    if start_time is None:
        start_time = get_start_time()
    if end_time is None:
        end_time = dt.utcnow()
    total_time = end_time - start_time

    # Prepare the query parameters
    params = get_query_params(start_time=start_time, end_time=end_time, search_query=search_query, categories=categories,
                              max_results=max_results)
    # Make the API request
    if verbose:
        print('Contacting API')
    response = requests.get(f'http://export.arxiv.org/api/query?search_query={query}', params=params)
    if verbose:
        print('Response status code - ', response.status_code)
    if response.status_code == 200:
        # Parse the XML response using feedparser
        feed = feedparser.parse(response.content)
        if (len(feed.entries) == max_results) and (mode == 'expand_to_time'): # Recursive call if there are more than 100 papers in the timeframe
            articles1 = query_arXiv(categories=categories, start_time=start_time, end_time=end_time-total_time/2)
            articles2 = query_arXiv(categories=categories, start_time=end_time-total_time/2, end_time=end_time)
            articles = pd.concat([articles1, articles2], ignore_index=True)
            return articles
        articles = pd.DataFrame(columns = ['id', 'arxiv_doi', 'title', 'published', 'authors', 'arxiv_primary_category',
                                           'categories', 'summary', 'arxiv_affiliation', 'arxiv_journal_ref'])
        
        for entry in feed.entries:
            etime, doi, arx_aff, jref = parse_entry(entry)
            articles.loc[len(articles)] = [entry.id, doi, entry.title, etime, [author.name for author in entry.authors],
                                           entry.arxiv_primary_category, [tag['term'] for tag in entry.tags],
                                           entry.summary, arx_aff, jref]

        if (len(articles) < max_results) and (mode == 'expand_to_max'):
            articles2 = query_arXiv(categories=categories, start_time=start_time-total_time*2, end_time=start_time)
            articles = pd.concat([articles, articles2], ignore_index=True).head(max_results)
        return articles
    else:
        print('Error:', response.status_code)
        return []

# def get_best_matches(text_to_match, tokenizer, )
    
if __name__ == '__main__':
    articles = query_arXiv(search_query='',categories=['cs.AI', 'cs.CL'], start_time=dt.utcnow()-td(days=3))
    print(len(articles))

    print('a')