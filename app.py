import datetime

import investpy

search_result = investpy.search_quotes(text='apple', products=['stocks'],
                                       countries=['united states'], n_results=1)
recent_data = search_result.retrieve_recent_data()

df = investpy.funds.search_funds(by='isin',value='LU0913601281')

print(df['name'])