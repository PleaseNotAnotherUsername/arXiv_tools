import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import transformers

from query_tools import query_arXiv

def get_tokens(texts, tokenizer, max_len = 256):
    tokens = [tokenizer.encode_plus(
            text,
            None,
            add_special_tokens=True,
            max_length=max_len,
            padding='max_length',
            return_token_type_ids=True,
            truncation=True
        )['attention_mask'] for text in texts]
    return tokens 

def sort_by_similarity(tokensa, tokensb):
    similarity = np.array(cosine_similarity(tokensa,tokensb))
    return(np.argsort(-similarity[0]))

def get_tokenizer_instance(tokenizer, **kwargs):
    if tokenizer == 'DistilBert':
        return transformers.DistilBertTokenizer.from_pretrained('distilbert-base-uncased', **kwargs)
    else:
        print('Unknown tokenizer!')
        return

class best_arXiv_results():
    def __init__(self, tokenizer='DistilBert', max_results=256, query_mode = 'expand_to_time'):
        self.tokenizer = get_tokenizer_instance(tokenizer)
        self.max_results = max_results
        self.query_mode = query_mode

    def get_results(self, search_query='', categories=None, start_time=None, end_time=None, verbose=False):
        self.results = query_arXiv(search_query=search_query, categories=categories, start_time=start_time,
                              end_time=end_time, max_results=self.max_results, verbose=verbose, mode=self.query_mode)
    
    

        
if __name__ == '__main__':
    tokenizer = 'DistilBert'
    max_len = 512
    
    text_to_match = 'machine learning'
    text_token = get_tokens([text_to_match], tokenizer=tokenizer, max_len=max_len)
    arxiv_summary_tokens = get_tokens(articles.summary, tokenizer=tokenizer, max_len=max_len)
    arg_ids = sort_by_similarity(text_token, arxiv_summary_tokens)

    print('max', articles.iloc[arg_ids[0]].title)
    print(articles.iloc[arg_ids[0]].summary)
    print('max2', articles.iloc[arg_ids[1]].title)
    print(articles.iloc[arg_ids[1]].summary)